from app import db

class ExecucaoTarefa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tarefa_id = db.Column(db.Integer, db.ForeignKey('tarefa.id'), nullable=False)
    data = db.Column(db.Date, nullable=False)
    percentual = db.Column(db.Float, nullable=False)

    tarefa = db.relationship('Tarefa', backref=db.backref('execucoes', lazy=True))
