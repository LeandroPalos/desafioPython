# Sistema Bancário em Python (POO)

Sistema bancário simples em linha de comando, implementado em Python com **Programação Orientada a Objetos**. Demonstra herança, classes abstratas, encapsulamento (properties) e composição.

## Funcionalidades

Aplicação CLI com menu interativo. Permite:

- Cadastrar usuários (CPF, nome, data de nascimento, endereço)
- Criar contas correntes associadas a um usuário
- Listar todas as contas
- Realizar **depósitos** e **saques** (com limite de valor por saque e limite de saques diários)
- Exibir o **extrato** da conta com histórico de transações
- Validar saldo insuficiente, valor inválido e limite excedido

## Stack

- Python 3 (sem dependências externas — usa apenas `abc`, `datetime` e `textwrap` da stdlib)

## Estrutura

```
desafioPython/
├── desafioClasses.py        # definição das classes do domínio
├── desafioExtraClasses.py   # CLI com menu e fluxo principal
├── .gitignore
└── README.md
```

## Modelagem (classes)

```
Cliente (base)
└── PessoaFisica            # adiciona nome, cpf, data_nascimento

Conta (base)
└── ContaCorrente           # adiciona limite e limite de saques

Transacao (ABC)
├── Deposito
└── Saque

Historico                   # mantém a lista de transações da conta
```

- Um `Cliente` pode ter várias `Conta`s.
- Uma `Conta` tem um `Historico` (composição).
- `Deposito` e `Saque` implementam a interface `Transacao` (ABC) e sabem se aplicar a uma `Conta`.

## Como rodar

```bash
git clone https://github.com/LeandroPalos/desafioPython.git
cd desafioPython
python desafioExtraClasses.py
```

## Menu da aplicação

```
================ MENU ================
[d]   Depositar
[s]   Sacar
[e]   Extrato
[nc]  Nova conta
[lc]  Listar contas
[nu]  Novo usuário
[q]   Sair
```

## Fluxo de uso típico

1. `[nu]` Cadastrar um usuário (CPF, nome, data de nascimento, endereço)
2. `[nc]` Criar uma conta para esse usuário (informa o CPF)
3. `[d]` Depositar um valor na conta
4. `[s]` Sacar um valor (respeitando limite e quantidade de saques)
5. `[e]` Conferir o extrato
