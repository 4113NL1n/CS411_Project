#!/bin/bash

# Load environment variables
export $(grep -v '^#' .env | xargs)

# Initialize the database
./sql/create_db.sh

# Start the application
python app.py
