# CS411_Project
Boston University CS 411 final Project

The app has 2 parts, a user and weather. User will prompt the user to log in or create account. Weather will allow user to search for weather, forecast, alerts, and air quality in a area.

## Route: `/create`
- **Request Type**: `POST`
- **Purpose**: Creates a new user account with a username and password.
- **Request Body**:
  - `username` (String): User's chosen username.
  - `password` (String): User's chosen password.
- **Response Format**: JSON
  - **Success Response Example**:
    - **Code**: 200
    - **Content**:
      ```json
      {
        "message": "Account created successfully"
      }
      ```
- **Example Request**:
  ```json
  {
    "username": "newuser123",
    "password": "securepassword"
  }

Route: /login
● Request Type: POST
● Purpose: Log in with the user's username and password
● Request Body:
○ username (String): User's username.
○ password (String): User's password.
● Response Format: JSON
○ Success Response Example:
■ Code: 200
■ Content: { "message": "Logged in" }
● Example Request:
{
"username": "newuser123",
"password": "securepassword"
}
● Example Response:
{
"message": "Logged in",
"status": "200"
}


Route: /password
● Request Type: POST
● Purpose: Changes the user's old password with the new one
● Request Body:
○ username (String): User's username.
○ old_password (String): User's old password.
○ new_password (String): User's new password.
● Response Format: JSON
○ Success Response Example:
■ Code: 200
■ Content: { "message": "Password updated successfully" }
● Example Request:
{
"username": "newuser123",
"old_password": "securepassword"
"new_password": "newsecurepassword"
}
● Example Response:
{
"message": "Password updated successfully",
"status": "200"
}

Route: /password
● Request Type: POST
● Purpose: Changes the user's old password with the new one
● Request Body:
○ username (String): User's username.
○ old_password (String): User's old password.
○ new_password (String): User's new password.
● Response Format: JSON
○ Success Response Example:
■ Code: 200
■ Content: { "message": "Password updated successfully" }
● Example Request:
{
"username": "newuser123",
"old_password": "securepassword"
"new_password": "newsecurepassword"
}
● Example Response:
{
"message": "Password updated successfully",
"status": "200"
}
Route: /weather/favorite
● Request Type: GET
● Purpose: Get the users favorite location
● Request Body:
● Response Format: JSON
○ Success Response Example:
■ Code: 200
■ Content: {[]}
● Example Request:
{
}
● Example Response:
{
"[Boston]"
}

Route: /weather/<city>
● Request Type: GET
● Purpose: Get the weather for the user's chosen city
● Request Body:
○ city (String): any city
● Response Format: JSON
○ Success Response Example:
■ Code: 200
■ Content: {"{data}" }
● Example Request:
{
"city": "Boston",
}
● Example Response:
{
  "curr": 43.57,
  "high": 45.3,
  "location": "Boston",
  "low": 43.57,
  "main": "Mist"
}


Route: /weather/forecast/<city>
● Request Type: GET
● Purpose: Get the forecast for the user's chosen city
● Request Body:
○ city (String): any city
● Response Format: JSON
○ Success Response Example:
■ Code: 200
■ Content: {"{data}" }
● Example Request:
{
"city": "Boston",
}
● Example Response:
{
[
  {
    "curr": 43.48,
    "high": 44.71,
    "location": "Boston",
    "low": 43.48,
    "main": "Rain"
  },
  {
    "curr": 47.3,
    "high": 47.3,
    "location": "Boston",
    "low": 47.3,
    "main": "Rain"
  },
  {
    "curr": 39.6,
    "high": 39.6,
    "location": "Boston",
    "low": 39.6,
    "main": "Clouds"
  },
  {
    "curr": 30.56,
    "high": 30.56,
    "location": "Boston",
    "low": 30.56,
    "main": "Clear"
  },
  {
    "curr": 34.72,
    "high": 34.72,
    "location": "Boston",
    "low": 34.72,
    "main": "Clouds"
  }
]
}



Route: /weather/air/<city>/<state_code>/<country_code>
● Request Type: GET
● Purpose: Get the air quality for the user's chosen city
● Request Body:
○ city (String): any city=
○ state_code (String): any state
○ country_code (String): any country

● Response Format: JSON
○ Success Response Example:
■ Code: 200
■ Content: {"{'air': 'good'}" }
● Example Request:
{
"city": "Boston",
"state_code": "MA",
"country_code": "US"
}
● Example Response:
{
   "air": "good"
}



Route: /weather/alerts/<state_code>
● Request Type: GET
● Purpose: Get the weather alerts for the user's chosen state
● Request Body:
○ city (String): state
● Response Format: JSON
○ Success Response Example:
■ Code: 200
■ Content: {"{data}" }
● Example Request:
{
"state_code": "MA",
}
● Example Response:
{
"* WHAT...Mixed precipitation expected. Total snow and sleet\naccumulations of 1 to 3 inches and ice accumulations around one\ntenth of an inch.\n\n* WHERE...In Massachusetts, Northern Berkshire County. In Vermont,\nBennington and Windham Counties.\n\n* WHEN...Until 10 AM EST Tuesday.\n\n* IMPACTS...Plan on slippery road conditions. The hazardous\nconditions could impact the Monday evening and Tuesday morning\ncommutes.\n\n* ADDITIONAL DETAILS...Snow and sleet will continue into this\nevening. The precipitation will transition to plain rain and\nfreezing rain tonight. Freezing rain and freezing drizzle will\ncontinue especially over elevated surfaces overnight into Tuesday\nmorning with light ice accumulations."}



Route: /weather/favorite/save/<city>
● Request Type: PUT
● Purpose: Put the user chosen city into a list of favorites
● Request Body:
○ city (String): any city
● Response Format: JSON
○ Success Response Example:
■ Code: 200
■ Content: {[
  "Boston"
] }
● Example Request:
{
"city": "Boston"
}
● Example Response:
{
   [
  "Boston"
]
}
