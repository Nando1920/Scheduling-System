from flask import Blueprint, request

from extensions import db
from models.prescription_pickup import PrescriptionPickup, PrescriptionPickupSchema

pickups_endpoints = Blueprint('pickups_endpoints', __name__)
pickup_schema = PrescriptionPickupSchema()


@pickups_endpoints.route('/add_pickup', methods=['POST'])
def add_new_pickup() -> (dict, int):
    data = request.json if request.is_json else request.form
    new_pickup = PrescriptionPickup(prescription=data['prescription'],
                                    staff=data['staff'],
                                    delivered_on=data['delivered_on'])
    db.session.add(new_pickup)
    db.session.commit()
    return pickup_schema.jsonify(new_pickup), 200
