'''
Neste problema você deve ler um número, indicando uma linha da matriz na qual uma operação deve ser realizada, um caractere maiúsculo, 
indicando a operação que será realizada, e todos os elementos de uma matriz M[12][12]. 
Em seguida, calcule e mostre a soma ou a média dos elementos que estão na área verde da matriz, conforme for o caso.
A imagem abaixo ilustra o caso da entrada do valor 2 para a linha da matriz, demonstrando os elementos que deverão ser considerados na operação.
'''

def matriz_esqueleto(linha,coluna):
    matriz = []
    for l in range(linha):
        matriz.append([0] * coluna)
    return matriz

def criar_matriz(matriz, linha, coluna):
    for l in range(linha):
        for c in range(coluna):
            matriz[l][c] = float(input())

def soma_linha(matriz, linha_esp, linha, coluna):
    soma = 0
    for l in range(linha):
        if l == linha_esp:
            for c in range(coluna):
                soma = soma + matriz[l][c]
    return soma

# Base do programa começa aqui

linha = coluna = 12
matriz = matriz_esqueleto(linha, coluna)

linha_esp = int(input())
resposta_calculo = input()

criar_matriz(matriz, linha, coluna)

if resposta_calculo.upper() == 'S':
    calc = soma_linha(matriz, linha_esp, linha, coluna)
elif resposta_calculo.upper() == 'M':
    calc = (soma_linha(matriz, linha_esp, linha, coluna) / linha)

print(f'{calc:.1f}')