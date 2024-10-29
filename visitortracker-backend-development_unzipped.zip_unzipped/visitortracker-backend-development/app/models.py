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


@dataclass
class EmployeeAddress(db.Model):
    __tablename__ = 'tbl_master_EmployeeAddress'

    SNO = db.Column(db.Integer, primary_key=True)
    EmployeeCode = db.Column(db.String(20), nullable=True)
    AddressType = db.Column(db.String(20), nullable=True)
    Mobile = db.Column(db.String(20), nullable=True)
    Email = db.Column(db.String(50), nullable=True)


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


@dataclass
class SettingsMaster(db.Model):
    __tablename__ = 'tbl_master_Settings'

    id = db.Column(db.Integer, primary_key=True,
                   nullable=False, autoincrement=True)
    Menu = db.Column(db.String(100), nullable=True)
    Description = db.Column(db.String(100), nullable=True)
    UserId = db.Column(db.String(50), nullable=True)
    Orientation = db.Column(db.String(50), nullable=True)
    PageSize = db.Column(db.String(50), nullable=True)
    Config = db.Column(db.Text, nullable=True)
    Value = db.Column(db.Text, nullable=True)
    ValueTwo = db.Column(db.Text, nullable=True)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


@dataclass
class ReportDesignMaster(db.Model):
    __tablename__ = 'tbl_master_ReportDesign'

    id = db.Column(db.Integer, primary_key=True,
                   nullable=False, autoincrement=True)
    Menu = db.Column(db.String(100), nullable=True)
    Description = db.Column(db.String(100), nullable=True)
    UserId = db.Column(db.String(50), nullable=True)
    Config = db.Column(db.Text, nullable=True)
    Value = db.Column(db.Text, nullable=True)
    ValueTwo = db.Column(db.Text, nullable=True)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


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
    VisitorId = db.Column(db.String(50), nullable=True)
    CompanyId = db.Column(db.String(50), nullable=True)

    CreatedAt = db.Column(db.DateTime, default=datetime.utcnow)
    UpdatedAt = db.Column(db.DateTime, default=datetime.utcnow,
                          onupdate=datetime.utcnow)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

@dataclass
class MenuMaster(db.Model):
    __tablename__ = 'tbl_MenuMaster'

    id = db.Column(db.Integer, primary_key=True,
                   nullable=False, autoincrement=True)
    nav_bar_name = db.Column(db.String(255), nullable=True)
    isdrobdown = db.Column(db.String(5), nullable=True)
    uri_link = db.Column(db.String(255), nullable=True)
    parent_id = db.Column(db.Integer, db.ForeignKey(
        'tbl_MenuMaster.id'), nullable=True)
    icon_name = db.Column(db.String(255), nullable=True)
    status = db.Column(db.String(50), nullable=True)
    order = db.Column(db.Integer, nullable=True)
    deleted_at = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    children = db.relationship(
        "MenuMaster", backref='parent', remote_side=[id])

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
