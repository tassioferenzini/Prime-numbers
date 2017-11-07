# -*- coding: utf-8 -*-
from math import sqrt

arquivo = open('primos.txt', 'w')
#arquivo.write("Primos:\n2 \n")
numero = 3
primos = [2,]
while (True):
    ehprimo = 1
    for i in primos:
        if numero % i == 0:
            ehprimo = 0
            break
        if i > sqrt(numero):
            break
    if (ehprimo):
        primos.append(numero)
        arquivo.write(str(numero) + "\n")
    numero=numero+1
