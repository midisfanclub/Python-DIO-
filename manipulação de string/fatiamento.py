nome = "Guilherme Arthur de Carvalho"

nome [0] # G
nome [:9] #  Guilherme
nome [10:] # Arthur de Carvalho
nome [10:16] # Arthur
nome [10:16:2] # de 2 em 2 --> Atu
nome [:] # Guilherme Arthur de Carvalho
nome [::-1] # ohlavraC ed ruhtrA emrehliuG
nome [-1] # ultima letra --> o

print (nome [::-1])

