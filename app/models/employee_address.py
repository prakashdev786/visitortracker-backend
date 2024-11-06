from app import db
from werkzeug.security import generate_password_hash
from dataclasses import dataclass
from sqlalchemy.inspection import inspect
from datetime import datetime

@dataclass
class EmployeeAddress(db.Model):
    __tablename__ = 'tbl_master_EmployeeAddress'

    SNO = db.Column(db.Integer, primary_key=True)
    EmployeeCode = db.Column(db.String(20), nullable=True)
    AddressType = db.Column(db.String(20), nullable=True)
    Mobile = db.Column(db.String(20), nullable=True)
    Email = db.Column(db.String(50), nullable=True)
