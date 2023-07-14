'''
Faça um programa que leia um vetor X[10]. 
Substitua a seguir, todos os valores nulos e negativos do vetor X por 1. 
Em seguida mostre o vetor X.
'''

X = [0] * 10

for c in range(0, 10):

    valor = int(input())

    if valor <= 0:
        valor = 1

    X[c] = valor
    
    print(f'X[{c}] = {X[c]}')