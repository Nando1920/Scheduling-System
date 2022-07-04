from sqlalchemy_serializer import SerializerMixin

from extensions import db, ma


class MedicationBloodTests(db.Model, SerializerMixin):
    __tablename__ = 'medications_blood_tests'
    medication = db.Column(db.Integer, primary_key=True)
    blood_test = db.Column(db.String, primary_key=True)
    frequency_days = db.Column(db.Integer, nullable=False)
    mandatory = db.Column(db.Boolean, nullable=False)


class MedicationBloodTestsSchema(ma.Schema):
    class Meta:
        fields = ('medication', 'blood_test', 'frequency_days', 'mandatory')
