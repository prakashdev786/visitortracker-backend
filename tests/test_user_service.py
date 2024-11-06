import unittest
from unittest.mock import patch
from app import create_app
from app.services.user_service import login_user_service, reset_password_service

class UserServiceTestCase(unittest.TestCase):
    def setUp(self):
        """Set up the test client and application context."""
        self.app = create_app('testing') 
        self.app_context = self.app.app_context()
        self.app_context.push() 

    def tearDown(self):
        """Tear down the test client and application context."""
        self.app_context.pop()  

    @patch('app.models.user.User.query')
    def test_login_user_service_success(self, mock_query):
        """Test successful login user service."""
        # Set up mock return value
        mock_user = type('User', (object,), {'id': 1, 'UserName': 'test_user', 'UPassword': 'test_pass'})
        mock_query.filter_by.return_value.first.return_value = mock_user
        
        data = {'UserName': 'test_user', 'UPassword': 'test_pass'}
        result, error, message = login_user_service(data)
        
        self.assertIsNotNone(result)
        self.assertEqual(result['UserName'], 'test_user')
        self.assertIsNone(error)
        self.assertIsNone(message)

    @patch('app.models.user.User.query')
    def test_login_user_service_failure(self, mock_query):
        """Test login user service failure due to invalid credentials."""
        mock_query.filter_by.return_value.first.return_value = None
        
        data = {'UserName': 'wrong_user', 'UPassword': 'wrong_pass'}
        result, error, message = login_user_service(data)
        
        self.assertIsNone(result)
        self.assertTrue(error)
        self.assertEqual(message, "Invalid username or password")

    @patch('app.models.user.User.query')
    def test_reset_password_service_success(self, mock_query):
        """Test successful reset password service."""
        mock_user = type('User', (object,), {'EmployeeCode': '950288', 'UPassword': 'seb0fvvg'})
        mock_query.filter_by.return_value.first.return_value = mock_user

        # Mock email sending
        with patch('app.mail.send') as mock_send:
            data = {'UserName': 'test_user'}
            result, error, message = reset_password_service(data)
        
            self.assertIsNone(error)
            self.assertEqual(message, 'Password reset successfully. Please check your mail.')

    @patch('app.models.user.User.query')
    def test_reset_password_service_user_not_found(self, mock_query):
        """Test reset password service user not found."""
        mock_query.filter_by.return_value.first.return_value = None
        
        data = {'UserName': 'non_existent_user'}
        result, error, message = reset_password_service(data)
        
        self.assertIsNone(result)
        self.assertTrue(error)
        self.assertEqual(message, "User not found")

if __name__ == '__main__':
    unittest.main()
