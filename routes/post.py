from flask import Blueprint

# Import your controller functions
from controllers.post import add_cve

# Create a Blueprint instance
post_bp = Blueprint('post_bp', __name__)

# Define routes using the Blueprint instance
post_bp.route('/addCVE', methods=['POST'])(add_cve)

