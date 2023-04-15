# Aula 07 - Desafio 006
# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

#Eu
n1=int(input('Digite um valor: '))
n2=n1*2
n3=n1*3
n4=n1**(1/2)
print('O dobro de {} é {}, o triplo é {} e a raiz  quadrada é {:.2f}'.format(n1,n2,n3,n4))


#Guanabara
n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro de {} vale {}.'.format(n, d))
print('O triplo de {} vale {}. \nA raiz quadrada de {} vale {:.2f}.'.format(n, t, n, r))

# Outra forma
# n = int(input('Digite um número: '))
# print('O dobro de {} vale {}.'.format(n, (n*2)))
# print('O triplo de {} vale {}. \nA raiz quadrada de {} vale {:.2f}.'.format(n, (n*3), n,(n**1/2)))

# ou outra forma de calcular a raiz quadrada:
# print('O triplo de {} vale {}. \nA raiz quadrada de {} vale {:.2f}.'.format(n, (n*3), n, pow(n,(1/2))))



# ChatGPT
# num = float(input('Digite um número: '))
# dobro = num * 2
# triplo = num * 3
# raiz_quadrada = num ** 0.5
# print('O dobro de {} é {}'.format(num, dobro))
# print('O triplo de {} é {}'.format(num, triplo))
# print('A raiz quadrada de {} é {:.2f}'.format(num, raiz_quadrada))
