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
    [sg.T('')]
]

janela = sg.Window('inicial', layout=layout, size=(250, 300))

while True:
    event, value = janela.read()

    if event == sg.WINDOW_CLOSED:
        break
    if event == 'ASSISTIR UM FILME ALEATÓRIO':
        janela.hide()
        Filme.filme()
        break
    if event == 'GERENCIAR OS FILMES':
        janela.hide()
        Filmes.filmes()
        break