import PySimpleGUI as sg
import listarArquivos as lsa
from random import randint

sg.theme('DarkTeal12')

size = (35,3)

layout_frame = [
                [sg.Text(f'{lsa.filme}', background_color='green', size=(90,3), key='titulo')],
                [sg.Text('GENÊRO', background_color='green', size=size),sg.Text('NOTA', background_color='green',size=size)],
                [sg.Text('DURAÇÃO', background_color='green', size=size),sg.Text('ANO', background_color='green',size=size)]
                ]

layout = [
    [sg.Image(filename=r'E:\\Matheus\Imagens_Filmes\Constantine.png', size=(600,550))],
    [sg.Frame('INFORMAÇÕES', layout_frame, size=(500,100),font=('Arial',15))],
    [sg.T('')],
    [sg.Button('SAIR',size=(22, 3)),sg.Button('GERAR',size=(21, 3)),sg.Button('ASSISTIR',size=(22, 3))],
    [sg.T('')]
]

janela = sg.Window('inicial', layout=layout, size=(600, 880))
def filme():
    while True:
        event, value = janela.read()

        if event == sg.WINDOW_CLOSED or event == 'SAIR':
            break
        if event == 'GERAR':
            lista = lsa.lista
            tam = len(lista) - 1
            filme = lista[randint(0,tam)]
            janela.Element('titulo').Update(filme)
            

if __name__ == '__main__':
    filme()