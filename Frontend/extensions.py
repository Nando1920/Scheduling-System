from flask_login import LoginManager

from common import requests_commons

login_manager = LoginManager()
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(nhs_number):
    return requests_commons.get_and_check(f'http://127.0.0.1:5060/get_staff/{nhs_number}')
