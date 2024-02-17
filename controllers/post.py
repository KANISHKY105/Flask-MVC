from flask import Flask, jsonify, request
from models.CVE import CVE, db


def add_cve():
    try:
        data = request.json

        # Validate required fields
        required_fields = ['cve_id', 'severity', 'cvss', 'affected_packages', 'description', 'cwe_id']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing required field: {field}'}), 400

        # Create a new CVE instance
        new_cve = CVE(
            cve_id=data['cve_id'],
            severity=data['severity'],
            cvss=data['cvss'],
            affected_packages=data['affected_packages'],
            description=data['description'],
            cwe_id=data['cwe_id']
        )

        # Add the new CVE to the database
        db.session.add(new_cve)
        db.session.commit()

        return jsonify({'message': 'CVE added successfully'}), 201
    except Exception as e:
        return jsonify({'error': f'Error adding CVE: {str(e)}'}), 500