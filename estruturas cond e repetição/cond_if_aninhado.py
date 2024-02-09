saque = float(input('Digite o valor que deseja sacar: '))
saldo = 200
tipo_conta = input('Sua conta é normal ou universitária?\n')
cheque_especial = 200


if tipo_conta == 'normal':
    if saldo >= saque:
        print('Sacando...')
    elif saque <= saldo + cheque_especial :
        print("Sacando do cheque especial")
    else: 
        print('Saldo insuficiente')

elif tipo_conta == 'universitária' or 'universitaria':
    if saldo >= saque:
        print('Sacando...')
    else: 
        print('Saldo insuficiente!')

else:
    print('O sistema não reconheceu esse tipo de conta')
