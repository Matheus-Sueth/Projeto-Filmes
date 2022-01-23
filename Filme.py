import PySimpleGUI as sg
from random import randint
from os import startfile
import re
import Pastas


def ver_imagens(lista, filme, ano):
    imagem_filme = 'ERRO.png'
    for imagem in lista:
        if imagem == 'ERRO.png':
            continue

        aux_imagem = re.split(r"[()]\s*",imagem)

        if aux_imagem[0] == filme and aux_imagem[1] == ano and aux_imagem[2] == '.png':
            imagem_filme = imagem
    return imagem_filme


def aleatorio(aux,tam):
    while True:
        numero = randint(0,tam)
        if tam <= 0:
            return -2
        if not numero in aux:
            aux.append(numero)
            return numero
        if len(aux) > tam:
            return -1


cam_filme = Pastas.cam_filme
cam_imagem = Pastas.cam_imagem
aux_aleatorio = []
banco = Pastas.banco
cursor = Pastas.cursor
cursor.execute('SELECT * FROM FILME ORDER BY NOME, ANO')
lista_filme = cursor.fetchall()
tam_filme = len(lista_filme)
sg.theme('DarkTeal12')
size = (30,3)

try:
    filme = lista_filme[aleatorio(aux_aleatorio,tam_filme)]
    imagem_filme = filme[6]
    layout_frame = [
        [sg.Text(f'\n{filme[1]}', background_color='green', size=(90, 3), key='titulo', font=('Arial', 12),
                  justification='center')],
        [sg.Text(f'\n{filme[2]}', background_color='green', justification='center', size=size, key='ano',
                  font=('Arial', 12)),
         sg.Text(f'\n{filme[4]}', background_color='green', size=size, key='nota', justification='center',
                  font=('Arial', 12))],
        [sg.Text(f'\n{filme[5]}', background_color='green', justification='center', size=(90, 3), font=('Arial', 12),
                  key='genero')]
    ]

    layout = [
        [sg.Image(filename=f'{cam_imagem}/{imagem_filme}', size=(600, 550), key='imagem')],
        [sg.Frame('INFORMAÇÕES', layout_frame, size=(500, 100), font=('Arial', 15))],
        [sg.T('')],
        [sg.Button('VOLTAR', size=(22, 3)), sg.Button('GERAR', size=(21, 3)), sg.Button('ASSISTIR', size=(22, 3))],
        [sg.T('')]
    ]
except:
    filme = []
    imagem_filme = ''
    layout_frame = [
        [sg.Text(f'\n', background_color='green', size=(90, 3), key='titulo', font=('Arial', 12),
                  justification='center')],
        [sg.Text(f'\n', background_color='green', justification='center', size=size, key='ano',
                  font=('Arial', 12)),
         sg.Text(f'\n', background_color='green', size=size, key='nota', justification='center',
                  font=('Arial', 12))],
        [sg.Text(f'\n', background_color='green', justification='center', size=(90, 3), font=('Arial', 12),
                  key='genero')]
    ]

    layout = [
        [sg.Image(filename=f'', size=(600, 550), key='imagem')],
        [sg.Frame('INFORMAÇÕES', layout_frame, size=(500, 100), font=('Arial', 15))],
        [sg.T('')],
        [sg.Button('VOLTAR', size=(22, 3)), sg.Button('GERAR', size=(21, 3)), sg.Button('ASSISTIR', size=(22, 3))],
        [sg.T('')]
    ]

janela = sg.Window('inicial', layout=layout, size=(600, 880))


def inicio(filme=filme, verifica=False):
    if verifica:
        janela.un_hide()

    while True:
        event, value = janela.read()

        if event == sg.WINDOW_CLOSED:
            return False

        if event == 'GERAR':
            numero_aleatorio = aleatorio(aux_aleatorio,tam_filme)
            if numero_aleatorio == -2:
                sg.popup('Não existem filmes cadastrados',font=('Arial',16),title='ERRO')
                continue
            if numero_aleatorio == -1:
                sg.popup('Todos os filmes já foram vistos',font=('Arial',16),title='ALERTA')
                aux_aleatorio.clear()
                numero_aleatorio = 0
                aux_aleatorio.append(numero_aleatorio)
            filme = lista_filme[numero_aleatorio]
            imagem_filme = filme[6]
            janela.Element('titulo').Update(f'\n{filme[1]}')
            janela.Element('ano').Update(f'\n{filme[2]}')
            janela.Element('nota').Update(f'\n{filme[4]}')
            janela.Element('genero').Update(f'\n{filme[5]}')
            janela.Element('imagem').Update(filename=f'{cam_imagem}/{imagem_filme}', size=(600, 550))

        if event == 'ASSISTIR':
            try:
                caminho_filme = f'{filme[1]} ({filme[2]}){filme[3]}'
            except:
                sg.popup('ACIONE O ADMINISTRADOR', font=('Arial', 20),title='ERRO')
                continue

            try:
                startfile(f'{cam_filme}/{caminho_filme}')
                return False
            except:
                sg.popup('ACIONE O ADMINISTRADOR', font=('Arial', 20),title='ERRO')

        if event == 'VOLTAR':
            janela.hide()
            return True


if __name__ == '__main__':
    inicio()
