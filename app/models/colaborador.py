from app import db

class Colaborador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cargo = db.Column(db.String(50), nullable=False)
    custo_hora = db.Column(db.Float, nullable=False)
