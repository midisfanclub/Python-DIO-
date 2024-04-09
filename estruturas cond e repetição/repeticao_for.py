# for

# mostra as vogais de um texto
texto = input('Informe um texto: ')
VOGAL = 'AEIOU'

for letra in texto: 
    if letra.upper() in VOGAL:
        print(letra, end='')

else:
    print()
    print('fim')


#tabuada do 5
for numero in range(0, 51, 5):
    print(numero, end=" ") #end para ficar lado a lado nao em baixo

