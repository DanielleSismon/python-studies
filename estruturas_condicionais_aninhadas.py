conta_normal = True
conta_universitaria = False

saldo = 2000
saque = 1500
cheque_especial = 500

if conta_normal:
    if saldo >= saque:
        print('Saque realizado com sucesso!')
    elif saque <= (saldo + cheque_especial):
        print('Saque realizado com uso de seu Cheque Especial!')
    else:
        print('Não foi possível realizar o saque, saldo insuficiente!')
elif conta_universitaria:
    if saldo >= saque:
        print('Saque realizado com sucesso!')
    else:
        print('Saldo insuficiente!')
else:
    print('Desculpe, não foi reconhecido seu tipo de conta. Por favor, entre em contato com seu gerente.')            