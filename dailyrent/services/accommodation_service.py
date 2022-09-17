# -------------------------------------------------AccommodationServices---------------------------------------------------------------------------------
import datetime
from fastapi import HTTPException, status
from models.enum import BookingStatus

from models.models import Accommodation, Booking
from services.booking_service import booking_services


class AccommodationService():

    async def create_accommodation(self, accommodation_type, city, country, schema, current_user, db):
        if current_user.hoster:
            data = schema.dict()
            data['user_id'] = current_user.id
            data['accommodation_type'] = accommodation_type
            data['city'] = city
            data['country'] = country
            data['created_at'] = datetime.datetime.utcnow()
            user = Accommodation(**data)
            db.add(user)
            db.commit()
            db.refresh(user)
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="No rights to create accommodations")
        return user

    async def get_accommodation(self, db, id, current_user):
        accommodation = db.query(Accommodation).filter_by(user_id=current_user.id, id=id).first()
        return accommodation

    async def update_accommodation(self, db, id, current_user, schema, accommodation_type, city, country):
        data = schema.dict()
        data['accommodation_type'] = accommodation_type
        data['city'] = city
        data['country'] = country
        accommodation = await self.get_accommodation(db, id, current_user)
        for key, value in data.items():
            setattr(accommodation, key, value)
        accommodation.updated_at = datetime.datetime.utcnow()
        db.commit()
        db.refresh(accommodation)
        return accommodation

    async def delete_accommodation(self, db, id, current_user):
        specify_accommodation = db.query(Accommodation).filter_by(user_id=current_user.id, id=id).first()
        db.delete(specify_accommodation)
        db.commit()
        raise HTTPException(status_code=status.HTTP_200_OK, detail='Specify accommodation was deleted successfully')


    async def searching_accommodations(self, date_start, date_end, country, city, accommodation_type, persons, db):
        filtered_accommodation = []
        
        accommodation = db.query(Accommodation).all()

        for accommodation in accommodation:

            if ((accommodation.country == country or country is None) and
                (accommodation.city == city or city is None) and
                (accommodation.accommodation_type == accommodation_type or accommodation_type is None) and
                (accommodation.persons == persons or persons is None) and
                (await booking_services.check_is_available_booking(db, accommodation.id, date_start, date_end))):
                
                accommodation = {
                        'id': accommodation.id, 
                        'name': accommodation.name, 
                        'persons': accommodation.persons, 
                        'accommodation_type': accommodation.accommodation_type,
                        'city': accommodation.city,
                        'country': accommodation.country,
                        'price': accommodation.price,
                        'is_active': accommodation.is_active,
                        'created_at': accommodation.created_at,
                        'updated_at': accommodation.updated_at,
                                }
                filtered_accommodation.append(accommodation)

        if filtered_accommodation == []:
            raise HTTPException(status_code=status.HTTP_200_OK, detail='Sorry but no free accommodation')
        return filtered_accommodation


    async def get_all_accommodations(self, db, current_user):
        filtered_accommodation = []
        accommodation = db.query(Accommodation).filter_by(user_id=current_user.id).all()

        for accommodation in accommodation:
            bookings = db.query(Booking).filter_by(accommodation_id=accommodation.id).all()
            bookings = [
                        {           
                        'id': booking.id,
                        'date_start': booking.date_start,
                        'date_end': booking.date_end,
                        'persons': booking.persons,
                        'price': booking.price,
                        'status': booking.status,
                        'created_at': booking.created_at,
                        'updated_at': booking.updated_at}
                        for booking in bookings if booking.status == BookingStatus.WAITING or booking.status == BookingStatus.FINISHED ]

            accommodation = {
                        'id': accommodation.id, 
                        'name': accommodation.name, 
                        'persons': accommodation.persons, 
                        'accommodation_type': accommodation.accommodation_type,
                        'city': accommodation.city,
                        'country': accommodation.country,
                        'price': accommodation.price,
                        'is_active': accommodation.is_active,
                        'created_at': accommodation.created_at,
                        'updated_at': accommodation.updated_at,
                        'bookings': bookings}

            filtered_accommodation.append(accommodation)

        return filtered_accommodation


accommodation_services = AccommodationService()

