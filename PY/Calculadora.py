# -*- coding: utf-8 -*-
"""
Calculadora
Autor: Science - Soluções de T.I.
Função: Fazer cálculos de soma, subtração, multiplicação e divisão

"""
print("----------Calculadora----------")

sair = False

while sair == False:

	num1 = input("Digite o primeiro número: ")
	num1 = int(num1)
	operador = input("Digite um operador (+-*/): ")
	num2 = input("Digite o segundo valor: ")
	num2 = int(num2)

	#soma +
	if operador == "+":
		operacao = num1 + num2

	#subtração -
	if operador == "-":
		operacao = num1 - num2

	#multiplicação *
	if operador == "*":
		operacao = num1 * num2

	#divisão /
	if operador == "/":
		operacao = num1 / num2

	#resultado
	print("Resultado: ")
	print(operacao)

	botao = input("Deseja sair? (S/N)")
	if botao == "s":
		sair = True
