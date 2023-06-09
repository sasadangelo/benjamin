from flask import Blueprint
from ..controllers.employees_controller import get_employees, create_employee, update_employee, delete_employee

employees_bp = Blueprint('employees_blueprint', __name__)

employees_bp.route('/employees', methods=['GET'])(get_employees)
employees_bp.route('/create-employee', methods=['GET'])(create_employee)
employees_bp.route('/create-employee', methods=['POST'])(create_employee)
employees_bp.route('/update-employee/<int:id>', methods=['GET'])(update_employee)
employees_bp.route('/update-employee/<int:id>', methods=['POST'])(update_employee)
employees_bp.route('/delete-employee/<int:id>', methods=['GET'])(delete_employee)
