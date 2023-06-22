from app.models.teams import Team
from app.models.employees import Employee
from flask import request, abort, render_template, redirect, url_for
from app.services import teams_service
from app.services import employees_service

GET_TEAMS_ENDPOINT = 'teams_blueprint.get_teams'

def get_teams():
    teams = teams_service.get_all_teams()
    return render_template("index.html", teams = teams)

def delete_team(id):
    teams_service.delete_team_by_id(id)

    # Reindirizza l'utente alla pagina dei teams
    return redirect(url_for(GET_TEAMS_ENDPOINT))

def create_team():
    if request.method == 'GET':
        employees=Employee.query.all()
        return render_template('create-team.html', employees=employees)

    team_data = {
        'name': request.form['name'],
        'team_members': request.form.getlist('team_members[]')
    }

    teams_service.create_team(team_data)

    # Reindirizza l'utente alla pagina delle gare
    return redirect(url_for(GET_TEAMS_ENDPOINT))

def update_team(id):
    team = teams_service.get_team_by_id(id)
    if team is None:
        abort(404)

    if request.method == 'GET':
        all_employees = employees_service.get_all_employees()
        available_employees = [employee for employee in all_employees if employee not in team.team_members]
        return render_template('update-team.html', team=team, available_employees=available_employees)

    team_data = {
        'name': request.form['name'],
        'team_members': request.form.getlist('team_members[]')
    }

    teams_service.update_team(id, team_data)

    # reindirizza l'utente alla pagina dei teams
    return redirect(url_for(GET_TEAMS_ENDPOINT))
