import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

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
    username = "Allen"  
    password = "123456" 
    create_user(name=username, password=password)  
    expected_query = normalize_whitespace(
        """INSERT INTO user (username, salt, pass) 
        VALUES (?, ?, ?);
    """)
    actual_query = normalize_whitespace(mock_cursor.execute.call_args[0][0])
    assert actual_query == expected_query

def test_log_in(mock_cursor,mocker):
    username = "Allen"  
    password = "123456" 
    Hashpassword, salt = hash_password(password)
    mocker.patch("model.user_model.check_user", return_value=False)
    mock_cursor.fetchone.return_value = [Hashpassword]
    assert log_in(username, password) == True

def test_update_pass(mocker,mock_cursor):
    username = "Allen"  
    password = "123456" 
    Hashpassword, salt = hash_password(password)
    mocker.patch("model.user_model.check_user", return_value=False)
    mocker.patch("model.user_model.check_password", return_value=True)
    mock_cursor.fetchone.return_value = [Hashpassword]
    assert update_pass(username,password,"feewfew") == True
    

