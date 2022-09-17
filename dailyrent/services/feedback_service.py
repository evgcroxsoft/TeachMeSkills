# -------------------------------------------------FeedbackServices---------------------------------------------------------------------------------
from fastapi import HTTPException, status

from models.models import Accommodation, Booking, RenterFeedback, HosterFeedback
from models.enum import BookingStatus
import tasks


class FeedbackService():

    async def create_feedback(self, db, schema, current_user, rating, background_tasks):
        '''
        Func check Renter or Hoster and store feedback in DB
        '''
        data = schema.dict()
        booking_in_db = db.query(Booking).filter_by(id=data['booking_id']).first()
        if booking_in_db:
            if not await self.feedback_create_if_renter(db, data, current_user, booking_in_db, background_tasks, rating):
                await self.feedback_create_if_hoster(db, data, current_user, booking_in_db, background_tasks, rating)
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No bookings in db")


    async def feedback_create_if_renter(self, db, data, current_user, booking_in_db, background_tasks, rating):
        '''
        Func check Renter and save data in table RenterFeedback:
        1. Is it your booking?
        2. Is booking status is finished?
        3. Have you left your review before?
        '''
        if current_user.renter:
            if booking_in_db.user_id == current_user.id and booking_in_db.status == BookingStatus.FINISHED:
                if db.query(RenterFeedback).filter_by(user_id=current_user.id, booking_id=booking_in_db.id).first():
                    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="You have already left feedback")
                else:
                    data['user_id'] = current_user.id
                    data['rating'] = rating
                    feedback = RenterFeedback(**data)
                    db.add(feedback)
                    db.commit()
                    db.refresh(feedback)
                    background_tasks.add_task(tasks.send_email)
                    return feedback
            else:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Booking status not finished")
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No rights to create feedback")   


    async def feedback_create_if_hoster(self, db, data, current_user, booking_in_db, background_tasks, rating):
        '''
        Func check Hoster and save data in table HosterFeedback:
        1. Is this booking related to your accommodation?
        2. Is booking status is finished?
        3. Have you left your review before?
        '''
        if current_user.hoster: 

            booking_accommodation = db.query(Booking, Accommodation).join(Accommodation).filter_by(id=booking_in_db.id, user_id=current_user.id).first()
            hoster_feedback = db.query(HosterFeedback).filter_by(user_id=current_user.id, booking_id=booking_in_db.id).first()

            if booking_accommodation and booking_in_db.status == BookingStatus.finished:
                if hoster_feedback:
                    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="You have already leaved feedback")
                else:
                    data['user_id'] = current_user.id
                    data['rating'] = rating
                    feedback = HosterFeedback(**data)
                    db.add(feedback)
                    db.commit()
                    db.refresh(feedback)
                    background_tasks.add_task(tasks.send_email)
                    return feedback
            else:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Booking status not finished")
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No rights to create feedback")  


feedback_services = FeedbackService()