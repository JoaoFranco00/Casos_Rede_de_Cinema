# Sistema Rede de Cinemas

Projeto desenvolvido para a atividade de Engenharia de Software, com base no estudo de caso de uma rede de cinemas.

O sistema permite cadastrar cinemas, filmes e sessões, além de registrar o público das sessões e consultar os dados pela interface web.

---

## Tecnologias Utilizadas

- Python
- Flask
- SQLite
- HTML
- CSS básico

---

## Resumo da Arquitetura

    cinema_project/
    ├── app.py                         ← Ponto de entrada web (Flask)
    ├── main.py                        ← Ponto de entrada CLI
    ├── requirements.txt
    ├── db/
    │   ├── __init__.py
    │   └── database.py                ← Conexão SQLite + criação das tabelas
    ├── model/
    │   ├── __init__.py
    │   ├── cinema.py
    │   ├── filme.py
    │   ├── sessao.py
    │   ├── ator.py
    │   ├── diretor.py
    │   └── genero.py
    ├── repository/
    │   ├── __init__.py
    │   ├── cinema_repository.py
    │   ├── filme_repository.py
    │   └── sessao_repository.py
    ├── service/
    │   ├── __init__.py
    │   ├── cinema_service.py
    │   ├── filme_service.py
    │   └── sessao_service.py
    ├── controller/
    │   ├── __init__.py
    │   ├── cinema_controller.py
    │   ├── filme_controller.py
    │   └── sessao_controller.py
    ├── view/
    │   ├── __init__.py
    │   └── sessao_view_web.py
    └── templates/
        └── sessoes.html

---

## Como Baixar e Abrir o Projeto

Depois de baixar o projeto, extraia o arquivo `.zip`.

Entre na pasta do projeto pelo terminal:

    cd caminho/da/pasta/cinema_project

Exemplo:

    cd C:\Users\SeuNome\Downloads\cinema_project

---

## Como Instalar as Dependências

Antes de abrir o sistema, instale as dependências do projeto.

Rode:

    pip install -r requirements.txt

Se o comando `pip` não funcionar, use:

    python -m pip install -r requirements.txt

ou:

    py -m pip install -r requirements.txt

O arquivo `requirements.txt` deve conter:

    flask

---

## Como Abrir o Site

Para iniciar o sistema web, rode:

    python app.py

ou, no Windows:

    py app.py

Se tudo estiver certo, o terminal vai mostrar algo parecido com:

    Running on http://127.0.0.1:5000

Depois disso, abra o navegador e acesse:

    http://127.0.0.1:5000

Esse endereço abre o site local do sistema.

---

## Como Utilizar o Sistema

### 1. Cadastrar Cinema

Na tela inicial, localize a área de cadastro de cinema.

Preencha os campos:

- nome do cinema;
- cidade;
- estado;
- endereço;
- capacidade total.

Depois clique em:

    Salvar Cinema

O cinema ficará disponível para ser usado no cadastro de sessões.

---

### 2. Cadastrar Filme

Na área de cadastro de filme, preencha:

- título;
- duração em minutos;
- gênero;
- diretor;
- elenco;
- classificação indicativa.

Depois clique em:

    Salvar Filme

O filme ficará disponível para ser selecionado no cadastro de sessões.

---

### 3. Cadastrar Sessão

Na área de cadastro de sessão, selecione:

- cinema;
- filme;
- sala;
- data;
- horário inicial.

Depois clique em:

    Salvar Sessão

O sistema irá calcular o horário final da sessão com base na duração do filme e no intervalo obrigatório.

---

### 4. Registrar Público da Sessão

Depois de cadastrar uma sessão, vá até a área de registro de público.

Selecione a sessão desejada e informe a quantidade de espectadores presentes.

Depois clique em:

    Registrar Público

O sistema valida se o público informado não ultrapassa a capacidade do cinema.

---

### 5. Consultar Sessões

Na própria tela inicial, o sistema lista as sessões cadastradas com informações como:

- cinema;
- filme;
- data;
- horário inicial;
- horário final;
- sala;
- público registrado.

---

### 6. Consultar Totais de Público

Na parte inferior da tela, o sistema mostra:

- total de público por filme;
- total de público por cinema.

Essas informações são atualizadas conforme os públicos das sessões são registrados.

---

## Como Encerrar o Sistema

Para parar o servidor local, volte ao terminal onde o sistema está rodando e pressione:

    CTRL + C

Isso encerra o Flask e libera o endereço local.

---
