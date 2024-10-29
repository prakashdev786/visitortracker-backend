from flask import jsonify
from app.services.user_service import login_user_service, reset_password_service, get_users_service, update_user_permission_service
from ..utils.responses import create_response


def login_user(data):
    user, error, message = login_user_service(data)
    if error:
        return jsonify({'error': error, 'message': message, 'status': 'error'}), 401

    return create_response('Login successful', data=[user], status='success'), 200


def reset_password(data):
    try:

        result, error, message = reset_password_service(data)
        if error:
            return jsonify({'error': error, 'message': message, 'status': 'error'}), 400
        return create_response('Password reset successful', data=result, status='success'), 200

    except Exception as err:
        return jsonify({'error': str(err), 'message': 'Internal Server Error', 'status': 'error'}), 500


def get_users():
    try:
        result, error, message = get_users_service()
        if error:
            return jsonify({'error': error, 'message': message, 'status': 'error'}), 400
        return create_response('data fetched successfully', data=result, status='success'), 200

    except Exception as err:
        return jsonify({'error': str(err), 'message': 'Internal Server Error', 'status': 'error'}), 500


def update_user_permission(data):
    try:
        result, error, message = update_user_permission_service(data)

        if error:
            return jsonify({'error': error, 'message': message, 'data': result, 'status': 'error'}), 400

        return create_response(message, data=result, status='success'), 200

    except Exception as err:
        return jsonify({'error': str(err), 'message': 'Internal Server Error', 'status': 'error'}), 500
