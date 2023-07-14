'''
Escreva um programa que leia um valor inteiro N. 
Este N é a quantidade de linhas de saída que serão apresentadas na execução do programa.
'''

N = int(input())
pum = 1

for c in range (1, N+1):
    print(f'{pum} {pum+1} {pum+2} PUM')
    pum += 4