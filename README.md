# CS411_Project
Boston University CS 411 final Project

The app has 2 parts, a user and weather. User will prompt the user to log in or create account. Weather will allow user to search for weather, forecast, alerts, and air quality in a area.

## Running the Program: `/Guide`
Create a .env file in the root directory, in that file add
- **SQL_CREATE_TABLE_PATH=sql/create_user_table.sql**
- **DB_PATH = sql/user.db**
- **CREATE_DB = true**
Generate a API key from OpenWeatherApi. Put it as API_KEY="your_key" in the env file. Run the reqruiements.txt and run dockerfile, then you could do `python app.py` or `flask run` then try out all the different endpoitn apis!


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
- **Example Resonse**:
  ```json
  {
    "message": "Account created successfully"
  }

## Route: `/login`
- **Request Type**: `POST`
- **Purpose**: Log in with the user's username and password.
- **Request Body**:
  - `username` (String): User's username.
  - `password` (String): User's password.
- **Response Format**: JSON
  - **Success Response Example**:
    - **Code**: 200
    - **Content**:
      ```json
      {
        "message": "Logged in"
      }
      ```
- **Example Request**:
  ```json
  {
    "username": "newuser123",
    "password": "securepassword"
  }
- **Example Resoibse**:
  ```json
  {
    "message": "Logged in"

  }

## Route: `/password`
- **Request Type**: `POST`
- **Purpose**: Changes the user's old password with the new one.
- **Request Body**:
  - `username` (String): User's username.
  - `old_password` (String): User's old password.
  - `new_password` (String): User's new password.
- **Response Format**: JSON
  - **Success Response Example**:
    - **Code**: 200
    - **Content**:
      ```json
      {
        "message": "Password updated successfully"
      }
      ```
- **Example Request**:
  ```json
  {
    "username": "newuser123",
    "old_password": "securepassword",
    "new_password": "newsecurepassword"
  }
- **Example Response**:
  ```json
  {
    "message": "Password updated successfully"
  }



 
## Route: `/weather/favorite`
- **Request Type**: `GET`
- **Purpose**: Get the user's favorite location.
- **Request Body**: None
- **Response Format**: JSON
  - **Success Response Example**:
    - **Code**: 200
    - **Content**:
      ```json
      { [] }
      ```
- **Example Request**:
  ```json
  {"Boston"}



## Route: `/weather/<city>`
- **Request Type**: `GET`
- **Purpose**: Get the weather for the user's chosen city.
- **Request Body**:
  - `city` (String): any city.
- **Response Format**: JSON
  - **Success Response Example**:
    - **Code**: 200
    - **Content**:
      ```json
      {
        "curr": 43.57,
        "high": 45.3,
        "location": "Boston",
        "low": 43.57,
        "main": "Mist"
      }
      ```
- **Example Request**:
  ```json
  {
    "city": "Boston"
  }
- **Example Response**:
  ```json
  {
    "curr": 43.57,
    "high": 45.3,
    "location": "Boston",
    "low": 43.57,
    "main": "Mist"
  }


## Route: `/weather/forecast/<city>`
- **Request Type**: `GET`
- **Purpose**: Get the forecast for the user's chosen city.
- **Request Body**:
  - `city` (String): any city.
- **Response Format**: JSON
  - **Success Response Example**:
    - **Code**: 200
    - **Content**:
      ```json
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
      ```
- **Example Request**:
  ```json
  {
    "city": "Boston"
  }
- **Example Response**:
  ```json
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



## Route: `/weather/air/<city>/<state_code>/<country_code>`
- **Request Type**: `GET`
- **Purpose**: Get the air quality for the user's chosen city.
- **Request Body**:
  - `city` (String): any city.
  - `state_code` (String): any state.
  - `country_code` (String): any country.
- **Response Format**: JSON
  - **Success Response Example**:
    - **Code**: 200
    - **Content**:
      ```json
      {
        "air": "good"
      }
      ```
- **Example Request**:
  ```json
  {
    "city": "Boston",
    "state_code": "MA",
    "country_code": "US"
  }
- **Example Response**:
  ```json
  {
    "air": "good"
  }

## Route: `/weather/alerts/<state_code>`
- **Request Type**: `GET`
- **Purpose**: Get the weather alerts for the user's chosen state.
- **Request Body**:
  - `state_code` (String): the state code (e.g., "MA").
- **Response Format**: JSON
  - **Success Response Example**:
    - **Code**: 200
    - **Content**:
      ```json
      {
        "data": "* WHAT...Mixed precipitation expected. Total snow and sleet\naccumulations of 1 to 3 inches and ice accumulations around one\ntenth of an inch.\n\n* WHERE...In Massachusetts, Northern Berkshire County. In Vermont,\nBennington and Windham Counties.\n\n* WHEN...Until 10 AM EST Tuesday.\n\n* IMPACTS...Plan on slippery road conditions. The hazardous\nconditions could impact the Monday evening and Tuesday morning\ncommutes.\n\n* ADDITIONAL DETAILS...Snow and sleet will continue into this\nevening. The precipitation will transition to plain rain and\nfreezing rain tonight. Freezing rain and freezing drizzle will\ncontinue especially over elevated surfaces overnight into Tuesday\nmorning with light ice accumulations."
      }
      ```
- **Example Request**:
  ```json
  {
    "state_code": "MA"
  }
- **Example Response**:
  ```json
  {
    "data": "* WHAT...Mixed precipitation expected. Total snow and sleet\naccumulations of 1 to 3 inches and ice accumulations around one\ntenth of an inch.\n\n* WHERE...In Massachusetts, Northern Berkshire County. In Vermont,\nBennington and Windham Counties.\n\n* WHEN...Until 10 AM EST Tuesday.\n\n* IMPACTS...Plan on slippery road conditions. The hazardous\nconditions could impact the Monday evening and Tuesday morning\ncommutes.\n\n* ADDITIONAL DETAILS...Snow and sleet will continue into this\nevening. The precipitation will transition to plain rain and\nfreezing rain tonight. Freezing rain and freezing drizzle will\ncontinue especially over elevated surfaces overnight into Tuesday\nmorning with light ice accumulations."
  }

## Route: `/weather/favorite/save/<city>`
- **Request Type**: `PUT`
- **Purpose**: Add the user-chosen city to a list of favorites.
- **Request Body**:
  - `city` (String): the city to be added to the list of favorites (e.g., "Boston").
- **Response Format**: JSON
  - **Success Response Example**:
    - **Code**: 200
    - **Content**:
      ```json
      [
        "Boston"
      ]
      ```
- **Example Request**:
  ```json
  {
    "city": "Boston"
  }
- **Example Response**:
  ```json
  {
    "Boston"
  }