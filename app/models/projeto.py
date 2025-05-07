from app import db
from app.models.tarefa import Tarefa
from app.models.topico import Topico

class Projeto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    prazo_nominal = db.Column(db.Integer, nullable=False)
    data_inicio = db.Column(db.Date, nullable=False)

    def get_tarefas(self):
        return Tarefa.query.join(Topico).filter(Topico.projeto_id == self.id).all()
