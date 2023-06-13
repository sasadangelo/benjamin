from app.models.teams import Team
from app.models.employees import Employee
from flask import request, abort, render_template, redirect, url_for
from app.services.teams_service import get_all_teams, get_team_by_id, create_new_team, update_team, delete_team_by_id
from app.services import teams_service

GET_TEAMS_ENDPOINT = 'teams_blueprint.get_teams'

def get_teams():
    teams = get_all_teams()
    return render_template("index.html", teams = teams)

def delete_team(id):
    delete_team_by_id(id)

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

    create_new_team(team_data)

    # Reindirizza l'utente alla pagina delle gare
    return redirect(url_for(GET_TEAMS_ENDPOINT))

def update_team(id):
    team = get_team_by_id(id)
    if team is None:
        abort(404)

    if request.method == 'GET':
        return render_template('update-team.html', team = team)

    team_data = {
        'name': request.form['name']
    }

    teams_service.update_team(id, team_data)

    # reindirizza l'utente alla pagina dei teams
    return redirect(url_for(GET_TEAMS_ENDPOINT))
