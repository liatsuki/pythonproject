# Aula 07 - Desafio 009
# Faça um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada

#Eu
num=int(input('Escolha uma tabuada: '))
n1=num*1
n2=num*2
n3=num*3
n4=num*4
n5=num*5
n6=num*6
n7=num*7
n8=num*8
n9=num*9
n10=num*10
print('{} x 1 = {}'.format(num, n1))
print('{} x 2 = {}'.format(num, n2))
print('{} x 3 = {}'.format(num, n3))
print('{} x 4 = {}'.format(num, n4))
print('{} x 5 = {}'.format(num, n5))
print('{} x 6 = {}'.format(num, n6))
print('{} x 7 = {}'.format(num, n7))
print('{} x 8 = {}'.format(num, n8))
print('{} x 9 = {}'.format(num, n9))
print('{} x 10 = {}'.format(num, n10))


#Guanabara
num=int(input('Digite um número para ver sua tabuada: '))
print('='*12)
print('{} x {:<2} = {}'.format(num, 1, num*1))
print('{} x {:<2} = {}'.format(num, 2, num*2))
print('{} x {:<2} = {}'.format(num, 3, num*3))
print('{} x {:<2} = {}'.format(num, 4, num*4))
print('{} x {:<2} = {}'.format(num, 5, num*5))
print('{} x {:<2} = {}'.format(num, 6, num*6))
print('{} x {:<2} = {}'.format(num, 7, num*7))
print('{} x {:<2} = {}'.format(num, 8, num*8))
print('{} x {:<2} = {}'.format(num, 9, num*9))
print('{} x {:<2} = {}'.format(num, 10, num*10))
print('='*12)
