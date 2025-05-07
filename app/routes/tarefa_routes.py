from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models.tarefa import Tarefa
from app.models.colaborador import Colaborador
from app.models.topico import Topico
from datetime import datetime

tarefa_bp = Blueprint('tarefa', __name__)

@tarefa_bp.route('/topico/<int:topico_id>/adicionar_tarefa', methods=['GET', 'POST'])
def adicionar_tarefa(topico_id):
    topico = Topico.query.get_or_404(topico_id)
    colaboradores = Colaborador.query.all()

    # Impede adicionar tarefas em tópicos com subtópicos
    if Topico.query.filter_by(parent_id=topico.id).count() > 0:
        return "Erro: Este tópico possui sub-tópicos e não pode ter tarefas.", 400

    if request.method == 'POST':
        nova_tarefa = Tarefa(
            nome=request.form['nome'],
            topico_id=topico.id,
            responsavel_id=int(request.form['responsavel_id']),
            horas_planejadas=float(request.form.get('horas_planejadas', 0.0)),
            data_inicio_planejada=datetime.strptime(request.form['data_inicio'], '%Y-%m-%d').date(),
            data_fim_planejada=datetime.strptime(request.form['data_fim'], '%Y-%m-%d').date()
        )
        db.session.add(nova_tarefa)
        db.session.commit()
        return redirect(url_for('projeto.visualizar_projeto', projeto_id=topico.projeto_id))

    return render_template('adicionar_tarefa.html', topico=topico, colaboradores=colaboradores)


@tarefa_bp.route('/tarefa/<int:tarefa_id>/editar', methods=['GET', 'POST'])
def editar_tarefa(tarefa_id):
    tarefa = Tarefa.query.get_or_404(tarefa_id)
    colaboradores = Colaborador.query.all()

    if request.method == 'POST':
        tarefa.nome = request.form['nome']
        tarefa.responsavel_id = int(request.form['responsavel_id'])
        tarefa.horas_planejadas = float(request.form.get('horas_planejadas', 0.0))
        tarefa.data_inicio_planejada = datetime.strptime(request.form['data_inicio_planejada'], '%Y-%m-%d').date()
        tarefa.data_fim_planejada = datetime.strptime(request.form['data_fim_planejada'], '%Y-%m-%d').date()

        db.session.commit()
        return redirect(url_for('projeto.visualizar_projeto', projeto_id=tarefa.topico.projeto_id))

    return render_template('editar_tarefa.html', tarefa=tarefa, colaboradores=colaboradores)


@tarefa_bp.route('/tarefa/<int:tarefa_id>/atualizar_execucao', methods=['GET', 'POST'])
def atualizar_execucao_tarefa(tarefa_id):
    tarefa = Tarefa.query.get_or_404(tarefa_id)

    if request.method == 'POST':
        tarefa.data_inicio_executada = (
            datetime.strptime(request.form['data_inicio_executada'], '%Y-%m-%d').date()
            if request.form.get('data_inicio_executada') else None
        )
        tarefa.data_fim_executada = (
            datetime.strptime(request.form['data_fim_executada'], '%Y-%m-%d').date()
            if request.form.get('data_fim_executada') else None
        )
        tarefa.horas_executadas = float(request.form.get('horas_executadas', 0.0))
        tarefa.percentual_execucao = float(request.form.get('percentual_execucao', 0.0))

        db.session.commit()
        return redirect(url_for('projeto.visualizar_projeto', projeto_id=tarefa.topico.projeto_id))

    return render_template('atualizar_execucao_tarefa.html', tarefa=tarefa)
