from flask import jsonify, send_file
from ..utils.responses import create_response
from app.services.common_service import (get_settings_by_userid_service, create_settings_service, create_employee_by_csv_service,
                                         create_employee_service, save_report_template_service, get_design_service, preview_report_template_service,
                                         create_menu_service, get_menus_service, get_menu_by_userid_service)


def get_settings_by_userid(data):
    try:

        result, error, message = get_settings_by_userid_service(data)
        if error:
            return jsonify({'error': error, 'message': message, 'status': 'error'}), 400
        return create_response('data fetched successfully', data=result, status='success'), 200

    except Exception as err:
        return jsonify({'error': str(err), 'message': 'Internal Server Error', 'status': 'error'}), 500


def create_settings(data):
    try:

        result, error, message = create_settings_service(data)
        if error:
            return jsonify({'error': error, 'message': message, 'status': 'error'}), 400
        return create_response(message, data=result, status='success'), 200

    except Exception as err:
        return jsonify({'error': str(err), 'message': 'Internal Server Error', 'status': 'error'}), 500


def create_employee_by_csv(data):
    try:
        result, error, message = create_employee_by_csv_service(data)

        if error:
            return jsonify({'error': error, 'message': message, 'data': result, 'status': 'error'}), 400

        return create_response('Created successfully', data=result, status='success'), 200

    except Exception as err:
        return jsonify({'error': str(err), 'message': 'Internal Server Error', 'status': 'error'}), 500


def create_employee(data):
    try:
        result, error, message = create_employee_service(data)

        if error:
            return jsonify({'error': error, 'message': message, 'data': result, 'status': 'error'}), 400

        return create_response(message, data=result, status='success'), 200

    except Exception as err:
        return jsonify({'error': str(err), 'message': 'Internal Server Error', 'status': 'error'}), 500


def save_report_template(data):
    try:
        result, error, message = save_report_template_service(data)

        if error:
            return jsonify({'error': error, 'message': message, 'data': result, 'status': 'error'}), 400

        return create_response(message, data=result, status='success'), 200

    except Exception as err:
        return jsonify({'error': str(err), 'message': 'Internal Server Error', 'status': 'error'}), 500


def preview_report_template(data):
    try:
        result, error, message = preview_report_template_service(data)

        if error:
            return jsonify({'error': error, 'message': message, 'data': result, 'status': 'error'}), 400

        return send_file(result.get('file'), as_attachment=True, download_name=result.get('filename'), mimetype=result.get('mimetype')), 200

    except Exception as err:
        return jsonify({'error': str(err), 'message': 'Internal Server Error', 'status': 'error'}), 500


def get_design_controller(data):
    try:

        result, error, message = get_design_service(data)

        if error:
            return jsonify({'error': error, 'message': message, 'data': result, 'status': 'error'}), 400

        return create_response(message, data=result, status='success'), 200

    except Exception as err:
        return jsonify({'error': str(err), 'message': 'Internal Server Error', 'status': 'error'}), 500


def create_menu_controll(data):
    try:
        result, error, message = create_menu_service(data)

        if error:
            return jsonify({'error': error, 'message': message, 'data': result, 'status': 'error'}), 400

        return create_response(message, data=result, status='success'), 200

    except Exception as err:
        return jsonify({'error': str(err), 'message': 'Internal Server Error', 'status': 'error'}), 500


def get_menus_control(data):
    try:

        result, error, message = get_menus_service(data)

        if error:
            return jsonify({'error': error, 'message': message, 'data': result, 'status': 'error'}), 400

        return create_response(message, data=result, status='success'), 200

    except Exception as err:
        return jsonify({'error': str(err), 'message': 'Internal Server Error', 'status': 'error'}), 500


def get_menu_by_userid(data):
    try:

        result, error, message = get_menu_by_userid_service(data)

        if error:
            return jsonify({'error': error, 'message': message, 'data': result, 'status': 'error'}), 400

        return create_response(message, data=result, status='success'), 200

    except Exception as err:
        return jsonify({'error': str(err), 'message': 'Internal Server Error', 'status': 'error'}), 500
