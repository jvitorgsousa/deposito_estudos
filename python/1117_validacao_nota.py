'''
-Faça um programa que leia as notas referentes às duas avaliações de um aluno. Calcule e imprima a média semestral. 
-Faça com que o algoritmo só aceite notas válidas (uma nota válida deve pertencer ao intervalo [0,10]). 
-Cada nota deve ser validada separadamente.Faça um programa que leia as notas referentes às duas avaliações de um aluno. 
-Calcule e imprima a média semestral. 
-Faça com que o algoritmo só aceite notas válidas (uma nota válida deve pertencer ao intervalo [0,10]). 
-Cada nota deve ser validada separadamente.

Se uma nota inválida  for lida, deve ser impressa a mensagem "nota invalida".
Quando duas notas válidas forem lidas, deve ser impressa a mensagem "media = " seguido do valor do cálculo. 
O valor deve ser apresentado com duas casas após o ponto decimal.
'''

soma = 0
cont = 0

while cont < 2:
  
  nota = float(input())

  if nota < 0 or nota > 10:
    print('nota invalida')
  else:
    cont += 1
    soma = nota + soma

print(f'media = {soma/cont}')
