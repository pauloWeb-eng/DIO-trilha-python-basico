LIMITE_DIARIO = 3
LIMITE_SAQUE = 500.0
AGENCIA = "0001"

usuarios = {}
contas = {}
saldo = 0.0
operacao = 0
deposito = 0.0
saque = 0.0
extrato = ""
mensagem = """
=========================Conta Bancária=========================

Por favor, digite a operação desejada
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Criar Usuário
    [5] Criar Conta
    [0] Sair
================================================================

"""
def criar_usuario(dicionario,nome,data,cpf,endereco):
    dicionario.setdefault(cpf,{"nome":nome,"data":data,"endereco":endereco})
    return dicionario
def criar_conta(dicionario,cpf,agencia):
    dicionario.setdefault((len(dicionario)+1),{"agencia":agencia,"cpf":cpf})
    return dicionario
def depositar(saldo, deposito,extrato):
    if(deposito>=0):
        saldo+=deposito
        print("Depósito efetuado com sucesso!\n")
        extrato=f"{extrato}\ndepósito: {deposito}"
    else:
        print("Valor de depósito inválido.\n")
    return saldo,extrato

def sacar(saque,saldo,limite_diario,limite_saque,extrato):
    if saque>=0:
        if saque<=saldo:
            if limite_diario<=3:
                if saque<=limite_saque:
                    saldo-=saque
                    print("Saque efetuado com sucesso!\n")
                    extrato =f"{extrato}\nsaque: {saque}"
                else:
                    print("Valor de saque superior ao limite permitido.")
            else:
                print("Número máximo de saques diários atingido.")
        else:
            print("Valor de saque maior que o saldo disponível.")
    else:
        print("Valor de saque inválido.")
    return saldo,extrato


def emitir_extrato(saldo,/,*,extrato):
    extrato = f"saldo: {saldo}\n{extrato}"
    print("Extrato".center(17,"#")+"\n"+extrato)

while True:
    print(mensagem)
    operacao = int(input("Operação: "))
    if(operacao == 1):
        deposito = float(input("Valor de Depósito: "))
        tupla=depositar(saldo,deposito,extrato)
        saldo,extrato=tupla[0],tupla[1]
    elif operacao == 2:
        saque = float(input("Valor de saque: "))
        tupla=sacar(saque=saque,saldo=saldo,limite_diario=LIMITE_DIARIO,limite_saque=LIMITE_SAQUE,extrato=extrato)
        saldo,extrato=tupla[0],tupla[1]
    elif operacao == 3:
        emitir_extrato(saldo,extrato=extrato)
    elif operacao == 4:
        nome = input("Digite seu nome: ")
        data = input("Digite sua data de nascimento: ")
        cpf = input("Digite seu CPF: ")
        endereco = input("Digite seu endereco: ")
        if(cpf in usuarios):
            print("Usuario já existe")
        else:
            dicionario= usuarios.copy()
            dicionario = criar_usuario(dicionario,nome,data,cpf,endereco)
            usuarios = dicionario.copy()
            print("Usuario criado!!")
    elif operacao == 5:
        cpf = input("Digite seu CPF: ")
        if(cpf in usuarios):
            dicionario = contas.copy()
            dicionario = criar_conta(dicionario,cpf,AGENCIA)
            contas = dicionario.copy()
            print("Conta criada!!!")
        else:
            print("Usuario não existe.")
    elif operacao == 0:
        break
    else:
        print("Operacão Inválida.")
print("Obrigado por utilizar nossos serviços!")
