'''
Leia uma quantidade indeterminada de duplas de valores inteiros X e Y. 
Escreva para cada X e Y uma mensagem que indique se estes valores foram digitados em ordem crescente ou decrescente.

O Programa deve ser encerrado quando X == Y.
'''

entrada = input()

X, Y = entrada.split()
X = int(X)
Y = int(Y)

while X != Y:
  
  if X > Y:
    print('Decrescente')
  else:
    print('Crescente')
 
  entrada = input()
  X, Y = entrada.split()
  X = int(X)
  Y = int(Y)

