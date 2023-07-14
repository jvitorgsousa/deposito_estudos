'''
Leia um valor inteiro N. Este valor será a quantidade de valores inteiros X que serão lidos em seguida.
Mostre quantos destes valores X estão dentro do intervalo [10,20] e quantos estão fora do intervalo, mostrando essas informações.
'''

N = int(input())

cont_in = cont_out = 0

for c in range(0, N):

    valor = int(input())
    
    if valor >= 10 and valor < 20:
        cont_in += 1
    else:
        cont_out +=1
        
print(f'{cont_in} in')
print(f'{cont_out} out')