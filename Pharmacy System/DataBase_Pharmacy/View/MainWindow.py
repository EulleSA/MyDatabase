from tkinter import *
from .AddWindow import *
#from pony.orm import *


#https://www.pycursos.com/tkinter-sqlite3/

#db = Database()

class MainWindow:
    def __init__(self, master):
        self.master = master
        master.title("Pharmacy System")
        self.master["bg"] = "pink"

        bt1 = Button(self.master, width=20, text="Funcionario",command=self.tela_funcionario)
        bt1.place(x=100,y=100)

        bt2 = Button(self.master, width=20, text="Fornecedor",command=self.tela_fornecedor)
        bt2.place(x=100,y=150)

        bt3 = Button(self.master, width=20, text="Produto",command=self.tela_produto)
        bt3.place(x=100,y=200)
        self.master.geometry("350x350+100+100")

    def tela_funcionario(self):
        Funcionario_Window()

    def tela_fornecedor(self):
        #Criar a cache aqui.
        if(Fornecedor_ORM.verifica_banco() == []):
            self.janela = Tk()
            self.janela.title("ERRO")
            self.msg = Label(self.janela,text="O sistema não possui nenhum funcionário cadastrado!",font=('Calibri',12),fg='black').grid(row=3,column=2) 
            self.janela["bg"] = "pink"
                    
            self.janela.geometry("425x100+200+100")

            self.janela.mainloop()
            
        else:
            Fornecedor_Window()
    
    def tela_produto(self):
         #Criar a cache aqui.
        if(Produto_ORM.verifica_banco() == []):
            self.janela = Tk()
            self.janela.title("ERRO")
            self.msg = Label(self.janela,text="O sistema não possui nenhum funcionário cadastrado!",font=('Calibri',12),fg='black').grid(row=3,column=2) 
            self.janela["bg"] = "pink"
                    
            self.janela.geometry("425x100+200+100")

            self.janela.mainloop()
            
        else:
            Produto_Window()

