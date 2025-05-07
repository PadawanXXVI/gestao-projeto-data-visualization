import os

class Config:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    # Caminho do banco de dados SQLite
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'database.db')
    
    # Desativa alertas desnecessários do SQLAlchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Para segurança futura (como CSRF, sessão, etc.)
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'chave-secreta-padrao'
