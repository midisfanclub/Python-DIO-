saldo = 2000
saque = int(input('Digite o valor a ser sacado: '))

status = 'Sucesso' if saque <= saldo else 'Falha'

print(f'{status} ao realizar o saque!')