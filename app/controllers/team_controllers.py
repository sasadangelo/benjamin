# app/routes/team_routes.py
from flask import render_template, request, redirect, url_for
from app.models.team import Team
from app.models import db
from app.services.team_service import TeamService
from . import team_bp

@team_bp.route('/')
def index():
    teams = TeamService.get_all_teams()
    return render_template('index.html', teams=teams)

@team_bp.route('/create', methods=['POST'])
def create_team():
    team_name = request.form['team_name']
    TeamService.create_team(team_name)
    return redirect(url_for('team_bp.index'))

@team_bp.route('/delete/<int:team_id>', methods=['POST'])
def delete_team(team_id):
    team = TeamService.get_team_by_id(team_id)
    if team:
        TeamService.delete_team(team)
    return redirect(url_for('team_bp.index'))
