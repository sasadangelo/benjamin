from app import db
from app.models.teams import Team
from app.models.employees import Employee
from app.models.employees import teams_employees

def get_all_teams():
    teams = Team.query.all()
    return teams

def get_team_by_id(id):
    team = Team.query.get(id)
    return team

def delete_team_by_id(id):
    team = Team.query.get(id)
    if team:
        db.session.delete(team)
        db.session.commit()

def create_new_team(team_data):
    team = Team(
        name=team_data['name']
    )

    employee_ids = team_data['team_members']

    db.session.add(team)
    db.session.flush()

    team_members = [{'team_id': team.id, 'employee_id': employee_id} for employee_id in employee_ids]

    db.session.execute(teams_employees.insert(), team_members)
    db.session.commit()

def update_team(id, team_data):
    team = Team.query.get(id)
    if team:
        team.name=team_data['name']
        db.session.commit()
