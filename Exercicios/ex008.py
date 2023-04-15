# Aula 07 - Desafio 008
# Escreva um programa que leia um valor em metros e exiba convertido em centrimetros e milimetros

#Eu
n1=float(input('Valor em metros: '))
cent=n1*100
mili=n1*1000
print('O valor em metros é de {}, convertido em centimetros é de {} e em milimetros é de {}'.format(n1,cent,mili))