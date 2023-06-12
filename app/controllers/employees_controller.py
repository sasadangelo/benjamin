from app.models.employees import Employee
from flask import render_template, request, redirect, url_for, abort
from app.services.employees_service import get_all_employees, get_employee_by_id, create_new_employee, update_employee, delete_employee_by_id
from app.services import employees_service

GET_EMPLOYEES_ENDPOINT = 'employees_blueprint.get_employees'

def get_employees():
    employees = get_all_employees()
    return render_template("employees.html", employees = employees)

def delete_employee(id):
    delete_employee_by_id(id)

    # Reindirizza l'utente alla pagina delle gare
    return redirect(url_for(GET_EMPLOYEES_ENDPOINT))

def create_employee():
    if request.method == 'GET':
        return render_template('create-employee.html')

    employee_data = {
        'name': request.form['name'],
    }

    create_new_employee(employee_data)

    # Reindirizza l'utente alla pagina delle gare
    return redirect(url_for(GET_EMPLOYEES_ENDPOINT))

def update_employee(id):
    employee = get_employee_by_id(id)
    if employee is None:
        abort(404)

    if request.method == 'GET':
        return render_template('update-employee.html', employee = employee)

    employee_data = {
        'name': request.form['name'],
    }

    employees_service.update_employee(id, employee_data)

    # reindirizza l'utente alla pagina delle gare
    return redirect(url_for(GET_EMPLOYEES_ENDPOINT))




