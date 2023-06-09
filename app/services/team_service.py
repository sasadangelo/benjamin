# app/services/team_service.py
from app.models.team import Team, db

class TeamService:
    @staticmethod
    def get_all_teams():
        return Team.query.all()

    @staticmethod
    def get_team_by_id(team_id):
        return Team.query.get(team_id)

    @staticmethod
    def create_team(name):
        team = Team(name=name)
        db.session.add(team)
        db.session.commit()
        return team

    @staticmethod
    def update_team(team, name):
        team.name = name
        db.session.commit()

    @staticmethod
    def delete_team(team):
        db.session.delete(team)
        db.session.commit()
