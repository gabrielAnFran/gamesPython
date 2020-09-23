import random
def jogar():


    print("**************************")
    print("Bem vindo ao jogo de adivinhação")
    print("**************************")

    num_secreto = round(random.randrange(1, 101))
    print(num_secreto)
    total_de_tentativas = 0
    pontos = 1000

    print('Escolha a dificuldade')
    print('1 - Fácil | 2 - Médio | 3 - Difícil')

    dificuldade = int(input('Dificuldade: '))

    if(dificuldade == 1):
        total_de_tentativas = 20
    elif(dificuldade == 2):
        total_de_tentativas = 10
    elif(dificuldade == 3):
        total_de_tentativas = 3
    else:
        print('Dificuldade inválida')

    for rodada in range (1,total_de_tentativas+1):

        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute = int(input('Entre com um número entre 1 e 100: '))
        acertou = chute == num_secreto
        maior = chute > num_secreto
        menor = chute < num_secreto

        if (chute >1 and chute<=100):
            if (acertou):
                print("Acertou")
                break
            else :
                if(maior):
                    print("Seu chute foi maior que o a resposta correta")
                    perde = chute - num_secreto
                    pontos = pontos - perde

                elif(menor):
                    print("Seu chute foi menor que o a resposta correta")
                    perde = num_secreto - chute
                    pontos = pontos - perde
                else:
                    print('Numero inválido')
                    continue

    print('Voce terminou o jogo com {}/1000'.format(pontos), 'pontos')
    print('Fim')

if(__name__ == '__main__'):
    jogar()
