from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app.routes.projeto_routes import projeto_bp
app.register_blueprint(projeto_bp)

from app.routes.tarefa_routes import tarefa_bp
app.register_blueprint(tarefa_bp)

from app.routes.topico_routes import topico_bp
app.register_blueprint(topico_bp)

from app.routes.colaborador_routes import colaborador_bp
app.register_blueprint(colaborador_bp)

from app.routes.dashboard_routes import dashboard_bp
app.register_blueprint(dashboard_bp)

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Inicializar extensões
    db.init_app(app)
    migrate.init_app(app, db)

    # Registrar blueprints (rotas)
    from app.routes.projeto_routes import projeto_bp
    app.register_blueprint(projeto_bp)

    # Registrar outros blueprints aqui depois...

    return app
