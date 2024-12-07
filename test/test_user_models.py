import pytest
import requests
import re
import sqlite3
import logging
from unittest import mock
from models.user_models import create_user,hash_password,check_password
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
    mocker.patch("models.user_models.get_db_connection", mock_get_db_connection)
    return mock_cursor 

def test_create_user(mock_cursor): 
    username = "Allen"  
    password = "123456" 
    create_user(name=username, password=password)  
    expected_query = normalize_whitespace(
        """INSERT INTO user (username, pass, salt) 
        VALUES (?, ?, ?);
    """)
    actual_query = normalize_whitespace(mock_cursor.execute.call_args[0][0])
    assert actual_query == expected_query