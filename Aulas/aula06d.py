n = float(input('Digite um valor: '))
print(n)

n = str(input('Digite um valor: '))
print(type(n))

n = bool(input('Digite um valor: '))
print(type(n))

# Aparece True se tiver algum valor lá dentro,
# senão vai aparecer False
n = bool(input('Digite um valor: '))
print(n)

n = input('Digite um valor: ')
print(type(n))

# Saber se o 'n' é numerico, se não for vai aparecer False
n = input('Digite um valor: ')
print(n.isnumeric())

# Saber se o 'n' é letra, se não for vai aparecer False
n = input('Digite um valor: ')
print(n.isalpha())

# Saber se o 'n' é alpha numerico, se não for vai aparecer False
n = input('Digite um valor: ')
print(n.isalnum())

# isupper - é para letras maiusculas
# islower - é para letras minusculas