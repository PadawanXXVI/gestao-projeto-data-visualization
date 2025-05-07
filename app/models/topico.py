from app import db

class Topico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    projeto_id = db.Column(db.Integer, db.ForeignKey('projeto.id'), nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('topico.id'), nullable=True)

    subtitulos = db.relationship('Topico', backref=db.backref('parent', remote_side=[id]), lazy=True)
