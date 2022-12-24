import PySimpleGUI as sg

class TelaLoguin:
    def __init__(self):
        #layout
        layout = [
            [sg.Text('Loguin',size=(5,0)),sg.Input(size=(15,0),key='usuario')],
            [sg.Text('Senha',size=(5,0)),sg.Input(size=(15,0),key='senha')],
            [sg.Button('Entrar')]

        ]
        #janela
        self.janela = sg.Window('Sistema de Loguin').layout(layout)

        #dados
        self.button, self.values = self.janela.Read()

    def Iniciar(self):
            loguin = self.values('usuario')
            senha = self.values('senha')
            print(f'O loguin é: {loguin}')
            print(f'A senha é: {senha}')

tela = TelaLoguin()
tela.Iniciar()


