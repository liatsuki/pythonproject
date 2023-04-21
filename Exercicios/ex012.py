# Aula 07 - Desafio 012
# Faça um algoritmo que leia o preço de um produto e mostre o seu novo preço, com 5% de desconto

#Eu
n1=float(input('Preço do produto: '))
desc=n1-(n1*0.05)
print('Novo preço com 5% de desconto: {}€'.format(desc))

#Guanabara
preço = float(input('Qual é o preço do produto? '))
novo = n1 - (n1 * 5 / 100)
print('O produto que custava {:.2f}€, na promoçao com desconto de 5% vai custar {:.2f}€'.format(preço, novo))


#ChatGPT
# preco_produto = float(input("Digite o preço do produto: "))
# desconto = preco_produto * 0.05
# novo_preco = preco_produto - desconto
# print(f"O novo preço com 5% de desconto é {novo_preco:.2f}€")
