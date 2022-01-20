import PySimpleGUI as sg
import sqlite3 as sql
from os import startfile
from PIL import Image
import Pastas


sg.theme('DarkTeal12')

cam_filme = Pastas.cam_filme
cam_imagem = Pastas.cam_imagem

size_text, size_input = (10,1), (70,1)
font_text = ('Arial',16)
lista = ['NÃO ASSISTIDO','PÉSSIMO', 'RUIM DEMAIS', 'RUIM', 'MAIS OU MENOS', 'BOM', 'MUITO BOM', 'EXCELENTE']
lista2 = ['','NOME','ANO','NOTA','GENÊRO']
banco = sql.connect('filmes.db')
cursor = banco.cursor()
cursor.execute('SELECT * FROM FILME')
valores = cursor.fetchall()
valores_nm = [nome[1]+'___'+nome[2] for nome in valores]
size = (30,3)

layout_frame = [
                [sg.Text(f'\n', background_color='green', size=(90,3), key='titulo',font=('Arial',12), justification='center')],
                [sg.Text(f'\n', background_color='green', justification='center', size=size, key='ano',font=('Arial',12)),sg.Text(f'\n', background_color='green',size=size, key='nota', justification='center', font=('Arial',12))],
                [sg.Text(f'\n', background_color='green', justification='center', size=(90,3), font=('Arial',12), key='genero')]
                ]


layout = [
    [sg.Input(f'TOTAL DE FILMES = {len(valores)}',size=(21, 3), justification='center', disabled=True, key='tam'), sg.T(' '*55), sg.Input(f'FILMES RETORNADOS = ?', key='retorno',justification='center', size=(25, 3), disabled=True)],
    [sg.T('')],
    [sg.Input('', key='nome_filtro', size=(40,2)),sg.Combo(lista2, key='campo_filtro', size=(10,1)),sg.Button('FILTRAR', size=(20,2))],
    [sg.T('')],
    [sg.Listbox(valores_nm, key='filmes', size=(92,3),font=('Arial',12))],
    [sg.Image(filename=f'', size=(600,550), key='imagem')],
    [sg.Frame('INFORMAÇÕES', layout_frame, size=(500,50),font=('Arial',15))],
    [sg.T('')],
    [sg.Button('VOLTAR',size=(22, 3)), sg.Button('VISUALIZAR',size=(21, 3)), sg.Button('ASSISTIR',size=(22, 3))],
    [sg.T('')]
]

janela = sg.Window('inicial', layout=layout, size=(600, 1050))


def formatar_imagem(caminho):
    im = Image.open(caminho)
    im.thumbnail((600, 550), Image.ANTIALIAS)
    im.save(caminho, 'PNG')
    return caminho


def banco_dados(banco_de_dados):
    cursor_banco = banco_de_dados.cursor()
    cursor_banco.execute('SELECT * FROM FILME')
    return cursor_banco.fetchall()


def ler(verifica=False):
    global resultados
    if verifica:
        janela.un_hide()

    while True:
        event, value = janela.read()
        #sg.popup(event,value)

        if event == sg.WINDOW_CLOSED:
            return False
        else:
            cursor.execute('SELECT * FROM FILME')
            resultado = cursor.fetchall()
            janela.Element('tam').Update(f'TOTAL DE FILMES = {len(resultado)}')

        if event == 'VISUALIZAR':
            try:
                if value['filmes'] == '':
                    sg.popup('ERRO\nNÃO FOI SELECIONADO NENHUM FILME', font=('Arial', 20))
                else:
                    aux = value["filmes"][0].split('___')
                    cursor.execute(f'SELECT * FROM FILME WHERE NOME == "{aux[0]}" AND ANO == {aux[1]}')
                    resultados = cursor.fetchall()
                    janela.Element('titulo').Update(f'\n{resultados[0][1]}')
                    janela.Element('ano').Update(f'\n{resultados[0][2]}')
                    janela.Element('nota').Update(f'\n{resultados[0][4]}')
                    janela.Element('genero').Update(f'\n{resultados[0][5]}')
                    janela.Element('imagem').Update(filename=formatar_imagem(f'{cam_imagem}/{resultados[0][6]}'), size=(600, 550))
            except (RuntimeError, TypeError, NameError, FileNotFoundError, IndexError) as erro2:
                sg.popup(f'ERRO\nACIONE O ADMINISTRADOR, {erro2}', font=('Arial', 20))

        if event == 'ASSISTIR':
            try:
                startfile(f'{cam_filme}/{resultados[0][1]} ({resultados[0][2]}){resultados[0][3]}')
                return False
            except (RuntimeError, TypeError, NameError, FileNotFoundError, IndexError) as erro2:
                sg.popup(f'ERRO\nACIONE O ADMINISTRADOR, {erro2}', font=('Arial', 20))

        if event == 'VOLTAR':
            janela.hide()
            return True

        if event == 'FILTRAR':
            try:
                if value["campo_filtro"] == '' and value["nome_filtro"] == '':
                    cursor.execute('SELECT * FROM FILME')
                    resultados = cursor.fetchall()
                    nomes = [nome[1]+'___'+nome[2] for nome in resultados]
                    janela.Element('filmes').Update(nomes)
                    janela.Element('retorno').Update('FILMES RETORNADOS = ?')
                elif value["campo_filtro"] == '' or value["nome_filtro"] == '':
                    if not value["campo_filtro"] in lista2:
                        sg.popup('ERRO\nO CAMPO LISTBOX NÃO ACEITA ESSE TEXTO', font=('Arial', 20))
                        continue
                    sg.popup('ERRO\nTODOS OS CAMPOS DEVEM SER PREENCHIDOS', font=('Arial', 20))
                else:
                    if value["campo_filtro"] == 'NOME':
                        cursor.execute(f'SELECT * FROM FILME WHERE NOME LIKE "%{value["nome_filtro"]}%"')
                    elif value["campo_filtro"] == 'ANO':
                        cursor.execute(f'SELECT * FROM FILME WHERE ANO == {value["nome_filtro"]}')
                    elif value["campo_filtro"] == 'GENÊRO':
                        cursor.execute(f'SELECT * FROM FILME WHERE GENÊRO LIKE "%{value["nome_filtro"]}%"')
                    elif value["campo_filtro"] == 'NOTA':
                        cursor.execute(f'SELECT * FROM FILME WHERE NOTA LIKE "%{value["nome_filtro"]}%"')

                    resultados = cursor.fetchall()
                    nomes = [nome[1]+'___'+nome[2] for nome in resultados]
                    janela.Element('filmes').Update(nomes)
                    janela.Element('retorno').Update(f'FILMES RETORNADOS = {len(resultados)}')
            except sql.Error as erro:
                sg.popup(erro)
            except (RuntimeError, TypeError, NameError, FileNotFoundError, IndexError) as erro2:
                sg.popup(f'ERRO\nACIONE O ADMINISTRADOR, {erro2}', font=('Arial', 20))
                janela.Element('filmes').Update(valores_nm)
                janela.Element('retorno').Update('FILMES RETORNADOS = ?')
                janela.Element('campo_filtro').Update('')
                janela.Element('nome_filtro').Update('')


if __name__ == '__main__':
    ler()
