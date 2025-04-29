# 📚 Documentação dos Modelos de Dados

Este documento descreve detalhadamente os modelos de dados utilizados no sistema de Gestão de Projetos, implementados com SQLAlchemy no Flask.

---

## 🗂️ Projeto

**Descrição geral:**  
Representa um projeto a ser gerenciado, contendo informações básicas como nome, prazo e data de início.

**Campos:**
- `id` (Integer, PK) → Identificador único do projeto.
- `nome` (String(100)) → Nome do projeto.
- `prazo_nominal` (Integer) → Duração prevista do projeto em dias.
- `data_inicio` (Date) → Data de início do projeto.

**Relacionamentos:**
- Um projeto se relaciona indiretamente com tarefas através dos tópicos (`Topico`).

---

## 🗂️ Topico

**Descrição geral:**  
Representa as divisões organizacionais de um projeto, podendo ser tópicos ou subtópicos hierárquicos.

**Campos:**
- `id` (Integer, PK) → Identificador único do tópico.
- `nome` (String(100)) → Nome do tópico ou subtópico.
- `projeto_id` (Integer, FK) → Referência ao projeto ao qual o tópico pertence.
- `parent_id` (Integer, FK, nullable) → Referência ao tópico pai (caso seja um subtópico).

**Relacionamentos:**
- `subtitulos` → Lista de subtópicos filhos relacionados ao tópico.
- `tarefas` → Tarefas associadas a este tópico.

---

## 🗂️ Tarefa

**Descrição geral:**  
Representa uma atividade ou tarefa a ser executada dentro de um tópico do projeto.

**Campos:**
- `id` (Integer, PK) → Identificador único da tarefa.
- `nome` (String(100)) → Nome da tarefa.
- `topico_id` (Integer, FK) → Relacionamento com o tópico (`Topico`) ao qual pertence.
- `responsavel_id` (Integer, FK) → Relacionamento com o colaborador (`Colaborador`) responsável pela tarefa.
- `data_inicio_planejada` (Date) → Data prevista para início da tarefa.
- `data_fim_planejada` (Date) → Data prevista para término da tarefa.
- `horas_planejadas` (Float) → Quantidade de horas planejadas para execução da tarefa.
- `data_inicio_executada` (Date, nullable) → Data real de início da tarefa.
- `data_fim_executada` (Date, nullable) → Data real de término da tarefa.
- `horas_executadas` (Float, default=0.0) → Horas efetivamente gastas na execução.
- `percentual_execucao` (Float, default=0.0) → Percentual de conclusão da tarefa.

**Relacionamentos:**
- `responsavel` → Colaborador associado como responsável pela tarefa.
- `topico` → Tópico ao qual a tarefa pertence.
- `execucoes` → Registros de execução (`ExecucaoTarefa`) associados a esta tarefa.

---

## 🗂️ Colaborador

**Descrição geral:**  
Representa os colaboradores que podem ser atribuídos como responsáveis pelas tarefas dos projetos.

**Campos:**
- `id` (Integer, PK) → Identificador único do colaborador.
- `nome` (String(100)) → Nome completo do colaborador.
- `cargo` (String(50)) → Cargo ou função do colaborador no projeto.
- `custo_hora` (Float) → Custo por hora trabalhada do colaborador.

**Relacionamentos:**
- `tarefas` → Tarefas que foram atribuídas a este colaborador.

---

## 🗂️ ExecucaoTarefa

**Descrição geral:**  
Registra o progresso diário das tarefas, permitindo a construção das curvas de execução e burndown.

**Campos:**
- `id` (Integer, PK) → Identificador único do registro de execução.
- `tarefa_id` (Integer, FK) → Referência à tarefa executada.
- `data` (Date) → Data da execução registrada.
- `percentual` (Float) → Percentual de execução da tarefa acumulado até a data.

**Relacionamentos:**
- `tarefa` → Referência à tarefa relacionada a este registro de execução.

---

# 📝 Observações Gerais

- Todos os relacionamentos utilizam **chaves estrangeiras** (ForeignKey) adequadamente configuradas.
- A relação entre Projetos → Tópicos → Tarefas permite modelar estruturas hierárquicas complexas.
- O histórico de execução (`ExecucaoTarefa`) possibilita análises detalhadas do progresso real versus planejado.
- O custo do projeto pode ser inferido combinando-se o custo por hora dos colaboradores com as horas executadas.

---
