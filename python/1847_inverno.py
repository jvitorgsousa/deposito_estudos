'''
Se a temperatura desceu do 1º para o 2º dia, mas subiu ou permaneceu constante do 2º para o 3º, as pessoas ficam felizes.
Se a temperatura subiu do 1º para o 2º dia, mas desceu ou permaneceu constante do 2º para o 3º, as pessoas ficam tristes.
Se a temperatura subiu do 1º para o 2º dia e do 2º para o 3º, mas subiu do 2º para o 3º menos do que subira do 1º para o 2º, as pessoas ficam tristes.
Se a temperatura subiu do 1º para o 2º dia e do 2º para o 3º, mas subiu do 2º para o 3º no mínimo o tanto que subira do 1º para o 2º, as pessoas ficam felizes.
Se a temperatura desceu do 1º para o 2º dia e do 2º para o 3º, mas desceu do 2º para o 3º menos do que descera do 1º para o 2º, as pessoas ficam felizes.
Se a temperatura desceu do 1º para o 2º dia e do 2º para o 3º, mas desceu do 2º para o 3º no mínimo o tanto que descera do 1º para o 2º, as pessoas ficam tristes.
Se a temperatura permaneceu constante do 1º para o 2º dia, as pessoas ficam felizes se subiu do 2º para o 3º dia ou tristes caso contrário.
'''

A, B, C = input().split()

A = int(A)
B = int(B)
C = int(C)

if A > B and B <= C:
     print(':)')

elif A < B and B >= C:
    print(':(')

elif A < B and B < C and (B - A) > (C - B):
    print(':(')

elif A < B and B < C and (C - B) >= (B - A):
     print(':)')

elif A > B and B > C and (A - B) > (B - C):
     print(':)')

elif A > B and B > C and (A - B) >= (B - C):
     print(':(')

elif A == B and B < C:
     print(':)')

elif A == B and B > C:
     print(':(')

else:
    print(':(')

