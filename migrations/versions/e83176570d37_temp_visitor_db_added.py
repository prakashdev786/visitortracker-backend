"""temp visitor db added

Revision ID: e83176570d37
Revises: 
Create Date: 2024-10-30 13:56:57.095116

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'e83176570d37'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # op.create_table('tbl_MenuMaster',
    # sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    # sa.Column('nav_bar_name', sa.String(length=255), nullable=True),
    # sa.Column('isdrobdown', sa.String(length=5), nullable=True),
    # sa.Column('uri_link', sa.String(length=255), nullable=True),
    # sa.Column('parent_id', sa.Integer(), nullable=True),
    # sa.Column('icon_name', sa.String(length=255), nullable=True),
    # sa.Column('status', sa.String(length=50), nullable=True),
    # sa.Column('order', sa.Integer(), nullable=True),
    # sa.Column('deleted_at', sa.DateTime(), nullable=True),
    # sa.Column('created_at', sa.DateTime(), nullable=True),
    # sa.Column('updated_at', sa.DateTime(), nullable=True),
    # sa.ForeignKeyConstraint(['parent_id'], ['VisitorTrack.tbl_MenuMaster.id'], ),
    # sa.PrimaryKeyConstraint('id'),
    # schema='VisitorTrack'
    # )
    # op.create_table('tbl_master_EmployeeAddress',
    # sa.Column('SNO', sa.Integer(), nullable=False),
    # sa.Column('EmployeeCode', sa.String(length=20), nullable=True),
    # sa.Column('AddressType', sa.String(length=20), nullable=True),
    # sa.Column('Mobile', sa.String(length=20), nullable=True),
    # sa.Column('Email', sa.String(length=50), nullable=True),
    # sa.PrimaryKeyConstraint('SNO'),
    # schema='VisitorTrack'
    # )
    # op.create_table('tbl_master_EmployeeMain',
    # sa.Column('SNO', sa.Integer(), autoincrement=True, nullable=False),
    # sa.Column('EmployeeCode', sa.String(length=50), nullable=True),
    # sa.Column('AlternateCode', sa.String(length=50), nullable=True),
    # sa.Column('ShortName', sa.String(length=50), nullable=True),
    # sa.Column('FirstName', sa.String(length=30), nullable=True),
    # sa.Column('MiddleName', sa.String(length=30), nullable=True),
    # sa.Column('LastName', sa.String(length=50), nullable=True),
    # sa.Column('DateofBirth', sa.DateTime(), nullable=True),
    # sa.Column('DateofJoining', sa.DateTime(), nullable=True),
    # sa.Column('Company', sa.String(length=50), nullable=True),
    # sa.Column('Department', sa.String(length=50), nullable=True),
    # sa.Column('Designation', sa.String(length=50), nullable=True),
    # sa.Column('Category', sa.String(length=50), nullable=True),
    # sa.Column('EmailID', sa.String(length=50), nullable=True),
    # sa.Column('ContactNo', sa.String(length=20), nullable=True),
    # sa.PrimaryKeyConstraint('SNO'),
    # schema='VisitorTrack'
    # )
    # op.create_table('tbl_master_ReportDesign',
    # sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    # sa.Column('Menu', sa.String(length=100), nullable=True),
    # sa.Column('Description', sa.String(length=100), nullable=True),
    # sa.Column('UserId', sa.String(length=50), nullable=True),
    # sa.Column('Config', sa.Text(), nullable=True),
    # sa.Column('Value', sa.Text(), nullable=True),
    # sa.Column('ValueTwo', sa.Text(), nullable=True),
    # sa.PrimaryKeyConstraint('id'),
    # schema='VisitorTrack'
    # )
    # op.create_table('tbl_master_Settings',
    # sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    # sa.Column('Menu', sa.String(length=100), nullable=True),
    # sa.Column('Description', sa.String(length=100), nullable=True),
    # sa.Column('UserId', sa.String(length=50), nullable=True),
    # sa.Column('Orientation', sa.String(length=50), nullable=True),
    # sa.Column('PageSize', sa.String(length=50), nullable=True),
    # sa.Column('Config', sa.Text(), nullable=True),
    # sa.Column('Value', sa.Text(), nullable=True),
    # sa.Column('ValueTwo', sa.Text(), nullable=True),
    # sa.PrimaryKeyConstraint('id'),
    # schema='VisitorTrack'
    # )
    # op.create_table('tbl_master_Userperms',
    # sa.Column('id', sa.Integer(), nullable=False),
    # sa.Column('UserName', sa.String(length=50), nullable=True),
    # sa.Column('UPassword', sa.String(length=10), nullable=True),
    # sa.Column('EmployeeCode', sa.String(length=50), nullable=True),
    # sa.Column('AccessControl', sa.Text(), nullable=True),
    # sa.PrimaryKeyConstraint('id'),
    # schema='VisitorTrack'
    # )
    # op.create_table('vis_tbl_Appointments',
    # sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    # sa.Column('AppNumber', sa.String(length=50), nullable=True),
    # sa.Column('AppDate', sa.String(length=50), nullable=True),
    # sa.Column('AppTime', sa.String(length=50), nullable=True),
    # sa.Column('CompanyName', sa.String(length=100), nullable=True),
    # sa.Column('VisitorName', sa.String(length=100), nullable=True),
    # sa.Column('VisitorCategory', sa.String(length=50), nullable=True),
    # sa.Column('AddressLine1', sa.String(length=200), nullable=True),
    # sa.Column('AddressLine2', sa.String(length=200), nullable=True),
    # sa.Column('City', sa.String(length=100), nullable=True),
    # sa.Column('State', sa.String(length=100), nullable=True),
    # sa.Column('PinCode', sa.String(length=20), nullable=True),
    # sa.Column('TelePhone', sa.String(length=20), nullable=True),
    # sa.Column('MobileNumber', sa.String(length=20), nullable=True),
    # sa.Column('EmailId', sa.String(length=100), nullable=True),
    # sa.Column('Purpose', sa.String(length=500), nullable=True),
    # sa.Column('TempVisitorId', sa.String(length=50), nullable=True),
    # sa.Column('CreatedAt', sa.DateTime(), nullable=True),
    # sa.Column('UpdatedAt', sa.DateTime(), nullable=True),
    # sa.PrimaryKeyConstraint('id'),
    # schema='VisitorTrack'
    # )
    op.create_table('vis_tbl_Temp_Visitors',
    sa.Column('SNO', sa.Integer(), nullable=False),
    sa.Column('AppNumber', sa.String(length=50), nullable=True),
    sa.Column('VisitorName', sa.String(length=100), nullable=True),
    sa.Column('VisitorCategory', sa.String(length=100), nullable=True),
    sa.Column('EmailID', sa.String(length=100), nullable=True),
    sa.Column('MobileNumber', sa.String(length=100), nullable=True),
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
    sa.Column('VisitorImage', sa.String(length=100), nullable=True),
    sa.Column('createdAt', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updatedAt', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('SNO'),
    schema='VisitorTrack'
    )
    # op.create_table('vis_tbl_master_Company',
    # sa.Column('SNO', sa.Integer(), nullable=False),
    # sa.Column('Company', sa.String(length=100), nullable=True),
    # sa.Column('AddressLine1', sa.String(length=100), nullable=True),
    # sa.Column('AddressLine2', sa.String(length=100), nullable=True),
    # sa.Column('Area', sa.String(length=50), nullable=True),
    # sa.Column('City', sa.String(length=50), nullable=True),
    # sa.Column('State', sa.String(length=50), nullable=True),
    # sa.Column('Country', sa.String(length=50), nullable=True),
    # sa.Column('PinCode', sa.String(length=50), nullable=True),
    # sa.Column('Contact1', sa.String(length=50), nullable=True),
    # sa.Column('Contact2', sa.String(length=50), nullable=True),
    # sa.Column('Phone', sa.String(length=50), nullable=True),
    # sa.Column('Fax', sa.String(length=50), nullable=True),
    # sa.Column('Mobile', sa.String(length=50), nullable=True),
    # sa.Column('Email', sa.String(length=50), nullable=True),
    # sa.Column('WebSite', sa.String(length=250), nullable=True),
    # sa.Column('TypeOfService', sa.String(length=50), nullable=True),
    # sa.Column('TypeOfIndustry', sa.String(length=50), nullable=True),
    # sa.Column('Active', sa.String(length=50), nullable=True),
    # sa.Column('InActiveDate', sa.DateTime(timezone=True), nullable=True),
    # sa.Column('VisitorType', sa.String(length=50), nullable=True),
    # sa.Column('ContractEndDate', sa.DateTime(timezone=True), nullable=True),
    # sa.Column('createdAt', sa.DateTime(timezone=True), nullable=True),
    # sa.Column('updatedAt', sa.DateTime(timezone=True), nullable=True),
    # sa.PrimaryKeyConstraint('SNO'),
    # schema='VisitorTrack'
    # )
    # op.create_table('vis_tbl_master_Visitors',
    # sa.Column('SNO', sa.Integer(), nullable=False),
    # sa.Column('VisitorName', sa.String(length=100), nullable=True),
    # sa.Column('Company', sa.String(length=100), nullable=True),
    # sa.Column('VisitorCategory', sa.String(length=100), nullable=True),
    # sa.Column('MobileNumber', sa.String(length=100), nullable=True),
    # sa.Column('EmailID', sa.String(length=100), nullable=True),
    # sa.Column('FirstVisitDate', sa.String(length=100), nullable=True),
    # sa.Column('LastVisitDate', sa.String(length=100), nullable=True),
    # sa.Column('IDCardType', sa.String(length=100), nullable=True),
    # sa.Column('IDCardNumber', sa.String(length=100), nullable=True),
    # sa.Column('createdAt', sa.DateTime(timezone=True), nullable=True),
    # sa.Column('updatedAt', sa.DateTime(timezone=True), nullable=True),
    # sa.PrimaryKeyConstraint('SNO'),
    # schema='VisitorTrack'
    # )
    # op.create_table('vis_tbl_trans_VistorLog24',
    # sa.Column('SNO', sa.Integer(), autoincrement=True, nullable=False),
    # sa.Column('IDCardImageName', sa.String(length=100), nullable=True),
    # sa.Column('VisitorID', sa.String(length=50), nullable=True),
    # sa.Column('CompanyID', sa.String(length=50), nullable=True),
    # sa.Column('PassNumber', sa.String(length=50), nullable=True),
    # sa.Column('PassDate', sa.DateTime(), nullable=True),
    # sa.Column('BadgeNumber', sa.String(length=50), nullable=True),
    # sa.Column('Company', sa.String(length=100), nullable=True),
    # sa.Column('VisitorName', sa.String(length=100), nullable=True),
    # sa.Column('VisCategory', sa.String(length=100), nullable=True),
    # sa.Column('MobileNumber', sa.String(length=100), nullable=True),
    # sa.Column('VisTotal', sa.String(length=100), nullable=True),
    # sa.Column('VisPurpose', sa.String(length=100), nullable=True),
    # sa.Column('VehicleNumber', sa.String(length=100), nullable=True),
    # sa.Column('VisAdditional', sa.String(length=100), nullable=True),
    # sa.Column('ReturnableItems', sa.Text(), nullable=True),
    # sa.Column('VehicleNo', sa.String(length=100), nullable=True),
    # sa.Column('EmployeeCode', sa.String(length=100), nullable=True),
    # sa.Column('Department', sa.String(length=100), nullable=True),
    # sa.Column('InTime', sa.DateTime(), nullable=True),
    # sa.Column('OutTime', sa.DateTime(), nullable=True),
    # sa.Column('ImageName', sa.String(length=100), nullable=True),
    # sa.Column('AppointmentNumber', sa.String(length=100), nullable=True),
    # sa.Column('VehcileType', sa.String(length=50), nullable=True),
    # sa.Column('VehicleCompany', sa.String(length=50), nullable=True),
    # sa.Column('DriverName', sa.String(length=50), nullable=True),
    # sa.Column('CabInTime', sa.String(length=50), nullable=True),
    # sa.Column('CabOutTime', sa.String(length=50), nullable=True),
    # sa.PrimaryKeyConstraint('SNO'),
    # schema='VisitorTrack'
    # )
    # op.drop_table('vis_tbl_Appointments')
    # op.drop_table('tbl_master_Userperms')
    # op.drop_table('tbl_master_EmployeeAddress')
    # op.drop_table('tbl_master_Settings')
    # op.drop_table('vis_tbl_master_Visitors')
    # op.drop_table('tbl_MenuMaster')
    # op.drop_table('tbl_master_ReportDesign')
    # op.drop_table('vis_tbl_master_Company')
    # with op.batch_alter_table('tbl_master_EmployeeMain', schema=None) as batch_op:
    #     batch_op.drop_index('idxtbl_master_EmployeeMain_SNO')

    # op.drop_table('tbl_master_EmployeeMain')
    # op.drop_table('vis_tbl_trans_VistorLog24')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vis_tbl_trans_VistorLog24',
    sa.Column('SNO', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('PassNumber', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('PassDate', postgresql.TIMESTAMP(precision=6), autoincrement=False, nullable=True),
    sa.Column('BadgeNumber', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('Company', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('VisitorName', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('VisCategory', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('MobileNumber', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('VisTotal', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('VisPurpose', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('VehicleNumber', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('VisAdditional', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('ReturnableItems', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('VehicleNo', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('EmployeeCode', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('Department', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('InTime', postgresql.TIMESTAMP(precision=6), autoincrement=False, nullable=True),
    sa.Column('OutTime', postgresql.TIMESTAMP(precision=6), autoincrement=False, nullable=True),
    sa.Column('ImageName', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('AppointmentNumber', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('VehcileType', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('VehicleCompany', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('DriverName', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('CabInTime', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('CabOutTime', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('IDCardImageName', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('VisitorID', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('CompanyID', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('SNO', name='vis_tbl_trans_VistorLog24_pkey')
    )
    op.create_table('tbl_master_EmployeeMain',
    sa.Column('EmployeeCode', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('AlternateCode', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('ShortName', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('FirstName', sa.VARCHAR(length=30), autoincrement=False, nullable=True),
    sa.Column('MiddleName', sa.VARCHAR(length=30), autoincrement=False, nullable=True),
    sa.Column('LastName', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('DateofBirth', postgresql.TIMESTAMP(precision=6), autoincrement=False, nullable=True),
    sa.Column('DateofJoining', postgresql.TIMESTAMP(precision=6), autoincrement=False, nullable=True),
    sa.Column('DateofProbation', postgresql.TIMESTAMP(precision=6), autoincrement=False, nullable=True),
    sa.Column('DateofConfirmation', postgresql.TIMESTAMP(precision=6), autoincrement=False, nullable=True),
    sa.Column('DateofLeaving', postgresql.TIMESTAMP(precision=6), autoincrement=False, nullable=True),
    sa.Column('DateofLastReJoining', postgresql.TIMESTAMP(precision=6), autoincrement=False, nullable=True),
    sa.Column('DateofLastBreak', postgresql.TIMESTAMP(precision=6), autoincrement=False, nullable=True),
    sa.Column('FathersName', sa.VARCHAR(length=30), autoincrement=False, nullable=True),
    sa.Column('Sex', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
    sa.Column('Company', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('SubDepartment', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('Department', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('Designation', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('SuperDepartment', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('Status', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('Grade', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('Location', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('Division', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('Category', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('LeaveReportingTo', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('ShiftPattern', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('ShiftDate', postgresql.TIMESTAMP(precision=6), autoincrement=False, nullable=True),
    sa.Column('LeaveControl', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('LeaveCondition', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('HolidayPattern', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('ShiftsAllowed', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('PunchStatus', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('User_Create', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
    sa.Column('User_Creation_Dt', postgresql.TIMESTAMP(precision=6), autoincrement=False, nullable=True),
    sa.Column('User_Mod', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('User_Mod_Dt', postgresql.TIMESTAMP(precision=6), autoincrement=False, nullable=True),
    sa.Column('Workstation_Id', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('Status_Flag', sa.VARCHAR(length=1), autoincrement=False, nullable=True),
    sa.Column('CoffPattern', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('WorkSpan', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
    sa.Column('FirstLastPunch', sa.VARCHAR(length=15), autoincrement=False, nullable=True),
    sa.Column('OverTime', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('RFIDCode', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
    sa.Column('ReaderGroup', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('LeaveAutoGrant', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('LeaveSecondApproval', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('FirstPunch', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('BranchState', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('FixedOffDay', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
    sa.Column('LateOTAdjust', sa.VARCHAR(length=25), autoincrement=False, nullable=True),
    sa.Column('DateofConfirmationDue', postgresql.TIMESTAMP(precision=6), autoincrement=False, nullable=True),
    sa.Column('BandLevel', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('SubLevel', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('BloodGroup', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('Module', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('Band', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('UnionName', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('EmergencyNo', sa.VARCHAR(length=30), autoincrement=False, nullable=True),
    sa.Column('Type', sa.VARCHAR(length=30), autoincrement=False, nullable=True),
    sa.Column('SubType1', sa.VARCHAR(length=30), autoincrement=False, nullable=True),
    sa.Column('SubType2', sa.VARCHAR(length=30), autoincrement=False, nullable=True),
    sa.Column('Plant', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('CostCenter', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('Spouse', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('EmailID', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('Supervisor', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('Approver', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('ServiceWeightage', sa.VARCHAR(length=1), autoincrement=False, nullable=True),
    sa.Column('SuperAnnuation', sa.VARCHAR(length=1), autoincrement=False, nullable=True),
    sa.Column('VariablePay', sa.VARCHAR(length=1), autoincrement=False, nullable=True),
    sa.Column('ServiceAgreeStaus', sa.VARCHAR(length=500), autoincrement=False, nullable=True),
    sa.Column('DiscipilinaryActions', sa.VARCHAR(length=500), autoincrement=False, nullable=True),
    sa.Column('SuperAnnuationPer', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('OldEmpCode', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('Tittle', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('Married', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('Position', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('JoinDesig', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('TrainingPeriod', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('GroupJoinDate', postgresql.TIMESTAMP(precision=6), autoincrement=False, nullable=True),
    sa.Column('NeemCode', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('ContactNo', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('DateOfSuperAnnuation', postgresql.TIMESTAMP(precision=6), autoincrement=False, nullable=True),
    sa.Column('MobilePunchAllowed', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('SelfieMandatory', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('SNO', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('SNO', name='tbl_master_EmployeeMain_pkey')
    )
    with op.batch_alter_table('tbl_master_EmployeeMain', schema=None) as batch_op:
        batch_op.create_index('idxtbl_master_EmployeeMain_SNO', ['SNO'], unique=False)

    op.create_table('vis_tbl_master_Company',
    sa.Column('SNO', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('Company', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('AddressLine1', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('AddressLine2', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('Area', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('City', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('State', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('Country', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('PinCode', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('Contact1', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('Contact2', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('Phone', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('Fax', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('Mobile', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('Email', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('WebSite', sa.VARCHAR(length=250), autoincrement=False, nullable=True),
    sa.Column('TypeOfService', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('TypeOfIndustry', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('Active', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('InActiveDate', postgresql.TIMESTAMP(timezone=True, precision=6), autoincrement=False, nullable=True),
    sa.Column('VisitorType', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('ContractEndDate', postgresql.TIMESTAMP(timezone=True, precision=6), autoincrement=False, nullable=True),
    sa.Column('createdAt', postgresql.TIMESTAMP(timezone=True, precision=6), autoincrement=False, nullable=True),
    sa.Column('updatedAt', postgresql.TIMESTAMP(timezone=True, precision=6), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('SNO', name='vis_tbl_master_Company_pkey')
    )
    op.create_table('tbl_master_ReportDesign',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('Menu', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('Description', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('UserId', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('Config', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('Value', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('ValueTwo', sa.TEXT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='tbl_master_ReportDesign_pkey')
    )
    op.create_table('tbl_MenuMaster',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('nav_bar_name', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('isdrobdown', sa.VARCHAR(length=5), autoincrement=False, nullable=True),
    sa.Column('uri_link', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('parent_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('icon_name', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('status', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('order', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('deleted_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['parent_id'], ['tbl_MenuMaster.id'], name='tbl_MenuMaster_parent_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='tbl_MenuMaster_pkey')
    )
    op.create_table('vis_tbl_master_Visitors',
    sa.Column('SNO', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('VisitorName', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('Company', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('VisitorCategory', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('MobileNumber', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('EmailID', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('FirstVisitDate', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('LastVisitDate', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('IDCardType', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('IDCardNumber', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('createdAt', postgresql.TIMESTAMP(timezone=True, precision=6), autoincrement=False, nullable=True),
    sa.Column('updatedAt', postgresql.TIMESTAMP(timezone=True, precision=6), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('SNO', name='vis_tbl_master_Visitors_pkey')
    )
    op.create_table('tbl_master_Settings',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('Menu', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('Description', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('UserId', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('Orientation', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('PageSize', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('Config', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('Value', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('ValueTwo', sa.TEXT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='tbl_master_Settings_pkey')
    )
    op.create_table('tbl_master_EmployeeAddress',
    sa.Column('SNO', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('EmployeeCode', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('AddressType', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('AddressName', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('AddressLine1', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('AddressLine2', sa.VARCHAR(length=40), autoincrement=False, nullable=True),
    sa.Column('AddressLine3', sa.VARCHAR(length=40), autoincrement=False, nullable=True),
    sa.Column('City', sa.VARCHAR(length=30), autoincrement=False, nullable=True),
    sa.Column('State', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('PinCode', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
    sa.Column('Telephone', sa.VARCHAR(length=25), autoincrement=False, nullable=True),
    sa.Column('Fax', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('Mobile', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('Email', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('User_Create', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
    sa.Column('User_Creation_Dt', postgresql.TIMESTAMP(precision=6), autoincrement=False, nullable=True),
    sa.Column('User_Mod', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
    sa.Column('User_Mod_Dt', postgresql.TIMESTAMP(precision=6), autoincrement=False, nullable=True),
    sa.Column('Workstation_Id', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('Status_Flag', sa.VARCHAR(length=1), autoincrement=False, nullable=True),
    sa.Column('District', sa.VARCHAR(length=75), autoincrement=False, nullable=True),
    sa.Column('EmergencyNo', sa.VARCHAR(length=75), autoincrement=False, nullable=True)
    )
    op.create_table('tbl_master_Userperms',
    sa.Column('UserName', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('UPassword', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
    sa.Column('Site', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('MenuName', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('Parent', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('Class', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('ResourceId', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('Department', sa.VARCHAR(length=250), autoincrement=False, nullable=True),
    sa.Column('Designation', sa.VARCHAR(length=250), autoincrement=False, nullable=True),
    sa.Column('Grade', sa.VARCHAR(length=250), autoincrement=False, nullable=True),
    sa.Column('Category', sa.VARCHAR(length=1700), autoincrement=False, nullable=True),
    sa.Column('EmployeeCode', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
    sa.Column('Company', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('Location', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('Status', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('DeviceId', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('FCMToken', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('DeviceType', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('IsResetPassword', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('ForgotPasswordLinkDate', postgresql.TIMESTAMP(precision=6), autoincrement=False, nullable=True),
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id', name='tbl_master_Userperms_pkey')
    )
    op.create_table('vis_tbl_Appointments',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('AppNumber', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('AppDate', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('AppTime', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('CompanyName', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('VisitorName', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('VisitorCategory', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('AddressLine1', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('AddressLine2', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('City', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('State', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('PinCode', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('TelePhone', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('MobileNumber', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('EmailId', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('Purpose', sa.VARCHAR(length=500), autoincrement=False, nullable=True),
    sa.Column('VisitorId', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('CompanyId', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('CreatedAt', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('UpdatedAt', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='vis_tbl_Appointments_pkey')
    )
    op.drop_table('vis_tbl_trans_VistorLog24', schema='VisitorTrack')
    op.drop_table('vis_tbl_master_Visitors', schema='VisitorTrack')
    op.drop_table('vis_tbl_master_Company', schema='VisitorTrack')
    op.drop_table('vis_tbl_Temp_Visitors', schema='VisitorTrack')
    op.drop_table('vis_tbl_Appointments', schema='VisitorTrack')
    op.drop_table('tbl_master_Userperms', schema='VisitorTrack')
    op.drop_table('tbl_master_Settings', schema='VisitorTrack')
    op.drop_table('tbl_master_ReportDesign', schema='VisitorTrack')
    op.drop_table('tbl_master_EmployeeMain', schema='VisitorTrack')
    op.drop_table('tbl_master_EmployeeAddress', schema='VisitorTrack')
    op.drop_table('tbl_MenuMaster', schema='VisitorTrack')
    # ### end Alembic commands ###