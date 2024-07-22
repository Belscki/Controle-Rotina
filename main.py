from tkinter import *
from Front.frontend import FrontEnd, root, style

class App(FrontEnd):
    def __init__(self):
        self.root= root
        self.style = style
        self.caminho_icone = 'Icone.ico'
        self.Janela()
        self.frames()
        self.ObjetivosLista()
        self.Botoes()
        self.atualizar_data()
        self.TabelaBDD()
        self.select_lista()
        self.Entrys()
        self.BDDvariaveis()
        self.add_cliente()
        self.exclude_cliente()
        root.mainloop()

App()