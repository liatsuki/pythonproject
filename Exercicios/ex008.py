# Aula 07 - Desafio 008
# Escreva um programa que leia um valor em metros e exiba convertido em centrimetros e milimetros

#Eu
n = float(input('Uma distância em metros: '))
km = n / 1000
hm = n / 100
dam = n / 10
dm = n * 10
cm = n * 100
mm = n * 1000
print('A medida de {:.0f}m corresponde a : \n {:.0f}km \n {:.0f}hm \n {:.0f}dam \n {:.0f}dm \n {:.0f}cm \n {:.0f}mm'.format(n, km, hm, dam, dm, cm, mm))