import PySimpleGUI as sg
import AddFilme as add
import sqlite3 as sql

banco = sql.connect('filmes.db')
cursor = banco.cursor()

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
    [sg.T('')],
    [sg.Button('VOLTAR',size=(30, 3))],
    [sg.T('')]
]

janela = sg.Window('CRUD', layout=layout, size=(250, 500))

def filmes(verifica_add=False):
    if verifica_add:
        janela.un_hide()
        
    while True:
        event, value = janela.read()

        if event == sg.WINDOW_CLOSED:
            return False
        
        if event == 'VER FILME' or event == 'ALTERAR FILME' or event == 'DELETAR FILME':
            sg.popup('Desculpe estamos em manutenção', font=('Arial',20))
            
        if event == 'ADICIONAR FILME':
            janela.hide()
            if add.adicionar(verifica_add):
                janela.un_hide()
                verifica_add = True
            else:
                return False
                
                
        if event == 'VOLTAR':
            janela.hide()
            return True
            
            

if __name__ == '__main__':
    aux_funcao = filmes()