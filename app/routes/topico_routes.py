from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models.topico import Topico
from app.models.tarefa import Tarefa
from datetime import datetime

topico_bp = Blueprint('topico', __name__)


@topico_bp.route('/projeto/<int:projeto_id>/adicionar_topico', methods=['GET', 'POST'])
def adicionar_topico(projeto_id):
    if request.method == 'POST':
        nome = request.form['nome']
        parent_id = request.form.get('parent_id')
        parent_id = int(parent_id) if parent_id else None

        # Impede criação de sub-tópico se o pai já tem tarefas
        if parent_id:
            if Tarefa.query.filter_by(topico_id=parent_id).count() > 0:
                return "Erro: Este tópico já possui tarefas e não pode ter sub-tópicos.", 400

        novo_topico = Topico(nome=nome, projeto_id=projeto_id, parent_id=parent_id)
        db.session.add(novo_topico)
        db.session.commit()
        return redirect(url_for('projeto.visualizar_projeto', projeto_id=projeto_id))

    topicos = Topico.query.filter_by(projeto_id=projeto_id).all()
    return render_template('adicionar_topico.html', projeto_id=projeto_id, topicos=topicos)


@topico_bp.route('/editar_topico/<int:topico_id>', methods=['GET', 'POST'])
def editar_topico(topico_id):
    topico = Topico.query.get_or_404(topico_id)

    if request.method == 'POST':
        topico.nome = request.form['nome']
        db.session.commit()
        return redirect(url_for('projeto.visualizar_projeto', projeto_id=topico.projeto_id))

    return render_template('editar_topico.html', topico=topico)


@topico_bp.route('/excluir_topico/<int:topico_id>')
def excluir_topico(topico_id):
    topico = Topico.query.get_or_404(topico_id)
    projeto_id = topico.projeto_id

    # Impede exclusão se houver subtópicos
    if Topico.query.filter_by(parent_id=topico.id).count() > 0:
        return "Erro: Não é possível excluir um tópico que possui subtópicos.", 400

    db.session.delete(topico)
    db.session.commit()
    return redirect(url_for('projeto.visualizar_projeto', projeto_id=projeto_id))
