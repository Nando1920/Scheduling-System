from sqlalchemy_serializer import SerializerMixin

from extensions import db, ma


class BloodTests(db.Model, SerializerMixin):
    __tablename__ = 'blood_tests'
    blood_test_type = db.Column(db.String, primary_key=True)
    hours_before_results = db.Column(db.Integer, nullable=True)


class BloodTestsSchema(ma.Schema):
    class Meta:
        fields = ('blood_test_type', 'hours_before_results')
