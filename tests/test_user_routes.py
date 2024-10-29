import unittest
from unittest.mock import patch
from app import create_app
from app.models import User

class UserRoutesTestCase(unittest.TestCase):
    def setUp(self):
        """Set up test client."""
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        """Teardown test environment."""
        self.app_context.pop()

    @patch('app.controllers.user_controller.login_user')
    def test_login_success(self, mock_login_user):
        """Test successful login."""
        mock_login_user.return_value = {"status": "success"}, 200
        user = User.query.filter_by(UserName='prakash').first() 
        response = self.client.post('/api/users/login', json={'UserName': 'prakash', 'UPassword': user.UPassword })

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login successful', response.data)

    @patch('app.controllers.user_controller.login_user')
    def test_login_failure(self, mock_login_user):
        """Test failed login due to invalid credentials."""
        mock_login_user.return_value = {'error': 'Invalid username or password', 'status': 'error'}, 401
        response = self.client.post('/api/users/login', json={'UserName': 'wrong_user', 'UPassword': 'wrong_pass'})
        
        self.assertEqual(response.status_code, 401)
        self.assertIn(b'Invalid username or password', response.data)

    @patch('app.controllers.user_controller.reset_password')
    def test_reset_password_success(self, mock_reset_password):
        """Test successful password reset."""
        mock_reset_password.return_value = {"status": "success"}, 200
        response = self.client.post('/api/users/resetpassword', json={'UserName': 'prakash'})
        
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Password reset successful', response.data)

    @patch('app.controllers.user_controller.reset_password')
    def test_reset_password_failure(self, mock_reset_password):
        """Test failed password reset due to missing username."""
        mock_reset_password.return_value = {'error': 'Username is required', 'status': 'error'}, 400
        response = self.client.post('/api/users/resetpassword', json={})
        
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Username is required', response.data)

if __name__ == '__main__':
    unittest.main()
