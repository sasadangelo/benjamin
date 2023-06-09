# app/routes/__init__.py
from flask import Blueprint

team_bp = Blueprint('team_bp', __name__)
employee_bp = Blueprint('employee_bp', __name__)
calendar_bp = Blueprint('calendar_bp', __name__)

from . import team_routes, employee_routes, calendar_routes
