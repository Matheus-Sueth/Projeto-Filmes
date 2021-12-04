import PySimpleGUI as sg
import sqlite3 as sql

sg.theme('DarkTeal12')

size_text, size_input = (10,1), (30,1)
font_text = ('Arial',16)
lista = ['PÉSSIMO', 'RUIM DEMAIS', 'RUIM', 'MAIOS OU MENOS', 'BOM', 'MUITO BOM', 'EXCELENTE']
banco = sql.connect('filmes.db')
cursor = banco.cursor()

layout_frame = [
                [sg.Text('NOME:', background_color='green', size=size_text,font=font_text),
                 sg.Input('', background_color='green', size=size_input, key='nome',font=font_text)],  
                [sg.T('')],
                [sg.Text('ANO:', background_color='green',size=size_text,font=font_text),
                 sg.Input('', background_color='green', size=size_input, key='ano',font=font_text)],
                [sg.T('')],
                [sg.Text('NOTA:', background_color='green',size=size_text, font=font_text),
                 sg.Input('', background_color='green', size=size_input, key='nota',font=font_text)],                 
                [sg.T('')],
                [sg.Text('GENÊRO:', background_color='green', size=size_text, font=font_text),
                 sg.Input('', background_color='green', size=size_input, key='genero',font=font_text)],
                [sg.T('')],
                [sg.Text('IMAGEM:', background_color='green', size=size_text, font=font_text),
                 sg.Input('', background_color='green', size=size_input, key='imagem',font=font_text)]
                ]

layout = [
    [sg.Frame('INFORMAÇÕES DO FILME', layout_frame, size=(500,100),font=('Arial',15))],
    [sg.T('')],
    [sg.Button('VOLTAR',size=(20, 3)),sg.Button('ADICIONAR',size=(20, 3)),sg.FileBrowse('PROCURAR IMAGEM\nEM UMA\nPASTA', size=(20, 3))],
    [sg.T('')]
]

janela = sg.Window('ADICIONAR FILME', layout=layout, size=(550, 420))

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
                if value['nome'] == '' or value['ano'] == '' or value['nota'] == '' or value['genero'] == '':
                    sg.popup('Campos Vazios', font=('Arial',20))
                    continue
                
                if value['PROCURAR IMAGEM\nEM UMA\nPASTA'] == '' and not value['imagem'] == '':
                    imagem = value['imagem']
                elif value['imagem'] == '' and not value['PROCURAR IMAGEM\nEM UMA\nPASTA'] == '':
                    janela.Element('imagem').Update(value['PROCURAR IMAGEM\nEM UMA\nPASTA'])
                    imagem = value['PROCURAR IMAGEM\nEM UMA\nPASTA']
                else:
                    sg.popup('Você não selecionou uma imagem ou digitou seu caminho', font=('Arial',20))
                    continue
                
                if not value['nota'].upper() in lista:
                    sg.popup('NOTA DESCONHECIDA', font=('Arial',20))
                    continue
                
                nome = value['nome']
                ano = int(value['ano'])
                nota = value['nota']
                genero = value['genero']
                
                cursor.execute('SELECT NOME,ANO FROM FILME')
                valores = cursor.fetchall()
                id = len(valores)+1
                
                for filme in valores:
                    if filme[0] == nome and filme[1] == str(ano):
                        sg.popup(f'{nome} JÁ ESTÁ CADASTRADO', font=('Arial',20))
                        break
                else:   
                    cursor.execute(f'INSERT INTO FILME VALUES("'+str(id)+'","'+nome+'","'+str(ano)+'","'+nota+'","'+genero+'","'+imagem+'")')
                    banco.commit()
                
                sg.popup('Desculpe estamos em manutenção', font=('Arial',20))
            except sql.Error as erro:
                sg.popup(erro)
            except:
                sg.popup('ERRO\nVERIQUE SE TODOS OS CAMPOS ESTÃO CORRETOS', font=('Arial',20))
                

if __name__ == '__main__':
    adicionar()