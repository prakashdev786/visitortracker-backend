from flask import Blueprint, request
from ..utils.common_utils import get_request_data
from app.services.visitors_service import generate_appointment_number
from app.utils.jwt_decorator import  token_required
from app.controllers.visitors_controller import (get_companies, get_visitors, get_pass_number, create_visitor_pass,
                                                 get_visitors_category, get_employees, get_visitor_report, get_departments,
                                                 get_designation, create_appointment, get_appointments_controller,
                                                 get_appointment_by_appid,update_temp_visitor,get_temp_visitor_by_appnum)


visitor_bp = Blueprint('visitor_bp', __name__)


@visitor_bp.route('/getVisitors', methods=['GET'])
def getVistors():
    return get_visitors()


@visitor_bp.route('/getVisitorsCategory', methods=['GET'])
def getVisitorsCategory():
    return get_visitors_category()


@visitor_bp.route('/getcompanies', methods=['GET'])
def getCompanies():
    return get_companies()


@visitor_bp.route('/getEmployees', methods=['GET'])
def getEmployees():
    return get_employees()


@visitor_bp.route('/getDepartments', methods=['GET'])
def getDepartments():
    return get_departments()


@visitor_bp.route('/getDesignation', methods=['GET'])
def getDesignation():
    return get_designation()


@visitor_bp.route('/getPassNumber', methods=['GET'])
def getPassNumber():
    return get_pass_number()


@visitor_bp.route('/createVisitorPass', methods=['POST'])
def createVisitorPass():
    data = get_request_data()
    return create_visitor_pass(data)


@visitor_bp.route('/getVisitorReport', methods=['POST'])
def getVisitorReport():
    data = get_request_data()
    return get_visitor_report(data)


@visitor_bp.route('/createAppointment', methods=['POST'])
def createAppointment():
    data = get_request_data()
    return create_appointment(data)


@visitor_bp.route('/getAppointmentNumber', methods=['GET'])
def getAppointmentNumber():
    return generate_appointment_number()


@visitor_bp.route("/getAllAppointments", methods=['POST'])
@token_required
def getAllAppointments(current_user):
    data = get_request_data()
    return get_appointments_controller(data)


@visitor_bp.route("/getAppointmentByAppId", methods=['POST'])
def getAppointmentByAppId():
    data = get_request_data()
    return get_appointment_by_appid(data)


@visitor_bp.route("/updateTempVisitor", methods=['POST'])
def updateTempVisitor():
    data = get_request_data()
    return update_temp_visitor(data)


@visitor_bp.route("/getTempVisitorByAppNum", methods=['POST'])
def getTempVisitorByAppNum():
    data = get_request_data()
    return get_temp_visitor_by_appnum(data)
