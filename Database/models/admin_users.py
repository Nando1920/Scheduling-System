from sqlalchemy_serializer import SerializerMixin

from extensions import db, ma


class AdminUser(db.Model, SerializerMixin):
    __tablename__ = 'admin_users'
    email = db.Column(db.String(100), nullable=False, primary_key=True)
    password = db.Column(db.String(32), nullable=False)
    full_name = db.Column(db.String(25), nullable=False)
    phone_number = db.Column(db.String(20), nullable=True)


class AdminUserSchema(ma.Schema):
    class Meta:
        fields = ('email', 'password', 'full_name', 'phone_number')
