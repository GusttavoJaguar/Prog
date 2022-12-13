from random import randint
n  = int (randint(1,10))
p = 0
t = 0
print ("         ----------ADIVINHE O NÚMERO----------")
print ("")
sair = False

while sair == False:

  while p != n:
  	p = int(input("Chute um número de 1 à 100: "))
  	t += 1
  	if p == n:
  		print("ACERTOU!!! Placar %i" % t)
  	elif p < n:
  		print("Chute um valor maior")
  	else:
  		print("Chute um valor menor")

acao = input("Deseja sair do jogo? (S/N) ")
if acao == "s":
	sair = True
