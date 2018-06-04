
from .MainWindow import *
from sys import path
path.append("..")
import tkinter.ttk as ttk
from Control.Sessions import *


class Funcionario_Window:
    def __init__(self):
        self.janela = Tk()
        self.janela.geometry("420x400+100+100")
        self.janela["bg"] = "pink"
        self.janela.title("Funcionário")


        frame = LabelFrame(self.janela,text='Adicionar Novo')
        frame.grid(row=0,column=1)

        Label(frame,text='Nome').grid(row=1,column=1)
        self.name = Entry(frame)
        self.name.grid(row=1,column=2)
        
        Label(frame,text='CPF').grid(row=2,column=1)
        self.cpf = Entry(frame)
        self.cpf.grid(row=2,column=2)

        Label(frame,text='Sexo').grid(row=3,column=1)
        self.sexo = Entry(frame)
        self.sexo.grid(row=3,column=2)

        Label(frame,text='Ano Nascimento').grid(row=4,column=1)
        self.anoNascimento = Entry(frame)
        self.anoNascimento.grid(row=4,column=2)
        
        Button(frame,text='Adicionar',command=self.add_func).grid(row=5,column=2)
        self.message = Label(text='')
        self.message.grid(row=5,column=0)
        
        
        self.tree = ttk.Treeview(self.janela,height=10,column=2)
        self.tree.grid(row=6,column=0,columnspan=2)
        self.tree.heading('#0',text='Nome',anchor=W)
        self.tree.heading(2,text='CPF',anchor=W)

        Button(self.janela,text='Deletar').grid(row=7,column=0)
        Button(self.janela,text='Editar').grid(row=7,column=1)

        self.janela.mainloop()


    def add_func(self):
        nome = self.name.get()
        cpf =  self.cpf.get()
        sexo = self.sexo.get()
        anoNascimento = self.anoNascimento.get()
        
        Funcionario_ORM.add_funcionario(nome,cpf,sexo,anoNascimento)



class Fornecedor_Window:
    def __init__(self):
        self.janela2 = Tk()
        self.janela2.geometry("420x400+100+100")
        self.janela2["bg"] = "pink"
        self.janela2.title("Fornecedor")


        frame2 = LabelFrame(self.janela2,text='Adicionar Novo')
        frame2.grid(row=0,column=1)

        Label(frame2,text='Nome').grid(row=1,column=1)
        self.name2 = Entry(frame2)
        self.name2.grid(row=1,column=2)
        
        Label(frame2,text='CNPJ').grid(row=2,column=1)
        self.cnpj = Entry(frame2)
        self.cnpj.grid(row=2,column=2)

        Button(frame2,text='Adicionar',command=self.add_forn).grid(row=3,column=2)
        self.message = Label(text='')
        self.message.grid(row=3,column=0)
        
        
        self.tree = ttk.Treeview(self.janela2,height=10,column=2)
        self.tree.grid(row=4,column=0,columnspan=2)
        self.tree.heading('#0',text='Nome',anchor=W)
        self.tree.heading(2,text='CNPJ',anchor=W)

        Button(self.janela2,text='Deletar').grid(row=5,column=0)
        Button(self.janela2,text='Editar').grid(row=5,column=1)

        self.janela2.mainloop()


    def add_forn(self):
        nome = self.name2.get()
        cnpj = self.cnpj.get()
        Fornecedor_ORM.add_fornecedor(nome,cnpj)



class Produto_Window:
    def __init__(self):
        self.janela3 = Tk()
        self.janela3.geometry("420x400+100+100")
        self.janela3["bg"] = "pink"
        self.janela3.title("Produto")


        frame3 = LabelFrame(self.janela3,text='Adicionar Novo')
        frame3.grid(row=0,column=1)

        Label(frame3,text='Nome').grid(row=1,column=1)
        self.name3 = Entry(frame3)
        self.name3.grid(row=1,column=2)
        
        Label(frame3,text='Preco').grid(row=2,column=1)
        self.price = Entry(frame3)
        self.price.grid(row=2,column=2)

        Label(frame3,text='Quantidade').grid(row=3,column=1)
        self.quant = Entry(frame3)
        self.quant.grid(row=3,column=2)


        Button(frame3,text='Adicionar',command=self.add_prod).grid(row=4,column=2)
        self.message = Label(text='')
        self.message.grid(row=4,column=0)
        
        
        self.tree = ttk.Treeview(self.janela3,height=10,column=2)
        self.tree.grid(row=5,column=0,columnspan=2)
        self.tree.heading('#0',text='Nome',anchor=W)
        self.tree.heading(2,text='CNPJ',anchor=W)

        Button(self.janela3,text='Deletar').grid(row=6,column=0)
        Button(self.janela3,text='Editar').grid(row=6,column=1)

        self.janela3.mainloop()


    def add_prod(self):
        nome = self.name3.get()
        preco = self.price.get()
        quantidade = self.quant.get()
        Produto_ORM.add_produto(nome,preco,quantidade)








        #WIDGETS
'''
        self.lb1 = Label(self.janela,text="Nome",bg="white")
        self.lb2 = Label(self.janela,text="CPF",bg="white")
        self.lb3 = Label(self.janela,text="Sexo",bg="white")
        self.lb4 = Label(self.janela,text="Ano de Nascimento",bg="white")

        self.ed_name = Entry(self.janela,)
        self.ed_cpf = Entry(self.janela,)
        self.ed_sexo = Entry(self.janela,)
        self.ed_anoNascimento = Entry(self.janela,)

        self.btn1 = Button(self.janela, text="Confirmar", command=self.add)
        self.btn2 = Button(self.janela, text="Cancelar", command=self.exit_add)

        #LAYOUT
        self.lb1.grid(row=0,column=0)
        self.lb2.grid(row=1,column=0)
        self.lb3.grid(row=2,column=0)
        self.lb4.grid(row=3,column=0)

        self.ed_name.grid(row=0,column=1)
        self.ed_cpf.grid(row=1,column=1)
        self.ed_sexo.grid(row=2,column=1)
        self.ed_anoNascimento.grid(row=3,column=1)

        self.btn1.grid(row=6,column=1,sticky=W)
        self.btn2.grid(row=6,column=1,sticky=E)
'''
        

   
    
