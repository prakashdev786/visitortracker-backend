import os
from datetime import datetime, timezone
from app import create_app, db
from app.models import User, EmployeeAddress, EmployeeMain, MenuMaster
from sqlalchemy import text
import json

app = create_app(os.getenv("CONFIG_MODE"))


def seed_data():
    with app.app_context():
        # Create tables if they don't exist
        db.create_all()
        db.session.execute(
            text('TRUNCATE TABLE "tbl_master_Userperms" RESTART IDENTITY CASCADE'))
        db.session.execute(
            text('TRUNCATE TABLE "tbl_master_EmployeeAddress" RESTART IDENTITY CASCADE'))
        db.session.execute(
            text('TRUNCATE TABLE "tbl_master_EmployeeMain" RESTART IDENTITY CASCADE'))
        db.session.execute(
            text('TRUNCATE TABLE "tbl_MenuMaster" RESTART IDENTITY CASCADE'))
        db.session.commit()

        # Seed User data
        dumps_data = json.dumps({
            'access': {'dashboard': False, 'appointment': True, 'visitors': True, 'reports': True, 'employees': True, 'pass_designer': True, 'user_management': True},
            'manage': {'dashboard': False, 'appointment': False, 'visitors': True, 'reports': False, 'employees': False, 'pass_designer': False, 'user_management': True}
        })

        users = [
            User(
                UserName="admin",
                UPassword="admin",
                EmployeeCode="950288",
                AccessControl=dumps_data
            )
        ]

        # Add and commit User data
        db.session.bulk_save_objects(users)

        addresses = [
            EmployeeAddress(EmployeeCode="950288", AddressType="permanent",
                            Mobile="8838563796", Email="prakashzilch@gmail.com")
        ]

        db.session.bulk_save_objects(addresses)

        employees = [
            EmployeeMain(EmployeeCode="950288", AlternateCode="12345", ShortName="admin", DateofBirth="2000-04-09", DateofJoining="2020-01-10", Company="Zilch", Department="HR",
                         Designation="Manager", Category="Full-Time", EmailID="prakashzilch@gmail.com", ContactNo="1234567890")
        ]

        db.session.bulk_save_objects(employees)

        menu_data = [
            MenuMaster(
                nav_bar_name="Dashboard",
                isdrobdown="0",
                uri_link="dashboard",
                parent_id=None,
                icon_name="dashboard",
                status="1",
                order=2,
                created_at=datetime.now(timezone.utc),
                updated_at=datetime.now(timezone.utc)
            ),
            MenuMaster(
                nav_bar_name="Appointment",
                isdrobdown="0",
                uri_link="appointment",
                parent_id=None,
                icon_name="appointment",
                status="1",
                order=3,
                created_at=datetime.now(timezone.utc),
                updated_at=datetime.now(timezone.utc)
            ),

            MenuMaster(
                nav_bar_name="Visitors",
                isdrobdown="0",
                uri_link="visitors",
                parent_id=None,
                icon_name="visitors",
                status="1",
                order=4,
                created_at=datetime.now(timezone.utc),
                updated_at=datetime.now(timezone.utc)
            ),
            MenuMaster(
                nav_bar_name="Reports",
                isdrobdown="0",
                uri_link="reports",
                parent_id=None,
                icon_name="reports",
                status="1",
                order=5,
                created_at=datetime.now(timezone.utc),
                updated_at=datetime.now(timezone.utc)
            ),
            MenuMaster(
                nav_bar_name="Employees",
                isdrobdown="0",
                uri_link="employees",
                parent_id=None,
                icon_name="employees",
                status="1",
                order=6,
                created_at=datetime.now(timezone.utc),
                updated_at=datetime.now(timezone.utc)
            ),
            MenuMaster(
                nav_bar_name="Pass Designer",
                isdrobdown="0",
                uri_link="pass_designer",
                parent_id=None,
                icon_name="pass_designer",
                status="1",
                order=7,
                created_at=datetime.now(timezone.utc),
                updated_at=datetime.now(timezone.utc)
            ),
            MenuMaster(
                nav_bar_name="User Management",
                isdrobdown="0",
                uri_link="user_management",
                parent_id=None,
                icon_name="user_management",
                status="1",
                order=1,
                created_at=datetime.now(timezone.utc),
                updated_at=datetime.now(timezone.utc)
            ),
        ]

        db.session.bulk_save_objects(menu_data)

        # Commit all changes to the database
        db.session.commit()
        print("Data seeded successfully!")


if __name__ == '__main__':
    seed_data()
