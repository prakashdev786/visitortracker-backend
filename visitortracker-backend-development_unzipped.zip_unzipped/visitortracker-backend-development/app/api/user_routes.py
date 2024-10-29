from flask import Blueprint, request
from app.controllers.user_controller import login_user, reset_password, get_users, update_user_permission
from ..utils.common_utils import get_request_data

user_bp = Blueprint('user_bp', __name__)


@user_bp.route('/login', methods=['POST'])
def login():
    # data = request.get_json()
    data = get_request_data()
    return login_user(data)


@user_bp.route('/resetpassword', methods=['POST'])
def reset():
    data = get_request_data()
    return reset_password(data)


@user_bp.route('/getUsers', methods=['GET'])
def getUsers():
    return get_users()


@user_bp.route('/updateUserPermission', methods=['POST'])
def updateUserPermission():
    data = get_request_data()
    return update_user_permission(data)
