# Sistem_Banco_py 🏦
Este projeto é um sistema bancário simples em Python, executado via terminal, que permite o cadastro de usuários, gestão de saldo (depósito e saque) e visualização de dados da conta.

O objetivo do projeto é praticar lógica de programação, orientação a objetos e validações básicas, simulando o funcionamento de um banco.


🚀 Funcionalidades

-✅ Cadastro de usuário

-✅ Validação de dados do usuário

-✅ Gestão de saldo:

- > Depositar saldo

- >Sacar saldo

-✅ Ver saldo atual

-✅ Visualizar todos os dados do usuário

-✅ Menu interativo

-✅ Tratamento de erros de entrada


📁 projeto_banco/
│
├── main.py               # Arquivo principal (menu do sistema)
├── menu_usuario.py       # Cadastro e validação do usuário
├── saldo.py              # Gestão de saldo (depósito e saque)
├── verify.py             # Exibição dos dados do usuário
└── README.md             # Documentação do projeto


🧠 Como o sistema funciona

Ao iniciar o programa, o usuário visualiza um menu principal com as opções:

(1) Cadastrar usuário
(2) Gestão de saldo
(3) Verificar saldo da conta
(4) Ver todos os dados do usuário
(5) Sair


🔹 Cadastro de Usuário

- O usuário informa seus dados

- O sistema valida as informações

- O saldo é iniciado automaticamente


🔹 Gestão de Saldo

- Dentro dessa opção, o usuário pode:

- Depositar saldo

- Sacar saldo


🔹 Segurança

- Não é possível acessar saldo sem cadastro

- Não é permitido sacar mais do que o saldo disponível

- Entradas inválidas são tratadas


▶️ Como executar o projeto
Pré-requisitos:

-Python 3.10 ou superior instalado

Executar no terminal:

python main.py


🛠 Tecnologias utilizadas

- Python 3

- Programação Orientada a Objetos (POO)

- Estruturas de repetição

- Tratamento de exceções (try/except)


📄 Módulo de Cadastro de Usuário (menu_usuario.py)

Este módulo é responsável pelo cadastro e validação de usuários em um sistema bancário desenvolvido em Python.
Ele garante que os dados inseridos pelo usuário sejam válidos, consistentes e únicos, especialmente o e-mail, que não pode ser duplicado.


🎯 Objetivo do Módulo

- Coletar dados do usuário via terminal

- Validar idade mínima

- Validar formato e domínio do e-mail

- Impedir cadastro de e-mails duplicados


🧠 Funcionalidades
✅ Cadastro de Usuário

O cadastro solicita:

- Nome

- Idade

- E-mail

Todos os dados passam por validações antes de serem aceitos.


🔒 Validação de Idade

- Apenas usuários com 18 anos ou mais podem se cadastrar

- O sistema não permite avançar até que uma idade válida seja informada


📧 Validação de E-mail

- O e-mail informado deve:

- Pertencer ao domínio @gmail.com

- Estar em um formato válido (regex)

- Ter no máximo 100 caracteres

- Não estar cadastrado anteriormente

O sistema continua solicitando um novo e-mail até que todas as regras sejam atendidas.


🗂 Controle de E-mails Únicos

- Os e-mails cadastrados são armazenados em um set, garantindo:

- Alta performance na verificação

- Impedimento de cadastros duplicados

- Comparação ignorando letras maiúsculas e minúsculas


email_cadastrados = set()

🧩 Estrutura da Classe user
🔹 __init__

Inicializa o cadastro do usuário e armazena os dados em um dicionário:

self.user_data = {
    "Nome": ...,
    "Idade": ...,
    "Email": ...
}

🔹 validar_email(email)

Responsável por verificar:

- Domínio do e-mail

- Formato correto

- Limite de caracteres

Retorna o e-mail se for válido ou uma mensagem de erro.

🔹 validar_idade(idade)

- Verifica se o usuário tem pelo menos 18 anos


🔹 obter_idade_valida()

- Solicita a idade

- Trata erros de digitação

- Só permite avançar quando a idade for válida


▶️ Exemplo de Uso

usuario = user()
print(usuario.user_data)

🛠 Tecnologias Utilizadas

- Python 3

- Expressões Regulares (re)

- Programação Orientada a Objetos

- Estruturas de repetição

- Tratamento de exceções

📌 Observações

- Este módulo funciona em conjunto com outros arquivos do sistema bancário

- Ideal para projetos educacionais e aprendizado de validações

- Pode ser facilmente adaptado para uso com banco de dados

💰 Módulo de Gestão de Saldo (saldo.py)

Este módulo é responsável pelo controle e gerenciamento do saldo do usuário em um sistema bancário desenvolvido em Python.
Ele permite que o usuário deposite e saque valores, além de consultar o saldo atual por meio de um menu interativo no terminal.



🎯 Objetivo do Módulo

- Gerenciar o saldo do usuário

- Permitir depósitos e saques

- Impedir saques acima do saldo disponível

- Validar entradas numéricas

- Fornecer um menu simples e interativo


🧠 Funcionalidades
✅ Gestão de Saldo

O módulo apresenta um menu com as seguintes opções:

(1) Depositar saldo
(2) Sacar saldo
(3) Sair

O menu permanece ativo até o usuário escolher a opção de saída.



💵 Depósito de Saldo

- Permite adicionar valores positivos ao saldo

- Atualiza e exibe o saldo após o depósito

- Não aceita valores inválidos ou texto



🔒 Segurança e Validações

- Tratamento de erros com try/except

- Prevenção de saldo negativo

- Mensagens claras para entradas inválidas



🧩 Estrutura da Classe Saldo_user
🔹 __init__(saldo_inicial=0)

Inicializa o saldo do usuário.

self.saldo = saldo_inicial



🔹 gestao_saldo()

Exibe o menu de gestão de saldo e controla o fluxo das opções de depósito e saque.


🔹 depositar()

- Solicita um valor ao usuário

- Valida a entrada

- Soma o valor ao saldo

- Exibe o saldo atualizado


🔹 sacar()

- Solicita um valor ao usuário

- Valida a entrada

- Verifica se há saldo suficiente

- Subtrai o valor do saldo

- Exibe o saldo atualizado


▶️ Exemplo de Uso


saldo = Saldo_user()
saldo.gestao_saldo()


🛠 Tecnologias Utilizadas

Python 3

Programação Orientada a Objetos (POO)

Estruturas de repetição

Tratamento de exceções (try/except)



📌 Observações

-Este módulo funciona de forma integrada com o cadastro de usuários

- Ideal para projetos educacionais e aprendizado de lógica

- Pode ser facilmente adaptado para uso com banco de dados



📋 Módulo de Verificação e Exibição de Dados (verify.py)

Este módulo é responsável por exibir os dados do usuário e o saldo da conta em um sistema bancário desenvolvido em Python.
Ele centraliza a visualização das informações cadastradas, garantindo uma apresentação clara e organizada no terminal.


🎯 Objetivo do Módulo

- Exibir os dados pessoais do usuário

- Exibir o saldo atual da conta

- Centralizar a visualização das informações

- Facilitar a manutenção e organização do código



🧠 Funcionalidades
✅ Exibição de Dados do Usuário

O módulo apresenta:

- Nome do usuário

- Idade

- E-mail cadastrado

- Saldo atual da conta

As informações são exibidas apenas se os dados estiverem corretamente carregados.



🧩 Estrutura da Classe Verificar_dados

🔹 __init__(usuario, saldo)

Construtor da classe, responsável por:

- Receber o objeto do usuário

- Receber o objeto do saldo

- Armazenar essas informações internamente

self.usuario = usuario
self.saldo = saldo


🔹 exibir_dados()

Exibe no terminal todos os dados do usuário e o saldo atual da conta de forma organizada.

Exemplo de saída:

------- DADOS USUÁRIO -------

Nome   : João
Idade  : 25
E-mail : joao@gmail.com
Saldo  : R$ 1500.00



🛠 Tecnologias Utilizadas

- Python 3

- Programação Orientada a Objetos (POO)

- Manipulação de objetos e atributos



👨‍💻 Autor

Projeto desenvolvido para fins de aprendizado em Python, focando em lógica, boas práticas e organização de código.👨‍💻 Autor

Projeto desenvolvido para fins de aprendizado em Python, focando em lógica, boas práticas e organização de código.


