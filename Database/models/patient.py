from sqlalchemy_serializer import SerializerMixin

from extensions import db, ma


class Patient(db.Model, SerializerMixin):
    __tablename__ = 'patients'
    nhs_number = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(13), nullable=True)
    age = db.Column(db.Integer, unique=False, nullable=False)
    patient_prescriptions = db.relationship('PatientPrescriptions', backref='patients')


class PatientSchema(ma.Schema):
    class Meta:
        fields = ('nhs_number', 'full_name', 'email', 'phone_number', 'age')
