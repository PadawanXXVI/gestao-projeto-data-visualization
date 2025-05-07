# Sistema de Gestão de Projetos

Projeto Acadêmico da Disciplina **Data Visualization**  
Curso: **Tecnologia em Ciência de Dados**  
Faculdade de Tecnologia e Inovações Senac-DF  
Professor Orientador: **Ms. Guilherme Lustosa Ricarte**  
3º Semestre - 2025.1

---

## 📚 Objetivo
Desenvolver um sistema de gestão de projetos com visualização de dados aplicada, utilizando Flask, SQLAlchemy, Pandas e Plotly.

## 📂 Estrutura do Projeto
- Backend: Flask (modularizado com Blueprints)
- Banco de dados: SQLite + SQLAlchemy
- Visualização de dados: Pandas + Plotly
- Dashboard interativo: Curva S, Burndown, Caminho Crítico
- Documentação: GitHub Wiki + Jupyter Notebook (seguindo metodologia CRISP-DM)

## 🚀 Como Executar
1. Crie e ative o ambiente virtual:
    ```bash
    python -m venv venv
    source venv/Scripts/activate
    ```
2. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
3. Execute o sistema:
    ```bash
    python run.py
    ```

## 📊 Organização de Diretórios
- `run.py` - Ponto de entrada do sistema
- `app/` - Estrutura modular Flask
  - `routes/` - Rotas da aplicação
  - `models.py` - Modelos de banco de dados
  - `__init__.py` - Criação da aplicação
- `templates/` - Páginas HTML
- `static/` - CSS e JavaScript
- `docs/` - Documentação técnica:
  - [`analise_modelos.md`](docs/analise_modelos.md) – Modelos de dados explicados
  - [`analise_rotas.md`](docs/analise_rotas.md) – Rotas da aplicação com funções
  - [`fluxo_geral.md`](docs/fluxo_geral.md) – Fluxo do sistema e arquitetura
- `notebooks/` - Desenvolvimento CRISP-DM

---

## 🛠️ Ferramentas de Gestão
- **GitHub Projects**: organização de tarefas e cronograma
- **GitHub Issues**: controle de desenvolvimento
- **GitHub Wiki**: documentação complementar

---
