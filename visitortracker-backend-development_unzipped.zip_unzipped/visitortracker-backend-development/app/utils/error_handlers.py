

from flask import jsonify


def register_error_handlers(app):
    @app.errorhandler(415)
    def unsupported_media_type(error):
        return jsonify({
            'status': 'error',
            'message': 'Unsupported Media Type. Use Content-Type: application/json',
            'data': ''
        }), 415

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'status': 'error',
            'message': 'Bad Request: ' + str(error),
            'data': ''
        }), 400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'status': 'error',
            'message': 'Resource not found',
            'data': ''
        }), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            'status': 'error',
            'message': 'Internal server error. Please try again later.',
            'data': '',
        }), 500

    @app.errorhandler(Exception)
    def handle_exception(e):
        return jsonify({
            'error': 'Internal Server Error',
            'message': 'An unexpected error occurred',
            'status': 'error',
            'data': e
        }), 500
