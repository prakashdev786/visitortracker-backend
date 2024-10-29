from flask import jsonify
from ..utils.responses import create_response
from app.services.visitors_service import (get_companies_service, get_visitors_service,
                                           generate_pass_number, create_visitorpass_service,
                                           get_visitors_category_service,
                                           get_employees_service, get_visitor_report_service,
                                           get_departments_service,
                                           get_designation_service,
                                           create_appointment_service, get_appointments_service)


def get_visitors():
    try:

        result, error, message = get_visitors_service()
        if error:
            return jsonify({'error': error, 'message': message, 'status': 'error'}), 400
        return create_response('data fetched successfully', data=result, status='success'), 200

    except Exception as err:
        return jsonify({'error': str(err), 'message': 'Internal Server Error', 'status': 'error'}), 500


def get_visitors_category():
    try:

        result, error, message = get_visitors_category_service()
        if error:
            return jsonify({'error': error, 'message': message, 'status': 'error'}), 400
        return create_response('data fetched successfully', data=result, status='success'), 200

    except Exception as err:
        return jsonify({'error': str(err), 'message': 'Internal Server Error', 'status': 'error'}), 500


def get_companies():
    try:

        result, error, message = get_companies_service()
        if error:
            return jsonify({'error': error, 'message': message, 'status': 'error'}), 400
        return create_response('data fetched successfully', data=result, status='success'), 200

    except Exception as err:
        return jsonify({'error': str(err), 'message': 'Internal Server Error', 'status': 'error'}), 500


def get_employees():
    try:

        result, error, message = get_employees_service()
        if error:
            return jsonify({'error': error, 'message': message, 'status': 'error'}), 400
        return create_response('data fetched successfully', data=result, status='success'), 200

    except Exception as err:
        return jsonify({'error': str(err), 'message': 'Internal Server Error', 'status': 'error'}), 500


def get_departments():
    try:

        result, error, message = get_departments_service()
        if error:
            return jsonify({'error': error, 'message': message, 'status': 'error'}), 400
        return create_response('data fetched successfully', data=result, status='success'), 200

    except Exception as err:
        return jsonify({'error': str(err), 'message': 'Internal Server Error', 'status': 'error'}), 500


def get_designation():
    try:

        result, error, message = get_designation_service()
        if error:
            return jsonify({'error': error, 'message': message, 'status': 'error'}), 400
        return create_response('data fetched successfully', data=result, status='success'), 200

    except Exception as err:
        return jsonify({'error': str(err), 'message': 'Internal Server Error', 'status': 'error'}), 500


def get_pass_number():
    try:
        result, error, message = generate_pass_number()

        if error:
            return jsonify({'error': error, 'message': message, 'status': 'error'}), 400

        return create_response('data generated successfully', data=result, status='success'), 200

    except Exception as err:
        return jsonify({'error': str(err), 'message': 'Internal Server Error', 'status': 'error'}), 500


def create_visitor_pass(data):
    try:
        result, error, message = create_visitorpass_service(data)

        if error:
            return jsonify({'error': error, 'message': message, 'status': 'error'}), 400

        return create_response('Created successfully', data=result, status='success'), 200

    except Exception as err:
        return jsonify({'error': str(err), 'message': 'Internal Server Error', 'status': 'error'}), 500


def get_visitor_report(data):
    try:
        result, error, message = get_visitor_report_service(data)

        if error:
            return jsonify({'error': error, 'message': message, 'status': 'error'}), 400

        return create_response('data fetched successfully', data=result, status='success'), 200

    except Exception as err:
        return jsonify({'error': str(err), 'message': 'Internal Server Error', 'status': 'error'}), 500


def create_appointment(data):
    try:
        result, error, message = create_appointment_service(data)

        if error:
            return jsonify({'error': error, 'message': message, 'status': 'error'}), 400

        return create_response(message, data=result, status='success'), 200

    except Exception as err:
        return jsonify({'error': str(err), 'message': 'Internal Server Error', 'status': 'error'}), 500


def get_appointments_controller(data):
    try:

        result, error, message = get_appointments_service(data)

        if error:
            return jsonify({'error': error, 'message': message, 'data': result, 'status': 'error'}), 400

        return create_response(message, data=result, status='success'), 200

    except Exception as err:
        return jsonify({'error': str(err), 'message': 'Internal Server Error', 'status': 'error'}), 500
