from flask import Blueprint

# Import your controller functions
from controllers.get import get_all_cves, get_cve_details

# Create a Blueprint instance
get_bp = Blueprint('get_bp', __name__)

# Define routes using the Blueprint instance
get_bp.route('/<cve_id>', methods=['GET'])(get_cve_details)
get_bp.route('/all', methods=['GET'])(get_all_cves)
