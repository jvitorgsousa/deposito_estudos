'''
Escreva um algoritmo para calcular e escrever o valor de S, sendo S dado pela fórmula:
S = 1 + 3/2 + 5/4 + 7/8 + ... + 39/?
'''

x = 0
y = 1

for c in range(1,40, 2):
    x = (x + c / y)
    y = y * 2
    
print(f'{x:.2f}')