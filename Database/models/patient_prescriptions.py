from sqlalchemy_serializer import SerializerMixin

from extensions import db, ma


class PatientPrescriptions(db.Model, SerializerMixin):
    __tablename__ = 'patients_prescriptions'
    id = db.Column(db.Integer, primary_key=True)
    patient_nhs_number = db.Column(db.Integer, db.ForeignKey('patients.nhs_number'))
    medication_name = db.Column(db.String, db.ForeignKey('medications.medication_name'))
    first_dose = db.Column(db.DateTime, primary_key=True, nullable=False)
    days_frequency = db.Column(db.Integer, unique=False, nullable=False)
    repetitions = db.Column(db.Integer, unique=False, nullable=False)
    end_date = db.Column(db.DateTime, unique=False, nullable=False)


class PatientPrescriptionsSchema(ma.Schema):
    class Meta:
        fields = ('id', 'patient_nhs_number', 'medication_name', 'first_dose', 'days_frequency', 'repetitions', 'end_date')
