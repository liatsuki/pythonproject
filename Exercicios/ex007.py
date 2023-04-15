# Aula 07 - Desafio 007
# Desenvolva um programa que leia as duas notas de um aluno, calcula e mostre a sua média
# Dica: ordem de precendencia

#Eu
nota1=int(input('Nota 1 do Aluno: '))
nota2=int(input('Nota 2 do Aluno: '))
media=(nota1+nota2)/2
print('A média entre a nota {} e a nota {} é de {}'.format(nota1, nota2, media))


#ChatGPT
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
print("A média do aluno é:", round(media))
