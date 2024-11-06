from app import db
from werkzeug.security import generate_password_hash
from dataclasses import dataclass
from sqlalchemy.inspection import inspect
from datetime import datetime


@dataclass
class VisitorsMaster(db.Model):
    __tablename__ = 'vis_tbl_master_Visitors'

    SNO = db.Column(db.Integer, primary_key=True)
    VisitorName = db.Column(db.String(100), nullable=True)
    Company = db.Column(db.String(100), nullable=True)
    VisitorCategory = db.Column(db.String(100), nullable=True)
    MobileNumber = db.Column(db.String(100), nullable=True)
    EmailID = db.Column(db.String(100), nullable=True)
    FirstVisitDate = db.Column(db.String(100), nullable=True)
    LastVisitDate = db.Column(db.String(100), nullable=True)
    LastVisitDate = db.Column(db.String(100), nullable=True)
    IDCardType = db.Column(db.String(100), nullable=True)
    IDCardNumber = db.Column(db.String(100), nullable=True)
    createdAt = db.Column(db.DateTime(timezone=True), default=datetime.now)
    updatedAt = db.Column(db.DateTime(timezone=True),
                          default=datetime.now, onupdate=datetime.now)

    def as_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}