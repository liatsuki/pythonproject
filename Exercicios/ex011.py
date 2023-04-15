# Aula 07 - Desafio 011
# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m^2

#Eu
largura=float(input('Introduza a largura: '))
altura=float(input('Introduza a altura: '))
area=largura*altura
quant_tinta=area/2
print('Com uma largura de {} e com uma altura de {}, a área será de {}'.format(largura, altura, area))
print('Quantidade de tinta necessária:', quant_tinta)