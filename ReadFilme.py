import PySimpleGUI as sg
import sqlite3 as sql
from os import startfile
import re


sg.theme('DarkTeal12')

cam_filme = r'E:/Matheus/Filmes'
cam_imagem = r'E:/Matheus/Imagens_Filmes'

size_text, size_input = (10,1), (70,1)
font_text = ('Arial',16)
lista = ['PÉSSIMO', 'RUIM DEMAIS', 'RUIM', 'MAIS OU MENOS', 'BOM', 'MUITO BOM', 'EXCELENTE']
banco = sql.connect('filmes.db')
cursor = banco.cursor()
cursor.execute('SELECT * FROM FILME')
valores = cursor.fetchall()
aux_valor = 0
size = (30,3)

layout_frame = [
                [sg.Text(f'{valores[aux_valor][1]}', background_color='green', size=(90,3), key='titulo',font=('Arial',12))],
                [sg.Text(f'{valores[aux_valor][2]}', background_color='green', size=size, key='ano',font=('Arial',12)),sg.Text(f'{valores[aux_valor][4]}', background_color='green',size=size, key='nota', font=('Arial',12))],
                [sg.Text(f'{valores[aux_valor][5]}', background_color='green', size=(90,3), font=('Arial',12), key='genero')]
                ]


layout = [
    [sg.T(''),sg.Input(f'TOTAL DE FILMES = {len(valores)}',size=(21, 3), justification='center', disabled=True), sg.T(''*50), sg.Button('FILTRAR',size=(23, 1)), sg.T(''), sg.Input(f'ID = {valores[aux_valor][0]}', key='id',justification='center', size=(21, 3))],
    [sg.Image(filename=f'{cam_imagem}/{valores[aux_valor][6]}', size=(600,550), key='imagem')],
    [sg.Frame('INFORMAÇÕES', layout_frame, size=(500,100),font=('Arial',15))],
    [sg.T('')],
    [sg.Button('VOLTAR',size=(16, 3)), sg.Button('ANTERIOR',size=(16, 3), image_filename='1.png'), sg.Button('PRÓXIMO',size=(16, 3), image_filename='2.png'), sg.Button('ASSISTIR',size=(16, 3))],
    [sg.T('')]
]

janela = sg.Window('inicial', layout=layout, size=(600, 920))


def ler(verifica=False,aux=aux_valor):
    if verifica:
        janela.un_hide()

    while True:
        event, value = janela.read()

        if event == sg.WINDOW_CLOSED:
            return False

        if event == 'ANTERIOR':
            try:
                if aux == 0:
                    sg.popup('ERRO\nESSE É O PRIMEIRO FILME DA LISTA', font=('Arial', 20))
                else:
                    aux -= 1
                    janela.Element('id').Update(f'ID = {valores[aux][0]}')
                    janela.Element('titulo').Update(valores[aux][1])
                    janela.Element('ano').Update(valores[aux][2])
                    janela.Element('nota').Update(valores[aux][4])
                    janela.Element('genero').Update(valores[aux][5])
                    janela.Element('imagem').Update(filename=f'{cam_imagem}/{valores[aux][6]}', size=(600,550))
            except:
                sg.popup('ERRO\nACIONE O ADMINISTRADOR', font=('Arial', 20))

        if event == 'PRÓXIMO':
            try:
                if aux == len(valores)-1:
                    sg.popup('ERRO\nESSE É O ÚLTIMO FILME DA LISTA', font=('Arial', 20))
                else:
                    aux+=1
                    janela.Element('id').Update(f'ID = {valores[aux][0]}')
                    janela.Element('titulo').Update(valores[aux][1])
                    janela.Element('ano').Update(valores[aux][2])
                    janela.Element('nota').Update(valores[aux][4])
                    janela.Element('genero').Update(valores[aux][5])
                    janela.Element('imagem').Update(filename=f'{cam_imagem}/{valores[aux][6]}', size=(600,550))
            except:
                sg.popup('ERRO\nACIONE O ADMINISTRADOR', font=('Arial', 20))

        if event == 'ASSISTIR':
            startfile(f'{cam_filme}')
            return False

        if event == 'VOLTAR':
            janela.hide()
            return True


if __name__ == '__main__':
    ler()
