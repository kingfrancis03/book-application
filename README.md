## Book Application

Demonstration of my exisiting Python3 skills
An application that reads, saves, updates, and deletes addresses

My approach to this assignment involves taking an address, obtaining its coordinates, and saving it to the database. For each inputted address, I utilize the geopy's Nominatim library to extract coordinates and additional data. However, I have encountered legitimate addresses from the Philippines that throw errors because there are no recorded towns, house numbers, or streets. Therefore, I have implemented a solution to strip the inputted string address until I obtain a valid address.

# Limitiations

- Using the Geopy API, the saved coordinates are not accurate, some are not precise enough, resulting in a loss of about 5 to 10 meters.

## Features
- Create, Update, Delete Adresses
- Get List of All Address
- Given longitude, latitude and proximity, Retrieves saved addresses within the range of proximity

## Technology

- FastAPI - For rest framework
- SQLAlchemy - For Database ORM
- SQLite - Database
- Geopy - GeoLocation Library
- Nominatim - GeoLocation API

## Installation

This App requires ***python_version=3.9*** to run.

1. clone this repository into your local

```sh
git clone https://github.com/kingfrancis03/book-application.git
```

2. Choose an virutal env of your chice and pip install the requirements.txt

```sh
pip install -r requirements.txt
```

## How to Run
```sh
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

# Open Swagger

 **<http://localhost:8000/docs>**
 
 ## Endpoints

1. ### Get Addresses

   - **Description:** Get all the list of addresses saved in the database.
   - **Method:** `GET`
   - **Path:** `/address`
   - **Query Params**
      - `address_id`(Optional): To get a single address 
   - **Response:**
     - `200 OK`: Successful response.
     ```json
        {
          "status": "string",
          "message": "string",
          "data": [
            {
              "input_address": "string",
              "address_id": 0,
              "latitude": 0,
              "longitude": 0
            }
          ]
        }
     ```
2. ### Create Addresses

   - **Description:** Create address.
   - **Method:** `POST`
   - **Path:** `/address`
   - **Request Body:**
     ```json
     {
        "input_address": "string"
     }
     ```
   - **Response:**
     - `200 OK`: Successful response.
     ```json
        {
          "status": "string",
          "message": "string",
          "data": {
            "address_id": 0
        }
     ```
     - Failed response.
     ```json
      {
        "detail": {
            "message": "string"
         }
      }
     ```
3. ### Update Address

   - **Description:** Update address with addressID
   - **Method:** `PUT`
   - **Path:** `/address/<address_id>`
   - **Request Body:** (if applicable)
     ```json
     {
        "input_address": "string"
     }
     ```
   - **Response:**
     - `200 OK`: Successful response.
     ```json
        {
          "status": "string",
          "message": "string",
          "data": {
            "address_id": 0
        }
        }
     ```
     - Failed response.
     ```json
      {
        "detail": {
            "message": "string"
         }
      }
     ```
  4. ### Delete Address

   - **Description:** Delete address with addressID
   - **Method:** `DELETE`
   - **Path:** `/address/<address_id>`
   - **Response:**
     - `200 OK`: Successful response.
     ```json
        {
          "status": "string",
          "message": "string",
          "data": {
            "deleted_address_id": 0
          }
        }
     ```
     - Failed response.
     ```json
      {
        "detail": {
            "message": "string"
         }
      }
     ```
5. ### Find Address Nearby

   - **Description:** Find Address Nearby with coordinates and proximity
   - **Method:** `GET`
   - **Path:** `/address/address-nearby`
   - **Query Params:**
     - `longitude`
     - `latitude`
     - `proximity`: range of distance to be search within the area measured by kilometer
   - **Response:**
     - `200 OK`: Successful response.
     ```json
        {
          "status": "string",
          "message": "string",
          "data": [
            {
              "input_address": "string",
              "address_id": 0,
              "latitude": 0,
              "longitude": 0
            }
          ]
        }
     ````