saldo = 1000
saque = 200 
limite = 500

print(saldo >= saque and saque <= limite)

print (saldo >= saque or saque <= limite)

print(not (saldo >= saque or saque <= limite))

print(not saldo >= saque or saque <= limite)

print((saldo >= saque and saque <= limite) or (saldo >= saque and saque <= limite))

saldo_aceito = (saldo > saque)
limite_aceito = (saque < limite)
saque_aceito = saldo_aceito and limite_aceito
print(saque_aceito)
