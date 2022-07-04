from sqlalchemy_serializer import SerializerMixin

from extensions import db, ma


class PrescriptionPickup(db.Model, SerializerMixin):
    prescription = db.Column(db.Integer, primary_key=True)
    staff = db.Column(db.String, db.ForeignKey('staff_members.email'))
    delivered_on = db.Column(db.DateTime, nullable=False)


class PrescriptionPickupSchema(ma.Schema):
    class Meta:
        fields = ('prescription', 'staff', 'delivered_on')
