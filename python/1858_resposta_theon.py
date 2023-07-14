'''
Theon pode dizer que seu algoz é alguma dentre N pessoas. 
Considere que as pessoas são numeradas de 1 a N. 
Se Theon responder que seu algoz é a pessoa i, Ramsay irá atingi-lo Ti vezes.
'''

num = int(input())

entry = input().split()

for c in range(num):
    entry[c] = int(entry[c])

print(entry.index(min(entry)) + 1)