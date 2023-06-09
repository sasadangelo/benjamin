from app import db
from app.models.teams import Team

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
        name=team_data['name'],
    )
    db.session.add(team)
    db.session.commit()

def update_team(id, team_data):
    team = Team.query.get(id)
    if team:
        team.name=race_data['name']
        db.session.commit()
