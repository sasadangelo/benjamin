from flask import Blueprint
from ..controllers.employees_controller import get_employees, create_employee, update_employee, delete_employee

employees_blueprint = Blueprint('employees_blueprint', __name__)

employees_blueprint.route('/employees', methods=['GET'])(get_employees)
employees_blueprint.route('/create-employee', methods=['GET'])(create_employee)
employees_blueprint.route('/create-employee', methods=['POST'])(create_employee)
employees_blueprint.route('/update-employee/<int:id>', methods=['GET'])(update_employee)
employees_blueprint.route('/update-employee/<int:id>', methods=['POST'])(update_employee)
employees_blueprint.route('/delete-employee/<int:id>', methods=['GET'])(delete_employee)
