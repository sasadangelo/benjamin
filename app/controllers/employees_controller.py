from app.models.employee import Employee
from flask import render_template, request, redirect, url_for, abort
from app.models import db
from app.services.employees_service import EmployeeService

GET_EMPLOYEES_ENDPOINT = 'employees_bp.get_employees'

def get_employees():
    employees = get_all_employees()
    return render_template("index.html", employees = employees)

def delete_employee(id):
    delete_employee_by_id(id)

    # Reindirizza l'utente alla pagina delle gare
    return redirect(url_for(GET_EMPLOYEES_ENDPOINT))

def create_employee():
    if request.method == 'GET':
        return render_template('create-employee.html')

    employee_data = {
        'name': request.form['employee_name'],
    }

    create_new_employee(employee_data)

    # Reindirizza l'utente alla pagina delle gare
    return redirect(url_for(GET_EMPLOYEES_ENDPOINT))

def update_create_new_employee(id):
    employee = get_employee_by_id(id)
    if employee is None:
        abort(404)

    if request.method == 'GET':
        return render_template('update-employee.html', employee = employee)

    employee_data = {
        'name': request.form['employee_name'],
    }

    employee_datas_service.update_employee_data(id, employee_data_data)

    # reindirizza l'utente alla pagina delle gare
    return redirect(url_for(GET_EMPLOYEES_ENDPOINT))




