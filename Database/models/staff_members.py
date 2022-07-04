from sqlalchemy_serializer import SerializerMixin

from extensions import db, ma


class StaffMember(db.Model, SerializerMixin):
    __tablename__ = 'staff_members'
    email = db.Column(db.String(100), nullable=False, primary_key=True)
    nhs_number = db.Column(db.Integer, nullable=False, primary_key=True)
    password = db.Column(db.String(32), nullable=False)
    full_name = db.Column(db.String(25), nullable=False)
    phone_number = db.Column(db.String(20), nullable=True)


class StaffMemberSchema(ma.Schema):
    class Meta:
        fields = ('email', 'nhs_number', 'password', 'full_name', 'phone_number')
