import PySimpleGUI as sg
import Filme

sg.theme('DarkTeal12')
layout = [
    [sg.T('')],
    [sg.Text('MEUS FILMES', justification='center',size=(100,2), font=('Arial',22))],
    [sg.T('')],
    [sg.Button('INICIAR',size=(30, 3))]
]

janela = sg.Window('inicial', layout=layout, size=(220, 200))

while True:
    event, value = janela.read()

    if event == sg.WINDOW_CLOSED:
        break
    if event == 'INICIAR':
        sg.popup('Entrando')
        janela.hide()
        Filme.filme()
        break