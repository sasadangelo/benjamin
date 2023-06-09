# app/routes/team_routes.py
from flask import render_template, request, redirect, url_for
from app.models.team import Team
from app.models import db
from app.services.teams_service import TeamService
from . import team_bp

def index():
    teams = TeamService.get_all_teams()
    return render_template('index.html', teams=teams)

def create_team():
    team_name = request.form['team_name']
    TeamService.create_team(team_name)
    return redirect(url_for('team_bp.index'))

def delete_team(team_id):
    team = TeamService.get_team_by_id(team_id)
    if team:
        TeamService.delete_team(team)
    return redirect(url_for('team_bp.index'))
