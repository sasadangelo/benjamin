# app/app.py
from flask import Flask
from config import Config
from app.routes.team_routes import team_bp
from app.routes.employee_routes import employee_bp
from app.routes.calendar_routes import calendar_bp

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
