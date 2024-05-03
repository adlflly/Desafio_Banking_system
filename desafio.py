
def menu():
    menu = """\n
    —————————— MENU ——————————
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNovo usuário
    [5]\tNova conta
    [0]\tSair
    →  """
    return input((menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
          saldo += valor 
          extrato += f"\tDepósito: R$ {valor:.2f}\n"
          print("\n‖‖ Depósito realizado com sucesso ‖‖")

    else:
          print("Operação invalida, verifique o valor informado.")

    return saldo, extrato 


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print("Não é possivel realizar o saque, Você não tem saldo suficiente.")

        elif excedeu_limite: 
            print("Não é possivel realizar o saque, O valor do saque excede o limite")

        elif excedeu_saques:
            print("Não é possivel realizar o saque, Número de saques diários excedido")
        
        elif valor > 0:
            saldo -= valor 
            extrato += f"\tSaque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("‖‖ Saque realizado com sucesso! ‖‖")

        else:
            print("Operação invalida, verifique o valor informado")

        return saldo, extrato



def exibir_extrato(saldo, /, *, extrato):
        print("\n—————————— Extrato ——————————")
        print("Nenhuma movimentação realizada." if not extrato else extrato)
        print(f"\n\tSaldo: R$ {saldo:.2f}")
        print("———————————————————————————————")

def criar_usuario(usuarios):
    cpf = input("Informe o cpf(Apenas os números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
          print("\nEste cpf está atribuído a um usuário Existente!")
          return
    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Informe sua data de nascimento(dd-mm-aaaa): ")
    endereco = input("Iforme seu endereço(Rua - numero - bairo - cidade/sigla do estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("‖‖ Usuário registrado com sucesso! ‖‖")


def filtrar_usuario(cpf, usuarios):
     usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
     return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe seu CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n‖‖ Conta criada com sucesso! ‖‖")

        return {"agencia": agencia, "numero_conta": numero_conta,"usuario": usuario}
     
    print("\nUsuario não encontrado! Verifique seu CPF ou crie um usuário!")




def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: ")) 
            
            saldo, extrato = depositar(saldo, valor, extrato)


        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
        elif opcao == "3":
             exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
             criar_usuario(usuarios)
        elif opcao == "5":
             numero_conta = len(contas) + 1
             conta = criar_conta(AGENCIA, numero_conta, usuarios)

             if conta:
                  contas.append(conta)
        elif opcao == "0":
             break 
        
        else:
             print("Opção invalida, digite novamente a opção desejada.")

main()
    