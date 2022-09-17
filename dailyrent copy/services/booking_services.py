# -------------------------------------------------BookingServices---------------------------------------------------------------------------------
from datetime import timedelta
from fastapi import HTTPException, status

from models.models import Accommodation, Booking
from models.enum import BookingStatus
import tasks


class BookingServices():

    def create_booking(self, db, schema, current_user, background_tasks):
        '''
        Check and compare dates, if ok
        '''
        if current_user.renter:
            data = schema.dict()
            if self.check_is_available_booking(db, data['accommodation_id'], data['date_start'], data['date_end']) == True or None:
                accommodation = db.query(Accommodation).filter_by(id=data['accommodation_id']).first()
                data['user_id'] = current_user.id
                data['price'] = accommodation.price
                data['status'] = BookingStatus.waiting
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


    def get_booking(self, db, id, current_user):
        booking = db.query(Booking).filter_by(
            user_id=current_user.id).filter_by(id=id).first()
        return booking

    def update_booking(self, db, id, current_user, schema):
        data = schema.dict()
        booking = self.get_booking(db, id, current_user)
        for key, value in data.items():
            setattr(booking, key, value)
        db.commit()
        db.refresh(booking)
        return booking

    def delete_booking(self, db, id, current_user):
        specify_booking = db.query(Booking).filter_by(
            user_id=current_user.id).filter_by(id=id).first()
        if specify_booking.status == BookingStatus.waiting:
            db.delete(specify_booking)
            db.commit()
            raise HTTPException(status_code=status.HTTP_200_OK,
                                detail='Specify booking was deleted successfully')

    def check_dates_booking(self, b1, b2, s1, s2):
        booking_period = [b1 + timedelta(days=x) for x in range((b2-b1).days + 1)]
        searching_period = [s1 + timedelta(days=x) for x in range((s2-s1).days + 1)]
        for book in booking_period:
            for search in searching_period:
                if book == search:
                    return True


    def check_status_booking(self, status, bookings_db):
        filtered_booking = []
        for booking in bookings_db:
            if booking.status == status or status == None:
                filtered_booking.append(booking)
        return filtered_booking

    def check_is_available_booking(self, db, accommodation_id, searching_date_start, searching_date_end):
        '''
        Func returns True if booking is available for searching:
        '''
        booking_in_db = db.query(Booking).filter_by(accommodation_id=accommodation_id).all()

        if booking_in_db == []: # if accommodation hasn't any bookings
            return True

        result = []
        for booking in booking_in_db:

            if booking.status == BookingStatus.declined or booking.status == BookingStatus.finished:
                return True

            elif booking.status == BookingStatus.waiting or booking.status == BookingStatus.approved:
                compare_dates = self.check_dates_booking(booking.date_start, booking.date_end, searching_date_start, searching_date_end)
                result.append(compare_dates) # create list of all compare_dates True and False

            for bool in result:
                if bool == True: return False # Rerurn True if booking with status waiting or approved has the dates are not free

booking_services = BookingServices()
