from tkinter import *
from .AddWindow import *
from Control.Controller import *

class MainWindow:
    def __init__(self, master, dao_factory):
        
        self.dao_factory = dao_factory

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
        tabela_vazia = ControlFuncionario.verifica_tabela_fornecedor()
        if(tabela_vazia == True):
            self.janela = Tk()
            self.janela.title("ERRO")
            self.msg = Label(self.janela,text="O sistema não possui nenhum funcionário cadastrado!",font=('Calibri',12),fg='black').grid(row=3,column=2) 
            self.janela["bg"] = "pink"

            self.janela.geometry("425x100+200+100")

            self.janela.mainloop()
        else:
            Funcionario_Window(self.dao_factory)

    def tela_fornecedor(self):
        Fornecedor_Window(self.dao_factory)
    
    def tela_produto(self):
        Produto_Window(self.dao_factory)

