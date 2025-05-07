from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models.colaborador import Colaborador

colaborador_bp = Blueprint('colaborador', __name__)


@colaborador_bp.route('/adicionar_colaborador', methods=['GET', 'POST'])
def adicionar_colaborador():
    if request.method == 'POST':
        nome = request.form['nome']
        cargo = request.form['cargo']
        custo_hora = float(request.form['custo_hora'])

        novo_colaborador = Colaborador(nome=nome, cargo=cargo, custo_hora=custo_hora)
        db.session.add(novo_colaborador)
        db.session.commit()
        return redirect(url_for('projeto.index'))

    return render_template('adicionar_colaborador.html')


@colaborador_bp.route('/excluir_colaborador/<int:colaborador_id>')
def excluir_colaborador(colaborador_id):
    colaborador = Colaborador.query.get_or_404(colaborador_id)
    db.session.delete(colaborador)
    db.session.commit()
    return redirect(url_for('projeto.index'))


@colaborador_bp.route('/editar_colaborador/<int:colaborador_id>', methods=['GET', 'POST'])
def editar_colaborador(colaborador_id):
    colaborador = Colaborador.query.get_or_404(colaborador_id)

    if request.method == 'POST':
        colaborador.nome = request.form['nome']
        colaborador.cargo = request.form['cargo']
        colaborador.custo_hora = float(request.form['custo_hora'])
        db.session.commit()
        return redirect(url_for('projeto.index'))

    return render_template('editar_colaborador.html', colaborador=colaborador)
