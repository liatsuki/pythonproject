# Aula 07 - Desafio 010
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

n1=float(input('Valor em euros: '))
s=n1*1455.188
print('O valor convertido para won é de {}'.format(s))


#valor arrendondado - chatgpt
n1 = float(input('Valor em Euros: '))
won = n1 * 1455.188
won_arredondado = round(won, 2)
print('O valor convertido para Wons é de', won_arredondado)

