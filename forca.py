import random

def jogar():

    imprimir_intro()
    palavra_secreta = escolher_palavra()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    print(letras_acertadas)

    enforcou = False
    acertou = False
    erro = 0


    while(not enforcou and not acertou ):
        chute = input('Letra: ')
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0

            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1

        else:
            erro +=1
            print('Erro: {} / 6'.format(erro))
        enforcou = erro == 6
        if (enforcou):
            print('Game Over')
            break
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
        if(acertou):
            print('Você acertou')


def imprimir_intro():
    print("**************************")
    print("Bem vindo ao jogo da forca")
    print("**************************")

def escolher_palavra():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def inicializa_letras_acertadas(palavra):
    return ['_' for letra in palavra]



if(__name__ == '__main__'):
    jogar()

