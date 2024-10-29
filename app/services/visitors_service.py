from flask import request
from app.models import CompanyMaster, VisitorsMaster, VisitorsLog, EmployeeMain, AppointMents
from ..utils.common_utils import save_image
from sqlalchemy import text, or_, desc, asc, cast, Date
import string
import re
from datetime import datetime
from app import db
import uuid


def get_visitors_service():

    data = VisitorsMaster.query.all()

    data_dict = [visitors.as_dict() for visitors in data]

    if not data:
        return None, True, "No data found"

    return data_dict, None, None


def get_visitors_category_service():

    data = VisitorsMaster.query.with_entities(
        VisitorsMaster.VisitorCategory).distinct().all()

    data_dict = [{"label": categories[0]} for categories in data]

    print(data_dict, 'categories')

    if not data:
        return None, True, "No data found"

    return data_dict, None, None


def get_companies_service():

    data = CompanyMaster.query.all()

    data_dict = [newdata.as_dict() for newdata in data]

    if not data:
        return None, True, "No data found"

    return data_dict, None, None


def get_employees_service():

    data = EmployeeMain.query.distinct(EmployeeMain.EmployeeCode).order_by(
       EmployeeMain.EmployeeCode.desc(), EmployeeMain.SNO.desc()).limit(200).all()

    data_dict = [newdata.as_dict() for newdata in data]

    if not data:
        return None, True, "No data found"

    return data_dict, None, None


def get_departments_service():

    data = EmployeeMain.query.with_entities(
        EmployeeMain.Department).distinct().all()

    data_dict = [{"Department": newdata[0]} for newdata in data]

    if not data:
        return None, True, "No data found"

    return data_dict, None, None


def get_designation_service():

    data = EmployeeMain.query.with_entities(
        EmployeeMain.Designation).distinct().all()

    data_dict = [{"Designation": newdata[0]} for newdata in data]

    if not data:
        return None, True, "No data found"

    return data_dict, None, None


def generate_pass_number():
    today_date = datetime.now().strftime('%Y%m%d')

    total_visitors_today = VisitorsLog.query.filter(
        VisitorsLog.InTime >= datetime.now().date()).count()

    next_number = total_visitors_today + 1

    sequence_str = f'{next_number:03}'

    pass_number = f'{sequence_str}/{today_date}'

    return pass_number, None, None


def create_visitorpass_service(data):
    try:

        # fields = {key: data.get(key) for key in [
        #     'AppointmentNumber', 'PassNumber', 'BadgeNumber', 'InTime',
        #     'VisTotal', 'VisPurpose', 'VisAdditional', 'VehicleNumber',
        #     'ReturnableItems', 'EmployeeCode', 'Department',
        #     'VisitorName', 'VisCategory', 'MobileNumber',
        #     'EmailID', 'Company', 'IDCardType', 'IDCardNumber',
        #     'VisitorImage', 'IDCardImage'
        # ]}

        pass_number = data.get('PassNumber')

        if not pass_number:
            return None, True, 'PassNumber is required'

        existing_pass = VisitorsLog.query.filter_by(
            PassNumber=pass_number).first()

        if existing_pass:
            return None, True, 'PassNumber already exists'

        sanitized_pass_number = re.sub(r'[<>:"/\\|?*]', '_', pass_number)

        # Check existing visitor or create a new one
        visitor = VisitorsMaster.query.filter_by(
            MobileNumber=data.get('MobileNumber'),
            Company=data.get('Company'),
            VisitorName=data.get('VisitorName'),
        ).first()

        company = CompanyMaster.query.filter_by(Company=data.get('Company')).first() or CompanyMaster(
            Company=data.get('Company'),
            AddressLine1=data.get('AddressLine1'),
            AddressLine2=data.get('AddressLine2'),
            State=data.get('State'),
            Country=data.get('Country'),
            PinCode=data.get('PinCode'),
            Mobile=data.get('MobileNumber'),
            Email=data.get('EmailID'),
            createdAt=datetime.now(),
            updatedAt=datetime.now()
        )
        db.session.add(company) if company.SNO is None else None
        db.session.flush()

        if not visitor:

            visitor = VisitorsMaster(
                VisitorName=data.get('VisitorName'),
                Company=company.Company,
                VisitorCategory=data.get('VisCategory'),
                MobileNumber=data.get('MobileNumber'),
                EmailID=data.get('EmailID'),
                IDCardType=data.get('IDCardType'),
                IDCardNumber=data.get('IDCardNumber'),
                createdAt=datetime.now(),
                updatedAt=datetime.now()
            )
            db.session.add(visitor)
            db.session.flush()  # Get visitor ID

        # Update last visit date
        visitor.LastVisitDate = datetime.now() if visitor else None
        visitor.updatedAt = datetime.now() if visitor else None

        # Handle image uploads
        unique_id = str(uuid.uuid4().hex)
        visitor_image_path = save_image(data.get('VisitorImage'), f'{sanitized_pass_number}_{unique_id}_{data.get('VisitorImage').filename}', "VisitorFiles") if data.get('VisitorImage') else None
        id_card_image_path = save_image(data.get('IDCardImage'), f'{sanitized_pass_number}_{unique_id}_{data.get('IDCardImage').filename}', "VisitorFiles") if data.get('IDCardImage') else None

        visitor_pass_log = VisitorsLog(
            IDCardImageName=id_card_image_path,
            VisitorID=visitor.SNO,
            CompanyID=company.SNO if company else None,
            Company=data.get('Company'),
            PassNumber=data.get('PassNumber'),
            PassDate=datetime.now(),
            BadgeNumber=data.get('BadgeNumber'),
            VisitorName=data.get('VisitorName'),
            VisCategory=data.get('VisCategory'),
            MobileNumber=data.get('MobileNumber'),
            VisTotal=data.get('VisTotal'),
            VisPurpose=data.get('VisPurpose'),
            VehicleNumber=data.get('VehicleNumber'),
            VisAdditional=data.get('VisAdditional'),
            ReturnableItems=data.get('ReturnableItems'),
            EmployeeCode=data.get('EmployeeCode'),
            Department=data.get('Department'),
            InTime=data.get('InTime'),
            ImageName=visitor_image_path,
            AppointmentNumber=data.get('AppointmentNumber')
        )

        db.session.add(visitor_pass_log)
        db.session.commit()
        return 'Created successfully', None, None

    except Exception as err:
        db.session.rollback()
        return None, str(err), 'Internal Server Error'


def get_visitor_report_service(data):
    try:

        from_date = data.get('from_date')
        to_date = data.get('to_date')
        employee_name = data.get('employee_name', [])
        employee_department = data.get('employee_department', [])
        visitor_company = data.get('visitor_company', [])
        visitor_name = data.get('visitor_name', [])
        visitor_category = data.get('visitor_category', [])
        purpose = data.get('purpose', [])

        query = VisitorsLog.query

        if from_date:
            query = query.filter(VisitorsLog.InTime >= from_date)
        if to_date:
            query = query.filter(VisitorsLog.InTime <= to_date)

        # if employee_name:
        #     query = query.filter(VisitorsLog.VisitorName.ilike(f"%{employee_name}%"))

        if employee_name:
            query = query.filter(VisitorsLog.VisitorName.in_(employee_name))

        if employee_department:
            query = query.filter(
                VisitorsLog.Department.in_(employee_department))

        if visitor_company:
            query = query.filter(VisitorsLog.Company.in_(visitor_company))

        if visitor_name:
            query = query.filter(VisitorsLog.VisitorName.in_(visitor_name))

        if visitor_category:
            query = query.filter(VisitorsLog.VisCategory.in_(visitor_category))

        if purpose:
            query = query.filter(VisitorsLog.VisPurpose.in_(purpose))

        results = query.all()

        # logs = [log.as_dict() for log in results]
        logs = []
        for log in results:
            log_dict = log.as_dict()

            log_dict['InTime'] = log.InTime.strftime(
                "%d-%m-%Y %I:%M %p") if log.InTime else None
            log_dict['OutTime'] = log.OutTime.strftime(
                "%d-%m-%Y %I:%M %p") if log.OutTime else None
            logs.append(log_dict)

        return logs, None, 'data fetched successfully'

    except Exception as e:
        return None, str(e), 'Internal Server Error'


def generate_appointment_number():
    today_date = datetime.now().strftime('%Y%m%d')

    total_appointment_today = AppointMents.query.filter(
        AppointMents.CreatedAt >= datetime.now().date()).count()

    next_number = total_appointment_today + 1

    sequence_str = f'{next_number:03}'

    pass_number = f'{sequence_str}/{today_date}'

    return pass_number, None, None


def create_appointment_service(data):
    try:

        app_number = data.get('AppNumber')

        if not app_number:
            return None, True, 'Appointment Number is required'

        existing_appointment = AppointMents.query.filter_by(
            AppNumber=app_number).first()

        if existing_appointment:
            return None, True, 'Appointment number already exists'

        # Check existing visitor or create a new one
        visitor = VisitorsMaster.query.filter_by(
            MobileNumber=data.get('MobileNumber'),
            Company=data.get('CompanyName'),
            VisitorName=data.get('VisitorName'),
        ).first()

        company = CompanyMaster.query.filter_by(Company=data.get('CompanyName')).first() or CompanyMaster(
            Company=data.get('CompanyName'),
            AddressLine1=data.get('AddressLine1'),
            AddressLine2=data.get('AddressLine2'),
            City=data.get('City'),
            State=data.get('State'),
            Country=data.get('Country'),
            PinCode=data.get('PinCode'),
            Phone=data.get('TelePhone'),
            createdAt=datetime.now(),
            updatedAt=datetime.now()
        )
        db.session.add(company) if company.SNO is None else None
        db.session.flush()

        if not visitor:

            visitor = VisitorsMaster(
                VisitorName=data.get('VisitorName'),
                Company=company.Company,
                VisitorCategory=data.get('VisitorCategory'),
                MobileNumber=data.get('MobileNumber'),
                EmailID=data.get('EmailId'),
                createdAt=datetime.now(),
                updatedAt=datetime.now()
            )
            db.session.add(visitor)
            db.session.flush()  # Get visitor ID

        visitor_appointment = AppointMents(
            AppNumber=data.get('AppNumber'),
            CompanyName=data.get('CompanyName'),
            VisitorName=data.get('VisitorName'),
            VisitorCategory=data.get('VisitorCategory'),
            AddressLine1=data.get('AddressLine1'),
            AddressLine2=data.get('AddressLine2'),
            MobileNumber=data.get('MobileNumber'),
            City=data.get('City'),
            Purpose=data.get('Purpose'),
            State=data.get('State'),
            PinCode=data.get('PinCode'),
            TelePhone=data.get('TelePhone'),
            EmailId=data.get('EmailId'),
            AppTime=data.get('AppTime'),
            AppDate=data.get('AppDate'),
            CreatedAt=datetime.now(),
            UpdatedAt=datetime.now(),
            VisitorId=visitor.SNO,
            CompanyId=company.SNO if company else None
        )

        db.session.add(visitor_appointment)
        db.session.commit()
        return visitor_appointment.as_dict(), None, 'Created successfully'

    except Exception as err:
        db.session.rollback()
        return None, str(err), 'Internal Server Error'


def get_appointments_service(data):
    try:
        if not data or (not data.get('filter') and not data.get('sorting') and not data.get('search_data')):
            data = AppointMents.query.all()
            appointment_dict = [appointment.as_dict() for appointment in data]
            return appointment_dict, None, None

        filters = data.get('filter', {})
        sorting = data.get('sorting', {})
        search_data = data.get('search_data', '')

        query = AppointMents.query

        # Apply filters
        for column, value in filters.items():
            if hasattr(AppointMents, column):
                query = query.filter(getattr(AppointMents, column) == value)

        # Apply date range filtering
        if 'StartDate' in filters and 'EndDate' in filters:
            start_date = datetime.strptime(filters['StartDate'], '%Y-%m-%d')
            end_date = datetime.strptime(filters['EndDate'], '%Y-%m-%d')
            query = query.filter(
                cast(AppointMents.AppDate, Date).between(start_date, end_date))

        # Apply search multiple fields
        if search_data:
            search_columns = ['VisitorName',
                              'AppDate', 'CompanyName', 'AppNumber']
            search_filters = [getattr(AppointMents, col).ilike(
                f'%{search_data}%') for col in search_columns if hasattr(AppointMents, col)]
            if search_filters:
                query = query.filter(or_(*search_filters))

        # Apply sorting
        for column, order in sorting.items():
            if hasattr(AppointMents, column):
                if order == 'asc':
                    query = query.order_by(asc(getattr(AppointMents, column)))
                elif order == 'desc':
                    query = query.order_by(desc(getattr(AppointMents, column)))

        data = query.all()

        appointment_dict = [appointment.as_dict() for appointment in data]

        if not data:
            return None, True, "No data found"

        return appointment_dict, None, None

    except Exception as err:
        db.session.rollback()
        return None, str(err), 'Internal Server Error'
