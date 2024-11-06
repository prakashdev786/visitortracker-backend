import logging
from logging.handlers import RotatingFileHandler
import os

def configure_logging(app):
    """Configure logging for the Flask application."""
    # Create a directory for log files if it doesn't exist
    if not os.path.exists('logs'):
        os.makedirs('logs')

    # Set up a file handler for logging
    file_handler = RotatingFileHandler('logs/app.log', maxBytes=10240, backupCount=10)
    file_handler.setLevel(logging.INFO)

    # Set up a console handler for logging
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Define the logging format
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add the handlers to the app's logger
    app.logger.addHandler(file_handler)
    app.logger.addHandler(console_handler)
    app.logger.setLevel(logging.INFO)  # Set the minimum logging level
