import unittest
from app import app
from common import json_commons
from controller import search_controllers


class TestSearchController(unittest.TestCase):

    def test_search_patient_email(self):
        email = "JS@hotmail.co.uk"
        expected={"nhs_number": 4685112, "full_name": "Tom Snizzing", "email": "JS@hotmail.co.uk", "phone_number": "0754482152", "age":48}
        with app.app_context():
            response = search_controllers.search_email(email)
            response_data = response[0].data
            response_json = json_commons.load_from_string(response_data)
        self.assertEqual(response_json[0], expected)

    def test_search_patient_nhs_num(self):
        nhs = 4715112
        expected = {"nhs_number": 4715112, "full_name": "Joshua Snizzing", "email": "JS@hotmail.co.uk", "phone_number": "0754482152", "age":48}
        with app.app_context():
            response = search_controllers.search_nhs_num(nhs)
            response_data = response[0].data
            response_json = json_commons.load_from_string(response_data)
        self.assertEqual(response_json[0], expected)

    def test_search_patient_name(self):
        name = "Joshua Snizzing"
        expected = {"nhs_number": 4715112, "full_name": "Joshua Snizzing", "email": "JS@hotmail.co.uk", "phone_number": "0754482152", "age":48}
        with app.app_context():
            response = search_controllers.search_full_name(name)
            response_data = response[0].data
            response_json = json_commons.load_from_string(response_data)
        self.assertEqual(response_json[0], expected)


if __name__ == '__main__':
    unittest.main()
