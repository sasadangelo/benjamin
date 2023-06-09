from app.models.team import Team
from flask import request, abort, render_template, redirect, url_for
from app.services.teams_service import get_all_teams, get_team_by_id, create_new_team, update_team, delete_team_by_id
from app.services import teams_service

GET_TEAMS_ENDPOINT = 'teams_bp.get_teams'

def get_teams():
    teams = get_all_teams()
    return render_template("index.html", races = races)

def delete_team(id):
    delete_team_by_id(id)
    # Reindirizza l'utente alla pagina dei teams
    return redirect(url_for(GET_RACES_ENDPOINT))

def create_team():
    if request.method == 'GET':
        return render_template('create-team.html')

    team_data = {
        'name': request.form['name'],
    }

    create_new_team(team_data)

    # Reindirizza l'utente alla pagina delle gare
    return redirect(url_for(GET_TEAMS_ENDPOINT))

def update_team(id):
    race = get_team_by_id(id)
    if race is None:
        abort(404)

    if request.method == 'GET':
        return render_template('update-team.html', team = team)

    team_data = {
        'name': request.form['name'],
    }

    races_services.update_race(id, team_data)

    # reindirizza l'utente alla pagina dei teams
    return redirect(url_for(GET_TEAMS_ENDPOINT))
