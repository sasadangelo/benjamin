# app/routes/calendar_routes.py
from flask import render_template
from . import calendar_bp

@calendar_bp.route('/calendar')
def show_calendar():
    # Logica per ottenere i dati del calendario e passarli al template
    # Ad esempio, puoi ottenere i dati dal tuo servizio o modello

    # Esempio di dati di esempio per il calendario
    calendar_data = [
        {'date': '2023-01-01', 'employee_id': 1, 'status': 'presenza'},
        {'date': '2023-01-01', 'employee_id': 2, 'status': 'permesso'},
        # ...
    ]

    return render_template('team_calendar.html', calendar_data=calendar_data)

