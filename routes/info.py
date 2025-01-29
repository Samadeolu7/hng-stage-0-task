from fastapi import APIRouter
from fastapi.responses import JSONResponse
from datetime import datetime

router = APIRouter()

@router.get("/info", response_class=JSONResponse)
def get_info():
    return {
        "email": "samadeolu7@gmail.com",
        "current_datetime": datetime.now().isoformat() + "Z",
        "github_url": "https://github.com/samadeolu7/hng-stage-0-task"
    }