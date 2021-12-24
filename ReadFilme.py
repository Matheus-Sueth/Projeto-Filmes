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

layout_frame_1 = [
                [sg.Text(f'\n{valores[aux_valor][1]}', background_color='green', size=(90,3), key='titulo',font=('Arial',12), justification='center')],
                [sg.Text(f'\n{valores[aux_valor][2]}', background_color='green', justification='center', size=size, key='ano',font=('Arial',12)),sg.Text(f'\n {valores[aux_valor][4]}', background_color='green',size=size, key='nota', justification='center', font=('Arial',12))],
                [sg.Text(f'\n{valores[aux_valor][5]}', background_color='green', justification='center', size=(90,3), font=('Arial',12), key='genero')]
                ]


layout_tab_1 = [
    [sg.T(''),sg.Input(f'TOTAL DE FILMES = {len(valores)}',size=(22, 3), justification='center', disabled=True, key='tam'), sg.T(''*50), sg.Button('FILTRAR',size=(22, 1)), sg.T(''), sg.Input(f'ID = {valores[aux_valor][0]}', key='id',justification='center', size=(21, 3), disabled=True)],
    [sg.Image(filename=f'{cam_imagem}/{valores[aux_valor][6]}', size=(600,550), key='imagem')],
    [sg.Frame('INFORMAÇÕES', layout_frame_1, size=(500,100),font=('Arial',15))],
    [sg.T('')],
    [sg.Button('VOLTAR',size=(16, 3)), sg.Button('ANTERIOR',size=(16, 3), image_filename='1.png'), sg.Button('PRÓXIMO',size=(16, 3), image_filename='2.png'), sg.Button('ASSISTIR',size=(16, 3))],
    [sg.T('')]
]

layout_tab_2 = [
    [sg.Listbox(valores, size=(80,10))],
    [sg.Button('SELECIONAR')],
    [sg.T('')]
]

layout = [
        [sg.TabGroup([[sg.Tab('FILME', layout_tab_1), sg.Tab('LISTA', layout_tab_2)]])]
        ]

janela = sg.Window('inicial', layout=layout, size=(600, 1000))


def ler(verifica=False,aux=aux_valor):
    if verifica:
        janela.un_hide()

    while True:
        event, value = janela.read()
        sg.popup(event,value)

        if event == sg.WINDOW_CLOSED:
            return False
        else:
            cursor.execute('SELECT * FROM FILME')
            resultados = cursor.fetchall()
            janela.Element('tam').Update(f'TOTAL DE FILMES = {len (resultados)}')

        if event == 'ANTERIOR':
            try:
                if aux == 0:
                    sg.popup('ERRO\nESSE É O PRIMEIRO FILME DA LISTA', font=('Arial', 20))
                else:
                    aux -= 1
                    janela.Element('id').Update(f'ID = {resultados[aux][0]}')
                    janela.Element('titulo').Update(f'\n{resultados[aux][1]}')
                    janela.Element('ano').Update(f'\n{resultados[aux][2]}')
                    janela.Element('nota').Update(f'\n{resultados[aux][4]}')
                    janela.Element('genero').Update(f'\n{resultados[aux][5]}')
                    janela.Element('imagem').Update(filename=f'{cam_imagem}/{resultados[aux][6]}', size=(600, 550))
            except:
                sg.popup('ERRO\nACIONE O ADMINISTRADOR', font=('Arial', 20))

        if event == 'PRÓXIMO':
            try:
                if aux == len(resultados)-1:
                    sg.popup('ERRO\nESSE É O ÚLTIMO FILME DA LISTA', font=('Arial', 20))
                else:
                    aux+=1
                    janela.Element('id').Update(f'ID = {resultados[aux][0]}')
                    janela.Element('titulo').Update(f'\n{resultados[aux][1]}')
                    janela.Element('ano').Update(f'\n{resultados[aux][2]}')
                    janela.Element('nota').Update(f'\n{resultados[aux][4]}')
                    janela.Element('genero').Update(f'\n{resultados[aux][5]}')
                    janela.Element('imagem').Update(filename=f'{cam_imagem}/{resultados[aux][6]}', size=(600, 550))
            except:
                sg.popup('ERRO\nACIONE O ADMINISTRADOR', font=('Arial', 20))

        if event == 'ASSISTIR':

            startfile(f'{cam_filme}/{resultados[aux][1]} ({resultados[aux][2]}){resultados[aux][3]}')
            return False

        if event == 'VOLTAR':
            janela.hide()
            return True

        if event == 'FILTRAR':
            pass


if __name__ == '__main__':
    ler()
