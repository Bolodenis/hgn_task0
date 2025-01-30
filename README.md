# Backend Stage 0 Task - Public API

## Project Description
This project is the implementation of the Stage 0 task for the HNG12 Backend internship. The goal of the task is to develop a public API that provides basic information about the developer, including:

- The registered email address.
- The current datetime (UTC) in ISO 8601 format.
- The GitHub URL of the project repository.

The API is developed using **Flask** and is deployed to a publicly accessible platform.

## API Endpoint
- **URL**: `https://<your-deployed-url>/`
- **Method**: `GET`

### Example Response:
```json
{
  "email": "your-email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/yourusername/hgn_task0"
}
```

# Technology Stack
- Programming Language: Python
- Framework: Flask
- CORS: Flask-CORS (for Cross-Origin Resource Sharing)
- DateTime: Python's datetime library for current UTC time

# Setup Instructions
# Prerequisites
Make sure you have Python 3.x installed on your local machine. You will also need pip for managing Python packages.

# Installation Steps
## Clone the repository:
```
git clone https://github.com/yourusername/hgn_task0.git
```
## Navigate to the project directory:
```
cd hgn_task0
```
## Create a virtual environment and activate it:
- On Windows:
```
  python -m venv venv
.\venv\Scripts\activate

```
- On MacOs:
```
python3 -m venv venv
source venv/bin/activate
```

## Install the required dependencies:
```
pip install -r requirements.txt
```
## Run the application:
```
python3 app.py
```

This will start the Flask server locally, and the API will be available at http://127.0.0.1:5000/.

# API Documentation
## Endpoint: /
- Method: GET
- Response Format: JSON
## Response Example:
```
{
  "email": "bollodenis@gmail.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/yourusername/hgn_task0"
}
```
# Deployment Instructions
This API has been deployed on Render. You can access the live version here:
- URL: https://<[my_url](https://hgn-task0.onrender.com/)]

# License
### Key Sections:
1. **Project Description**: Describes the task and purpose of the project.
2. **API Endpoint**: Specifies the URL and method of the API.
3. **Technology Stack**: Lists the technologies used (Flask, Python, CORS, etc.).
4. **Setup Instructions**: Explains how to set up the project locally, including installing dependencies and running the Flask server.
5. **API Documentation**: Provides details on how to interact with the API and gives a sample response.
6. **Backlink**: Includes a required backlink to the job portal for hiring developers, based on the stack used.
7. **Deployment**: Mentions the deployed URL for the live version of the API.

## Hire Python Developers
Looking to hire skilled Python developers? Check out [HNG Python Developers](https://hng.tech/hire/python-developers).









