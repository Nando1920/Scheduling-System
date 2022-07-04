from sqlalchemy_serializer import SerializerMixin

from extensions import db, ma


class Medications(db.Model, SerializerMixin):
    __tablename__ = 'medications'
    medication_name = db.Column(db.String, primary_key=True)
    unit_of_measurement = db.Column(db.String, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    prescriptions = db.relationship('PatientPrescriptions', backref='medications')


class MedicationsSchema(ma.Schema):
    class Meta:
        fields = ('medication_name', 'unit_of_measurement', 'amount')
