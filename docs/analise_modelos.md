# 🧱 Análise dos Modelos do Banco de Dados

Este documento descreve, de forma clara e acessível, os modelos de dados utilizados no projeto de **Sistema de Gestão de Projetos com Visualização Interativa**, estruturado com Flask e SQLAlchemy.

---

## 📦 Modelos

### 🔸 Projeto (`Projeto`)
- **id**: Identificador único do projeto.
- **nome**: Nome do projeto.
- **prazo_nominal**: Prazo total estimado (em dias).
- **data_inicio**: Data de início oficial do projeto.

📌 Este modelo permite **centralizar as tarefas e tópicos**. Possui um método auxiliar `.get_tarefas()` que retorna todas as tarefas associadas ao projeto, conectando com os tópicos relacionados.

---

### 🔸 Tópico (`Topico`)
- **id**: Identificador do tópico.
- **nome**: Nome do tópico.
- **projeto_id**: Projeto ao qual o tópico está vinculado.
- **parent_id**: Se for um subtópico, armazena o `id` do tópico pai.

📚 Permite estruturar **tópicos e subtópicos em árvore**, ideal para dividir o projeto por fases, departamentos ou áreas temáticas.

---

### 🔸 Tarefa (`Tarefa`)
- **id**: Identificador da tarefa.
- **nome**: Nome da tarefa.
- **topico_id**: Tópico ao qual a tarefa pertence.
- **responsavel_id**: Colaborador responsável.
- **datas**: Planejadas e executadas (início e fim).
- **horas**: Planejadas e executadas.
- **percentual_execucao**: Progresso da tarefa (%).

🔁 Possui relacionamento com:
- `Topico`: a que pertence.
- `Colaborador`: quem realiza.
- `ExecucaoTarefa`: histórico detalhado de avanço.

---

### 🔸 Colaborador (`Colaborador`)
- **id**: Identificador do colaborador.
- **nome**: Nome completo.
- **cargo**: Cargo ou função no projeto.
- **custo_hora**: Custo por hora (usado para relatórios e BI).

👤 Cada colaborador pode ser responsável por várias tarefas.

---

### 🔸 Execução da Tarefa (`ExecucaoTarefa`)
- **id**: Identificador da execução.
- **tarefa_id**: Tarefa associada.
- **data**: Data do registro de execução.
- **percentual**: Avanço registrado (%).

📈 Permite construir a **Curva S executada**, analisando a evolução real do projeto.

---

## 🗂️ Localização no Projeto

Todos os modelos agora estão centralizados em:
```bash
app/models/
```

Separá-los permite organização, reuso e clareza.
