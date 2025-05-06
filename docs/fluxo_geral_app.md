# 📘 Fluxo Geral do app.py

## 🔷 1. Visão Geral

O sistema é um **aplicativo Flask** voltado para a **gestão de projetos com visualizações de dados interativas**, construído para fins acadêmicos na disciplina *Data Visualization*.  
Combina:
- Backend com Flask + SQLAlchemy
- Dashboard com Plotly
- Banco de dados SQLite
- Análises estruturadas com Pandas

## 🔶 2. Configuração Inicial

- Criação do app Flask
- Caminho do banco de dados SQLite é configurado com:
```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'database.db')
```

- SQLAlchemy é inicializado com ```db = SQLAlchemy(app)```
- Migrations são gerenciadas por ```Flask-Migrate```

## 🧱 3. Modelos (SQLAlchemy)

### 🔹 Projeto

Campos: ```id```, ```nome```, ```prazo_nominal```, ```data_inicio```

Função auxiliar: ```.get_tarefas()``` → retorna todas as tarefas do projeto

### 🔹 Tópico

Campos: ```id```, ```nome```, ```projeto_id```, ```parent_id```

Permite estruturação hierárquica (tópico → subtópico)

Relacionamento com tarefas

## 🔹 Tarefa

Planejamento e execução de tarefas

Campos: datas previstas e executadas, horas, percentual

Relacionamentos:

```topico_id``` → Tópico

```responsavel_id``` → Colaborador

```execucoes``` → Histórico de execução

### 🔹 Colaborador

Campos: ```nome```, ```cargo```, ```custo_hora```

Relacionamento com tarefas

### 🔹 ExecucaoTarefa

Histórico de execução com percentual diário

Campos: ```tarefa_id```, ```data```, ```percentual```

## 🌐 4. Rotas Principais

| Rota                              | Método   | Descrição                                        |
| --------------------------------- | -------- | ------------------------------------------------ |
| `/`                               | GET      | Página inicial com projetos e colaboradores      |
| `/dashboard/<projeto_id>`         | GET      | Gera dashboard com gráficos interativos          |
| `/projeto/<projeto_id>`           | GET      | Visualiza o projeto com tarefas, tópicos e Gantt |
| `/projeto/<id>/adicionar_topico`  | GET/POST | Adiciona tópico ou subtópico                     |
| `/topico/<id>/adicionar_tarefa`   | GET/POST | Adiciona tarefa a um tópico                      |
| `/tarefa/<id>/editar`             | GET/POST | Edita dados planejados da tarefa                 |
| `/tarefa/<id>/atualizar_execucao` | GET/POST | Atualiza a execução real da tarefa               |
| `/editar_projeto/<id>`            | GET/POST | Edita dados de um projeto                        |
| `/editar_topico/<id>`             | GET/POST | Edita dados de um tópico                         |
| `/adicionar_projeto`              | GET/POST | Cria novo projeto                                |
| `/adicionar_colaborador`          | GET/POST | Cria novo colaborador                            |
| `/excluir_*`                      | GET      | Exclusão de projeto, colaborador ou tópico       |
| `/projeto/<id>/gantt`             | GET      | Mostra gráfico Gantt com Plotly                  |

## 📊 5. Visualizações com Plotly

Geradas na rota ```/dashboard/<projeto_id>```:
- Curva S: Nominal × Planejado × Executado
- Burndown: Trabalho restante ao longo do tempo
- Alocação de Recursos: Horas planejadas por colaborador
- Execução por Tarefa: Barra horizontal com percentual
- Execução por Tópico: Média de execução por categoria
- Caminho Crítico: Gantt do tópico com maior duração estimada

Rota ```/projeto/<projeto_id>```:
- Gantt Planejado: com metas visuais (prazo contratual e meta de 70%)

## ⚙️ 6. Funções Auxiliares

```organizar_topicos(topicos, parent_id=None, nivel=0)```

- Estrutura recursiva que organiza tópicos e subtópicos em ordem hierárquica
- Usada para exibir corretamente a árvore de tópicos no template

## 🔁 7. Fluxo de Execução Esperado

1. Criar um projeto com nome, prazo e data inicial
2. Adicionar tópicos e, opcionalmente, subtópicos
3. Cadastrar tarefas por tópico e associar a um colaborador
4. Atualizar execução das tarefas com datas e percentual
5. Acessar o dashboard para acompanhar:
    - Progresso total
    - Atrasos
    - Caminho crítico
    - Distribuição de carga de trabalho

## ✅ 8. Observações Finais

- O ```app.py``` centraliza tanto os modelos quanto todas as rotas
- Estrutura clara e modular
- Boas práticas com SQLAlchemy e Flask
- Excelente base para aplicar as fases seguintes do CRISP-DM (Exploração e Modelagem com Pandas e Plotly)