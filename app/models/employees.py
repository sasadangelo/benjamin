from .. import db

class Employee(db.Model):
    __tablename__ = "employee"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, autoincrement=True)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }

    def __init__(self, name):
        self.name = name
