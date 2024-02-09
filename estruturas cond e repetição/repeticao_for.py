# for e while

texto = input('Informe um texto: ')
VOGAL = 'AEIOU'

for letra in texto: 
    if letra.upper() in VOGAL:
        print(letra, end='')

else:
    print()
    print('fim')

for numero in range(0, 51, 5):
    print(numero, end=" ")

