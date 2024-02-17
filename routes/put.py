from flask import Blueprint

# Import your controller functions
from controllers.put import update_cve

# Create a Blueprint instance
put_bp = Blueprint('put_bp', __name__)

# Define routes using the Blueprint instance
put_bp.route('/<cve_id>', methods=['PUT'])(update_cve)

