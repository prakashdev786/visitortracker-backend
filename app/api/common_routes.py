from flask import Blueprint,  jsonify
from app.controllers.common_controller import get_settings_by_userid, create_settings, create_employee_by_csv, create_employee, save_report_template, get_design_controller, preview_report_template, create_menu_controll, get_menus_control, get_menu_by_userid
from ..utils.common_utils import get_request_data
import json
import os

common_bp = Blueprint('common_bp', __name__)


@common_bp.route("/getSettingsByUserId/<string:user_id>", methods=['GET'])
def getSettingsByUserId(user_id):
    return get_settings_by_userid(user_id)


@common_bp.route("/createSettings", methods=['POST'])
def createSettings():
    data = get_request_data()
    return create_settings(data)


@common_bp.route('/createEmployeeByCsv', methods=['POST'])
def createEmployeeByCsv():
    data = get_request_data()
    return create_employee_by_csv(data)


@common_bp.route('/createEmployee', methods=['POST'])
def createEmployee():
    data = get_request_data()
    return create_employee(data)


@common_bp.route('/saveReportTemplate', methods=['POST'])
def saveReportTemplate():
    data = get_request_data()
    return save_report_template(data)


@common_bp.route('/previewReportTemplate', methods=['POST'])
def previewReportTemplate():
    data = get_request_data()
    return preview_report_template(data)


@common_bp.route("/getDesign", methods=['GET'])
def getDesign():
    data = get_request_data()
    return get_design_controller(data)


@common_bp.route("/getReportColumn", methods=['GET'])
def getReportColumn():

    static_folder_path = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), '../../static/data/report_columns.json')
    try:
        with open(static_folder_path) as json_file:
            data = json.load(json_file)
        return jsonify(data)

    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404


@common_bp.route('/createMenu', methods=['POST'])
def createMenu():
    data = get_request_data()
    return create_menu_controll(data)


@common_bp.route("/getAllMenu", methods=['GET'])
def getAllMenu():
    data = get_request_data()
    return get_menus_control(data)


@common_bp.route("/getMenuByUserId", methods=['GET'])
def getMenuByUserId():
    data = get_request_data()
    return get_menu_by_userid(data)
