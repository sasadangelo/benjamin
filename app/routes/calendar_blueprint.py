from flask import Blueprint
from ..controllers.calendar_controller import get_calendar

calendar_bp = Blueprint('calendar_blueprint', __name__)

calendar_bp.route('/calendar', methods=['GET'])(get_calendar)
