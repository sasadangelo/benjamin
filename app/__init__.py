# __init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///calendar.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from app.routes import team_bp, employee_bp, calendar_bp
    app.register_blueprint(team_bp)
    app.register_blueprint(employee_bp)
    app.register_blueprint(calendar_bp)

    return app
