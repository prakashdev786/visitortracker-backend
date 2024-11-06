from app import db
from werkzeug.security import generate_password_hash
from dataclasses import dataclass
from sqlalchemy.inspection import inspect
import uuid
from datetime import datetime

@dataclass
class AppointMents(db.Model):
    __tablename__ = "vis_tbl_Appointments"

    id = db.Column(db.Integer, primary_key=True,
                   nullable=False, autoincrement=True)
    AppNumber = db.Column(db.String(50), nullable=True)
    AppDate = db.Column(db.String(50), nullable=True)
    AppTime = db.Column(db.String(50), nullable=True)
    CompanyName = db.Column(db.String(100), nullable=True)
    VisitorName = db.Column(db.String(100), nullable=True)
    VisitorCategory = db.Column(db.String(50), nullable=True)
    AddressLine1 = db.Column(db.String(200), nullable=True)
    AddressLine2 = db.Column(db.String(200), nullable=True)
    City = db.Column(db.String(100), nullable=True)
    State = db.Column(db.String(100), nullable=True)
    PinCode = db.Column(db.String(20), nullable=True)
    TelePhone = db.Column(db.String(20), nullable=True)
    MobileNumber = db.Column(db.String(20), nullable=True)
    EmailId = db.Column(db.String(100), nullable=True)
    Purpose = db.Column(db.String(500), nullable=True)
    TempVisitorId = db.Column(db.String(50), nullable=True)
    # CompanyId = db.Column(db.String(50), nullable=True)

    CreatedAt = db.Column(db.DateTime, default=datetime.utcnow)
    UpdatedAt = db.Column(db.DateTime, default=datetime.utcnow,
                          onupdate=datetime.utcnow)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


@dataclass
class TempVisitorMaster(db.Model):
    __tablename__ = 'vis_tbl_Temp_Visitors'

    SNO = db.Column(db.Integer, primary_key=True)
    AppointId = db.Column(db.String(100), unique=True, nullable=False, default=lambda: str(uuid.uuid4()))
    AppNumber = db.Column(db.String(50), nullable=True)
    VisitorName = db.Column(db.String(100), nullable=True)
    VisitorCategory = db.Column(db.String(100), nullable=True)
    EmailId = db.Column(db.String(100), nullable=True)
    MobileNumber = db.Column(db.String(100), nullable=True)
    Purpose = db.Column(db.String(500), nullable=True)
    """ company details"""
    
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
    TelePhone = db.Column(db.String(20), nullable=True)
    """ /company details end"""

    VisitorImage = db.Column(db.String(100), nullable=True)
    VisitorIdCardImage = db.Column(db.String(100), nullable=True)
    createdAt = db.Column(db.DateTime(timezone=True), default=datetime.now)
    updatedAt = db.Column(db.DateTime(timezone=True),
                          default=datetime.now, onupdate=datetime.now)

    def as_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}
