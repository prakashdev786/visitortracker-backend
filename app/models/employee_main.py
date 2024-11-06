from app import db
from werkzeug.security import generate_password_hash
from dataclasses import dataclass
from sqlalchemy.inspection import inspect
from datetime import datetime


@dataclass
class EmployeeMain(db.Model):
    __tablename__ = 'tbl_master_EmployeeMain'

    SNO = db.Column(db.Integer, primary_key=True, autoincrement=True)
    EmployeeCode = db.Column(db.String(50))
    AlternateCode = db.Column(db.String(50))
    ShortName = db.Column(db.String(50))
    FirstName = db.Column(db.String(30))
    MiddleName = db.Column(db.String(30))
    LastName = db.Column(db.String(50))
    DateofBirth = db.Column(db.DateTime)
    DateofJoining = db.Column(db.DateTime)
    Company = db.Column(db.String(50))
    Department = db.Column(db.String(50))
    Designation = db.Column(db.String(50))
    Category = db.Column(db.String(50))
    EmailID = db.Column(db.String(50))
    ContactNo = db.Column(db.String(20))

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}