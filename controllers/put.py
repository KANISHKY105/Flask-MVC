from flask import Flask, jsonify, request
from models.CVE import CVE, db

def update_cve(cve_id):
    try:
        cve = CVE.query.filter_by(cve_id=cve_id).first()

        if cve:
            # Parse the JSON data from the request
            data = request.json

            # Update the CVE attributes
            cve.cve_id = data.get('cve_id', cve.cve_id)
            cve.severity = data.get('severity', cve.severity)
            cve.cvss = data.get('cvss', cve.cvss)
            cve.affected_packages = data.get('affected_packages', cve.affected_packages)
            cve.description = data.get('description', cve.description)
            cve.cwe_id = data.get('cwe_id', cve.cwe_id)

            # Commit the changes to the database
            db.session.commit()

            return jsonify({'message': f'CVE {cve_id} updated successfully'})
        else:
            return jsonify({'error': f'CVE ID {cve_id} not found'}), 404
    except Exception as e:
        return jsonify({'error': f'Error updating CVE: {str(e)}'}), 500