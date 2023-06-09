import os
from flask import Flask
from app import db, migrate
from app.routes.teams_blueprint import team_bp
from app.routes.employees_blueprint import employees_bp
from app.routes.calendar_blueprint import calendar_bp
from config import config

def create_app(config_name):
    app = Flask(__name__, template_folder='app/templates', static_folder='app/static')
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        db.create_all()

    return app

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
app.register_blueprint(teams_bp)
app.register_blueprint(employees_bp)
app.register_blueprint(calendar_bp)
