import PySimpleGUI as sg

sg.theme('DarkTeal12')

size_text, size_input = (10,1), (30,1)
font_text = ('Arial',16)

layout_frame = [
                [sg.Text('FILME:', background_color='green', size=size_text,font=font_text),sg.Input('', background_color='green', size=size_input, key='titulo',font=font_text)],  
                [sg.T('')],
                [sg.Text('ANO:', background_color='green',size=size_text, key='ano',font=font_text)],
                [sg.T('')],
                [sg.Text('NOTA:', background_color='green',size=size_text, font=font_text)],
                [sg.T('')],
                [sg.Text('GENÊRO:', background_color='green', size=size_text, font=font_text)],
                [sg.T('')],
                [sg.FileBrowse('IMAGEM:', size=size_text, font=font_text),sg.Text('', background_color='green',size=(50,1), font=('Arial',10))]
                ]


layout = [
    [sg.Frame('INFORMAÇÕES DO FILME', layout_frame, size=(500,100),font=('Arial',15))],
    [sg.T('')],
    [sg.Button('VOLTAR',size=(22, 3)),sg.Button('ADICIONAR',size=(21, 3))],
    [sg.T('')]
]

janela = sg.Window('ADICIONAR FILME', layout=layout, size=(600, 480))

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
            sg.popup('Desculpe estamos em manutenção', font=('Arial',20))
            

if __name__ == '__main__':
    aux_funcao = adicionar()