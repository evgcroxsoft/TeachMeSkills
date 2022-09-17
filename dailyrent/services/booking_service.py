# -------------------------------------------------BookingServices---------------------------------------------------------------------------------
import enum
from datetime import datetime, timedelta, date
from fastapi import HTTPException, status

from models.models import Accommodation, Booking
from models.enum import BookingStatus
import tasks


class BookingService():

    async def create_booking(self, db, schema, current_user, background_tasks):
        '''
        Check and compare dates, if ok
        '''
        if current_user.renter:
            data = schema.dict()
            if self.check_is_available_booking(db, data['accommodation_id'], data['date_start'], data['date_end']) == True or None:
                accommodation = db.query(Accommodation).filter_by(id=data['accommodation_id']).first()
                data['user_id'] = current_user.id
                data['price'] = accommodation.price
                data['status'] = BookingStatus.WAITING
                data['created_at'] = datetime.utcnow()
                user = Booking(**data)
                db.add(user)
                db.commit()
                db.refresh(user)
                background_tasks.add_task(tasks.send_email)
                return user
            else:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No dates to create bookings, choose another")        
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No rights to create bookings")


    async def get_booking(self, db, id, current_user):
        booking = db.query(Booking).filter_by(user_id=current_user.id, id=id).first()
        return booking

    async def update_booking(self, db, id, current_user, schema):
        data = schema.dict()
        booking = self.get_booking(db, id, current_user)
        for key, value in data.items():
            setattr(booking, key, value)
        booking.updated_at = datetime.datetime.utcnow()
        db.commit()
        db.refresh(booking)
        return booking

    async def delete_booking(self, db, id, current_user):
        specify_booking = db.query(Booking).filter_by(user_id=current_user.id, id=id).first()
        if specify_booking.status == BookingStatus.WAITING:
            db.delete(specify_booking)
            db.commit()
            raise HTTPException(status_code=status.HTTP_200_OK,
                                detail='Specify booking was deleted successfully')

    async def check_dates_booking(self, b1: date, b2: date, s1: date, s2: date) -> True:
        booking_period = [b1 + timedelta(days=x) for x in range((b2-b1).days + 1)]
        searching_period = [s1 + timedelta(days=x) for x in range((s2-s1).days + 1)]
        for book in booking_period:
            for search in searching_period:
                if book == search:
                    return True


    async def check_status_booking(self, status: enum, bookings):
        filtered_booking = [booking for booking in bookings if booking.status == status or status is None]
        return filtered_booking


    async def check_is_available_booking(self, db, accommodation_id, searching_date_start, searching_date_end):
        '''
        Func returns True if booking is available for searching:
        '''
        bookings = db.query(Booking).filter_by(accommodation_id=accommodation_id).all()
        if bookings == []: # if accommodation hasn't any bookings
            return True

        results = []
        for booking in bookings:
            
            if booking.status == BookingStatus.DECLINED or booking.status == BookingStatus.FINISHED:
                return True
            elif booking.status == BookingStatus.WAITING or booking.status == BookingStatus.APPROVED:
                # True if dates match!
                check_dates = await self.check_dates_booking(booking.date_start, booking.date_end, searching_date_start, searching_date_end)
                results.append(check_dates)
        if [bool for bool in results if bool is True]: # Check all bokings in one accommodation do they have True, if Yes, return False!
            return False
        else:
            return True


booking_services = BookingService()
