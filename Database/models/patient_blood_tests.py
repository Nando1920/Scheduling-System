from sqlalchemy_serializer import SerializerMixin

from extensions import db, ma


class PatientBloodTests(db.Model, SerializerMixin):
    __tablename__ = 'patients_blood_tests'
    patient_nhs_number = db.Column(db.Integer, primary_key=True)
    blood_test = db.Column(db.Integer, primary_key=True)
    date_taken = db.Column(db.DateTime, unique=False, nullable=False)


class PatientBloodTestsSchema(ma.Schema):
    class Meta:
        fields = ('patient_nhs_number', 'blood_test', 'date_taken')
