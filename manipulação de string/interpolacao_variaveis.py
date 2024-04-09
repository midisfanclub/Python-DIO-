# metodo .format
nome = "alice"
idade = "24"
profissão = "estudante"
faculdade = "Senac"

print ("olá, meu nome é {}, tenho {} anos, sou {} no {}".format (nome, idade, profissão, faculdade))

print ("olá, meu nome é {0}, tenho {1} anos, sou {2} no {3}".format (nome, idade, profissão, faculdade))

# f strings
nome = "alice"
idade = "24"
profissão = "estudante"
faculdade = "Senac"

print (f"olá, meu nome é {nome}, tenho {idade} anos, sou {profissão} no {faculdade}.")

pi = 3.14159

print (f"Valor de PI: {pi:.2f}") # duas casas decimais depois da virgula

print (f"Valor de PI: {pi:10.2f}") # 10 espaços ("width") e duas casas depois da virgula

