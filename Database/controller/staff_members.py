from flask import Blueprint, jsonify
from sqlalchemy.orm import Query

from models.staff_members import StaffMember, StaffMemberSchema

staff_endpoints = Blueprint('staff_endpoints', __name__)
staff_member_schema = StaffMemberSchema()


@staff_endpoints.route('/get_staff/by_email/<string:email>', methods=['GET'])
def get_staff_by_email(email: str) -> (dict, int):
    query = StaffMember.query.filter_by(email=email)
    return respond(query)


@staff_endpoints.route('/get_staff/by_nsh_number/<string:nhs_number>', methods=['GET'])
def get_staff_by_nhs_number(nhs_number: str) -> (dict, int):
    query = StaffMember.query.filter_by(nhs_number=nhs_number)
    return respond(query)


def respond(query: Query) -> (dict, int):
    staff_member = query.first()
    if staff_member:
        return staff_member_schema.jsonify(staff_member), 200
    else:
        return jsonify(msg='User not found'), 404
