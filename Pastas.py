import PySimpleGUI as sg
from os import listdir


def main():
    caminho_filme = ''
    caminho_imagem = ''
    size_text, size_input = (10, 1), (70, 1)
    font_text = ('Arial', 16)

    layout = [
        [sg.FolderBrowse('FILME:', button_color='green', size=size_text, font=font_text),
         sg.Input('Aperte o botão FILME', size=size_input, key='arquivo', font=font_text, disabled=True)],
        [sg.T('')],
        [sg.FolderBrowse('IMAGEM:', button_color='green', size=size_text, font=font_text),
         sg.Input('Aperte o botão IMAGEM', size=size_input, key='imagem', font=font_text, disabled=True)],
        [sg.T('')],
        [sg.T('  '*40), sg.Button('VERIFICAR', size=(45, 3))],
        [sg.T('')]
    ]

    window = sg.Window('Pasta com Filmes e Imagens', layout, finalize=True)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            exit()
        if event == 'VERIFICAR':
            try:
                caminho_filme = values['arquivo']
                caminho_imagem = values['imagem']
                listdir(caminho_imagem)
                listdir(caminho_filme)
                sg.popup('Pastas Encontradas')
                window.close()
                return caminho_filme, caminho_imagem
            except:
                sg.popup('Pastas Não Encontradas')


try:
    cam_filme = r'E://Matheus/Filmes'
    cam_imagem = r'C://Matheus/Imagens_Filmes'
    listdir(cam_imagem)
    listdir(cam_filme)
except:
    cam_filme, cam_imagem = main()
