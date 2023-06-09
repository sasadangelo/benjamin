# app/routes/employee_routes.py
from flask import render_template, request, redirect, url_for
from app.models.employee import Employee
from app.models import db
from app.services.employee_service import EmployeeService
from . import employee_bp

@employee_bp.route('/create', methods=['POST'])
def create_employee():
    employee_name = request.form['employee_name']
    EmployeeService.create_employee(employee_name)
    return redirect(url_for('employee_bp.index'))

@employee_bp.route('/delete/<int:employee_id>', methods=['POST'])
def delete_employee(employee_id):
    employee = EmployeeService.get_employee_by_id(employee_id)
    if employee:
        EmployeeService.delete_employee(employee)
    return redirect(url_for('employee_bp.index'))
