'''SORTEANDO UMA ORDEM NA LISTA'''

import random

aluno1 = input('Primeiro aluno: ')
aluno2 = input('Segundo aluno: ')
aluno3 = input('Terceiro aluno: ')
lista = [aluno1, aluno2, aluno3]
random.shuffle(lista)
print('A ordem é: ')
print(lista)
