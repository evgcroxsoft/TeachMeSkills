#________________________________________________________FEEDBACK__________________________________________________________________________________

from fastapi import APIRouter, Depends, status, BackgroundTasks
from sqlalchemy.orm import Session

from database.app_db import get_db
from models.enum import FeedbackRating
from schemas.schemas import BaseFeedbackScheme, UserRetrieveScheme
from services.feedback_service import feedback_services
from services.user_service import user_services

router = APIRouter()


# ----------------------------------------------------/api/v1/feedback----------------------------------------------------------------------------------

@router.post('/feedback', status_code=status.HTTP_201_CREATED)
async def create_feedback(
                        rating: FeedbackRating,
                        background_tasks: BackgroundTasks, 
                        schema: BaseFeedbackScheme,
                        current_user: UserRetrieveScheme = Depends(user_services.get_current_is_active_user),
                        db: Session = Depends(get_db)):
    return await feedback_services.create_feedback(db, schema, current_user, rating, background_tasks)
  