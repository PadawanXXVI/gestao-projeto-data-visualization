# 🌐 Documentação das Rotas do Sistema

Este documento apresenta de forma acessível **todas as rotas (endpoints)** do sistema. Cada rota está associada a uma ação do sistema, como visualizar projetos, adicionar tarefas ou gerar dashboards.

As rotas estão agora organizadas por arquivos separados em:
```bash
app/routes/
```

---

## 📋 Rotas Principais

| Rota                              | Método | Função                                  | Template                     |
|----------------------------------|--------|------------------------------------------|------------------------------|
| `/`                              | GET    | Página inicial                          | `index.html`                 |
| `/dashboard/<projeto_id>`        | GET    | Visualização de gráficos do projeto     | `dashboard_projeto.html`     |
| `/projeto/<projeto_id>`          | GET    | Detalhes e Gantt do projeto             | `projeto.html`               |
| `/projeto/<projeto_id>/gantt`    | GET    | Exibe apenas o Gantt                    | `gantt.html`                 |

---

## ➕ Cadastro de Dados

| Rota                                           | Método  | Função                                  | Template                      |
|------------------------------------------------|---------|------------------------------------------|-------------------------------|
| `/adicionar_projeto`                          | GET/POST| Adiciona novo projeto                   | `adicionar_projeto.html`      |
| `/projeto/<id>/adicionar_topico`              | GET/POST| Adiciona tópico ou subtópico            | `adicionar_topico.html`       |
| `/topico/<id>/adicionar_tarefa`               | GET/POST| Cadastra nova tarefa                    | `adicionar_tarefa.html`       |
| `/adicionar_colaborador`                      | GET/POST| Cadastra colaborador                    | `adicionar_colaborador.html`  |

---

## ✏️ Edição e Atualização

| Rota                                           | Método  | Função                                  | Template                      |
|------------------------------------------------|---------|------------------------------------------|-------------------------------|
| `/editar_projeto/<id>`                        | GET/POST| Editar nome, prazo e data                | `editar_projeto.html`         |
| `/editar_topico/<id>`                         | GET/POST| Editar nome do tópico                    | `editar_topico.html`          |
| `/tarefa/<id>/editar`                         | GET/POST| Editar planejamento da tarefa            | `editar_tarefa.html`          |
| `/tarefa/<id>/atualizar_execucao`             | GET/POST| Atualizar progresso da tarefa            | `atualizar_execucao_tarefa.html`|

---

## 🗑️ Exclusão

- `/excluir_projeto/<id>` → Exclui projeto
- `/excluir_colaborador/<id>` → Exclui colaborador
- `/excluir_topico/<id>` → Exclui tópico (se não tiver subtópicos)
