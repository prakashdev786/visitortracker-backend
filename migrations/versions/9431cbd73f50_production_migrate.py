"""production migrate

Revision ID: 9431cbd73f50
Revises: 
Create Date: 2024-10-29 13:32:39.936893

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9431cbd73f50'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tbl_MenuMaster',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nav_bar_name', sa.String(length=255), nullable=True),
    sa.Column('isdrobdown', sa.String(length=5), nullable=True),
    sa.Column('uri_link', sa.String(length=255), nullable=True),
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.Column('icon_name', sa.String(length=255), nullable=True),
    sa.Column('status', sa.String(length=50), nullable=True),
    sa.Column('order', sa.Integer(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['parent_id'], ['tbl_MenuMaster.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tbl_master_EmployeeAddress',
    sa.Column('SNO', sa.Integer(), nullable=False),
    sa.Column('EmployeeCode', sa.String(length=20), nullable=True),
    sa.Column('AddressType', sa.String(length=20), nullable=True),
    sa.Column('Mobile', sa.String(length=20), nullable=True),
    sa.Column('Email', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('SNO')
    )
    op.create_table('tbl_master_EmployeeMain',
    sa.Column('SNO', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('EmployeeCode', sa.String(length=50), nullable=True),
    sa.Column('AlternateCode', sa.String(length=50), nullable=True),
    sa.Column('ShortName', sa.String(length=50), nullable=True),
    sa.Column('FirstName', sa.String(length=30), nullable=True),
    sa.Column('MiddleName', sa.String(length=30), nullable=True),
    sa.Column('LastName', sa.String(length=50), nullable=True),
    sa.Column('DateofBirth', sa.DateTime(), nullable=True),
    sa.Column('DateofJoining', sa.DateTime(), nullable=True),
    sa.Column('Company', sa.String(length=50), nullable=True),
    sa.Column('Department', sa.String(length=50), nullable=True),
    sa.Column('Designation', sa.String(length=50), nullable=True),
    sa.Column('Category', sa.String(length=50), nullable=True),
    sa.Column('EmailID', sa.String(length=50), nullable=True),
    sa.Column('ContactNo', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('SNO')
    )
    op.create_table('tbl_master_ReportDesign',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('Menu', sa.String(length=100), nullable=True),
    sa.Column('Description', sa.String(length=100), nullable=True),
    sa.Column('UserId', sa.String(length=50), nullable=True),
    sa.Column('Config', sa.Text(), nullable=True),
    sa.Column('Value', sa.Text(), nullable=True),
    sa.Column('ValueTwo', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tbl_master_Settings',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('Menu', sa.String(length=100), nullable=True),
    sa.Column('Description', sa.String(length=100), nullable=True),
    sa.Column('UserId', sa.String(length=50), nullable=True),
    sa.Column('Orientation', sa.String(length=50), nullable=True),
    sa.Column('PageSize', sa.String(length=50), nullable=True),
    sa.Column('Config', sa.Text(), nullable=True),
    sa.Column('Value', sa.Text(), nullable=True),
    sa.Column('ValueTwo', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tbl_master_Userperms',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('UserName', sa.String(length=50), nullable=True),
    sa.Column('UPassword', sa.String(length=10), nullable=True),
    sa.Column('EmployeeCode', sa.String(length=50), nullable=True),
    sa.Column('AccessControl', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vis_tbl_Appointments',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('AppNumber', sa.String(length=50), nullable=True),
    sa.Column('AppDate', sa.String(length=50), nullable=True),
    sa.Column('AppTime', sa.String(length=50), nullable=True),
    sa.Column('CompanyName', sa.String(length=100), nullable=True),
    sa.Column('VisitorName', sa.String(length=100), nullable=True),
    sa.Column('VisitorCategory', sa.String(length=50), nullable=True),
    sa.Column('AddressLine1', sa.String(length=200), nullable=True),
    sa.Column('AddressLine2', sa.String(length=200), nullable=True),
    sa.Column('City', sa.String(length=100), nullable=True),
    sa.Column('State', sa.String(length=100), nullable=True),
    sa.Column('PinCode', sa.String(length=20), nullable=True),
    sa.Column('TelePhone', sa.String(length=20), nullable=True),
    sa.Column('MobileNumber', sa.String(length=20), nullable=True),
    sa.Column('EmailId', sa.String(length=100), nullable=True),
    sa.Column('Purpose', sa.String(length=500), nullable=True),
    sa.Column('VisitorId', sa.String(length=50), nullable=True),
    sa.Column('CompanyId', sa.String(length=50), nullable=True),
    sa.Column('CreatedAt', sa.DateTime(), nullable=True),
    sa.Column('UpdatedAt', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vis_tbl_master_Company',
    sa.Column('SNO', sa.Integer(), nullable=False),
    sa.Column('Company', sa.String(length=100), nullable=True),
    sa.Column('AddressLine1', sa.String(length=100), nullable=True),
    sa.Column('AddressLine2', sa.String(length=100), nullable=True),
    sa.Column('Area', sa.String(length=50), nullable=True),
    sa.Column('City', sa.String(length=50), nullable=True),
    sa.Column('State', sa.String(length=50), nullable=True),
    sa.Column('Country', sa.String(length=50), nullable=True),
    sa.Column('PinCode', sa.String(length=50), nullable=True),
    sa.Column('Contact1', sa.String(length=50), nullable=True),
    sa.Column('Contact2', sa.String(length=50), nullable=True),
    sa.Column('Phone', sa.String(length=50), nullable=True),
    sa.Column('Fax', sa.String(length=50), nullable=True),
    sa.Column('Mobile', sa.String(length=50), nullable=True),
    sa.Column('Email', sa.String(length=50), nullable=True),
    sa.Column('WebSite', sa.String(length=250), nullable=True),
    sa.Column('TypeOfService', sa.String(length=50), nullable=True),
    sa.Column('TypeOfIndustry', sa.String(length=50), nullable=True),
    sa.Column('Active', sa.String(length=50), nullable=True),
    sa.Column('InActiveDate', sa.DateTime(timezone=True), nullable=True),
    sa.Column('VisitorType', sa.String(length=50), nullable=True),
    sa.Column('ContractEndDate', sa.DateTime(timezone=True), nullable=True),
    sa.Column('createdAt', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updatedAt', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('SNO')
    )
    op.create_table('vis_tbl_master_Visitors',
    sa.Column('SNO', sa.Integer(), nullable=False),
    sa.Column('VisitorName', sa.String(length=100), nullable=True),
    sa.Column('Company', sa.String(length=100), nullable=True),
    sa.Column('VisitorCategory', sa.String(length=100), nullable=True),
    sa.Column('MobileNumber', sa.String(length=100), nullable=True),
    sa.Column('EmailID', sa.String(length=100), nullable=True),
    sa.Column('FirstVisitDate', sa.String(length=100), nullable=True),
    sa.Column('LastVisitDate', sa.String(length=100), nullable=True),
    sa.Column('IDCardType', sa.String(length=100), nullable=True),
    sa.Column('IDCardNumber', sa.String(length=100), nullable=True),
    sa.Column('createdAt', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updatedAt', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('SNO')
    )
    op.create_table('vis_tbl_trans_VistorLog24',
    sa.Column('SNO', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('IDCardImageName', sa.String(length=100), nullable=True),
    sa.Column('VisitorID', sa.String(length=50), nullable=True),
    sa.Column('CompanyID', sa.String(length=50), nullable=True),
    sa.Column('PassNumber', sa.String(length=50), nullable=True),
    sa.Column('PassDate', sa.DateTime(), nullable=True),
    sa.Column('BadgeNumber', sa.String(length=50), nullable=True),
    sa.Column('Company', sa.String(length=100), nullable=True),
    sa.Column('VisitorName', sa.String(length=100), nullable=True),
    sa.Column('VisCategory', sa.String(length=100), nullable=True),
    sa.Column('MobileNumber', sa.String(length=100), nullable=True),
    sa.Column('VisTotal', sa.String(length=100), nullable=True),
    sa.Column('VisPurpose', sa.String(length=100), nullable=True),
    sa.Column('VehicleNumber', sa.String(length=100), nullable=True),
    sa.Column('VisAdditional', sa.String(length=100), nullable=True),
    sa.Column('ReturnableItems', sa.Text(), nullable=True),
    sa.Column('VehicleNo', sa.String(length=100), nullable=True),
    sa.Column('EmployeeCode', sa.String(length=100), nullable=True),
    sa.Column('Department', sa.String(length=100), nullable=True),
    sa.Column('InTime', sa.DateTime(), nullable=True),
    sa.Column('OutTime', sa.DateTime(), nullable=True),
    sa.Column('ImageName', sa.String(length=100), nullable=True),
    sa.Column('AppointmentNumber', sa.String(length=100), nullable=True),
    sa.Column('VehcileType', sa.String(length=50), nullable=True),
    sa.Column('VehicleCompany', sa.String(length=50), nullable=True),
    sa.Column('DriverName', sa.String(length=50), nullable=True),
    sa.Column('CabInTime', sa.String(length=50), nullable=True),
    sa.Column('CabOutTime', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('SNO')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vis_tbl_trans_VistorLog24')
    op.drop_table('vis_tbl_master_Visitors')
    op.drop_table('vis_tbl_master_Company')
    op.drop_table('vis_tbl_Appointments')
    op.drop_table('tbl_master_Userperms')
    op.drop_table('tbl_master_Settings')
    op.drop_table('tbl_master_ReportDesign')
    op.drop_table('tbl_master_EmployeeMain')
    op.drop_table('tbl_master_EmployeeAddress')
    op.drop_table('tbl_MenuMaster')
    # ### end Alembic commands ###