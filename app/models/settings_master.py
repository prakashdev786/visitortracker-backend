from app import db
from werkzeug.security import generate_password_hash
from dataclasses import dataclass
from sqlalchemy.inspection import inspect
from datetime import datetime



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