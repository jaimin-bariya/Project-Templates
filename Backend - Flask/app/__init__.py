import faulthandler
from flask_migrate import Migrate
from flask import Flask
from app.database import db # Secure 
from config import Config # Secure
from werkzeug.debug import DebuggedApplication

faulthandler.enable()  # Enable detailed crash reports for deep recursion



def Create_app():


    app = Flask(__name__)

    # Enable Werkzeug Debugger
    app.wsgi_app = DebuggedApplication(app.wsgi_app, evalex=True)




    app.config.from_object(Config)



    # Initialize Extensions 
    db.init_app(app)

    # Initialize Flask Migration 
    migrate = Migrate(app, db)


    # Import Blueprints inside the function to avoid circular imports
    from app.routes.user_routes import user_bp
    from app.routes.home_routes import home_bp

    # Register Blueprints (Routers)
    app.register_blueprint(user_bp)
    app.register_blueprint(home_bp)


    # Enable Werkzeug Debugger (Only in Debug Mode)
    if app.config.get("DEBUG", False):  
        app.wsgi_app = DebuggedApplication(app.wsgi_app, evalex=True)





    return app





