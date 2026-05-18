import textwrap
from desafioClasses import Cliente, PessoaFisica, Conta, ContaCorrente, Historico, Transacao, Deposito, Saque


def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n---> Cliente não tem conta! <---")
        return None
    return cliente.contas[0]


def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n---> Cliente não encontrado! <---")
        return

    valor = float(input("Informe o valor do depósito: "))
    conta = recuperar_conta_cliente(cliente)

    if not conta:
        return

    cliente.realizar_transacao(conta, Deposito(valor))


def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n---> Cliente não encontrado! <---")
        return

    valor = float(input("Informe o valor do saque: "))
    conta = recuperar_conta_cliente(cliente)

    if not conta:
        return

    cliente.realizar_transacao(conta, Saque(valor))


def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n---> Cliente não encontrado! <---")
        return

    conta = recuperar_conta_cliente(cliente)

    if not conta:
        return

    print("\n================ EXTRATO =================")
    transacoes = conta.historico.transacoes

    if not transacoes:
        print("Não existem movimentações.")
    else:
        for transacao in transacoes:
            print(f"{transacao['tipo']}:\tR$ {transacao['valor']:.2f}")

    print(f"\nSaldo:\t\tR$ {conta.saldo:.2f}")
    print("==========================================")


def criar_usuario(clientes):
    cpf = input("Informe o CPF (somente número): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\n---> CPF já existe no sistema! <---")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
    clientes.append(cliente)

    print("=== Usuário criado com sucesso! ===")


def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do usuário: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n---> Usuário não encontrado, tente novamente! <---")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.adicionar_conta(conta)

    print("\n=== Conta criada com sucesso! ===")


def listar_contas(contas):
    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))


def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            depositar(clientes)

        elif opcao == "s":
            sacar(clientes)

        elif opcao == "e":
            exibir_extrato(clientes)

        elif opcao == "nu":
            criar_usuario(clientes)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, selecione o menu corretamente.")


main()
