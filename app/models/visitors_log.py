from app import db
from werkzeug.security import generate_password_hash
from dataclasses import dataclass
from sqlalchemy.inspection import inspect
from datetime import datetime

@dataclass
class VisitorsLog(db.Model):
    __tablename__ = 'vis_tbl_trans_VistorLog24'

    SNO = db.Column(db.Integer, primary_key=True, autoincrement=True)
    IDCardImageName = db.Column(db.String(100), nullable=True)
    VisitorID = db.Column(db.String(50), nullable=True)
    CompanyID = db.Column(db.String(50), nullable=True)
    PassNumber = db.Column(db.String(50), nullable=True)
    PassDate = db.Column(db.DateTime, nullable=True)
    BadgeNumber = db.Column(db.String(50), nullable=True)
    Company = db.Column(db.String(100), nullable=True)
    VisitorName = db.Column(db.String(100), nullable=True)
    VisCategory = db.Column(db.String(100), nullable=True)
    MobileNumber = db.Column(db.String(100), nullable=True)
    VisTotal = db.Column(db.String(100), nullable=True)
    VisPurpose = db.Column(db.String(100), nullable=True)
    VehicleNumber = db.Column(db.String(100), nullable=True)
    VisAdditional = db.Column(db.String(100), nullable=True)
    ReturnableItems = db.Column(db.Text, nullable=True)
    VehicleNo = db.Column(db.String(100), nullable=True)
    EmployeeCode = db.Column(db.String(100), nullable=True)
    Department = db.Column(db.String(100), nullable=True)
    InTime = db.Column(db.DateTime, nullable=True)
    OutTime = db.Column(db.DateTime, nullable=True)
    ImageName = db.Column(db.String(100), nullable=True)
    AppointmentNumber = db.Column(db.String(100), nullable=True)
    VehcileType = db.Column(db.String(50), nullable=True)
    VehicleCompany = db.Column(db.String(50), nullable=True)
    DriverName = db.Column(db.String(50), nullable=True)
    CabInTime = db.Column(db.String(50), nullable=True)
    CabOutTime = db.Column(db.String(50), nullable=True)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}