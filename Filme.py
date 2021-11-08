import PySimpleGUI as sg
from random import randint
from os import listdir, startfile
import re

def ver_imagens(lista, filme, ano):
    imagem_filme = 'ERRO.png'
    for imagem in lista:
        if imagem == 'ERRO.png':
            continue
        aux_imagem = re.split(r"[()]\s*",imagem)
        if aux_imagem[0] == filme and aux_imagem[1] == ano:
            imagem_filme = imagem
    return imagem_filme

def aleatorio(aux,tam):
  while True:
    numero = randint(0,tam)
    if not numero in aux:
      aux.append(numero)
      return numero
    if len(aux) > tam:
      return -1

cam_filme = r'E://Matheus/Filmes'
cam_imagem = r'E://Matheus/Imagens_Filmes'
aux_aleatorio = []
lista_filme = listdir(cam_filme)
tam_filme = len(lista_filme) - 1
filme = lista_filme[aleatorio(aux_aleatorio,tam_filme)]
aux = re.split(r"[()]\s*",filme)
lista_imagens = listdir(cam_imagem)
imagem_filme = ver_imagens(lista_imagens, aux[0], aux[1])

sg.theme('DarkTeal12')

size = (30,3)

layout_frame = [
                [sg.Text(f'{aux[0]}', background_color='green', size=(90,3), key='titulo',font=('Arial',12))], 
                [sg.Text(f'{aux[1]}', background_color='green',size=size, key='ano',font=('Arial',12)),sg.Text('NOTA', background_color='green',size=size, font=('Arial',12))],
                [sg.Text('GENÊRO', background_color='green', size=(90,3), font=('Arial',12))]
                ]


layout = [
    [sg.Image(filename=f'{cam_imagem}/{imagem_filme}', size=(600,550), key='imagem')],
    [sg.Frame('INFORMAÇÕES', layout_frame, size=(500,100),font=('Arial',15))],
    [sg.T('')],
    [sg.Button('SAIR',size=(22, 3)),sg.Button('GERAR',size=(21, 3)),sg.Button('ASSISTIR',size=(22, 3))],
    [sg.T('')]
]

janela = sg.Window('inicial', layout=layout, size=(600, 880))
def inicio(filme=filme):
    while True:
        event, value = janela.read()

        if event == sg.WINDOW_CLOSED or event == 'SAIR':
            janela.hide()
            break

        if event == 'GERAR':
            numero_aleatorio = aleatorio(aux_aleatorio,tam_filme)
            if numero_aleatorio == -1:
                sg.popup('Todos os filmes já foram vistos')
                aux_aleatorio.clear()
                numero_aleatorio = 0
                aux_aleatorio.append(numero_aleatorio)
            filme = lista_filme[numero_aleatorio]
            aux = re.split(r"[()]\s*",filme)
            imagem_filme = ver_imagens(lista_imagens, aux[0], aux[1])
            janela.Element('titulo').Update(aux[0])
            janela.Element('ano').Update(aux[1])
            janela.Element('imagem').Update(filename=f'{cam_imagem}/{imagem_filme}', size=(600,550))

        if event == 'ASSISTIR':
            startfile(f'{cam_filme}/{filme}')
            break
            

if __name__ == '__main__':
    inicio()