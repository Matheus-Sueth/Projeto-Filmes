import PySimpleGUI as sg
import sqlite3 as sql
from os import listdir
import re

sg.theme('DarkTeal12')

cam_filme = r'E:/Matheus/Filmes'
cam_imagem = r'E:/Matheus/Imagens_Filmes'
aux_aleatorio = []
lista_filme = listdir(cam_filme)
lista_imagens = listdir(cam_imagem)

size_text, size_input = (10,1), (70,1)
font_text = ('Arial',16)
lista = ['PÉSSIMO', 'RUIM DEMAIS', 'RUIM', 'MAIS OU MENOS', 'BOM', 'MUITO BOM', 'EXCELENTE']
banco = sql.connect('filmes.db')
cursor = banco.cursor()

layout = [
    [sg.FileBrowse('FILME:', button_color='green', size=size_text,font=font_text),
        sg.Input('Aperte o botão FILME', size=size_input, key='arquivo',font=font_text, disabled=True)],
    [sg.T('')],
    [sg.T('NOTA:', justification='center', background_color='green',size=size_text, font=font_text),
        sg.Combo(lista, background_color='#5A9BC4', size=(70,7), key='nota',font=font_text)],
    [sg.T('')],
    [sg.T('GENÊRO:', justification='center', background_color='green', size=size_text, font=font_text),
        sg.Input('', background_color='#5A9BC4', size=size_input, key='genero',font=font_text)],
    [sg.T('')],
    [sg.FileBrowse('IMAGEM:', button_color='green', size=size_text, font=font_text),
        sg.Input('Aperte o botão IMAGEM', size=size_input, key='imagem',font=font_text, disabled=True)],
    [sg.T('')],
    [sg.Button('VOLTAR',size=(37, 3)),sg.Button('ADICIONAR',size=(37, 3)),sg.Button('PROCURAR',size=(37, 3))],
    [sg.T('')]
]

janela = sg.Window('ADICIONAR FILME', layout=layout, size=(950, 420))


def arrumar_genero(genero_antigo):
    aux_genero = re.split(r"[/]\s*", genero_antigo)
    aux_genero = [palavra.capitalize() for palavra in aux_genero]
    genero_arrumado = '/'.join(aux_genero)
    return genero_arrumado


def adicionar(verifica=False):
    if verifica:
        janela.un_hide()

    while True:
        event, value = janela.read()

        if event == sg.WINDOW_CLOSED:
            return False

        if event == 'VOLTAR':
            janela.hide()
            return True

        if event == 'PROCURAR':
            try:
                cursor.execute('SELECT NOME,ANO,EXTENSÃO,IMAGEM FROM FILME')
                valores = cursor.fetchall()

                for filme in lista_filme:
                    for valor in valores:
                        teste = f'{valor[0]} ({valor[1]}){valor[2]}'
                        if filme == teste:
                            sg.popup(f'{filme} JÁ ESTÁ CADASTRADO', font=('Arial', 20))
                            break
                    else:
                        imagem = re.split(r"[/.]\s*",filme)
                        janela.Element('arquivo').Update(f'{cam_filme}/{filme}')
                        janela.Element('imagem').Update(f'{cam_imagem}/{imagem[0]}.png')
                        #sg.popup(f'{filme} DEVE SER CADASTRADO', font=('Arial', 20))
                        break
                else:
                    sg.popup('NÃO HÁ ATUALIZAÇÕES', font=('Arial', 20))
            except:
                sg.popup('Erro ao Procurar Novos Filmes')

        if event == 'ADICIONAR':
            try:
                if value['arquivo'] == '' or value['nota'] == '' or value['genero'] == '' or value['imagem'] == '':
                    sg.popup('Campos Vazios', font=('Arial', 20))
                    continue

                if value['arquivo'] == 'Aperte o botão FILME' or value['imagem'] == 'Aperte o botão IMAGEM':
                    sg.popup('Campos Filme e/ou Imagem Vazios', font=('Arial', 20))
                    continue

                if not value['nota'] in lista:
                    sg.popup('Nota desconhecida', font=('Arial',20))
                    continue

                aux_filme = re.split(r"[/()]\s*",value['arquivo'])
                aux_imagem = re.split(r"[/]\s*",value['imagem'])
                nome = aux_filme[3].strip()
                ano = int(aux_filme[4])
                extensao = aux_filme[5].strip()
                nota = value['nota']
                genero = str(value['genero']).capitalize()
                imagem = aux_imagem[3]
                cursor.execute('SELECT NOME,ANO FROM FILME')
                valores = cursor.fetchall()
                id = len(valores)+1

                if '/' in genero:
                    genero = arrumar_genero(genero)

                for filme in valores:
                    if filme[0].strip() == nome and int(filme[1]) == ano:
                        sg.popup(f'{nome} JÁ ESTÁ CADASTRADO', font=('Arial',20))
                        break
                else:
                    cursor.execute(f'INSERT INTO FILME VALUES({id},"{nome}",{ano},"{extensao}","{nota}","{genero}","{imagem}")')
                    banco.commit()
                    sg.popup('Adicionado')
            except sql.Error as erro:
                sg.popup(erro)
            except:
                sg.popup('ERRO\nVERIQUE SE TODOS OS CAMPOS ESTÃO CORRETOS', font=('Arial',20))


if __name__ == '__main__':
    adicionar()
