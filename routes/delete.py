from flask import Blueprint

# Import your controller functions
from controllers.delete import delete_cve

# Create a Blueprint instance
delete_bp = Blueprint('delete_bp', __name__)

# Define routes using the Blueprint instance
delete_bp.route('/<cve_id>', methods=['DELETE'])(delete_cve)
