from app.models import SettingsMaster, EmployeeMain, EmployeeAddress, VisitorsLog, ReportDesignMaster, MenuMaster, User
from app.validator.common_schema import MenuUpdateSchema
from pydantic import BaseModel, ValidationError
from sqlalchemy import text
from app import db
import uuid
import pandas as pd
from io import BytesIO
from datetime import datetime, timezone
from flask import render_template_string, send_file, request
from xhtml2pdf import pisa
import os
import json


def get_settings_by_userid_service(user_id):

    data = SettingsMaster.query.filter_by(UserId=user_id).all()

    settings_dict = [settings.as_dict() for settings in data]

    if not data:
        return None, True, "No data found"

    return settings_dict, None, None


def get_design_service(data):
    filters = request.args.to_dict()

    query = ReportDesignMaster.query

    for column, value in filters.items():
        if hasattr(ReportDesignMaster, column):
            query = query.filter(getattr(ReportDesignMaster, column) == value)

    data = query.all()

    settings_dict = [settings.as_dict() for settings in data]

    if not data:
        return None, True, "No data found"

    return settings_dict, None, None


def create_settings_service(data):
    try:
        menu = data.get('Menu')
        user_id = str(data.get('UserId'))
        orientation = data.get('Orientation')
        page_size = data.get('PageSize')
        config = data.get('Config')

        if not user_id or not config:
            return None, True, 'UserId and Config are mandatory fields'

        existing_setting = SettingsMaster.query.filter_by(
            Menu=menu, UserId=user_id, Orientation=orientation, PageSize=page_size).first()

        if existing_setting:
            existing_setting.Config = config
            db.session.commit()
            return existing_setting.as_dict(), None, 'Settings updated successfully'

        else:
            # new entry
            new_setting = SettingsMaster(
                Menu=menu,
                UserId=user_id,
                Orientation=orientation,
                PageSize=page_size,
                Config=config
            )
            db.session.add(new_setting)
            db.session.commit()
            return new_setting.as_dict(), None, 'Settings updated successfully'

    except Exception as e:
        db.session.rollback()
        return None, str(e), 'Internal Server Error'


def create_employee_by_csv_service(data):
    try:

        import_file = data.get("import_file")

        if not import_file:
            return None,  "Bad Request", "No file provided"

        # Check file format (csv or excel)
        if import_file.filename.endswith('.csv'):

            df = pd.read_csv(BytesIO(import_file.read()))

        elif import_file.filename.endswith(('.xls', '.xlsx')):

            df = pd.read_excel(BytesIO(import_file.read()))

        else:
            return None, "Unsupported file format", "Bad Request"

        required_columns = ['EmployeeCode', 'FullName',
                            'Designation', 'Department', 'ContactNo']
        missing_columns = [
            col for col in required_columns if col not in df.columns]

        if missing_columns:
            return None, "ValidationError", f'Missing required columns: {", ".join(missing_columns)}'

        for _, row in df.iterrows():
            employee_code = str(row.get('EmployeeCode'))

            # Check if Employee exists
            existing_employee = EmployeeMain.query.filter_by(
                EmployeeCode=employee_code).first()

            existing_address = EmployeeAddress.query.filter_by(
                EmployeeCode=employee_code).first()

            if existing_employee:
                existing_employee.ShortName = row.get('FullName')
                existing_employee.FirstName = row.get('FullName')
                existing_employee.Department = row.get('Department')
                existing_employee.Designation = row.get('Designation')
                existing_employee.ContactNo = row.get('ContactNo')
                if existing_address:
                    existing_address.Mobile = row.get('ContactNo')
                else:
                    new_employee_address = EmployeeAddress(
                        EmployeeCode=employee_code,
                        AddressType="Permanent",
                        Mobile=row.get('ContactNo')
                    )
                    db.session.add(new_employee_address)

            else:
                new_employee = EmployeeMain(
                    EmployeeCode=str(row.get('EmployeeCode')),
                    AlternateCode=str(row.get('EmployeeCode')),
                    ShortName=row.get('FullName'),
                    FirstName=row.get('FullName'),
                    Department=row.get('Department'),
                    Designation=row.get('Designation'),
                    ContactNo=row.get('ContactNo'),
                    DateofJoining=datetime.now(timezone.utc)
                )
                new_employee_address = EmployeeAddress(
                    EmployeeCode=employee_code,
                    AddressType="Permanent",
                    Mobile=row.get('ContactNo')
                )
                db.session.add(new_employee)
                db.session.add(new_employee_address)

        db.session.commit()

        return [], None, 'Employees updated successfully'

    except Exception as e:
        db.session.rollback()
        return None, str(e), 'Internal Server Error'


def create_employee_service(data):
    try:
        employee_code = str(data.get('EmployeeCode'))
        employee_name = str(data.get('EmployeeName'))
        designation = data.get('Designation')
        department = data.get('Department')
        contact_no = data.get('ContactNo')

        if not employee_code or not employee_name:
            return None, True, 'Employee name and Employee code are mandatory fields'

        existing_employee = EmployeeMain.query.filter_by(
            EmployeeCode=employee_code).first()

        existing_address = EmployeeAddress.query.filter_by(
            EmployeeCode=employee_code).first()

        if existing_employee:
            existing_employee.ShortName = employee_name
            existing_employee.Department = department
            existing_employee.Designation = designation
            existing_employee.ContactNo = contact_no

            if existing_address:
                existing_address.Mobile = contact_no
            else:
                new_employee_address = EmployeeAddress(
                    EmployeeCode=employee_code,
                    AddressType="Permanent",
                    Mobile=contact_no
                )
                db.session.add(new_employee_address)

            db.session.commit()
            return existing_employee.as_dict(), None, 'Employee updated successfully'

        else:
            new_employee = EmployeeMain(
                EmployeeCode=employee_code,
                AlternateCode=employee_code,
                ShortName=employee_name,
                FirstName=employee_name,
                Department=department,
                Designation=designation,
                ContactNo=contact_no,
                DateofJoining=datetime.now(timezone.utc)
            )
            new_employee_address = EmployeeAddress(
                EmployeeCode=employee_code,
                AddressType="Permanent",
                Mobile=contact_no
            )
            db.session.add(new_employee)
            db.session.add(new_employee_address)
            db.session.commit()
            return new_employee.as_dict(), None, 'Employee created successfully'

    except Exception as e:
        db.session.rollback()
        return None, str(e), 'Internal Server Error'


def save_report_template_service(data):
    try:
        menu = data.get('Menu')
        description = data.get('Description')
        user_id = str(data.get('UserId'))
        value = data.get('Value')
        config = data.get('Config')

        if not user_id or not value:
            return None, True, 'UserId and value are mandatory fields'

        existing_setting = ReportDesignMaster.query.filter_by(
            Menu=menu, UserId=user_id).first()

        if existing_setting:
            existing_setting.Config = config
            existing_setting.Value = value
            db.session.commit()
            return existing_setting.as_dict(), None, 'Settings updated successfully'

        else:
            # new entry
            new_setting = ReportDesignMaster(
                Menu=menu,
                UserId=user_id,
                Description=description,
                Value=value,
                Config=config
            )
            db.session.add(new_setting)
            db.session.commit()
            return new_setting.as_dict(), None, 'Settings updated successfully'

    except Exception as e:
        db.session.rollback()
        return None, str(e), 'Internal Server Error'


def preview_report_template_service(data):
    try:
        menu = data.get('Menu')
        user_id = str(data.get('UserId'))
        value = data.get('Value')

        if not user_id or not value:
            return None, True, 'UserId and value are mandatory fields'

        existing_setting = ReportDesignMaster.query.filter_by(
            Menu=menu, UserId=user_id).first()

        if existing_setting:

            static_folder_path = os.path.join(os.path.dirname(
                os.path.abspath(__file__)), '../../static/data/report_columns.json')

            with open(static_folder_path) as json_file:
                data = json.load(json_file)

            if not data:
                return None, True, 'No data found'

            context = {item['label']: item['defaultValue'] for item in data}

            populated_html = render_template_string(value, **context)

            pdf_filename = f'{menu}_report_{datetime.now(timezone.utc)}.pdf'
            pdf_buffer = BytesIO()

            # Convert HTML to PDF
            pisa_status = pisa.CreatePDF(populated_html, dest=pdf_buffer)

            if pisa_status.err:
                return None, True, 'Visitor not found'

            pdf_buffer.seek(0)

            return {'file': pdf_buffer, 'filename': pdf_filename, 'mimetype': "application/pdf"}, None, 'success'

        return None, True, 'No report found'

    except Exception as e:
        db.session.rollback()
        return None, str(e), 'Internal Server Error'


def create_menu_service(data):
    try:

        try:
            validated_data = MenuUpdateSchema(**data)
        except ValidationError as e:
            return None, "ValidationError", f'Validation error: {e}'

        if 'id' in data and data['id']:

            menu_item = MenuMaster.query.get(data['id'])

            if not menu_item:
                return None, True, "Menu item not found"

            menu_item.nav_bar_name = validated_data.nav_bar_name
            menu_item.isdrobdown = validated_data.isdrobdown
            menu_item.uri_link = validated_data.uri_link
            menu_item.icon_name = validated_data.icon_name
            menu_item.status = validated_data.status
            menu_item.deleted_at = validated_data.deleted_at
            menu_item.parent_id = validated_data.parent_id
            if validated_data.order is not None:
                menu_item.order = validated_data.order

            db.session.commit()
            return menu_item.as_dict(), None, 'Menu updated successfully'
        else:
            if validated_data.order is None:
                max_order = db.session.query(
                    db.func.max(MenuMaster.order)).scalar() or 0
                validated_data.order = max_order + 1

            menu_item = MenuMaster(
                nav_bar_name=validated_data.nav_bar_name,
                isdrobdown=validated_data.isdrobdown,
                uri_link=validated_data.uri_link,
                parent_id=validated_data.parent_id,
                icon_name=validated_data.icon_name,
                status=validated_data.status,
                order=validated_data.order
            )

            db.session.add(menu_item)
            db.session.commit()
            return menu_item.as_dict(), None, 'Menu created successfully'

    except Exception as e:
        db.session.rollback()
        return None, str(e), 'Internal Server Error'


def build_menu_hierarchy(item, menu_items):
    children = [
        child for child in menu_items if child.parent_id == item.id]
    children_output = [build_menu_hierarchy(
        child) for child in children]  # Recursive call

    return {
        'id': item.id,
        'nav_bar_name': item.nav_bar_name,
        'isdrobdown': item.isdrobdown,
        'uri_link': item.uri_link,
        'parent_id': item.parent_id,
        'icon_name': item.icon_name,
        'status': item.status,
        'order': item.order,
        'children': children_output
    }


def get_menus_service(data):
    parent_id = request.args.get('parent_id', type=int)
    try:
        if parent_id:
            menu_items = MenuMaster.query.filter_by(parent_id=parent_id).all()
        else:
            menu_items = MenuMaster.query.all()

        if not menu_items:
            return [], None, 'No data found'

        menu_map = {item.id: item for item in menu_items}

        response = [build_menu_hierarchy(
            item, menu_items) for item in menu_items if item.parent_id is None]

        return response, None, 'Data fetched successfully'
    except Exception as e:
        db.session.rollback()
        return None, str(e), 'Internal Server Error'


def get_menu_by_userid_service(data):
    user_id = request.args.get('user_id', type=int)
    try:
        if user_id:
            user = User.query.filter_by(id=user_id).first()
        else:
            return None, 'ValidationError', 'User is required'

        if not user:
            return None, 'User not found', 'No data found'

        if not user.AccessControl or user.AccessControl is None:
            return [], None, 'No data found'

        if isinstance(user.AccessControl, str):
            access_control = json.loads(user.AccessControl)
        else:
            access_control = user.AccessControl

        menu_items = MenuMaster.query.all()

        filtered_menu_items = [
            item for item in menu_items
            if (
                item.uri_link in access_control.get(
                    'access', {}) and access_control['access'][item.uri_link]
            )
        ]

        map_filtered_menu = [item for item in filtered_menu_items]

        menu = [
            build_menu_hierarchy(item, map_filtered_menu)
            for item in map_filtered_menu
            if item.parent_id is None
        ]

        response = {'menu': menu, 'access_control': json.dumps(access_control ,sort_keys=False)}

        return response, None, 'Data fetched successfully'
    
    except Exception as e:
        db.session.rollback()
        return None, str(e), 'Internal Server Error'
