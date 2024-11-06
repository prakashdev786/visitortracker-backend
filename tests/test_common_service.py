import unittest
from unittest.mock import patch, MagicMock
from app.services.common_service import (
    get_settings_by_userid_service, create_employee_by_csv_service,
    create_settings_service, preview_report_template_service
)

from app.models.user import User
from io import BytesIO
from app import create_app, db


class CommonServiceTestCase(unittest.TestCase):
    def setUp(self):
        """Set up the test client and app context."""
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.ctx = self.app.app_context()
        self.ctx.push()
        db.create_all()
    
    def tearDown(self):
        """Tear down the test client and app context."""
        self.app_context.pop()

    @patch('app.models.settings_master.SettingsMaster.query.filter_by')
    def test_get_settings_by_userid_service_success(self, mock_query):
        """Test get_settings_by_userid_service for successful case."""
        # Mock the return value of the query
        user = User.query.filter_by(UserName='prakash').first()

        mock_setting = MagicMock(
            as_dict=lambda: {'UserId': user.id, 'Config': 'sample config'})
        mock_query.return_value.all.return_value = [mock_setting]

        data, error, message = get_settings_by_userid_service(str(user.id))

        self.assertFalse(error)
        self.assertEqual(data[0]['UserId'], f'{user.id}')

    def test_create_employee_by_csv_service_missing_file(self):
        """Test create_employee_by_csv_service with missing file."""
        data = {'import_file': None}
        result, error, message = create_employee_by_csv_service(data)
        self.assertIsNotNone(error)
        self.assertEqual(message, "No file provided")

    @patch('pandas.read_csv')
    @patch('app.models.employee_main.EmployeeMain.query.filter_by')
    @patch('app.models.employee_address.EmployeeAddress.query.filter_by')
    def test_create_employee_by_csv_service_success(self, mock_emp_query, mock_addr_query, mock_read_csv):
        """Test create_employee_by_csv_service for success."""
        # Create a mock DataFrame
        mock_df = MagicMock()
        mock_df.columns = ['EmployeeCode', 'FullName',
                           'Designation', 'Department', 'ContactNo']
        mock_df.iterrows.return_value = iter([
            (0, {'EmployeeCode': '112', 'FullName': 'prakash', 'Designation': 'dev',
             'Department': 'development', 'ContactNo': '8838563796'})
        ])
        mock_read_csv.return_value = mock_df

        mock_emp_query.return_value.first.return_value = None
        mock_addr_query.return_value.first.return_value = None

        mock_file = MagicMock()
        mock_file.read.return_value = b'EmployeeCode,FullName,Designation,Department,ContactNo\n112,prakash,dev,development,8838563796'
        mock_file.filename = 'test.csv'  # Setting the filename for validation

        data = {'import_file': mock_file}
        result, error, message = create_employee_by_csv_service(data)
        print(error, message, 'error')
        self.assertIsNone(error)
        self.assertEqual(message, 'Employees updated successfully')

    @patch('app.services.common_service.render_template_string')
    @patch('app.services.common_service.pisa.CreatePDF')
    def test_preview_report_template_service_success(self, mock_create_pdf, mock_render_template_string):
        """Test preview_report_template_service success case."""
        mock_render_template_string.return_value = "<h1>Sample Report</h1>"
        mock_create_pdf.return_value.err = False

        data = {
            'Menu': 'Testing',
            'UserId': '10001',
            'Value': '<h1>{{title}}</h1>'
        }

        response, error, message = preview_report_template_service(data)

        print(response, error, message, 'response, error, message')
        self.assertIsNone(error)
        self.assertEqual(message, 'success')
        self.assertEqual(response['mimetype'], 'application/pdf')


if __name__ == '__main__':
    unittest.main()
