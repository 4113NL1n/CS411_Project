import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
import json
from app import app
import pytest
import requests
import re
import sqlite3
import logging
from unittest import mock
from model.user_model import create_user,log_in,hash_password,update_pass
from contextlib import contextmanager

def normalize_whitespace(sql_query: str) -> str:
    return re.sub(r'\s+', ' ', sql_query).strip()

@pytest.fixture
def mock_cursor(mocker):
    mock_conn = mocker.Mock()
    mock_cursor = mocker.Mock()
    mock_conn.cursor.return_value = mock_cursor
    mock_cursor.fetchone.return_value = None  
    mock_cursor.fetchall.return_value = []
    mock_conn.commit.return_value = None
    @contextmanager
    def mock_get_db_connection():
        yield mock_conn  
    mocker.patch("model.user_model.get_db_connection", mock_get_db_connection)
    return mock_cursor 

def test_create_user(mock_cursor): 
    """
    Test user creation in the database.

    Args:
        mock_cursor: A mock cursor for simulating database interactions.

    Asserts:
        The SQL query executed matches the expected query format.
    """
    username = "Allen"  
    password = "123456" 
    create_user(name=username, password=password)  
    expected_query = normalize_whitespace(
        """INSERT INTO user (username, pass) 
        VALUES (?, ?);
    """)
    actual_query = normalize_whitespace(mock_cursor.execute.call_args[0][0])
    assert actual_query == expected_query

def test_create_acc_missing_fields():
    """
    Test the /create endpoint for handling missing username or password.
    """
    with app.test_client() as client:
        # Test case: Missing both fields
        response = client.post(
            '/create',
            data=json.dumps({}),
            content_type='application/json'
        )
        assert response.status_code == 400
        assert response.get_json() == {"error": "Username and password are required."}

        # Test case: Missing username
        response = client.post(
            '/create',
            data=json.dumps({"password": "securepassword"}),
            content_type='application/json'
        )
        assert response.status_code == 400
        assert response.get_json() == {"error": "Username and password are required."}

        # Test case: Missing password
        response = client.post(
            '/create',
            data=json.dumps({"username": "newuser123"}),
            content_type='application/json'
        )
        assert response.status_code == 400
        assert response.get_json() == {"error": "Username and password are required."}

def test_create_acc_user_already_exists(mocker):
    """
    Test the /create endpoint for handling a username that already exists.
    """
    username = "Allen"  
    password = "123456" 
    create_user(name=username, password=password)
    with app.test_client() as client:
        # Mock the create_user function to raise a ValueError
    
        response = client.post(
            '/create',
            data=json.dumps({"username": "Allen", "password": "123456"}),
            content_type='application/json'
        )
        assert response.get_json() == {"error": "Username 'Allen' is already taken."}

def test_log_in_route_invalid_credentials(mocker):
    """
    Test the /login endpoint for invalid credentials.
    """
    with app.test_client() as client:
        # Mock the log_in function to return False (invalid credentials)
        mocker.patch(
            "model.user_model.log_in",
            return_value=False
        )
        
        response = client.post(
            '/login',
            data=json.dumps({"username": "invalid_user", "password": "wrongpassword"}),
            content_type='application/json'
        )
        assert response.status_code == 401
        assert response.get_json() == {"message": "Invalid credentials"}

def test_log_in(mock_cursor,mocker):
    """
    Test user login by verifying credentials.

    Args:
        mock_cursor: A mock cursor for simulating database interactions.
        mocker: A mock object for patching functions.

    Asserts:
        Login succeeds when the correct username and password are provided.
    """
    username = "Allen"  
    password = "123456" 
    Hashpassword = hash_password(password)
    mocker.patch("model.user_model.check_user", return_value=False)
    mock_cursor.fetchone.return_value = [Hashpassword]
    assert log_in(username, password) == True

def test_update_pass(mocker,mock_cursor):
    """
    Test password update for a user.

    Args:
        mocker: A mock object for patching functions.
        mock_cursor: A mock cursor for simulating database interactions.

    Asserts:
        Password update succeeds when old password verification passes.
    """
    username = "Allen"  
    password = "123456" 
    Hashpassword = hash_password(password)
    mocker.patch("model.user_model.check_user", return_value=False)
    mocker.patch("model.user_model.check_password", return_value=True)
    mock_cursor.fetchone.return_value = [Hashpassword]
    assert update_pass(username,password,"feewfew") == True
    

