from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from .config import config
from .utils.error_handlers import register_error_handlers
from .utils.logging_config import configure_logging 
from sqlalchemy import MetaData
from flask_mail import Mail
from flask_jwt_extended import JWTManager
import os

metadata = MetaData(schema='VisitorTrack')
# db = SQLAlchemy(metadata=metadata)
db = SQLAlchemy()
jwt = JWTManager()
mail = Mail()


def create_app(config_mode="development"):
    app = Flask(__name__)
    CORS(app, origins='*')

    # Load config
    # app.config.from_object('app.config.Config')
    app.config.from_object(config[config_mode])

    # Register error handlers
    register_error_handlers(app)

    # Initialize extensions
    db.init_app(app)
    Migrate(app, db)
    mail.init_app(app)
    jwt.init_app(app)
    
    # Configure logging
    configure_logging(app)

    # Routes -> Register blueprints
    from app.api.user_routes import user_bp
    from app.api.visitors_routes import visitor_bp
    from app.api.common_routes import common_bp

    app.register_blueprint(user_bp, url_prefix='/api/users')
    app.register_blueprint(visitor_bp, url_prefix='/api/visitors')
    app.register_blueprint(common_bp, url_prefix='/api/common')

    # files access api
    @app.route('/files/<path:filename>', methods=['GET'])
    def serve_files(filename):
        return send_from_directory(os.path.join(app.root_path, '../static/uploads'), filename)
    
    return app
