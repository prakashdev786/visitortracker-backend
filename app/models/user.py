from app import db
from werkzeug.security import generate_password_hash
from dataclasses import dataclass
from sqlalchemy.inspection import inspect
from datetime import datetime


@dataclass
class User(db.Model):
    __tablename__ = "tbl_master_Userperms"
    # __table_args__ = {'schema': 'VisitorTrack'}

    id = db.Column(db.Integer, primary_key=True)
    UserName = db.Column(db.String(50), nullable=True)
    UPassword = db.Column(db.String(10), nullable=True)
    EmployeeCode = db.Column(db.String(50), nullable=True)
    AccessControl = db.Column(db.Text, nullable=True)

    def as_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}
    
