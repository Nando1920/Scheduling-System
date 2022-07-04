from datetime import datetime, timedelta

from common import requests_commons

__db_base_url = 'http://127.0.0.1:5002'
__api_base_url = 'http://127.0.0.1:5001'


def notify_blood_tests_pending():
    patients = requests_commons.get_and_check(f'{__db_base_url}/all_patients').json()
    for patient in patients:
        pending_blood_tests = requests_commons.get_and_check(f'{__api_base_url}/get_pending_blood_tests/{patient["nhs_number"]}').json()
        for pending_blood_test in pending_blood_tests:
            __notify(patient["nhs_number"], pending_blood_test)


def __notify(nhs_number: int, blood_test: str):
    patient_gp = requests_commons.get_and_check(f'{__db_base_url}/get_patient_general_practice/{nhs_number}').json()
    gp = requests_commons.get_and_check(f'{__db_base_url}/get_general_practice/{patient_gp["general_practice"]}').json()
    patient = requests_commons.get_and_check(f'{__db_base_url}/get_patient//{nhs_number}').json()

    notifications_data = {
        'general_practice_name': gp['name'],
        'general_practice_email': gp['email'],
        'blood_test_type': blood_test,
        'patient_name': patient['full_name'],
        'patient_email': patient['email'],
        'patient_phone_number': patient['phone_number'],
    }
    requests_commons.post_and_check(f'{__api_base_url}/notify_blood_test', notifications_data)
    pass
