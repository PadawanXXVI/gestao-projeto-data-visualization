import os

class Config:
    # Diretório base absoluto do projeto
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    # Caminho completo do banco de dados SQLite
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'database.db')

    # Desativa o rastreamento de modificações de objetos — economiza recursos
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Chave secreta usada para sessões, CSRF e segurança de formulários
    SECRET_KEY = os.environ.get('SECRET_KEY', 'chave-secreta-padrao')
