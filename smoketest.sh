BASE_URL = "http://127.0.0.1:5000"

check_health() {
    echo "Checking health status..."
    response=$(curl -s "$BASE_URL/health")
    echo "$response" | grep -q '"status": "healthy"'
    if [ $? -eq 0 ]; then
        echo "Service is healthy."
    else
        echo "Health check failed."
        exit 1
    fi
}

check_db() {
  echo "Checking database connection..."
  curl -s -X GET "$BASE_URL/db-check" | grep -q '"database_status": "healthy"'
  if [ $? -eq 0 ]; then
    echo "Database connection is healthy."
  else
    echo "Database check failed."
    exit 1
  fi
}


create_user(){
    echo "Creating user account..."
    response=$(curl -s -X POST -H "Content-Type: application/json" -d '{"username": "Allen", "password": "1223"}' "$BASE_URL/create")
    echo "$response" | grep -q '"message": "Account created successfully."'
    if [ $? -eq 0 ]; then
        echo "Account creation passed!"
    else
        echo "Account creation failed."
        exit 1
    fi
}

log_in(){
    echo "Logging in"
    response=$(curl -s -X POST -H "Content-Type: application/json" -d '{"username": "Allen", "password": "1223"}' "$BASE_URL/login")
    echo "$response" | grep -q '"message": "successfully."'
    if [ $? -eq 0 ]; then
        echo "login passed!"
    else
        echo "login failed."
        exit 1
    fi
}

# Run health check
Check-Health

check_db

create_user

log_in