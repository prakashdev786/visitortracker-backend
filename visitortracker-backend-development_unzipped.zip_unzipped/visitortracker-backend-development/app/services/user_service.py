from app.models import User, EmployeeAddress
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy import text
from flask_mail import Message
from app import db, mail
import string
import random
import json


def login_user_service(data):

    username = data.get('UserName')
    password = data.get('UPassword')

    if not username or not password:
        return None, True, "Username and password are required"

    user = User.query.filter_by(UserName=username).first()

    # if not user or not check_password_hash(user.UPassword, password):
    #     return None, "Invalid username or password"
    if not user or not user.UPassword == password:
        return None, True, "Invalid username or password"

    return {
        'id': user.id,
        'UserName': user.UserName,
        'AccessControl': json.dumps(user.AccessControl, sort_keys=False),
    }, None, None


def generate_random_password(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


def reset_password_service(data):
    user_name = data.get('UserName')

    if not user_name:
        return None, True, "Username is required"

    user = User.query.filter_by(UserName=user_name).first()
    if not user:
        return None, True, "User not found"

    new_password = generate_random_password()

    # Hash the new password
    # user.UPassword = generate_password_hash(new_password)
    # db.session.commit()

    user.UPassword = new_password
    db.session.commit()

    # email_query = text('''
    #     SELECT "tbl_master_EmployeeAddress"."Email"
    #     FROM "VisitorTrack"."tbl_master_EmployeeAddress"
    #     WHERE "EmployeeCode" = :employee_code
    # ''')
    # email_result = db.session.execute(
    #     email_query, {'employee_code': user.EmployeeCode}).fetchone()

    email_result = (
        db.session.query(EmployeeAddress.Email)
        .filter(EmployeeAddress.EmployeeCode == user.EmployeeCode)
        .first()
    )

    if email_result:
        email = email_result[0]
    else:
        return None, True, 'Email not found'

    msg = Message('Reset Password',
                  sender='prakash950288@gmail.com', recipients=[email])
    msg.body = f'Your new password is: {new_password}'

    try:
        mail.send(msg)
        return None, None,  'Password reset successfully. Please check your mail.'
    except Exception as e:
        return None, str(e), str(e)


def get_users_service():
    data = User.query.distinct(User.UserName).order_by(
        User.UserName.desc(), User.id.desc()).limit(200).all()

    data_dict = [newdata.as_dict() for newdata in data]

    if not data:
        return None, True, "No data found"

    return data_dict, None, 'data fetched successfully'


def update_user_permission_service(data):
    try:

        user_name = data.get("user_name")
        employee_code = data.get("employee_code")
        password = data.get("password")
        access_control = data.get("access_control")

        user = User.query.filter_by(UserName=user_name).first()

        if user:
            # if check_password_hash(user.password, password):
            if user.UPassword == password:
                user.AccessControl = access_control
                db.session.commit()

                return user, None, 'User permissions updated successfully'
            else:
                return None, 'ValidationError', 'Invalid password'
        else:
            new_user = User(
                UserName=user_name,
                EmployeeCode=employee_code,
                # UPassword=generate_password_hash(password),
                UPassword=password,
                AccessControl=access_control
            )
            db.session.add(new_user)
            db.session.commit()
            return new_user, None, 'User created successfully'
    except Exception as e:
        db.session.rollback()
        return None, str(e), 'Internal Server Error'
