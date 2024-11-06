from app import db
from werkzeug.security import generate_password_hash
from dataclasses import dataclass
from sqlalchemy.inspection import inspect
from datetime import datetime




@dataclass
class CompanyMaster(db.Model):
    __tablename__ = 'vis_tbl_master_Company'

    SNO = db.Column(db.Integer, primary_key=True)
    Company = db.Column(db.String(100), nullable=True)
    AddressLine1 = db.Column(db.String(100), nullable=True)
    AddressLine2 = db.Column(db.String(100), nullable=True)
    Area = db.Column(db.String(50), nullable=True)
    City = db.Column(db.String(50), nullable=True)
    State = db.Column(db.String(50), nullable=True)
    Country = db.Column(db.String(50), nullable=True)
    PinCode = db.Column(db.String(50), nullable=True)
    Contact1 = db.Column(db.String(50), nullable=True)
    Contact2 = db.Column(db.String(50), nullable=True)
    Phone = db.Column(db.String(50), nullable=True)
    Fax = db.Column(db.String(50), nullable=True)
    Mobile = db.Column(db.String(50), nullable=True)
    Email = db.Column(db.String(50), nullable=True)
    WebSite = db.Column(db.String(250), nullable=True)
    TypeOfService = db.Column(db.String(50), nullable=True)
    TypeOfIndustry = db.Column(db.String(50), nullable=True)
    Active = db.Column(db.String(50), nullable=True)
    InActiveDate = db.Column(db.DateTime(timezone=True), nullable=True)
    VisitorType = db.Column(db.String(50), nullable=True)
    ContractEndDate = db.Column(db.DateTime(timezone=True), nullable=True)

    createdAt = db.Column(db.DateTime(timezone=True), default=datetime.now)
    updatedAt = db.Column(db.DateTime(timezone=True),
                          default=datetime.now, onupdate=datetime.now)

    def as_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}

