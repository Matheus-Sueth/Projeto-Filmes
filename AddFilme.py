import PySimpleGUI as sg
import sqlite3 as sql
import re

sg.theme('DarkTeal12')

size_text, size_input = (10,1), (70,1)
font_text = ('Arial',16)
lista = ['PÉSSIMO', 'RUIM DEMAIS', 'RUIM', 'MAIS OU MENOS', 'BOM', 'MUITO BOM', 'EXCELENTE']
banco = sql.connect('filmes.db')
cursor = banco.cursor()

layout = [
    [sg.FileBrowse('FILME:', button_color='green', size=size_text,font=font_text),
        sg.T('Aperte o botão FILME', background_color='#5A9BC4', size=size_input, key='arquivo',font=font_text)],
    [sg.T('')],
    [sg.T('NOTA:', justification='center', background_color='green',size=size_text, font=font_text),
        sg.Combo(lista, background_color='#5A9BC4', size=(70,7), key='nota',font=font_text)],
    [sg.T('')],
    [sg.T('GENÊRO:', justification='center', background_color='green', size=size_text, font=font_text),
        sg.Input('', background_color='#5A9BC4', size=size_input, key='genero',font=font_text)],
    [sg.T('')],
    [sg.FileBrowse('IMAGEM:', button_color='green', size=size_text, font=font_text),
        sg.T('Aperte o botão IMAGEM', background_color='#5A9BC4', size=size_input, key='imagem',font=font_text)],
    [sg.T('')],
    [sg.Button('VOLTAR',size=(37, 3)),sg.Button('ADICIONAR',size=(37, 3)),sg.Button('MODO RÁPIDO',size=(37, 3))],
    [sg.T('')]
]

janela = sg.Window('ADICIONAR FILME', layout=layout, size=(950, 420))


def arrumar_genero(genero_antigo):
    aux_genero = re.split (r"[/]\s*", genero_antigo)
    aux_genero = [palavra.capitalize() for palavra in aux_genero]
    genero_arrumado = ['/'.join(aux_genero)]
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

        if event == 'ADICIONAR':
            try:
                if value['FILME:'] == '' or value['nota'] == '' or value['genero'] == '' or value['IMAGEM:'] == '':
                    sg.popup('Campos Vazios', font=('Arial', 20))
                    continue

                if not value['nota'] in lista:
                    sg.popup('Nota desconhecida', font=('Arial',20))
                    continue

                aux_filme = re.split(r"[/()]\s*",value['FILME:'])
                aux_imagem = re.split(r"[/]\s*",value['IMAGEM:'])
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
                    #cursor.execute('INSERT INTO FILME VALUES("'+str(id)+'","'+nome+'","'+str(ano)+'","'+nota+'","'+genero+'","'+imagem+'")')
                    #banco.commit()
                    sg.popup('Adicionado')
                    sg.popup('INSERT INTO FILME VALUES("'+str(id)+'","'+nome+'","'+str(ano)+'","'+extensao+'","'+nota+'","'+str(genero)+'","'+imagem+'")')
            except sql.Error as erro:
                sg.popup(erro)
            except:
                sg.popup('ERRO\nVERIQUE SE TODOS OS CAMPOS ESTÃO CORRETOS', font=('Arial',20))


if __name__ == '__main__':
    adicionar()
