from app import db
from werkzeug.security import generate_password_hash
from dataclasses import dataclass
from sqlalchemy.inspection import inspect
from datetime import datetime

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