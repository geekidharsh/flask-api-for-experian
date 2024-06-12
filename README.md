# Flask API

## Gene Data Processor. 
A Flask based API that provides two endpoints for data processing and health checks. 
It processes data from a CSV file based on the specified timestamp and performs a health check to ensure that the API is running fine.


## Endpoints

### Health Check - GET

- **URL**: `/health`
- **HTTP Method**: GET
- **Description**: This endpoint is used to verify if the API is running fine. 

- **Response**:
  - Status: `200 OK`
  - Content: JSON object containing the following keys:
    - `status`: Status of the API (`"success"`)
    - `message`: A message indicating the health status of the API.

### Get Data - POST

- **URL**: `/getData`
- **HTTP Method**: POST
- **Description**: The API expects a JSON payload containing the timestamp to filter the data.
- **Request Payload**:
  - Content: JSON object containing the following key:
    - `timestamp`: A string in the format `"MM-DD-YYYY"`
    - Sample:
    -   `{"timestamp": "07-02-2023"}`
- **Response**:
  - If the data structure is valid and the timestamp is correct, the API responds with a success message and the processed data.
    - Status: `200 OK`
    - Content: JSON object containing the following keys:
      - `status`: Status of the response 
      - `message`: A message indicating the processing status (`"Data processed successfully."`)
      - `data`: A list of dictionaries representing the processed data for the specified timestamp.

  - If the request payload is invalid or the timestamp format is incorrect, the API responds with an error message.
    - Status: `400 Bad Request`
    - Content: JSON object containing the following keys:
      - `status`: `"error"`
      - `message`: `"Invalid data structure"`

## How to Use

1. Install dependencies: `flask`, `pandas`, `request`

2. Run the API: To start the API server, run the following command in the terminal:
`python api-server.py`

3. Once the flask app is running, following are the two end points:
  - `http://127.0.0.1:5000/health - GET`
  - `http://127.0.0.1:5000/getData - POST`
4. An export of postman collection is included in the project for easy set up
