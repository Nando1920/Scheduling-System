from datetime import datetime, timedelta


def get_last_date_tested(patient_blood_tests: dict, blood_test: dict) -> datetime:
    last_date_tested = datetime.min
    for patient_blood_test in patient_blood_tests:
        if patient_blood_test['blood_test'] == blood_test:
            date_taken = datetime.fromisoformat(patient_blood_test['date_taken'])
            if last_date_tested < date_taken:
                last_date_tested = date_taken

    return last_date_tested


def test_is_pending(last_date_tested: datetime, frequency_days: int) -> bool:
    current_date = datetime.now()
    test_due_date = last_date_tested + timedelta(days=frequency_days)
    return current_date > test_due_date


def add_if_needed(pending_tests: list, medication_blood_test: dict):
    for test in pending_tests:
        if test["medication"] == medication_blood_test["medication"] \
                or test["blood_test"] == medication_blood_test["blood_test"]:
            return
    pending_tests.append(medication_blood_test)
