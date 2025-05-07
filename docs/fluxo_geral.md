# 🔁 Fluxo Geral da Aplicação

Este documento explica o funcionamento geral do sistema **após a modularização**.

---

## ⚙️ Estrutura Modular

A estrutura principal está organizada da seguinte forma:

```bash
app/
├── __init__.py              # Cria a aplicação Flask e registra rotas
├── models/                  # Modelos do banco de dados
│   └── (projeto.py, tarefa.py, etc.)
├── routes/                  # Rotas (BluePrints)
│   └── projeto_routes.py, tarefa_routes.py...
├── templates/               # HTMLs
├── static/                  # CSS, JS
├── config.py                # Configurações do sistema
run.py                       # Arquivo principal de execução
```

---

## 🧠 Processo de Execução

1. `run.py` chama `create_app()` de `app/__init__.py`
2. A aplicação Flask é criada com configurações (banco, secret key)
3. Extensões (SQLAlchemy, Migrate) são ativadas
4. Todas as rotas (blueprints) são registradas
5. O servidor Flask é iniciado e a aplicação está pronta para uso

---

## 🔍 Fluxo do Usuário no Sistema

1. **Página Inicial (`/`)** → Visualiza projetos existentes
2. **Adicionar Projeto** → Cria novo projeto
3. **Adicionar Tópico/Subtópico** → Cria estrutura organizacional
4. **Adicionar Tarefa** → Planeja atividades
5. **Atualizar Execução** → Alimenta os dados reais
6. **Dashboard** → Acompanha progresso por gráficos

---

## 📊 Visualizações (na rota `/dashboard/<id>`)

- **Curva S**: planejado × executado
- **Burndown**: trabalho restante
- **Alocação de Recursos**: carga por colaborador
- **Execução por Tarefa/Tópico**
- **Caminho Crítico**: Gantt da parte mais sensível do projeto

---

## 🔧 Tecnologias Utilizadas

- **Flask**: Framework web
- **SQLAlchemy**: ORM para manipular banco
- **SQLite**: Banco de dados leve
- **Plotly + Pandas**: Gráficos interativos e análise
- **Git + GitHub**: Controle de versão, issues e milestones

---

## 📘 Para Iniciantes

Se você é iniciante:
- Clone o repositório
- Crie o ambiente virtual
- Instale as dependências
- Rode com `python run.py`
- Use o navegador para acessar: `http://localhost:5000/`
