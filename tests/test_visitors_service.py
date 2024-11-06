import unittest
from unittest.mock import patch, MagicMock
from app.services.visitors_service import get_visitors_service
from app.models import VisitorsMaster
from app import create_app, db


class TestVisitorServices(unittest.TestCase):
    def setUp(self):
        """Set up the test client and app context."""
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        """Tear down the test client and app context."""
        self.app_context.pop()

    @patch('app.models.visitor_master.VisitorsMaster.query.all')
    def test_get_visitors_service_success(self, mock_visitors_all):
        # Mocking the result of VisitorsMaster.query.all
        mock_visitors_all.return_value = [
            MagicMock(as_dict=lambda: {'id': 1, 'name': 'John Doe'}),
            MagicMock(as_dict=lambda: {'id': 2, 'name': 'Jane Smith'}),
        ]

        result, error, message = get_visitors_service()

        print(result, error, message, 'result, error, message')

        # Assertions
        self.assertIsNone(error)
        # self.assertEqual(len(result), 2)
        # self.assertEqual(result[0]['name'], 'John Doe')
        self.assertEqual(message, None)

    # @patch('app.models.visitor_master.VisitorsMaster.query.all')
    # def test_get_visitors_service_no_data(self, mock_visitors_all):
    #     # Mocking the result when no data is found
    #     mock_visitors_all.return_value = []

    #     result, error, message = get_visitors_service()

    #     # Assertions
    #     self.assertIsNone(result)
    #     self.assertTrue(error)
    #     self.assertEqual(message, "No data found")
