from . import db

class Team(db.Model):
   __tablename__ = "team"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)

   def to_json(self):
      return {
         'id': self.id,
         'name': self.name
      }
   def __init__(self, name):
       self.name = name


#team_employee = db.Table('team_employee',
#    db.Column('team_id', db.Integer, db.ForeignKey('team.id'), primary_key=True),
#    db.Column('employee_id', db.Integer, db.ForeignKey('employee.id'), primary_key=True)
#)

#class Team(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    name = db.Column(db.String(50), nullable=False)
#    employees = db.relationship('Employee', secondary=team_employee, backref=db.backref('teams', lazy='dynamic'))
