from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class CVE(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cve_id = db.Column(db.Text, unique=True, nullable=False)
    severity = db.Column(db.Text, nullable=False)
    cvss = db.Column(db.Text, nullable=False)
    affected_packages = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    cwe_id = db.Column(db.Text, nullable=False)

    def __init__(self, cve_id, severity, cvss, affected_packages, description, cwe_id):
        self.cve_id = cve_id
        self.severity = severity
        self.cvss = cvss
        self.affected_packages = affected_packages
        self.description = description
        self.cwe_id = cwe_id
