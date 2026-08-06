# FAZENDO UMA TELA PARA MONTAGEM DE UM PERSONAGEM RPG:
dados={"nome":"","altura":"","peso":"","classe":"","naturalidade":""}
dados["nome"]=input("Entre com seu nome de guerra ")
print('HAHAHAHAHAHAH ! Seja bem vindo a essa grandiosa aventura e que os deuses tenham dó da sua alma.')
print('Qual sua altura ó nobre ' , dados["nome"], )
Altura=float(input(""))
if Altura<=1.69:
    print('Alto com um anão Ferreiro')
elif Altura>=1.69 and Altura<=1.79:
    print('Alto com um Pirata')
elif Altura>1.79 and Altura<=1.99:
    print('Alto como um Bárbaro')
else :
    print('Alto como um mágo')
peso=float(input('Escolha seu peso nobre senhor : '))
if peso<=60:
    print('Leve como uma dama \nHAHAHAHAHA!!!')
elif peso>60 and peso<=80:
    print('O senhor me parece em forma')
elif peso>80 and peso<=100 :
    print('Como um homem de verdade')
else:
    print("Cuidado para que não afunde o próprio návio \nHAHHAHAHAHAHAHA!!!")
print("Agora o mais importante, senhor. Sua classe : ")
print("Lista de Classe: \n\n 1 Mago \n\nUm homem alto, barbudo, calmo, pórem extremamente sábio. Esse é o mago, aquele escolhido pelo próprio Merlin para comandar essa longa jornada ")