from flask import jsonify
from models.CVE import CVE, db

def delete_cve(cve_id):
    try:
        cve = CVE.query.filter_by(cve_id=cve_id).first()

        if cve:
            # Delete the CVE from the database
            db.session.delete(cve)
            db.session.commit()

            return jsonify({'message': f'CVE {cve_id} deleted successfully'}), 200
        else:
            return jsonify({'error': f'CVE ID {cve_id} not found'}), 404
    except Exception as e:
        # Handle database-related errors
        return jsonify({'error': f'Error deleting CVE: {str(e)}'}), 500
