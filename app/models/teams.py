from .. import db
from app.models.teams_employees import teams_employees

class Team(db.Model):
    __tablename__ = "team"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    team_members = db.relationship('Employee', secondary=teams_employees, backref=db.backref('teams', lazy='dynamic'))

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }

    def __init__(self, name):
        self.name = name
