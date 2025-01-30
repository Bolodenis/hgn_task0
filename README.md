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
