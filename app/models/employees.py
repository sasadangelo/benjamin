from .. import db
from app.models.teams_employees import teams_employees

class Employee(db.Model):
    __tablename__ = "employee"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, autoincrement=True)
    teams = db.relationship('Team', secondary=teams_employees, backref=db.backref('teams', lazy='dynamic'))
    
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }

    def __init__(self, name):
        self.name = name
