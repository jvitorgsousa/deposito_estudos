'''
A primeira linha contém um inteiro T representando o tipo de chá (1 ≤ T ≤ 4). 
A segunda linha contém cinco inteiros A, B, C, D e E, que indica a resposta dada por cada competidor (1 ≤ A, B, C, D, E ≤ 4).
'''

tea = int(input())

lista_pessoas = input().split()

count_acertos = 0
for c in range(5):
    lista_pessoas[c] = int(lista_pessoas[c])
    if lista_pessoas[c] == tea:
        count_acertos += 1

print(count_acertos)