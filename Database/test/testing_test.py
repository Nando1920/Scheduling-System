import unittest
from controller import search_controller


class TestSearchController(unittest.TestCase):
    def test_search_patient_email(self):
        email = ""
        response = search_controller.filter_by_email(email)
        self.assertEqual(response, "")

    def test_search_patient_nhs_num(self):
        nhs = "123456789"
        response = search_controller.filter_by_nhs_number(nhs)
        self.assertEqual(response, "")

    def test_search_patient_name(self):
        name = ""
        response = search_controller.filter_by_name(name)
        self.assertEqual(response, "")


if __name__ == '__main__':
    unittest.main()
