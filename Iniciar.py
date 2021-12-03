import PySimpleGUI as sg
import Filme
import Filmes

sg.theme('DarkTeal12')
layout = [
    [sg.T('')],
    [sg.Text('MEUS FILMES', justification='center',size=(100,2), font=('Arial',22))],
    [sg.T('')],
    [sg.Button('ASSISTIR UM FILME ALEATÓRIO',size=(30, 3))],
    [sg.T('')],
    [sg.Button('GERENCIAR OS FILMES',size=(30, 3))],
    [sg.T('')],
    [sg.Button('SAIR',size=(30, 3))],
    [sg.T('')]
]

janela2 = sg.Window('inicial', layout=layout, size=(250, 400))
verifica_filmes, verifica_filme = False, False

while True:
    event, value = janela2.read()

    if event == sg.WINDOW_CLOSED or event == 'SAIR':
        break
    if event == 'ASSISTIR UM FILME ALEATÓRIO':
        janela2.hide()
        if Filme.inicio(verifica=verifica_filme):
            janela2.un_hide()
            verifica_filme = True
        else:
            verifica_filme = False
            break
    if event == 'GERENCIAR OS FILMES':
        janela2.hide()
        if Filmes.filmes(verifica_add=verifica_filmes):
            janela2.un_hide()
            verifica_filmes = True
        else:
            verifica_filmes = False
            break