'''
Faça um programa que leia um vetor A[100]. 
No final, mostre todas as posições do vetor que armazenam um valor menor ou igual a 10 e o valor armazenado em cada uma das posições.
'''

size = 100
A = [0] * size

for i in range(0, size):
    valor = float(input())
    A[i] = valor

for c in range(0, size):
    if A[c] <= 10:
        print(f'A[{c}] = {A[c]}')