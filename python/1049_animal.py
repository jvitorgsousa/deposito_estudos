'''
Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo o esquema abaixo(anexado no site), da esquerda para a direita.  
Em seguida conclua qual dos animais seguintes foi escolhido, através das três palavras fornecidas.
'''

tipo1 = str(input())
tipo2 = str(input())
tipo3 = str(input())

# Aves
if tipo1 == 'vertebrado' and tipo2 == 'ave' and tipo3 == 'carnivoro':
    print('aguia')

if tipo1 == 'vertebrado' and tipo2 == 'ave' and tipo3 == 'onivoro':
    print('pomba')

# Mamíferos 
if tipo1 == 'vertebrado' and tipo2 == 'mamifero' and tipo3 == 'onivoro':
    print('homem')
if tipo1 == 'vertebrado' and tipo2 == 'mamifero' and tipo3 == 'herbivoro':
    print('vaca')
    
# Insetos
if tipo1 == 'invertebrado' and tipo2 == 'inseto' and tipo3 == 'hematofago':
    print('pulga')
if tipo1 == 'invertebrado' and tipo2 == 'inseto' and tipo3 == 'herbivoro':
    print('lagarta')

# Anelídeos 
if tipo1 == 'invertebrado' and tipo2 == 'anelideo' and tipo3 == 'hematofago':
    print('sanguessuga')
if tipo1 == 'invertebrado' and tipo2 == 'anelideo' and tipo3 == 'onivoro':
    print('minhoca')