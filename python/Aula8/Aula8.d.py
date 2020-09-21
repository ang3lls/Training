'''SORTEANDO UM ITEM NA LISTA'''

import random

aluno1 = input('Primeiro aluno: ')
aluno2 = input('Segundo aluno: ')
aluno3 = input('Terceiro aluno: ')
aluno4 = input('Quarto aluno: ')
aluno5 = input('Quinto aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4, aluno5]
x = random.choice(lista)
print('O escolhido foi {}'.format(x))
