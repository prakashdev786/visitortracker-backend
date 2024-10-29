from flask import jsonify


def create_response(message, data=None, status='success'):
    response = {
        'message': message,
        'data': data,
        'status': status
    }
    return jsonify(response)
