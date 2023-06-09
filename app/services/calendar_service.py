# app/services/team_service.py
from app.models.team import Calendar, db

class CalendarService:
    @staticmethod
    def get_all_calendars():
        return Calendar.query.all()