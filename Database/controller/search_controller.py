from flask import Blueprint, request

from models.patient import Patient, PatientSchema
from models.patient_prescriptions import PatientPrescriptions, PatientPrescriptionsSchema

search_endpoints = Blueprint('search_endpoints', __name__)
many_patients_schema = PatientSchema(many=True)
many_prescriptions_schema = PatientPrescriptionsSchema(many=True)


@search_endpoints.route('/filter_patients/nhs_number/<string:nhs_number>', methods=['GET'])
def filter_by_nhs_number(nhs_number: str) -> (dict, int):
    patients = Patient.query.filter(Patient.nhs_number.like(f'%{nhs_number}%')).all()
    return many_patients_schema.jsonify(patients), 200


@search_endpoints.route('/filter_patients/full_name/<string:name>', methods=['GET'])
def filter_by_name(name: str) -> (dict, int):
    patients = Patient.query.filter(Patient.full_name.like(f'%{name}%')).all()
    return many_patients_schema.jsonify(patients), 200


@search_endpoints.route('/filter_patients/patient_prescriptions/<string:medication>', methods=['GET'])
def filter_by_medication(medication: str) -> (dict, int):
    patient_prescriptions = PatientPrescriptions.query.filter(PatientPrescriptions.medication_name.like(f'%{medication}%')).all()
    return many_prescriptions_schema.jsonify(patient_prescriptions), 200


@search_endpoints.route('/filter_patients/email/<string:email>', methods=['GET'])
def filter_by_email(email: str) -> (dict, int):
    patients = Patient.query.filter(Patient.email.like(f'%{email}%')).all()
    return many_patients_schema.jsonify(patients), 200
