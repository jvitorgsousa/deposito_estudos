'''
A entrada é composta de vários casos de testes. 
Cada caso é composto por um inteiro N (0<=N<=200) que indica o valor dos últimos N números da sequência.

A entrada termina com final de arquivo (EOF).
'''

def odeio_beecrowd(size):
    lista = [0]

    if size == 0:
        return lista

    for c in range(size+1):
        for i in range(c):
            lista.append(c)
    
    return lista

# programa

count = 1

N = int(input())
while True:
    try:
        lista = odeio_beecrowd(N)
        nums = ''

        if len(lista) == 1:
            nums = 'numero'
        else:
            nums = 'numeros'

        print(f'Caso {count}: {len(lista)} {nums}')        

        for c in range(len(lista)):
            if c == len(lista) - 1:
                print(lista[c])
            else:
                print(lista[c],end=' ')
        
        print()        
        count += 1

        N = int(input())
    except:
        break