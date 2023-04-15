# Aula 07 - Desafio 011
# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m^2

#Eu
largura=float(input('Largura da parede: '))
altura=float(input('Altura da parede: '))
area=largura*altura
quant_tinta=area/2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m2'.format(largura, altura, area))
print('Para pintar essa parede, você precisará de {}l de tinta'.format(quant_tinta))