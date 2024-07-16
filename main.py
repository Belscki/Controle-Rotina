from tkinter import *
from tkinter import ttk
import time
import sqlite3

root = Tk()
style = ttk.Style()

class BackEnd():
    def atualizar_data(self):
        self.tempo_atual = time.time()
        self.tempo_local = time.localtime(self.tempo_atual)
        self.dia = self.tempo_local.tm_mday
        self.dialabel.config(
            text= f"{self.dia}", 
            font= ('verdana', 30, 'bold'), 
            bg= "#A7C1C9"
            )

    def ConnectDb(self):
        self.conn = sqlite3.connect("dias.db")
        self.cursor = self.conn.cursor()

    def DesConnectDb(self):
        self.conn.close()

    def TabelaBDD(self):
        self.ConnectDb();
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS dias(
            ID INTEGER PRIMARY KEY,
            dia INT,
            title VARCHAR(60) NOT NULL,
            desc VARCHAR(120),
            status BOOLEAN
                            )
    """)
        self.conn.commit();
        self.DesConnectDb()

    def select_lista(self):
        self.Lista.delete(*self.Lista.get_children())
        self.ConnectDb()
        lista = self.cursor.execute(""" SELECT ID, dia, title, desc, status FROM dias
            ORDER BY dia ASC;""")
        #Espaço vazio em baio por conta do espaço vazio na tree view
        for i in lista:
            self.ListaCli.insert("", END, values=i)
        self.DesConnectDb()

    

class FrontEnd(BackEnd):
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
        root.mainloop()

    def Janela(self):
        self.root.title("Objetivos do Dia")
        self.root.configure(
            bg="#466068"
            )
        self.root.geometry("1200x900")
        self.root.minsize(
            width=1200, 
            height=900
            )
        self.root.iconbitmap(self.caminho_icone)

    def frames(self):
        self.topframe = Frame(
            self.root,
            bd = 4, 
            bg="#242B2D"
            )
        
        self.topframe.place(
            relx= 0.1,
            rely= 0.05, 
            relwidth= 0.8, 
            relheight= 0.2
            )

        self.quadradodia = Frame(
            self.topframe,
            bd = 4,
            bg="#A7C1C9"
            )
        
        self.quadradodia.place(
            relx= 0.4,
            rely= 0,
            relwidth= 0.20,
            relheight= 1
            )

        self.dialabel = Label(
            self.quadradodia
            )
        
        self.dialabel.place(
            relx= 0.25,
            rely= 0.5,
            relwidth= 0.5,
            relheight= 0.3)

        self.txtdialabel = Label(
            self.quadradodia
            )
        
        self.txtdialabel.place(
            relx= 0.25, 
            rely= 0.1,
            relwidth= 0.5,
            relheight= 0.3)
        
        self.txtdialabel.config(
            text="Dia",
            font=('verdana', 30, 'bold'),
            bg="#A7C1C9"
            )
    
        self.bottomframe = Frame(
            self.root,
            bd= 4,
            bg="#242B2D"
            )
        
        self.bottomframe.place(
            relx= 0.1,
            rely= 0.3,
            relwidth= 0.8,
            relheight= 0.65)

    def Botoes(self):
        self.btnCriar = Button(
            self.topframe,
            bd=2,
            bg="#0DFF09",
            text="+",
            font=('verdana', 16, 'bold'),
            )
        
        self.btnCriar.place(
            relx= 0.01,
            rely= 0.35,
            relwidth= 0.05,
            relheight= 0.25
            )

        self.btnApagar = Button(
            self.topframe,
            bd=2,
            bg="#A12020",
            text="-",
            font=('verdana', 16, 'bold')
            )
        
        self.btnApagar.place(
            relx= 0.07,
            rely= 0.35,
            relwidth= 0.05,
            relheight= 0.25
            )

    def ObjetivosLista(self):
        self.Lista = ttk.Treeview(
            self.bottomframe,
            height= 3,
            columns=("col1","col2","col3","col4")
            )
    
        
        self.Lista.heading("#0", text="ID")
        self.Lista.heading("col1", text="dia")
        self.Lista.heading("col2", text="title")
        self.Lista.heading("col3", text="desc")
        self.Lista.heading("col4", text="status")

        self.Lista.column("#0", width=25)
        self.Lista.column("col1", width=25)
        self.Lista.column("col2", width=150)
        self.Lista.column("col3", width=250)
        self.Lista.column("col4", width=50)

        self.Lista.place(
            relx= 0,
            rely= 0,
            relwidth= 1,
            relheight= 1
            )

        self.ScroolLista = Scrollbar(
            self.bottomframe,
            orient='vertical'
            )
        
        self.Lista.configure(
            yscroll= self.ScroolLista,
            )
        
        self.ScroolLista.place(
            relx= 0.978, 
            rely= 0.01, 
            relwidth= 0.02, 
            relheight= 0.988
            )
        
        self.style.configure(
            'Treeview',
            bg='#A7C1C9',
            foreground='#242B2D',
            rowheight=30,
            fieldbackground=''
        )

        self.style.configure(
            "Treeview.Heading",
            background="#242B2D",
            foreground="#242B2D",
            font=("Helvetica", 12, "bold")
            )

        self.style.map("Treeview")

FrontEnd()