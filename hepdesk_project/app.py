from flask import Flask
from extensions import db
from routes.supervisor import bp_supervisor
from routes.tech import bp_tech
from routes.admin import bp_admin # Assumindo que você criará o admin.py similar aos outros

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///helpdesk.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Registrar os módulos (Blueprints)
    app.register_blueprint(bp_supervisor)
    app.register_blueprint(bp_tech)
    app.register_blueprint(bp_admin)

    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
