from tkinter import * 
from tkinter import ttk
import tkinter as tk
from Back.backend import BackEnd
from Back.config import PlaceholderEntry

root = Tk()
style = ttk.Style()

class FrontEnd(BackEnd):

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
    
        self.middleframe = Frame(
            self.root,
            bd = 4, 
            bg="#242B2D"
        )

        self.middleframe.place(
            relx= 0.1,
            rely= 0.3, 
            relwidth= 0.8, 
            relheight= 0.2
        )

        self.bottomframe = Frame(
            self.root,
            bd= 4,
            bg="#242B2D"
            )
        
        self.bottomframe.place(
            relx= 0.1,
            rely= 0.55,
            relwidth= 0.8,
            relheight= 0.40)

    def Botoes(self):
        self.btnCriar = Button(
            self.topframe,
            bd=2,
            bg="#0DFF09",
            text="+",
            font=('verdana', 16, 'bold'),
            command=self.add_cliente
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
            font=('verdana', 16, 'bold'),
            command=self.exclude_cliente
            )
        
        self.btnApagar.place(
            relx= 0.07,
            rely= 0.35,
            relwidth= 0.05,
            relheight= 0.25
            )
        
        self.btnAlterar = Button(
            self.topframe,
            bd=2,
            bg="Yellow",
            text="/",
            font=('verdana', 16, 'bold'),
            command=self.alterar_cliente
            )
        
        self.btnAlterar.place(
            relx= 0.13,
            rely= 0.35,
            relwidth= 0.05,
            relheight= 0.25
            )


    def Entrys(self):
        self.Entrydia = Entry(
            self.middleframe,
            highlightbackground="black",
            highlightthickness="2",
        )
        self.Entrydia = PlaceholderEntry(
            self.middleframe,
            placeholder='dia'
        )
        self.Entrydia.place(
            relx= 0.05,
            rely= 0.3,
            relwidth= 0.05,
            relheight= 0.25
        )
        self.EntryID = Entry(
            self.middleframe,
            highlightbackground="black",
            highlightthickness="2"
        )
        self.EntryID = PlaceholderEntry(
            self.middleframe,
            placeholder='ID'
        )
        self.EntryID.place(
            relx= 0.05,
            rely= 0.65,
            relwidth= 0.05,
            relheight= 0.25
        )
        self.Entrytitle = Entry(
            self.middleframe,
            highlightbackground="black",
            highlightthickness="2"
        )
        self.Entrytitle = PlaceholderEntry(
            self.middleframe,
            placeholder='Titulo'
        )
        self.Entrytitle.place(
            relx= 0.125,
            rely= 0.3,
            relwidth= 0.15,
            relheight= 0.25
        )
        self.Entrydesc = Entry(
            self.middleframe,
            highlightbackground="black",
            highlightthickness="2"
        )
        self.Entrydesc = PlaceholderEntry(
            self.middleframe,
            placeholder='Descrição'
        )
        self.Entrydesc.place(
            relx= 0.3,
            rely= 0.3,
            relwidth= 0.65,
            relheight= 0.25
        )
        self.Entrystatus = Entry(
            self.middleframe,
            highlightbackground="black",
            highlightthickness="2"
        )
        self.Entrystatus = PlaceholderEntry(
            self.middleframe,
            placeholder='status'
        )
        self.Entrystatus.place(
            relx= 0.75,
            rely= 0.6,
            relwidth= 0.20,
            relheight= 0.25
        )

    def ObjetivosLista(self):
        self.Lista = ttk.Treeview(
            self.bottomframe,
            height= 3,
            columns=("col1","col2","col3","col4","col5")
            )
    
        
        self.Lista.heading("#0", text="")
        self.Lista.heading("#1", text="ID")
        self.Lista.heading("#2", text="dia")
        self.Lista.heading("#3", text="title")
        self.Lista.heading("#4", text="desc")
        self.Lista.heading("#5", text="status")

        self.Lista.column("#0", width=-100)
        self.Lista.column("#1", width=10)
        self.Lista.column("#2", width=10)
        self.Lista.column("#3", width=50)
        self.Lista.column("#4", width=250)
        self.Lista.column("#5", width=50)

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

