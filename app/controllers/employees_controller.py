from app.models.employees import Employee
from flask import render_template, request, redirect, url_for, abort
from app.services import employees_service

GET_EMPLOYEES_ENDPOINT = 'employees_blueprint.get_employees'

def get_employees():
    employees = employees_service.get_all_employees()
    return render_template("employees.html", employees = employees)

def delete_employee(id):
    employees_service.delete_employee_by_id(id)

    # Reindirizza l'utente alla pagina delle gare
    return redirect(url_for(GET_EMPLOYEES_ENDPOINT))

def create_employee():
    if request.method == 'GET':
        return render_template('create-employee.html')

    employee_data = {
        'name': request.form['name'],
    }

    employees_service.create_employee(employee_data)

    # Reindirizza l'utente alla pagina delle gare
    return redirect(url_for(GET_EMPLOYEES_ENDPOINT))

def update_employee(id):
    employee = employees_service.get_employee_by_id(id)
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




