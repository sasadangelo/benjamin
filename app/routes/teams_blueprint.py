from flask import Blueprint
from ..controllers.teams_controller import get_teams, create_team, update_team, delete_team

teams_blueprint = Blueprint('teams_blueprint', __name__)

teams_blueprint.route('/', methods=['GET'])(get_teams)
teams_blueprint.route('/teams', methods=['GET'])(get_teams)
teams_blueprint.route('/create-team', methods=['GET'])(create_team)
teams_blueprint.route('/create-team', methods=['POST'])(create_team)
teams_blueprint.route('/update-team/<int:id>', methods=['GET'])(update_team)
teams_blueprint.route('/update-team/<int:id>', methods=['POST'])(update_team)
teams_blueprint.route('/delete-team/<int:id>', methods=['GET'])(delete_team)
