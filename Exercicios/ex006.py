# Aula 07 - Desafio 006
# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

#Eu
n1=int(input('Digite um valor: '))
n2=n1*2
n3=n1*3
n4=n1**(1/2)
print('O dobro de {} é {}, o triplo é {} e a raiz  quadrada é {}'.format(n1,n2,n3,n4))


#ChatGPT
num = float(input('Digite um número: '))
dobro = num * 2
triplo = num * 3
raiz_quadrada = num ** 0.5
print('O dobro de {} é {}'.format(num, dobro))
print('O triplo de {} é {}'.format(num, triplo))
print('A raiz quadrada de {} é {:.2f}'.format(num, raiz_quadrada))
