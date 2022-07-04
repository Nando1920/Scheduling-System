from flask import Flask

from common import yaml_commons
from controller.authentication import auth_endpoints
from controller.system import system_endpoints
from extensions import login_manager


def register_extensions():
    login_manager.init_app(app)


def register_blueprints():
    app.register_blueprint(auth_endpoints)
    app.register_blueprint(system_endpoints)


config = yaml_commons.load_from_file('config.yml')

app = Flask(__name__)
app.secret_key = config['app_secret_key']

register_extensions()
register_blueprints()

if __name__ == '__main__':
    app.run()
