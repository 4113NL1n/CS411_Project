BASE_URL="http://127.0.0.1:5000"

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

create_user() {
    echo "Creating user account..."
    response=$(curl -s -X POST -H "Content-Type: application/json" -d '{"username": "testuser", "password": "password123"}' "$BASE_URL/create")
    echo "$response" | grep -q '"message": "Account created successfully."'
    if [ $? -eq 0 ]; then
        echo "Account creation passed!"
    else
        echo "Account creation failed: $response"
        exit 1
    fi
}

log_in() {
    echo "Logging in..."
    response=$(curl -s -X POST -H "Content-Type: application/json" -d '{"username": "testuser", "password": "password123"}' "$BASE_URL/login")
    echo "$response" | grep -q '"message": "Logged in"'
    if [ $? -eq 0 ]; then
        echo "Login passed!"
    else
        echo "Login failed: $response"
        exit 1
    fi
}

update_pass() {
    echo "Testing password update..."
    response=$(curl -s -X POST -H "Content-Type: application/json" -d '{"username": "testuser", "old_password": "password123", "new_password": "newpassword"}' "$BASE_URL/password")
    echo "$response" | grep -q '"message": "Password updated successfully"'
    if [ $? -eq 0 ]; then
        echo "Password update passed!"
    else
        echo "Password update failed: $response"
        exit 1
    fi
}

get_weather() {
    city="Boston"
    echo "Getting weather for $city..."
    response=$(curl -s -X GET "$BASE_URL/weather/$city")
    echo "$response" | grep -q '"location": "Boston"'
    if [ $? -eq 0 ]; then
        echo "Weather passed!"
    else
        echo "Weather failed: $response"
        exit 1
    fi
}

get_forecast() {
    city="Boston"
    echo "Getting forecast for $city..."
    response=$(curl -s -X GET "$BASE_URL/weather/forecast/$city")
    if [ -n "$response" ]; then
        echo "Forecast passed!"
    else
        echo "Forecast failed: $response"
        exit 1
    fi
}

get_air_quality() {
    city="Boston"
    state_code="MA"
    country_code="US"
    echo "Getting air quality for $city..."
    response=$(curl -s -X GET "$BASE_URL/weather/air/$city/$state_code/$country_code")
    echo "$response" | grep -q '"air": "good"'
    if [ $? -eq 0 ]; then
        echo "Air quality passed!"
    else
        echo "Air quality failed: $response"
        exit 1
    fi
}

get_alerts() {
    state_code="MA"
    echo "Getting alerts for state $state_code..."
    response=$(curl -s -X GET "$BASE_URL/weather/alerts/$state_code")
    if [ -n "$response" ]; then
        echo "Alerts passed!"
    else
        echo "Alerts failed: $response"
        exit 1
    fi
}

add_favorite() {
    city="Boston"
    echo "Adding $city to favorites..."
    response=$(curl -s -X PUT "$BASE_URL/weather/favorite/save/$city")
    echo "$response" | grep -q "$city"
    if [ $? -eq 0 ]; then
        echo "Favorite added passed!"
    else
        echo "Favorite add failed: $response"
        exit 1
    fi
}

get_favorites() {
    echo "Getting favorites..."
    response=$(curl -s -X GET "$BASE_URL/weather/favorite")
    echo "$response" | grep -q "Boston"
    if [ $? -eq 0 ]; then
        echo "Favorites passed!"
    else
        echo "Favorites failed: $response"
        exit 1
    fi
}

# Execute all checks
check_health
create_user
log_in
update_pass
get_weather
get_forecast
get_air_quality
get_alerts
add_favorite
get_favorites
