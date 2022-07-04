import flask
from flask import Blueprint, render_template, request

from common import requests_commons
from extensions import login_manager

auth_endpoints = Blueprint('auth_endpoints', __name__)


@auth_endpoints.route('/login', methods=['GET'])
def show_login() -> str:
    return render_template('login.html')


@auth_endpoints.route('/login', methods=['POST'])
def login() -> str:
    response = requests_commons.post_and_check(f'http://127.0.0.1:5060/login', data=request.form)
    return render_template('login.html')


@login_manager.unauthorized_handler
def unauthorized():
    return flask.redirect(flask.url_for('/login'))
