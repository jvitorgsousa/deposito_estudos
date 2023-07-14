'''
Escreva um algoritmo que leia 2 valores inteiros X e Y calcule a soma dos números que não são múltiplos de 13 entre X e Y, incluindo ambos.
'''

X = int(input())
Y = int(input())

soma = 0

if X > Y:
    for c in range(Y, X+1):
        if c % 13 != 0:
            soma += c
else:
    for c in range(X, Y+1):
        if c % 13 != 0:
            soma += c
            
print(soma)