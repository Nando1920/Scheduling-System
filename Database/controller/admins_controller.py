

from flask import Blueprint, jsonify, request

from extensions import db
from models.admin_users import AdminUser, AdminUserSchema

admin_endpoints = Blueprint('admin_endpoints', __name__)
admin_user_schema = AdminUserSchema()


@admin_endpoints.route('/add_admin', methods=['POST'])
def add_admin() -> (dict, int):
    data = request.json if request.is_json else request.form
    existing_admin = AdminUser.query.filter_by(email=data['email']).first()
    if not existing_admin:
        admin = AdminUser(email=data['email'],
                          password=data['password'],
                          full_name=data['full_name'],
                          phone_number=data['phone_number'])
        db.session.add(admin)
        db.session.commit()
        return admin_user_schema.jsonify(admin), 200
    return jsonify(msg="Admin user already exists"), 400


@admin_endpoints.route('/get_admin/<string:email>', methods=['GET'])
def get_admin(email: str) -> (dict, int):
    admin = AdminUser.query.filter_by(email=email).first()
    if admin:
        return admin_user_schema.jsonify(admin), 200
    else:
        return jsonify(msg='User not found'), 404
