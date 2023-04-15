# Aula 07 - Desafio 005
# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

#Eu
n1 = int(input('Digite um valor: '))
print(n1-1,n1,n1+1)


#ChatGPT
num = int(input('Digite um número inteiro: '))
antecessor = num - 1
sucessor = num + 1
print('O antecessor de {} é {} e seu sucessor é {}'.format(num, antecessor, sucessor))
