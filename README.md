# 🏦 Sistem_Banco_py

Sistema bancário simples desenvolvido em Python, executado via terminal. Permite cadastro de usuários, gestão de saldo e visualização de dados da conta.

> Projeto criado para praticar lógica de programação, orientação a objetos e validações básicas em Python.

---

## 🚀 Funcionalidades

- ✅ Cadastro de usuário com validação de dados
- ✅ Validação de idade mínima (18 anos)
- ✅ Validação de e-mail (formato, domínio e duplicidade)
- ✅ Depósito de saldo
- ✅ Saque de saldo (com verificação de saldo disponível)
- ✅ Consulta de saldo atual
- ✅ Visualização completa dos dados do usuário
- ✅ Menu interativo no terminal
- ✅ Tratamento de erros de entrada

---

## 📁 Estrutura do Projeto

```
projeto_banco/
│
├── main.py           # Arquivo principal (menu do sistema)
├── menu_usuario.py   # Cadastro e validação do usuário
├── saldo.py          # Gestão de saldo (depósito e saque)
├── verify.py         # Exibição dos dados do usuário
└── README.md         # Documentação do projeto
```

---

## ▶️ Como Executar

**Pré-requisito:** Python 3.10 ou superior instalado.

```bash
python main.py
```

---

## 🧠 Como o Sistema Funciona

Ao iniciar, o usuário vê o menu principal:

```
(1) Cadastrar usuário
(2) Gestão de saldo
(3) Verificar saldo da conta
(4) Ver todos os dados do usuário
(5) Sair
```

### 🔹 Cadastro de Usuário
O sistema solicita nome, idade e e-mail. Todos os dados passam por validação antes de serem aceitos e o saldo é iniciado automaticamente.

### 🔹 Gestão de Saldo
Submenu com as opções de depositar ou sacar saldo.

### 🔹 Segurança
- Acesso ao saldo exige cadastro prévio
- Saque bloqueado se valor exceder o saldo disponível
- Entradas inválidas são tratadas com `try/except`

---

## 📄 Módulos

### `menu_usuario.py` — Cadastro de Usuário

Responsável pelo cadastro e validação de dados. Garante que as informações sejam válidas, consistentes e únicas.

| Método | Descrição |
|---|---|
| `__init__` | Inicializa o cadastro e armazena os dados em um dicionário |
| `validar_email(email)` | Verifica domínio `@gmail.com`, formato (regex), limite de 100 chars e duplicidade |
| `validar_idade(idade)` | Confirma se o usuário tem 18 anos ou mais |
| `obter_idade_valida()` | Solicita a idade em loop até receber um valor válido |

> E-mails cadastrados são armazenados em um `set` — alta performance e sem duplicatas (case-insensitive).

---

### `saldo.py` — Gestão de Saldo

Controla o saldo do usuário com um menu interativo.

| Método | Descrição |
|---|---|
| `__init__(saldo_inicial=0)` | Inicializa o saldo |
| `gestao_saldo()` | Exibe o menu de depósito e saque |
| `depositar()` | Valida e soma o valor ao saldo |
| `sacar()` | Valida, verifica disponibilidade e subtrai o valor do saldo |

---

### `verify.py` — Verificação de Dados

Centraliza a exibição das informações do usuário.

| Método | Descrição |
|---|---|
| `__init__(usuario, saldo)` | Recebe os objetos de usuário e saldo |
| `exibir_dados()` | Exibe nome, idade, e-mail e saldo no terminal |

**Exemplo de saída:**
```
------- DADOS USUÁRIO -------
Nome   : João
Idade  : 25
E-mail : joao@gmail.com
Saldo  : R$ 1500.00
```

---

## 🛠️ Tecnologias Utilizadas

- Python 3
- Programação Orientada a Objetos (POO)
- Expressões Regulares (`re`)
- Estruturas de repetição
- Tratamento de exceções (`try/except`)

---

## 👨‍💻 Autor

Projeto desenvolvido para fins de aprendizado em Python, com foco em lógica, boas práticas e organização de código.