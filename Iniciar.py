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

janela2 = sg.Window('inicial', layout=layout, size=(250, 300))

while True:
    event, value = janela2.read()

    if event == sg.WINDOW_CLOSED:
        break
    if event == 'ASSISTIR UM FILME ALEATÓRIO':
        janela2.hide()
        abrir = Filme.inicio(Filme.filme)
        break
    if event == 'GERENCIAR OS FILMES':
        janela2.hide()
        Filmes.filmes()
        break