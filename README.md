# Hinge Homework

## How to use

### Run the setup script

./setup_project.sh

This will download the necessary packages for the python project and initialize
the database with tables and some data.


### Run the api

python3.7 app.py

That will start the api for testing.


## Database schema

The database is setup using the script setup_database.py. The schema is
described in the file database.json. Some dummy data defined in dummy_data.json
is entered at initialization as well.

### USER table

Represents a user of the app. 

- id            INTEGER PRIMARY KEY     Unique identifier for the user
- first_name    STRING                  First name
- last_name     STRING                  Last name
- description   STRING                  Short description
- birthdate     STRING  CANNOT BE NULL  Birthdate of the user
- gender        STRING                  Gender of the user      F/M/null
- gender_target STRING                  Gender preferences      F/M/null


### RATING table

Stores the rating between users.

- user          INTEGER PRIMARY KEY     Id of the user that entered the rating
- user_target   INTEGER PRIMARY KEY     Id of the user rated
- type          STRING                  Type of rating          L/B/R
- time          STRING                  Date/time of the rating

The types of ratings are:
- L:    Likes
- B:    Blocks
- R:    Reports


## Versionning

The versions available are v1 and v2. They prefix all endpoints in the api.

Differences between v1 and v2:
- "name" was renamed "first_name" in user definition
- new fields "last_name", "gender", "gender_target" in user definition
- the list of recommendations can be filtered with the gender / gender_target. 
  Those who have null values in those field will be included regardless.


## Endpoints

### /<string:version>/users
#### GET

Return the list of all users in the database.

#### V1 Response
{
  "users": [
    {
      "id": 101,
      "name": "Alice",
      "description": "Lorem Ipsum",
      "birthdate": "01/01/1990"
    },
    {
      "id": 102,
      "name": "Bob",
      "description": "Hi there",
      "birthdate": "03/30/1990"
    }
  ]
}

#### V2 Response
{
  "users": [
    {
      "id": 101,
      "first_name": "Alice",
      "last_name": "Smith",
      "birthdate": "01/01/1990",
      "description": "Lorem Ipsum",
      "gender": null,
      "gender_target": null
    },
    {
      "id": 102,
      "first_name": "Bob",
      "last_name": "John",
      "birthdate": "03/30/1990",
      "description": "Hi there",
      "gender": "M",
      "gender_target": null
    }
  ]
}

#### POST

Create a new user and return the information about that user. 

The user profile must be described as a JSON object, except for the id that
will be generated automatically. The description of the user depends on the
version. 
- If non-mandatory fields are not provided in the request, they will be null.
- If mandatory fields are not provided in the request, an error message will be
returned (mandatory fields are name/first_name and birthdate).

The response will be the description of the user plus the id.

##### V1 Request/Response
Request:
{
  "name": "Georges",
  "description": "Lorem Ipsum",
  "birthdate": "01/01/1990"
}
Response:
{
  "users": {
    "id": 107,
    "name": "Georges",
    "description": "Lorem Ipsum",
    "birthdate": "01/01/1990"
  }
}

##### V2 Response
Request:
{
  "users": {
    "first_name": "Georges",
    "last_name": "",
    "birthdate": "10/10/1990",
    "description": "",
    "gender": "M",
  }
}
Response:
{
  "user": {
    "id": 107,
    "first_name": "Georges",
    "last_name": "",
    "birthdate": "10/10/1990",
    "description": "",
    "gender": "M",
    "gender_target": null
  }
}



### /<string:version>/users/<int:user_id>
#### GET

Return the list of a given user identified by their user_id.

#### V1 Response
{
  "users": {
    "id": 107,
    "name": "Georges",
    "description": "Lorem Ipsum",
    "birthdate": "01/01/1990"
  }


#### V2 Response
{
  "user": {
    "id": 107,
    "first_name": "Georges",
    "last_name": "",
    "birthdate": "10/10/1990",
    "description": "",
    "gender": "M",
    "gender_target": null
  }
}

#### PUT

Update the profile of a given user identified by their user_id. 

This request works the same way as POST /<int:version>/users. The request and
responses format are the same. 



### /<string:version>/users/<int:user_id>/likes
#### GET

List all incomming likes for a given user. Incomming likes are any users that
liked the user identified by <user_id>, but that <user_id> did not yet rate.

No JSON body has to be sent. 

##### V1 Reponse
{
  "likes": [
    [
      103
    ],
    [
      104
    ],
    [
      105
    ]
  ]
}

##### V2 Response
{
  "likes": [
    "/v2/users/103",
    "/v2/users/104",
    "/v2/users/105"
  ]
}



### /<string:version>/users/<int:user_id>/matches
#### GET

List all matches for a given user. Matches are any users that liked the user
identified by <user_id>, and that <user_id> also liked.

No JSON body has to be sent. 

The responses have the same format as for the likes.



### /<string:version>/users/<int:user_id>/recommendations
#### GET

List all recommendations for a given user. Recommendations are users that did
not yet rate the given user (either by liking, blocking or reporting them) and
that the given user has not rated yet either. 

In v1, no JSON body has to be sent. 
In v2, we can send filters for the gender and gender_target to filter the
search. If no JSON body is sent, the response will include everyone regardless
of gender or gender preferences. 

The responses have the same format as for the likes.

##### V2 Request
Two filters are available:
- gender specify which gender we want the matches to be. It can be "F" for
  women, "M" for men, or null if we want both. 
- gender_target specify what the recommended user is looking for. The values
  are the same than for gender.
{
  "gender": "F",
  "gender_target": "M"
}



### /<string:version>/users/<int:user_id>/<string:rating>/<int:user_target>
#### POST

The given user identified by <user_id> gives the rating <rating> to the user
identified by <user_target>. 

The responses are the same regardless of the version.

The rating options are:
- "likes"
- "blocks"
- "reports"

##### Response
{
  "rating": {
    "user": 101,
    "user_target": 102,
    "type": "L",
    "time": "2019-05-20 09:50:06.849060"
  }
}


## Error management

When an error occurs, an error response will be sent with this format:

{
  "error": {
    "status": 400,
    "title": "Could not set rating",
    "details": "user and user_target are equal"
  }
}

The title is a high-level description of the error
The details is a more detailed description of the error, if available
The status matches the HTTP status code response. Only 4 of them are used:
- 200   Successful request (not used in error responses)
- 400   Bad request - the call to the API has errors
- 404   Not found - the resource was not found
- 500   Internal Server Error - an error on the api side
