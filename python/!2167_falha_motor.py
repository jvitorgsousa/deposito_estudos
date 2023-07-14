'''
A entrada é um teste do motor e é dada em duas linhas. A primeira tem o número N de medidas de velocidade do motor (1 < N ≤ 100). 
A segunda linha tem N inteiros: o número de RPM (rotações por minuto) Ri de cada medida (0 ≤ Ri ≤ 10000, para todo Ri, tal que 1 ≤ i ≤ N). 
Uma medida é considerada uma queda se é menor que a medida anterior.
'''

def check_queda(lista, tamanho):
    maior = 0 
    for c in range(tamanho):
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < maior:
            return c
    return 0

# programa principal

tamanho = int(input())

lista = input().split()
for i in range(tamanho):
  lista[i] = int(lista[i])

queda = check_queda(lista,tamanho)
if queda > 0:
    print(queda+1)
else:
    print(queda)