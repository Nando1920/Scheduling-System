import os

from flask import Flask

from common import yaml_commons
from extensions import db, ma


def register_extensions():
    db.init_app(app)
    ma.init_app(app)


def register_blueprints():
    from controller.admins_controller import admin_endpoints
    from controller.blood_tests_controller import blood_tests_endpoints
    from controller.general_practices_controller import general_practice_endpoints
    from controller.medication_blood_tests_controller import medication_blood_tests_endpoints
    from controller.medication_controller import medication_endpoints
    from controller.patient_blood_tests_controller import patient_blood_tests_endpoints
    from controller.patient_controller import patient_endpoints
    from controller.patient_general_practice_controller import patient_general_practice_endpoints
    from controller.prescription_controller import prescription_endpoints
    from controller.search_controller import search_endpoints
    from controller.staff_members import staff_endpoints
    from controller.system import system_endpoints

    app.register_blueprint(admin_endpoints)
    app.register_blueprint(blood_tests_endpoints)
    app.register_blueprint(general_practice_endpoints)
    app.register_blueprint(medication_blood_tests_endpoints)
    app.register_blueprint(medication_endpoints)
    app.register_blueprint(patient_blood_tests_endpoints)
    app.register_blueprint(patient_endpoints)
    app.register_blueprint(patient_general_practice_endpoints)
    app.register_blueprint(prescription_endpoints)
    app.register_blueprint(search_endpoints)
    app.register_blueprint(staff_endpoints)
    app.register_blueprint(system_endpoints)


current_dir = os.path.dirname(os.path.realpath(__file__))
config = yaml_commons.load_from_file(f'{current_dir}/config.yml')
db_config = config['database']

app = Flask(__name__)
app.secret_key = config['app_secret_key']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Before creating tables, create an empty schema on your database with the name you want to use
db_uri = f'mysql://{db_config["username"]}:{db_config["password"]}@{db_config["host"]}/{db_config["schema"]}'
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri

register_blueprints()
register_extensions()

if __name__ == '__main__':
    app.run()
