from app import db
from app.models.teams import Team
from app.models.employees import Employee

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

    employees = [Employee(id=employee_id) for employee_id in team_data['members']]
    team.team_members.extend(employees)

    db.session.add(team)
    db.session.commit()

def update_team(id, team_data):
    team = Team.query.get(id)
    if team:
        team.name=team_data['name']
        db.session.commit()
