'''
Leia um caractere maiúsculo, que indica uma operação que deve ser realizada e uma matriz M[12][12]. 
Em seguida, calcule e mostre a soma ou a média considerando somente aqueles elementos que estão na área superior da matriz.
'''

def matriz_base(linha, coluna):
    matriz = []
    for l in range(linha):
        matriz.append([0] * coluna)
    return matriz

def matriz_valores(matriz, linha, coluna):
    for l in range(linha):
        for c in range(coluna):
            matriz[l][c] = float(input())

# programa principal

linha = coluna = 12
matriz = matriz_base(linha, coluna)

resposta = input()

matriz_valores(matriz, linha, coluna)

soma = quant = 0

for l in range(5):
    for c in range(l+1, 11-l):
        soma = soma + matriz[l][c]
        quant = quant + 1

if resposta.upper() == 'S':
    print(f'{soma:.1f}')
elif resposta.upper() == 'M':
    print(f'{(soma)/quant:.1f}')
