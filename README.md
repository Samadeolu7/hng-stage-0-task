# HNG12 Stage 0 Task

## Project Description

This is a public API that returns basic information including the registered email address, current datetime, and GitHub URL of the project's codebase.

## Setup Instructions

1. Clone the repository:

    git clone https://github.com/yourusername/your-repo.git
    cd your-repo


2. Create a virtual environment and activate it:

    python -m venv my_env
    `venv\Scripts\activate`


3. Install the dependencies:

    pip install -r requirements.txt


4. Run the application:

    gunicorn -c gunicorn_config.py main:app


## API Documentation

### Endpoint URL

`GET /`

### Request/Response Format

#### Response (307 Temporary Redirect)
The client is redirected to `/info`.

`GET /info`

### Request/Response Format

#### Response (200 OK)

{
  "email": "samadeolu7@gmail.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/samadeolu7/hng-stage-0-task"
}

## Example Usage


curl -X GET "http://127.0.0.1:8000/info"


## Backlink

[Backlink to HNG python](https://hng.tech/hire/python-developers)