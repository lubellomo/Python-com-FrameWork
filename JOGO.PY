# jogo de advinhação
import random 

lista_pc = ['👌','🤦‍♂️','👍']
nossa_lista = ['👌','🤦‍♂️','👍']
aleatorio = random.choice(lista_pc)
escolha_personagem = input('teste')
resultado = aleatorio == escolha_personagem

print('acertou? - ', resultado)
print('escolha da maquina: ', aleatorio)
print('minha escolha:' , escolha_personagem)

# Pergunta: Qual o metal cujo símbolo químico é Au?


# # Resposta: Ouro. O símbolo vem do latim aurum.


# # Pergunta: Em qual continente fica o Deserto do Saara?


# # Resposta: No continente Africano.


# # Pergunta: Quem é o autor da obra "Dom Quixote"?


# # Resposta: Miguel de Cervantes.


# # Pergunta: Qual é o processo pelo qual as plantas transformam luz solar em energia química?


# # Resposta: Fotossíntese.



listas_perguntas = [
    '',
'Qual é o metal cujo símbolo químico é Au?',
'Em qual continente fica o Deserto do Saara?',
'Quem é o autor da obra "Dom Quixote?',
'Qual é o processo pelo qual as plantas transformam luz solar em energia química?']

pergunta = random.choice(listas_perguntas[1:])
print(pergunta)


lista_respostas = [
    '',
    '1 - Ouro. O símbolo vem do latim aurum.',
    '2 - No continente Africano.',
    '3 - Miguel de Cervantes.',
    '4 - Fotossíntese.'
]

print(lista_respostas[1:])
resposta = int(input(' escolha um numero - (1) (2) (3) (4)'))

i = listas_perguntas.index(pergunta)

pontos = 0
resultado = (resposta == i) + pontos

print ('resultado acertou?', resposta == i)
print ('pontuação' , resultado)




