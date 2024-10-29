import unittest
from unittest.mock import patch, MagicMock
from app.controllers.user_controller import login_user, reset_password
from app.services.user_service import login_user_service, reset_password_service
from app.models import User
from app import create_app

class UserControllerTestCase(unittest.TestCase):
    def setUp(self):
        """Set up test client and application context."""
        self.app = create_app('testing') 
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        """Teardown test environment."""
        self.app_context.pop()

    @patch('app.services.user_service.login_user_service')
    def test_login_user_success(self, mock_login_user_service):
        """Test successful user login."""
        mock_login_user_service.return_value = ({'id': 1, 'UserName': 'test_user'}, None, None)  
        user = User.query.filter_by(UserName='prakash').first()      
        data = {'UserName': 'prakash', 'UPassword': user.UPassword }
        
        response, status_code = login_user(data)
        
        self.assertEqual(status_code, 200)
        self.assertIn('Login successful', response.json['message'])

    @patch('app.services.user_service.login_user_service')
    def test_login_user_failure(self, mock_login_user_service):
        """Test failed login due to invalid credentials."""
        mock_login_user_service.return_value = (None, True, "Invalid username or password")
        data = {'UserName': 'wrong_user', 'UPassword': 'wrong_pass'}
        
        response, status_code = login_user(data)
        
        self.assertEqual(status_code, 401)
        self.assertIn('Invalid username or password', response.json['message'])

    @patch('app.services.user_service.reset_password_service')
    def test_reset_password_success(self, mock_reset_password_service):
        """Test successful password reset."""
        mock_reset_password_service.return_value = (None, None, 'Password reset successful.')
        data = {'UserName': 'prakash'}
        
        response, status_code = reset_password(data)
        
        self.assertEqual(status_code, 200)
        self.assertIn('Password reset successful', response.json['message'])

    @patch('app.services.user_service.reset_password_service')
    def test_reset_password_failure(self, mock_reset_password_service):
        """Test failed password reset due to missing username."""
        mock_reset_password_service.return_value = (None, True, "Username is required")
        data = {}
        
        response, status_code = reset_password(data)
        
        self.assertEqual(status_code, 400)
        self.assertIn('Username is required', response.json['message'])

if __name__ == '__main__':
    unittest.main()
