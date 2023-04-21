# Aula 07 - Desafio 013
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

#Eu
n1=float(input('Salário: '))
aum=n1+(n1*0.15)
print('O salário de {}€ com um aumento de 15% de aumento é de {}€'.format(n1, aum))

#Guanabara
salário = float(input('Salário: '))
novo = salário + (salário * 15 / 100)
print('Um funcionário que ganhava {:.2f}€, com 15% de aumento, passa a receber {:.2f}€'.format(salário, novo))