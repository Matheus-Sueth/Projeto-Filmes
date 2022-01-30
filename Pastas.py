import PySimpleGUI as sg
from os import listdir
import sqlite3 as sql
from os.path import exists

sg.theme('DarkTeal12')


def formata_string(texto):
    aux = set()
    for i in range(len(texto)):
        try:
            aux.add(texto.index('.', i, len(texto)))
        except:
            break
    aux = list(aux)
    aux.sort(reverse=True)
    return aux[0]


def caminhos():
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

    window = sg.Window('Pasta com Filmes e Imagens'.upper(), layout, finalize=True)

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
    cam_imagem = r'E://Matheus/Imagens_Filmes'
    listdir(cam_imagem)
    listdir(cam_filme)
except:
    cam_filme, cam_imagem = caminhos()

lista_imagem = [imagem[:formata_string(imagem) - len(imagem)] for imagem in listdir(cam_imagem)]
for imagem in lista_imagem:
    contador = lista_imagem.count(imagem)
    if contador > 1:
        sg.popup(f'Na pasta {imagem} existe {contador} arquivos com o mesmo nome {imagem}, remova os arquivos em excesso', font=('Arial', 20), title='ATENÇÃO')
        exit()
lista_filme = [filme[:formata_string(filme) - len(filme)] for filme in listdir(cam_filme)]
for filme in lista_filme:
    contador = lista_filme.count(filme)
    if contador > 1:
        sg.popup(f'Na pasta {cam_filme} existe {contador} arquivos com o mesmo nome {filme}, remova os arquivos em excesso', font=('Arial', 20), title='ATENÇÃO')
        exit()

caminho_banco = r'E://Matheus/Arquivos/Linguagens/PYTHON/Projetos/Projeto-Filme/filmes.db'
if exists(caminho_banco):
    banco = sql.connect(caminho_banco)
    cursor = banco.cursor()
    cursor.execute('SELECT * FROM FILME')
    lista_filme = cursor.fetchall()
    if len(lista_filme) > 0:
        if len(lista_filme[0]) != 7:
            sg.popup(f'Problema com banco de dados, exclua e faça outro', font=('Arial', 20), title='ERRO')
            exit()
    for id in range(0,len(lista_filme)):
        if None in lista_filme[id]:
            sg.popup(f'Problema com banco de dados, no id = {id}', font=('Arial', 20), title='ERRO')
            exit()

else:
    cont= 0
    while True:
        nome_banco = f'filme{cont}.db'
        try:
            banco = sql.connect(nome_banco)
            cursor = banco.cursor()
            cursor.execute(
                'CREATE TABLE "FILME" ( "ID" INTEGER, "NOME" TEXT, "ANO" TEXT, "EXTENSÃO" TEXT, "NOTA" TEXT, "GENÊRO" TEXT, "IMAGEM" TEXT, PRIMARY KEY("ID" AUTOINCREMENT) )')
        except:
            cont+=1
            continue
