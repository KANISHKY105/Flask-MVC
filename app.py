import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models.CVE import db

# Importing controllers fns
from routes.get import get_bp
from routes.post import post_bp
from routes.delete import delete_bp
from routes.put import put_bp

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Register the Blueprints with the Flask app
app.register_blueprint(get_bp, url_prefix='/cve')
app.register_blueprint(post_bp, url_prefix='/cve')
app.register_blueprint(delete_bp, url_prefix='/cve')
app.register_blueprint(put_bp, url_prefix='/cve')


@app.route("/", methods=['GET'])
def hello():
    return "Hello, World!"


    
if __name__ == '__main__' or __name__ == 'app':
    # Create tables if they don't exist
    with app.app_context():
        db.create_all()

    # Run the Flask app
    app.run()
    print("server started!!!")
