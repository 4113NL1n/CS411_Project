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

update_pass(){
    echo "Testing password update..."
    response=$(curl -s -X PUT -H "Content-Type: application/json" -d '{"username": "Allen", "old_passw": "1234","new_passw": "321"}' "$BASE_URL/update_pass_route")
    echo "$response" | grep -q '"message": "Password updated ."'
    if [ $? -eq 0 ]; then
        echo "Password update passed!"
    else
        echo "Password update failed."
        exit 1
    fi
}

get_weat(){
    city="boston"
    echo "Getting Weather"
    response=$(curl -s -X GET "$BASE_URL/weather/$city") 
    echo "$response" | grep -q '"weather" : "boston"'
if [ $? -eq 0 ]; then
        echo "weather passed!"
    else
        echo "weather failed."
        exit 1
    fi
}

get_fore(){
    city="boston"
    echo "Getting forecast"
    response=$(curl -s -X GET "$BASE_URL/weather/forecast/$city") 
        echo "$response" | grep -q '"forecast" : "boston"'
    if [ $? -eq 0 ]; then
        echo "forecast passed!"
    else
        echo "forecast failed."
        exit 1
    fi
}

get_ai(){
    city="boston"
    state_code="ma"
    country_code="US"
    echo "Getting air quality"
    response=$(curl -s -X GET "$BASE_URL/weather/air/$city/$state_code/$country_code") 
        echo "$response" | grep -q '"air quality" : "boston"'
    if [ $? -eq 0 ]; then
        echo "air passed!"
    else
        echo "air failed."
        exit 1
    fi
}

get_alert(){
    state_code="ma"
    echo "Getting alerts"
    response=$(curl -s -X GET "$BASE_URL/weather/alerts/$state_code") 
        echo "$response" | grep -q '"alerts" : "boston"'
    if [ $? -eq 0 ]; then
        echo "alerts passed!"
    else
        echo "alerts failed."
        exit 1
    fi
}

add_fave(){
    city="boston"
    echo "adding favorite"
    response=$(curl -s -X POST "$BASE_URL/weather/favorite/save/$city") 
        echo "$response" | grep -q '"saving" : "Boston"'
    if [ $? -eq 0 ]; then
        echo "saving passed!"
    else
        echo "saving failed."
        exit 1
    fi
}

get_fave(){
    echo "Getting favorite"
    response=$(curl -s -X GET "$BASE_URL/weather/favorite") 
        echo "$response" | grep -q '"favorite" : "list"'
    if [ $? -eq 0 ]; then
        echo "fave passed!"
    else
        echo "fave failed."
        exit 1
    fi
}

# Run health check
Check-Health

check_db

create_user

log_in

update_pass

get_weat

get_fore

get_ai

get_alert

add_fave

get_fave

