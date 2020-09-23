import forca
import Advinha

print("**************************")
print("*****Escolha seu jogo*****")
print("**************************")

print('1 - Forca | 2 - Adivinhação')


jogo = int(input('Jogo: '))

if(jogo == 1):
    print('Jogando forca')
    forca.jogar()

elif(jogo == 2):
    print('Jogando Adivinhação')
    Advinha.jogar()


