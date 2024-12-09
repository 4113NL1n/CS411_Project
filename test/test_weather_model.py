import pytest
from flask import Flask, jsonify
from app import app
from unittest.mock import patch

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client



def test_get_weather(client):
    """
    Test the route to fetch current weather for a city.

    Args:
        client: A test client instance for the Flask app.

    Asserts:
        Response status is 200.
    """
    response = client.get('/weather/Boston')
    assert response.status_code == 200
    
def test_get_forecast(client):
    """
    Test the route to fetch the 5-day weather forecast for a city.

    Args:
        client: A test client instance for the Flask app.

    Asserts:
        Response status is 200.
    """
    response =client.get("/weather/forecast/Boston")
    assert response.status_code == 200
    
def test_get_air(client):
    """
    Test the route to fetch air quality for a city.

    Args:
        client: A test client instance for the Flask app.

    Asserts:
        Response status is 200.
    """
    response =client.get("/weather/air/Boston/MA/US")
    assert response.status_code == 200

def test_get_alerts(client):
    """
    Test the route to fetch weather alerts for a state.

    Args:
        client: A test client instance for the Flask app.

    Asserts:
        Response status is 200.
    """
    response =client.get("/weather/alerts/NY")
    assert response.status_code == 200

def test_get_favorite(client):
    """
    Test the route to manage favorite cities.

    Args:
        client: A test client instance for the Flask app.

    Asserts:
        Response status is 200.
        Favorite cities are correctly saved and retrieved.
    """
    fave = []
    response = client.get("/weather/favorite")
    assert response.status_code == 200
    assert response.get_json() == fave
    client.put("/weather/favorite/save/Boston")
    fave = ["Boston"]
    
    # Step 4: Ensure that the favorite list now contains "Boston"
    response = client.get("/weather/favorite")
    assert response.status_code == 200
    assert response.get_json() == fave 