import pytest
from flask import Flask, jsonify
from app import app
from unittest.mock import patch

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client



def test_get_weather(client):
    response = client.get('/weather/Boston')
    assert response.status_code == 200
    
    
def test_get_forecast(client):
    response =client.get("/weather/forecast/Boston")
    assert response.status_code == 200
    
def test_get_air(client):
    response =client.get("/weather/air/Boston/MA/US")
    assert response.status_code == 200

def test_get_alerts(client):
    response =client.get("/weather/alerts/NY")
    assert response.status_code == 200

def test_get_favorite(client):
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