# Exercicio - #002 - Respondendo ao Usuário

# Desafio 002
# Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas
nome=input('Digite seu nome: ')
print('É um prazer te conhecer', nome,'!')

nome=input('Digite seu nome: ')
print('É um prazer te conhecer, {}!'.format(nome))

# Ambos os códigos pedem para o usuário digitar o seu nome e, em seguida, imprimem uma mensagem de boas-vindas na tela com o nome que foi digitado.

# A diferença entre os dois códigos é como eles inserem o nome na mensagem de boas-vindas. O primeiro código simplesmente adiciona o nome à mensagem usando vírgulas, enquanto o segundo código usa uma função chamada "format()" para adicionar o nome entre chaves na mensagem.

# A vantagem do segundo código é que ele é mais flexível e permite inserir várias variáveis e formatar mensagens mais complexas de uma maneira mais fácil de ler e entender. Mas, se você está escrevendo uma mensagem simples, o primeiro código pode ser mais fácil de usar.
