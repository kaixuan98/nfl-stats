from flask import Blueprint
from .offense import offense_bp

nfl_bp = Blueprint('nfl', __name__, url_prefix="/nfl")

# Register all nfl-related sub-blueprints
nfl_bp.register_blueprint(offense_bp)