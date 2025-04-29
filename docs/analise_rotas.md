# 📚 Documentação das Rotas do Sistema

Este documento descreve detalhadamente todas as rotas do sistema de Gestão de Projetos, suas funções e templates renderizados.

---

## 📋 Rotas Principais

### `/`
**Função:**  
Página inicial do sistema.

**Descrição:**  
Lista todos os projetos e colaboradores cadastrados.

**Método:**  
- GET

**Template:**  
- `index.html`

---

### `/dashboard/<int:projeto_id>`
**Função:**  
Dashboard do projeto.

**Descrição:**  
Gera gráficos de progresso (Curva S, Burndown, Caminho Crítico, Alocação de Recursos, Execução por Tarefa e Tópico).

**Método:**  
- GET

**Template:**  
- `dashboard_projeto.html`

---

### `/projeto/<int:projeto_id>`
**Função:**  
Visualizar detalhes do projeto.

**Descrição:**  
Lista tópicos e tarefas associadas a um projeto. Exibe Gantt planejado.

**Método:**  
- GET

**Template:**  
- `projeto.html`

---

### `/projeto/<int:projeto_id>/gantt`
**Função:**  
Visualizar Gantt separado.

**Descrição:**  
Exibe o gráfico Gantt planejado do projeto.

**Método:**  
- GET

**Template:**  
- `gantt.html`

---

## ➕ Cadastro de Dados

### `/adicionar_projeto`
**Função:**  
Adicionar novo projeto.

**Descrição:**  
Formulário para cadastrar um novo projeto.

**Métodos:**  
- GET (exibe o formulário)
- POST (processa o cadastro)

**Template:**  
- `adicionar_projeto.html`

---

### `/projeto/<int:projeto_id>/adicionar_topico`
**Função:**  
Adicionar novo tópico ou subtópico.

**Descrição:**  
Formulário para cadastrar tópicos e subtópicos vinculados a um projeto.

**Métodos:**  
- GET (exibe formulário)
- POST (processa cadastro)

**Template:**  
- `adicionar_topico.html`

---

### `/topico/<int:topico_id>/adicionar_tarefa`
**Função:**  
Adicionar nova tarefa.

**Descrição:**  
Formulário para cadastrar tarefas planejadas dentro de um tópico.

**Métodos:**  
- GET (exibe formulário)
- POST (processa cadastro)

**Template:**  
- `adicionar_tarefa.html`

---

### `/adicionar_colaborador`
**Função:**  
Adicionar novo colaborador.

**Descrição:**  
Formulário para cadastrar colaboradores no sistema.

**Métodos:**  
- GET (exibe formulário)
- POST (processa cadastro)

**Template:**  
- `adicionar_colaborador.html`

---

## ✏️ Edição de Dados

### `/editar_projeto/<int:projeto_id>`
**Função:**  
Editar detalhes de um projeto.

**Métodos:**  
- GET (exibe formulário)
- POST (processa edição)

**Template:**  
- `editar_projeto.html`

---

### `/editar_topico/<int:topico_id>`
**Função:**  
Editar detalhes de um tópico.

**Métodos:**  
- GET (exibe formulário)
- POST (processa edição)

**Template:**  
- `editar_topico.html`

---

### `/tarefa/<int:tarefa_id>/editar`
**Função:**  
Editar detalhes planejados de uma tarefa.

**Métodos:**  
- GET (exibe formulário)
- POST (processa edição)

**Template:**  
- `editar_tarefa.html`

---

### `/tarefa/<int:tarefa_id>/atualizar_execucao`
**Função:**  
Atualizar execução de uma tarefa.

**Métodos:**  
- GET (exibe formulário)
- POST (processa atualização)

**Template:**  
- `atualizar_execucao_tarefa.html`

---

## 🗑️ Exclusão de Dados

### `/excluir_projeto/<int:projeto_id>`
**Função:**  
Excluir projeto.

**Método:**  
- GET

**Ação:**  
- Deleta o projeto.

---

### `/excluir_colaborador/<int:colaborador_id>`
**Função:**  
Excluir colaborador.

**Método:**  
- GET

**Ação:**  
- Deleta o colaborador.

---

### `/excluir_topico/<int:topico_id>`
**Função:**  
Excluir tópico.

**Método:**  
- GET

**Descrição:**  
Deleta o tópico se não houver subtópicos vinculados.

---

# 📝 Observações Gerais

- Todas as rotas são protegidas contra erros básicos (ex.: uso de `get_or_404()` para recuperar registros).
- Todas as inserções e edições seguem o padrão GET para exibição de formulário e POST para envio de dados.
- Templates são renderizados utilizando o mecanismo padrão `render_template` do Flask.

---
