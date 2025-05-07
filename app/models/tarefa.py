from app import db

class Tarefa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    topico_id = db.Column(db.Integer, db.ForeignKey('topico.id'), nullable=False)
    responsavel_id = db.Column(db.Integer, db.ForeignKey('colaborador.id'), nullable=False)

    data_inicio_planejada = db.Column(db.Date, nullable=False)
    data_fim_planejada = db.Column(db.Date, nullable=False)
    horas_planejadas = db.Column(db.Float, default=0.0)

    data_inicio_executada = db.Column(db.Date, nullable=True)
    data_fim_executada = db.Column(db.Date, nullable=True)
    horas_executadas = db.Column(db.Float, default=0.0)

    percentual_execucao = db.Column(db.Float, default=0.0)

    responsavel = db.relationship('Colaborador', backref=db.backref('tarefas', lazy=True))
    topico = db.relationship('Topico', backref=db.backref('tarefas', lazy=True), overlaps="tarefas")
