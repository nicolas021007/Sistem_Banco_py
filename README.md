# Sistem_Banco_py 🏦
Este projeto é um sistema bancário simples em Python, executado via terminal, que permite o cadastro de usuários, gerenciamento de saldo e visualização de dados da conta.

O sistema funciona através de um menu interativo, onde o usuário escolhe as ações digitando números correspondentes às opções disponíveis.

📌 Funcionalidades

- ✅ Cadastro de usuário

- 💰 Adição de saldo à conta

- 📊 Consulta de saldo atual

- 📋 Visualização de todos os dados do usuário

- 🚪 Encerramento do programa


📁 projeto/

│
├── main.py                # Arquivo principal (menu do sistema)
├── menu_usuario.py        # Cadastro e dados do usuário
├── saldo.py               # Gerenciamento de saldo
└── verify.py              # Verificação e exibição dos dados


🧩 Descrição dos Módulos


- menu_usuario.py

Responsável por:

Criar o usuário

Armazenar os dados pessoais do cliente


- saldo.py

Responsável por:

Criar e gerenciar o saldo do usuário

Adicionar valores à conta


- verify.py

Responsável por:

Exibir todos os dados do usuário e o saldo atual



- main.py

Responsável por:

Exibir o menu principal

Controlar o fluxo do programa

Integrar todos os módulos


▶️ Como Executar o Projeto

1- Certifique-se de ter o Python 3 instalado:

python --version


2- Execute o arquivo principal:

python main.py


3- Utilize o menu exibido no terminal para navegar pelas opções.



⚠️ Tratamento de Erros

O sistema possui validações para:

- Entradas inválidas (letras no lugar de números)

- Tentativas de adicionar saldo sem cadastro

- Consulta de dados sem usuário registrado



🛠️ Tecnologias Utilizadas

- Python 3

- Programação Orientada a Objetos (POO)

- Estruturas de repetição e condicionais

- Tratamento de exceções (try/except)


📚 Objetivo do Projeto

Este projeto tem fins educacionais, sendo ideal para treinar:

- Organização de código em módulos

- Uso de classes e objetos

- Interação com o usuário via terminal

- Boas práticas básicas em Python