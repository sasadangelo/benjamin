# app/services/employee_service.py
from app.models.employee import Employee, db

class EmployeeService:
    @staticmethod
    def get_all_employees():
        return Employee.query.all()

    @staticmethod
    def get_employee_by_id(employee_id):
        return Employee.query.get(employee_id)

    @staticmethod
    def create_employee(name):
        employee = Employee(name=name)
        db.session.add(employee)
        db.session.commit()

    @staticmethod
    def delete_employee(employee):
        db.session.delete(employee)
        db.session.commit()
