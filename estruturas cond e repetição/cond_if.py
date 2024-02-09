saldo = 2000.00
saque = float(input('Informe o valor do saque: '))

if saldo >= saque:
    print('Sacando...')

elif saldo < 0:
    print('Saldo negativo, não é possível completar o saque')

else:
    print('Saldo insuficiente!') 

