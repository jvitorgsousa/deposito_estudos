'''
Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente, de modo que o lado A representa o maior dos 3 lados.
A seguir, determine o tipo de triângulo que estes três lados formam,
'''

entrada = input()

A, B, C = entrada.split()
A = float(A)
B = float(B)
C = float(C)

ordem = [A, B, C]
ordem.sort(reverse=True)

A = ordem[0]
B = ordem[1]
C = ordem[2]

if A >= B + C:
    print('NAO FORMA TRIANGULO')
else:
    if A**2 == B**2 + C**2:
        print('TRIANGULO RETANGULO')
    elif A**2 > B**2 + C**2:
        print('TRIANGULO OBTUSANGULO')
    elif A**2 < B**2 + C**2:
        print('TRIANGULO ACUTANGULO')

if A == B == C:
    print('TRIANGULO EQUILATERO')
elif A == B != C or A == C != B or B == C != A:
    print('TRIANGULO ISOSCELES')