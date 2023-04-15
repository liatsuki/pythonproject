n1 = int(input('Um valor: '))
n2 = int(input('Um valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, \n o produto é {} e a \n divisão é {:.3f}'.format(s,m, d), end=' >>> ')
print('Divisão inteira {} e potência {}'.format(di, e))

# {:.3f} por exemplo quero apenas com 3 casas decimais flutuantes
# para não quebrar os prints - end=' '
# Para quebrar - \n