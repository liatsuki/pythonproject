# Exercicio - #002 - Respondendo ao Usuário

# Desafio 002
# Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas
nome=input('Digite seu nome: ')
print('É um prazer te conhecer', nome,'!')

nome=input('Digite seu nome: ')
print('É um prazer te conhecer, {}!'.format(nome))

# Ambos os códigos pedem para o usuário digitar o seu nome e, em seguida,
# imprimem uma mensagem de boas-vindas na tela com o nome que foi digitado.

# A diferença entre os dois códigos é como eles inserem o nome na mensagem de boas-vindas.
# O primeiro código simplesmente adiciona o nome à mensagem usando vírgulas,
# enquanto o segundo código usa uma função chamada "format()" para adicionar o nome entre chaves na mensagem.

# A vantagem do segundo código é que ele é mais flexível e permite inserir várias variáveis
# e formatar mensagens mais complexas de uma maneira mais fácil de ler e entender.
# Mas, se você está escrevendo uma mensagem simples, o primeiro código pode ser mais fácil de usar.


# No primeiro código, a mensagem é criada como uma string que contém três partes separadas por vírgulas:
# a primeira parte é a string "É um prazer te conhecer", a segunda parte é a variável nome,
# que é definida a partir da entrada do usuário, e a terceira parte é a string final, que inclui um ponto de exclamação.

# No segundo código, a mensagem é criada como uma string única que contém apenas uma parte,
# mas usa o método format() para inserir o valor da variável nome no local correto da string.
# A string inclui um par de chaves {} onde o valor da variável nome deve ser inserido.

# A segunda forma é geralmente preferível porque torna mais fácil alterar a mensagem de saudação
# e também permite formatar a saída de outras formas. Por exemplo, poderíamos facilmente adicionar mais informações,
# como idade ou localização do usuário, usando o mesmo método format(). Além disso,
# o método format() permite que você especifique o tipo de formatação, o que pode ser útil em algumas situações.
