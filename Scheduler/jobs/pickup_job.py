from common import requests_commons
from datetime import datetime, timedelta


def patient_pickup():
    patients = requests_commons.get_and_check(f'http://127.0.0.1:5002/all_patients').json()
    for patient in patients:
        prescriptions = requests_commons.get_and_check(
            f'http://127.0.0.1:5002/get_patient_prescriptions/{patient["nhs_number"]}').json()
        for prescription in prescriptions:
            today = datetime.today()
            if datetime.fromisoformat(prescription['end_date']) < today:
                continue

            due_dates = []
            due_date = datetime.fromisoformat(prescription['first_dose'])
            for repetition in range(prescription['repetitions']):
                due_date += timedelta(days=prescription['days_frequency'])
                due_dates.append(due_date)
            tomorrow = datetime.today() + timedelta(days=1)
            if tomorrow in due_dates:
                email_data = {
                    "patient_name": patient['full_name'],
                    "medication": prescription['medication_name'],
                    "pickup_date": tomorrow,
                    "patient_email": patient['email']
                }
                requests_commons.post_and_check(f'http://127.0.0.1:5001/notify_pickup', email_data)
