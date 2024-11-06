from functools import wraps
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity

def token_required(f):
    @wraps(f)
    @jwt_required()
    def decorated_function(*args, **kwargs):
        current_user = get_jwt_identity()
        return f(current_user, *args, **kwargs)

    return decorated_function
