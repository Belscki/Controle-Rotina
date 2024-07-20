from tkinter import *
from tkinter import ttk
import time
import sqlite3

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
            self.Lista.insert("", END, values=i)
        self.DesConnectDb()

    def add_cliente(self):
        self.dia = self.Entrydia.get()
        self.title = self.Entrytitle.get()
        self.desc = self.Entrydesc.get()
        self.status = self.Entrystatus.get()

        self.ConnectDb()
        self.cursor.execute(""" INSERT INTO dias (dia, title, desc, status)
                            VALUES(?,?,?,?)""", (self.dia, self.title, self.desc, self.status))
        self.conn.commit()
        self.DesConnectDb()
        self.select_lista()
        
    # def exclude_cliente(self):
    #     self.id = self.EntryID.get()

    #     self.ConnectDb()
    #     self.cursor.execute(""" DELETE FROM dias WHERE ID = ?""", (self.id))
    #     self.conn.commit()
    #     self.DesConnectDb()
    #     self.select_lista()