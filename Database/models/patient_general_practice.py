from sqlalchemy_serializer import SerializerMixin

from extensions import db, ma


class PatientGeneralPractice(db.Model, SerializerMixin):
    __tablename__ = 'patient_general_practice'
    patient = db.Column(db.String(75), db.ForeignKey('patients.nhs_number'), primary_key=True)
    general_practice = db.Column(db.String(25), db.ForeignKey('general_practices.id'), primary_key=True)
    from_date = db.Column(db.DateTime(100), primary_key=True)


class PatientGeneralPracticeSchema(ma.Schema):
    class Meta:
        fields = ('patient', 'general_practice', 'from_date')
