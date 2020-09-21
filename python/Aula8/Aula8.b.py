'''CATETOS E HIPOTENUSA'''

from math import hypot

catetoO = float(input("Digite o valor do cateto oposto: "))
catetoA = float(input("Digite o valor do cateto adjacente: "))
hipotenusa = hypot(catetoO, catetoA)
print("O valor da hipotenusa é {:.2f}".format(hipotenusa))