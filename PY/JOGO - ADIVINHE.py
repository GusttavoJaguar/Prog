# -*- coding: utf-8 -*-
"""
Calculadora
Autor: Science - Soluções de T.I.
Função: Fazer cálculos de soma, subtração, multiplicação e divisão

"""

from random import randint
n  = int (randint(1,10))
p = 0
t = 0
sair = False

print ("----------ADIVINHE----------")


	while p != n == False:
		p = int(input("Chute um número de 1 à 10: "))
		t += 1
		if p == n:
			print("ACERTOU!!! Placar %i" % t)
		elif p < n:
			print("Chute um valor maior")
		else:
			print("Chute um valor menor")
		print("FIM DO JOGO")

botao = input("Deseja sair? (S/N)")
	if botao == "s":
		sair = True