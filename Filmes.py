import PySimpleGUI as sg

sg.theme('DarkTeal12')
layout = [
    [sg.T('')],
    [sg.Button('ADICIONAR FILME',size=(30, 3))],
    [sg.T('')],
    [sg.Button('VER FILME',size=(30, 3))],
    [sg.T('')],
    [sg.Button('ALTERAR FILME',size=(30, 3))],
    [sg.T('')],
    [sg.Button('DELETAR FILME',size=(30, 3))],
    [sg.T('')]
]

janela = sg.Window('CRUD', layout=layout, size=(250, 400))

def filmes():
    while True:
        event, value = janela.read()

        if event == sg.WINDOW_CLOSED:
            break
        if event == 'ADICIONAR FILME' or event == 'VER FILME' or event == 'ALTERAR FILME' or event == 'DELETAR FILME':
            sg.popup('Desculpe estamos em manutenção', font=('Arial',20))

if __name__ == '__main__':
    filmes()