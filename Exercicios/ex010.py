# Aula 07 - Desafio 010
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

n1 = float(input('Quanto dinheiro você tem na carteira? '))
s = n1 / 1.09
print('Com {:.2f}€ você pode comprar {:.2f}$.'.format(n1, s))


#valor arrendondado - chatgpt
# n1 = float(input('Valor em Euros: '))
# won = n1 * 1455.188
# won_arredondado = round(won, 2)
# print('O valor convertido para Wons é de', won_arredondado)

