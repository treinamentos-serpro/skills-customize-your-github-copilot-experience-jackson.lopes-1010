# 📘 Atividade: Building REST APIs com FastAPI

## 🎯 Objetivo

Construa uma API REST para gerenciar tarefas usando FastAPI. Pratique rotas HTTP, validação de dados com Pydantic, códigos de status e operações CRUD.

## 📝 Tarefas

### 🛠️ Criar a Aplicação e Consultar Tarefas

#### Descrição
Instale FastAPI e Uvicorn, execute o código inicial e complete as rotas para verificar se a API está ativa e listar as tarefas armazenadas em memória.

#### Requisitos
O programa concluído deve:

- Criar uma aplicação FastAPI chamada `app`.
- Responder a `GET /` com uma mensagem indicando que a API está ativa.
- Responder a `GET /tasks` com a lista de tarefas, inicialmente vazia.
- Permitir explorar e testar as rotas pela documentação interativa em `/docs`.

### 🛠️ Criar e Consultar uma Tarefa

#### Descrição
Implemente a criação de tarefas e a consulta de uma tarefa específica pelo identificador. Use os modelos Pydantic fornecidos para validar os dados recebidos e estruturar as respostas.

#### Requisitos
O programa concluído deve:

- Criar uma tarefa com `title` e `completed`, usando `False` como valor padrão para `completed`.
- Atribuir um identificador único a cada tarefa e armazená-la na lista em memória.
- Responder a `POST /tasks` com a tarefa criada e o código HTTP `201`.
- Responder a `GET /tasks/{task_id}` com a tarefa correspondente ou retornar `404` se ela não existir.
- Retornar `422` automaticamente quando os dados enviados não corresponderem ao modelo.

### 🛠️ Atualizar e Excluir Tarefas

#### Descrição
Complete as rotas para atualizar uma tarefa existente e removê-la. Trate identificadores inexistentes de forma consistente.

#### Requisitos
O programa concluído deve:

- Atualizar o título e o estado `completed` de uma tarefa por meio de `PUT /tasks/{task_id}`.
- Responder à atualização com a tarefa modificada ou retornar `404` se a tarefa não existir.
- Excluir uma tarefa por meio de `DELETE /tasks/{task_id}` e responder com o código HTTP `204` sem conteúdo.
- Retornar `404` ao tentar excluir uma tarefa inexistente.
