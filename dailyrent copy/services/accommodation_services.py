# -------------------------------------------------AccommodationServices---------------------------------------------------------------------------------
from fastapi import HTTPException, status

from models.models import Accommodation
from services.booking_services import booking_services


class AccommodationServices():

    def create_accommodation(self, db, schema, current_user, type, city, country):
        if current_user.hoster:
            data = schema.dict()
            data['user_id'] = current_user.id
            data['type'] = type
            data['city'] = city
            data['country'] = country
            user = Accommodation(**data)
            db.add(user)
            db.commit()
            db.refresh(user)
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="No rights to create accommodations")
        return user

    def get_accommodation(self, db, id, current_user):
        accommodation = db.query(Accommodation).filter_by(
            user_id=current_user.id).filter_by(id=id).first()
        return accommodation

    def update_accommodation(self, db, id, current_user, schema, type, city, country):
        data = schema.dict()
        data['type'] = type
        data['city'] = city
        data['country'] = country
        accommodation = self.get_accommodation(db, id, current_user)
        for key, value in data.items():
            setattr(accommodation, key, value)
        db.commit()
        db.refresh(accommodation)
        return accommodation

    def delete_accommodation(self, db, id, current_user):
        specify_accommodation = db.query(Accommodation).filter_by(
            user_id=current_user.id).filter_by(id=id).first()
        db.delete(specify_accommodation)
        db.commit()
        raise HTTPException(status_code=status.HTTP_200_OK,
                            detail='Specify accommodation was deleted successfully')


    def searching_accommodations(self, date_start, date_end, type, persons, city, country, db):
        filtered_accommodation = []
        accommodation_in_db = db.query(Accommodation).all()

        for accommodation in accommodation_in_db:

            if accommodation.country == country or country == None:

                if accommodation.city == city or city == None:

                    if accommodation.type == type or type == None:

                        if accommodation.persons == persons or persons == None:
                            
                            if booking_services.check_is_available_booking(db, accommodation.id, date_start, date_end):
                                filtered_accommodation.append(accommodation)
        if filtered_accommodation == []:
            raise HTTPException(status_code=status.HTTP_200_OK, detail='Sorry but no free accommodation')
        return filtered_accommodation    


accommodation_services = AccommodationServices()