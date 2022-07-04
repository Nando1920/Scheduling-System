from flask import Blueprint, jsonify, request

from extensions import db
from models.patient import Patient, PatientSchema

patient_endpoints = Blueprint('patient_endpoints', __name__)
single_patient_schema = PatientSchema()
many_patients_schema = PatientSchema(many=True)


@patient_endpoints.route('/add_patient', methods=['POST'])
def add_patient() -> (dict, int):
    data = request.json if request.is_json else request.form
    existing_patient = Patient.query.filter_by(nhs_number=data['nhs_number']).first()
    if not existing_patient:
        patient = Patient(nhs_number=data['nhs_number'],
                          full_name=data['full_name'],
                          email=data['email'],
                          phone_number=data['phone_number'],
                          age=data['age'])
        db.session.add(patient)
        db.session.commit()
        return single_patient_schema.jsonify(patient), 200
    return jsonify(msg='Patient already exist'), 400


@patient_endpoints.route('/get_patient/<string:nhs_number>', methods=['GET'])
def get_patient(nhs_number: str) -> (dict, int):
    this_patient = Patient.query.filter_by(nhs_number=nhs_number).first()
    if this_patient:
        return single_patient_schema.jsonify(this_patient), 200
    else:
        return jsonify(msg='Patient not found'), 404


@patient_endpoints.route('/all_patients', methods=['GET'])
def get_all_patient() -> [dict]:
    patients = Patient.query.all()
    return many_patients_schema.jsonify(patients)
