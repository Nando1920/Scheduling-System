from sqlalchemy_serializer import SerializerMixin

from extensions import db, ma


class GeneralPractices(db.Model, SerializerMixin):
    __tablename__ = 'general_practices'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(75))
    address = db.Column(db.String(25))
    email = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(13), nullable=True)
    patients = db.relationship('PatientGeneralPractice', backref='general_practices')


class GeneralPracticesSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'address', 'email', 'phone_number')
