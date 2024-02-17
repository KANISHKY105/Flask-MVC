from flask import Flask, jsonify
from models.CVE import CVE

def get_cve_details(cve_id):
    try:
        cve = CVE.query.filter_by(cve_id=cve_id).first()
        if cve:
            cve_details = {
                'cve_id': cve.cve_id,
                'severity': cve.severity,
                'cvss': cve.cvss,
                'affected_packages': cve.affected_packages,
                'description': cve.description,
                'cwe_id': cve.cwe_id
            }
            return jsonify(cve_details)
        else:
            return jsonify({'error': f'CVE ID {cve_id} not found'}), 404
    except Exception as e:
        return jsonify({'error': f'Error retrieving CVE details: {str(e)}'}), 500
    
    
def get_all_cves():
    try:
        cves = CVE.query.all()
        cve_list = []

        for cve in cves:
            cve_dict = {
                'cve_id': cve.cve_id,
                'severity': cve.severity,
                'cvss': cve.cvss,
                'affected_packages': cve.affected_packages,
                'description': cve.description,
                'cwe_id': cve.cwe_id
            }
            cve_list.append(cve_dict)

        return jsonify({'cves': cve_list})
    except Exception as e:
        return jsonify({'error': f'Error retrieving CVE details: {str(e)}'}), 500