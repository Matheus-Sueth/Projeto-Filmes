from os import chdir, listdir, startfile
from random import randint

cam = 'E://Matheus/Filmes'

chdir(cam)
lista = listdir()
tam = len(lista) - 1
filme = lista[randint(0,tam)]

def arquivo():
    while True:
        caminho = f'{cam}/{filme}'
        resposta = input('\nQuer esse ? (SIM/NAO)\n')
        if resposta.upper() == 'SIM':
            startfile(caminho)
            break
        else:
            filme = lista[randint(0,tam)]
            print(filme)


if __name__ == '__main__':
    print(f'O filme é {filme}')
    arquivo()