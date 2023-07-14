'''
Faça um programa que leia 5 valores inteiros. 
Conte quantos destes valores digitados são pares e mostre esta informação.
'''

cont = 0

for c in range(1, 6):
  
  value = int(input())
  
  if value % 2 == 0:
    cont += 1

print(f'{cont} valores pares')