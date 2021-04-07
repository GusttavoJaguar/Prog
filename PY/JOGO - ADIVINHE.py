# -*- coding: utf-8 -*-
"""
Jogo de adivinhação
Autor: Science - Soluções de T.I.
Função: Adivinhar o número que a máquina escolheu

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
