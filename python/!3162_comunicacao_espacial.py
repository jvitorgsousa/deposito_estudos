'''
A primeira linha da entrada possui um número inteiro N (2 <= N <= 10), que representa o número de naves no espaço a ser analisado. 
As N linhas seguintes receberão 3 valores inteiros, separados por espaço, indicando as coordenadas discretas x, y e z de cada nave.
'''

import math 

def naves(testes):
    lista = [0] * testes
    return lista 

def coordenadas(lista, testes):
    for c in range(testes):
        val = input().split()
        for r in range(3):
            val[r] = int(val[r])
        lista[c] = val
    
r = int(input())
lista = naves(r)
coordenadas(lista, r)

# programa

x = 0

resultado = []
for c in range(r):
    for j in range(r):
        
        distancia = math.sqrt((lista[j][0] - lista[x][0])**2 + (lista[j][1] - lista[x][1])**2 + (lista[j][2] - lista[x][2])**2)
        
        if x != j:
            resultado.append(distancia)

    sinal = min(resultado)

    if sinal <= 20:
        print('A')
    elif sinal > 20 and sinal <= 50:
        print('M')
    elif sinal > 50:
        print('B')

    resultado = []
    x += 1
