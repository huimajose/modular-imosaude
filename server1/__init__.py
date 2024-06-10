from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('server1.config.Config')
    
    
    with app.app_context():
        #Import controllers
        from controllers import file_controller
        
        return app