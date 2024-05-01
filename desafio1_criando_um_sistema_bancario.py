LIMITE_DIARIO = 3
LIMITE_SAQUE = 500.0

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
    [0] Sair
================================================================

"""
while True:
    print(mensagem)
    operacao = int(input("Operação: "))
    if(operacao == 1):
        deposito = float(input("Valor de Depósito: "))
        if(deposito>=0):
            saldo+=deposito
            print("Depósito efetuado com sucesso!\n")
            extrato=f"{extrato}\ndepósito: {deposito}"
        else:
            print("Valor de depósito inválido.\n")
    elif operacao == 2:
        saque = float(input("Valor de saque: "))
        if saque>=0:
            if saque<=saldo:
                if LIMITE_DIARIO<=3:
                    if saque<=LIMITE_SAQUE:
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
    elif operacao == 3:
        extrato = f"saldo: {saldo}\n{extrato}"
        print("Extrato".center(17,"#")+"\n"+extrato)
    elif operacao == 0:
        break
    else:
        print("Operacão Inválida.")
print("Obrigado por utilizar nossos serviços!")