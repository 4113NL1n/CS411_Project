BASE_URL="http://127.0.0.1:5000"


check_health() {
    echo "Checking health status..."
    echo "URL: $BASE_URL/health"  # Print the URL being accessed
    response=$(curl -v "$BASE_URL/health")  # Fetch the response
    echo "Response: $response"  # Print the full response to check
    echo "$response" | grep -q '"status":"healthy"'
    if [ $? -eq 0 ]; then
        echo "Service is healthy."
    else
        echo "Health check failed."
        exit 1
    fi
}


create_user(){
    echo "Creating user account..."
    response=$(curl -s -X POST -H "Content-Type: application/json" -d '{"username": "Allen", "password": "1223"}' "$BASE_URL/create")
    echo "Response: $response"  # Log the full response for debugging
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
    echo "$response" | grep -q '"message": "Logged in."'
    if [ $? -eq 0 ]; then
        echo "login passed!"
    else
        echo "login failed."
        exit 1
    fi
}

update_pass(){
    echo "Testing password update..."
    response=$(curl -s -X PUT -H "Content-Type: application/json" -d '{"username": "Allen", "old_passw": "1223","new_passw": "1234"}' "$BASE_URL/update_pass_route")
    echo "$response" | grep -q '"message": "Password updated successfully"'
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
    city_in_response=$(echo "$response" | jq -r '.location')
if [ "$city_in_response" == "boston" ]; then
        echo "Weather passed!"
    else
        echo "Weather failed."
        exit 1
    fi
}

get_fore(){
    city="boston"
    echo "Getting forecast"
    response=$(curl -s -X GET "$BASE_URL/weather/forecast/$city") 
    city_in_response=$(echo "$response" | jq -r '.location')
    if [ "$city_in_response" == "boston" ]; then
        echo "Weather passed!"
    else
        echo "Weather failed."
        exit 1
    fi
}

get_ai(){
    city="boston"
    state_code="ma"
    country_code="US"
    echo "Getting air quality"
    response=$(curl -s -X GET "$BASE_URL/weather/air/$city/$state_code/$country_code") 
        echo "$response" | grep -q '"air" : "good"'
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
    echo "Adding favorite"
    response=$(curl -s -X PUT "$BASE_URL/weather/favorite/save/$city")
    
    # Check if the city "boston" is in the response list
    echo "$response" | grep -q '"boston"'
    
    if [ $? -eq 0 ]; then
        echo "Saving passed!"
    else
        echo "Saving failed."
        exit 1
    fi
}

get(){
    city="boston"
    echo "Adding favorite"
    response=$(curl -s -X PUT "$BASE_URL/weather/favorite")
    
    echo "$response" | grep -q '"boston"'
    
    if [ $? -eq 0 ]; then
        echo "Saving passed!"
    else
        echo "Saving failed."
        exit 1
    fi
}

check_health
create_user

log_in

update_pass

get_weat

get_fore

get_ai

get_alert

add_fave

get_fave

