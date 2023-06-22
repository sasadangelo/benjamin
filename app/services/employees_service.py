from app import db
from app.models.employees import Employee

def get_all_employees():
    return Employee.query.all()

def get_employee_by_id(employee_id):
    return Employee.query.get(employee_id)

def delete_employee_by_id(id):
    employee = Employee.query.get(id)
    if employee:
        db.session.delete(employee)
        db.session.commit()

def create_employee(employee_data):
    employee = Employee(
        name=employee_data['name']
    )
    db.session.add(employee)
    db.session.commit()

def update_employee(id, employee_data):
    employee = Employee.query.get(id)
    if employee:
        employee.name=employee_data['name']
        db.session.commit()
