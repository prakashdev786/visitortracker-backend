from pydantic import BaseModel, model_validator, Field, field_validator,EmailStr
from typing import Optional
from datetime import datetime
from app import db
from app.models.menu_master import MenuMaster

class MenuUpdateSchema(BaseModel):
    id: Optional[int] = None
    nav_bar_name: Optional[str]
    isdrobdown: Optional[str]
    uri_link: Optional[str]
    parent_id: Optional[int]
    icon_name: Optional[str]
    status: Optional[str]
    order: Optional[int] = None
    deleted_at: Optional[datetime] = None

    @field_validator('id')
    def validate_id(cls, v):
        if v == '' or v is None:
            return None
        return int(v)

    @field_validator('uri_link')
    def validate_unique_uri_link(cls, v, info):
        if v:
       
            # Check if a menu item with the same uri_link already exists
            existing_menu = MenuMaster.query.filter_by(uri_link=v).first()

            # If 'id' exists in values (updating) and the URI is found, ensure it's not the same record
            if info.data.get('id') is not None:
                if existing_menu and existing_menu.id != info.data.get('id'):
                    raise ValueError('uri_link must be unique')
        return v

    @field_validator('parent_id', mode='before')
    def validate_parent_id(cls, v):
        if v == '':
            return None
        elif v is not None and int(v) < 0:
            raise ValueError('parent_id must be a positive integer or None')
        return v

    @field_validator("order", mode='before')
    def validate_order(cls, v):
        if v == '' or v is None:
            return None
        return int(v)

    model_config = {
        "from_attributes": True
    }



class UpdateTempVisitorSchema(BaseModel):
    AppNumber:str = Field(..., min_length=1, description="Appointment number is required")  
    VisitorName: str = Field(..., min_length=1, description="Visitor name is required")  
    VisitorCategory: str = Field(None, max_length=100)
    CompanyName: str = Field(None, max_length=100)
    EmailId: EmailStr = Field(None)  
    MobileNumber: str = Field(None,min_length=1)  
    AddressLine1: str = Field(None, max_length=500)
    AddressLine2: str = Field(None, max_length=500)
    City: str = Field(None, max_length=100)
    State: str = Field(None, max_length=100)
    TelePhone: str = Field(None, max_length=20)
    PinCode: str = Field(None, max_length=20)
    Purpose: str = Field(None, max_length=500)

    @model_validator(mode="before")
    def check_required_fields(cls, values):
        errors = {}
        for field_name, field in cls.model_fields.items():
            field_value = values.get(field.alias)
            
            if field.default is ... and (field_value is None or (isinstance(field_value, str) and not field_value.strip())):
                errors[field.alias] = field.field_info.description            
        
        if errors:
            raise ValueError(errors)
        return values
    
    model_config = {
        "from_attributes": True
    }