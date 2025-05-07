from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models.projeto import Projeto
from app.models.topico import Topico
from app.models.tarefa import Tarefa
from datetime import datetime
import pandas as pd
import plotly.express as px
from markupsafe import Markup

projeto_bp = Blueprint('projeto', __name__)


@projeto_bp.route('/')
def index():
    projetos = Projeto.query.all()
    return render_template('index.html', projetos=projetos)


@projeto_bp.route('/projeto/<int:projeto_id>')
def visualizar_projeto(projeto_id):
    projeto = Projeto.query.get_or_404(projeto_id)
    topicos = Topico.query.filter_by(projeto_id=projeto_id).all()
    tarefas = Tarefa.query.filter(Tarefa.topico_id.in_([t.id for t in topicos])).all()

    total_percentual = sum(t.percentual_execucao or 0 for t in tarefas)
    progresso_total = total_percentual / len(tarefas) if tarefas else 0.0

    # Função auxiliar para organizar tópicos
    def organizar_topicos(topicos, parent_id=None, nivel=0):
        organizados = []
        filtrados = sorted([t for t in topicos if t.parent_id == parent_id], key=lambda x: x.id)
        for topico in filtrados:
            organizados.append((topico, nivel))
            organizados.extend(organizar_topicos(topicos, topico.id, nivel + 1))
        return organizados

    # Gráfico de Gantt planejado
    df_gantt = pd.DataFrame([
        {
            "Tarefa": t.nome,
            "Responsável": t.responsavel.nome if t.responsavel else "Sem responsável",
            "Início Planejado": t.data_inicio_planejada,
            "Fim Planejado": t.data_fim_planejada
        } for t in tarefas
    ])
    df_gantt["Início Planejado"] = pd.to_datetime(df_gantt["Início Planejado"])
    df_gantt["Fim Planejado"] = pd.to_datetime(df_gantt["Fim Planejado"])

    fig = px.timeline(
        df_gantt,
        x_start="Início Planejado",
        x_end="Fim Planejado",
        y="Tarefa",
        color="Responsável",
        title=f"Gantt Planejado - {projeto.nome}"
    )
    fig.update_yaxes(autorange="reversed")

    gantt_html = fig.to_html(full_html=False)

    return render_template(
        'projeto.html',
        projeto=projeto,
        topicos=organizar_topicos(topicos),
        tarefas=tarefas,
        progresso_total=round(progresso_total, 2),
        hoje=datetime.today().strftime('%Y-%m-%d'),
        gantt_html=gantt_html
    )


@projeto_bp.route('/adicionar_projeto', methods=['GET', 'POST'])
def adicionar_projeto():
    if request.method == 'POST':
        nome = request.form['nome']
        prazo_nominal = int(request.form['prazo_nominal'])
        data_inicio = datetime.strptime(request.form['data_inicio'], '%Y-%m-%d').date()

        novo_projeto = Projeto(nome=nome, prazo_nominal=prazo_nominal, data_inicio=data_inicio)
        db.session.add(novo_projeto)
        db.session.commit()
        return redirect(url_for('projeto.index'))

    return render_template('adicionar_projeto.html')


@projeto_bp.route('/editar_projeto/<int:projeto_id>', methods=['GET', 'POST'])
def editar_projeto(projeto_id):
    projeto = Projeto.query.get_or_404(projeto_id)

    if request.method == 'POST':
        projeto.nome = request.form['nome']
        projeto.prazo_nominal = int(request.form['prazo_nominal'])
        projeto.data_inicio = datetime.strptime(request.form['data_inicio'], '%Y-%m-%d').date()

        db.session.commit()
        return redirect(url_for('projeto.index'))

    return render_template('editar_projeto.html', projeto=projeto)


@projeto_bp.route('/excluir_projeto/<int:projeto_id>')
def excluir_projeto(projeto_id):
    projeto = Projeto.query.get_or_404(projeto_id)
    db.session.delete(projeto)
    db.session.commit()
    return redirect(url_for('projeto.index'))


@projeto_bp.route('/projeto/<int:projeto_id>/gantt')
def gantt(projeto_id):
    projeto = Projeto.query.get_or_404(projeto_id)
    topicos = Topico.query.filter_by(projeto_id=projeto_id).all()
    tarefas = Tarefa.query.filter(Tarefa.topico_id.in_([t.id for t in topicos])).all()

    df = pd.DataFrame([
        {"Nome": t.nome, "Início": t.data_inicio_planejada, "Fim": t.data_fim_planejada} for t in tarefas
    ])
    fig = px.timeline(df, x_start="Início", x_end="Fim", y="Nome", title=f'📊 Gantt - {projeto.nome}')
    gantt_html = Markup(fig.to_html(full_html=False))

    return render_template('gantt.html', projeto=projeto, gantt_html=gantt_html)
