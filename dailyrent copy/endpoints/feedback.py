# -------------------------------------FEEDBACK--------/api/v1/feedback----------------------------------------------------------------------------------
from fastapi import Depends, status, BackgroundTasks
from sqlalchemy.orm import Session

from database.database import get_db
from models.enum import FeedbackRating
from schemas.schemas import BaseFeedbackScheme, UserInScheme
from services.feedback_services import feedback_services
from services import user_services

from fastapi import FastAPI
app = FastAPI()
v1 = FastAPI()
app.mount("/api/v1", v1)


@v1.post('/feedback', status_code=status.HTTP_201_CREATED)
async def create_feedback(
                        rating: FeedbackRating,
                        background_tasks: BackgroundTasks, 
                        schema: BaseFeedbackScheme,
                        current_user: UserInScheme = Depends(user_services.get_current_is_active_user),
                        db: Session = Depends(get_db)):
    return feedback_services.create_feedback(db, schema, current_user, rating, background_tasks)
