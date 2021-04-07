print('--------------------------------------CONVERSOR------------------------------------------')  
real = float(input('Quanto você quer converter? R$'))
dolar = real / 5.61
print('R${:.2f} são US${:.2f} de dólar americano'.format(real, dolar))
