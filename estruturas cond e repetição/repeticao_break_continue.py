while True:
    numero = int(input('Digite um número: '))

    if numero == 10:
        print('Parabéns você acertou!')
        break
        
    if numero % 2 == 0:
        continue
    
    print(numero)


    