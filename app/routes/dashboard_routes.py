from flask import Blueprint, render_template
from app import db
from app.models.projeto import Projeto
from app.models.topico import Topico
from app.models.tarefa import Tarefa
from app.models.execucao_tarefa import ExecucaoTarefa
from datetime import datetime, timedelta
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

dashboard_bp = Blueprint('dashboard', __name__)


@dashboard_bp.route('/dashboard/<int:projeto_id>')
def dashboard_projeto(projeto_id):
    projeto = Projeto.query.get_or_404(projeto_id)
    tarefas = Tarefa.query.join(Topico).filter(Topico.projeto_id == projeto.id).all()
    hoje = datetime.today().date()
    total_percentual = sum(t.percentual_execucao or 0 for t in tarefas)
    progresso_total = total_percentual / len(tarefas) if tarefas else 0.0

    # Status das Tarefas
    status_tarefas = {
        'Concluído': sum(1 for t in tarefas if t.percentual_execucao == 100),
        'Em Execução': sum(1 for t in tarefas if 0 < t.percentual_execucao < 100),
        'Atrasado': sum(1 for t in tarefas if t.data_fim_planejada and t.data_fim_planejada < hoje and t.percentual_execucao < 100),
        'Não Iniciadas': sum(1 for t in tarefas if (t.percentual_execucao or 0) == 0),
    }

    # Curva S - Nominal
    data_fim_nominal = projeto.data_inicio + timedelta(days=projeto.prazo_nominal)
    datas_nominal = pd.date_range(start=projeto.data_inicio, end=data_fim_nominal)
    nominal = [(i / (len(datas_nominal) - 1)) * 100 for i in range(len(datas_nominal))]

    # Curva S - Planejada
    progresso_planejado_por_data = {}
    for t in tarefas:
        dias = (t.data_fim_planejada - t.data_inicio_planejada).days + 1
        if dias <= 0:
            continue
        carga_diaria = 100 / dias
        for i in range(dias):
            dia = t.data_inicio_planejada + timedelta(days=i)
            progresso_planejado_por_data[dia] = progresso_planejado_por_data.get(dia, 0) + carga_diaria

    datas_planejado = sorted(progresso_planejado_por_data.keys())
    progresso_planejado = []
    acumulado = 0
    for d in datas_planejado:
        acumulado += progresso_planejado_por_data[d]
        progresso_planejado.append(acumulado / len(tarefas))

    # Curva S - Executada
    exec_data = ExecucaoTarefa.query.join(Tarefa).join(Topico).filter(Topico.projeto_id == projeto.id).all()
    if exec_data:
        df_exec = pd.DataFrame([{"Data": e.data, "Tarefa": e.tarefa_id, "Percentual": e.percentual} for e in exec_data])
        df_exec["Data"] = pd.to_datetime(df_exec["Data"])
        df_exec = df_exec.sort_values(["Tarefa", "Data"])
        df_exec["Acumulado"] = df_exec.groupby("Tarefa")["Percentual"].cummax()
        df_exec_diario = df_exec.groupby("Data")["Acumulado"].sum().reset_index()
        df_exec_diario["Progresso"] = df_exec_diario["Acumulado"] / len(tarefas)
        df_exec_diario["Linha"] = "Executado"
        df_exec_final = df_exec_diario[["Data", "Progresso", "Linha"]]
    else:
        df_exec_final = pd.DataFrame(columns=["Data", "Progresso", "Linha"])

    # Gráfico Curva S
    df_nominal = pd.DataFrame({"Data": datas_nominal, "Linha": "Nominal", "Progresso": nominal})
    df_planejado = pd.DataFrame({"Data": datas_planejado, "Linha": "Planejado", "Progresso": progresso_planejado})
    df_tempo = pd.concat([df_nominal, df_planejado, df_exec_final])

    fig_tempo = px.line(df_tempo, x="Data", y="Progresso", color="Linha",
                        title="📊 Progresso do Tempo",
                        labels={"Progresso": "Progresso (%)"})
    fig_tempo.update_layout(template="simple_white", font=dict(size=14), title_font=dict(size=18))

    # Gráfico Burndown
    trabalho_total = len(tarefas) * 100
    trabalho_restante_planejado = []
    acumulado_planejado = 0
    for d in datas_planejado:
        acumulado_planejado += progresso_planejado_por_data[d]
        restante = max(trabalho_total - acumulado_planejado, 0)
        trabalho_restante_planejado.append(restante / len(tarefas))

    df_burndown_nominal = pd.DataFrame({
        "Data": datas_nominal,
        "Trabalho (%)": [(1 - i / (len(datas_nominal) - 1)) * 100 for i in range(len(datas_nominal))],
        "Linha": "Nominal"
    })
    df_burndown_planejado = pd.DataFrame({
        "Data": datas_planejado,
        "Trabalho (%)": trabalho_restante_planejado,
        "Linha": "Planejado"
    })
    if exec_data:
        df_hist = pd.DataFrame([{"Data": e.data, "Tarefa": e.tarefa_id, "Percentual": e.percentual} for e in exec_data])
        df_hist["Data"] = pd.to_datetime(df_hist["Data"])
        df_hist = df_hist.sort_values(["Tarefa", "Data"])
        df_hist["Acumulado"] = df_hist.groupby("Tarefa")["Percentual"].cummax()
        df_diario = df_hist.groupby("Data")["Acumulado"].sum().reset_index()
        df_diario["Trabalho (%)"] = (trabalho_total - df_diario["Acumulado"]) / len(tarefas)
        df_diario["Linha"] = "Executado"
        df_burndown_exec = df_diario[["Data", "Trabalho (%)", "Linha"]]
    else:
        df_burndown_exec = pd.DataFrame(columns=["Data", "Trabalho (%)", "Linha"])

    df_burndown = pd.concat([df_burndown_nominal, df_burndown_planejado, df_burndown_exec])
    fig_burndown = px.line(df_burndown, x="Data", y="Trabalho (%)", color="Linha", title="📉 Burndown Chart")

    # Recursos e Execução por Tarefa
    df_recursos = pd.DataFrame([
        {"Colaborador": t.responsavel.nome, "Horas": t.horas_planejadas}
        for t in tarefas if t.responsavel
    ])
    fig_recursos = px.bar(df_recursos, x="Horas", y="Colaborador", orientation="h", title="👥 Alocação de Recursos")

    df_execucao = pd.DataFrame([
        {"Tarefa": t.nome, "Execução (%)": t.percentual_execucao or 0}
        for t in tarefas
    ])
    fig_execucao = px.bar(df_execucao, x="Tarefa", y="Execução (%)", title="📊 Execução por Tarefa")
    fig_execucao.update_layout(yaxis=dict(range=[0, 100]))

    # Execução por Tópico
    df_topico_execucao = pd.DataFrame([
        {"Tópico": t.topico.nome, "Execução": t.percentual_execucao or 0}
        for t in tarefas
    ])
    df_topico_resumo = df_topico_execucao.groupby("Tópico", as_index=False).mean()
    fig_topico = px.bar(df_topico_resumo, x="Tópico", y="Execução", title="📌 Execução por Tópico")

    return render_template(
        "dashboard_projeto.html",
        projeto=projeto,
        status_tarefas=status_tarefas,
        fig_tempo=fig_tempo.to_html(full_html=False),
        fig_burndown=fig_burndown.to_html(full_html=False),
        fig_recursos=fig_recursos.to_html(full_html=False),
        fig_execucao=fig_execucao.to_html(full_html=False),
        fig_topico=fig_topico.to_html(full_html=False),
        caminho_critico="(em cálculo futuro)",
        progresso_total=round(progresso_total, 2)
    )
