
from .MainWindow import *
from sys import path
path.append("..")
import tkinter.ttk as ttk
from Control.Sessions import *
from Model.Models import *

class Funcionario_Window:
    def __init__(self):
        self.janela = Tk()
        self.janela.geometry("650x450+100+100")
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
        self.message = Label(self.janela,text='',font=('arial',8),fg='red')
        self.message.grid(row=5,column=1)
        
        
        self.tree = ttk.Treeview(self.janela,height=10,columns=('Id','Nome'))
        self.tree.grid(row=6,column=0,columnspan=3)
        self.tree.heading('#0',text='Id',anchor=W)
        self.tree.heading('#1',text='Nome',anchor=W)
        self.tree.heading('#2',text='CPF',anchor=W)

        Button(self.janela,text='Deletar',command=self.delete_func).grid(row=7,column=0)
        Button(self.janela,text='Editar',command=self.edit_func).grid(row=7,column=1)

        Funcionario_ORM.get_fuc_all(self.tree)

        self.janela.mainloop()

    def add_func(self):
        nome = self.name.get()
        cpf =  self.cpf.get()
        sexo = self.sexo.get()
        anoNascimento = self.anoNascimento.get()
        if(len(self.name.get()) != 0 and len(self.cpf.get()) != 0 and len(self.sexo.get()) != 0 and len(self.anoNascimento.get())!=0):
            Funcionario_ORM.add_funcionario(nome,cpf,sexo,anoNascimento)
            self.message['text'] = 'Funcionario {} ADICIONADO COM SUCESSO '.format(self.name.get())
            self.name.delete(0,END)
            self.cpf.delete(0,END)
            self.sexo.delete(0,END)
            self.anoNascimento.delete(0,END)
            Funcionario_ORM.get_fuc_all(self.tree)
        else:
            self.message['text'] = 'POR FAVOR, INSIRA VALORES NOS CAMPOS FALTANTES!'
            

    def delete_func(self):
        Funcionario_ORM.delete_one_func(self.tree)
        self.message['text'] = 'FUNCIONARIO DELETADO COM SUCESSO ! '

    def edit_func(self):
        if(len(self.name.get()) != 0):
            Funcionario_ORM.edit_func_nome(self.tree,self.name.get())
        if(len(self.cpf.get()) != 0):
            Funcionario_ORM.edit_func_cpf(self.tree,self.cpf.get())
        if(len(self.sexo.get()) != 0):
            Funcionario_ORM.edit_func_sexo(self.tree,self.sexo.get())
        if(len(self.anoNascimento.get()) != 0):
            Funcionario_ORM.edit_func_anoNascimento(self.tree,self.anoNascimento.get())
        Funcionario_ORM.get_fuc_all(self.tree)


class Fornecedor_Window:
    def __init__(self):
        self.janela2 = Tk()
        self.janela2.geometry("650x400+100+100")
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
        self.message = Label(self.janela2,text='',font=('arial',8),fg='red')
        self.message.grid(row=3,column=1)
        
        self.tree = ttk.Treeview(self.janela2,height=10,columns=('Id','Nome'))
        self.tree.grid(row=4,column=0,columnspan=3)
        self.tree.heading('#0',text='Id',anchor=W)
        self.tree.heading('#1',text='Nome',anchor=W)
        self.tree.heading('#2',text='CNPJ',anchor=W)

        Button(self.janela2,text='Deletar',command=self.delete_forn).grid(row=5,column=0)
        Button(self.janela2,text='Editar',command=self.edit_forn).grid(row=5,column=1)

        Fornecedor_ORM.get_forn_all(self.tree)

        self.janela2.mainloop()


    def add_forn(self):
        nome = self.name2.get()
        cnpj = self.cnpj.get()
        if(len(self.name2.get()) != 0 and len(self.cnpj.get()) != 0):
            Fornecedor_ORM.add_fornecedor(nome,cnpj)
            self.message['text'] = 'FORNECEDOR {} ADICIONADO COM SUCESSO '.format(self.name2.get())
            self.name2.delete(0,END)
            self.cnpj.delete(0,END)
            
            Fornecedor_ORM.get_forn_all(self.tree)
        else:
            self.message['text'] = 'POR FAVOR, INSIRA VALORES NOS CAMPOS FALTANTES!'

    def delete_forn(self):
        Fornecedor_ORM.delete_one_forn(self.tree)
        self.message['text'] = 'FORNECEDOR DELETADO COM SUCESSO ! '
    
    def edit_forn(self):
        if(len(self.name2.get()) != 0):
            Fornecedor_ORM.edit_forn_nome(self.tree,self.name2.get())
        if(len(self.cnpj.get()) != 0):
            Fornecedor_ORM.edit_forn_cnpj(self.tree,self.cnpj.get())
        
        Fornecedor_ORM.get_forn_all(self.tree)


class Produto_Window:
    def __init__(self):
        self.janela3 = Tk()
        self.janela3.geometry("650x500+100+100")
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

        Label(frame3,text='Fornecedor').grid(row=4,column=1)        
        self.forn = Entry(frame3)
        self.forn.grid(row=4,column=2)

        Label(frame3,text='Funcionario').grid(row=5,column=1)
        self.func = Entry(frame3)
        self.func.grid(row=5,column=2) 

        Button(frame3,text='Adicionar',command=self.add_prod).grid(row=6,column=2)
        self.message = Label(self.janela3,text='',font=('arial',8),fg='red')
        self.message.grid(row=6,column=0)
        
        self.tree = ttk.Treeview(self.janela3,height=10,columns=('Id','Nome'))
        self.tree.grid(row=7,column=0,columnspan=3)
        self.tree.heading('#0',text='Id',anchor=W)
        self.tree.heading('#1',text='Nome',anchor=W)
        self.tree.heading('#2',text='Preco',anchor=W)
        Button(self.janela3,text='Deletar',command=self.delete_prod).grid(row=8,column=0)
        Button(self.janela3,text='Editar',command=self.edit_prod).grid(row=8,column=1)


        Produto_ORM.get_prod_all(self.tree)

        self.janela3.mainloop()

    def add_prod(self):
        nome = self.name3.get()
        preco = self.price.get()
        quantidade = self.quant.get()
        fornecedor = self.forn.get()
        funcionario = self.func.get()
        if(len(self.name3.get()) != 0 and len(self.price.get()) != 0 and len(self.quant.get()) != 0 ):
            Produto_ORM.add_produto(nome,preco,quantidade,fornecedor,funcionario)
            self.message['text'] = 'PRODUTO {} ADICIONADO COM SUCESSO '.format(nome)
            self.name3.delete(0,END)
            self.price.delete(0,END)
            self.quant.delete(0,END)
            self.forn.delete(0,END)
            self.func.delete(0,END)
            Produto_ORM.get_prod_all(self.tree)
        else:
            self.message['text'] = 'POR FAVOR, INSIRA VALORES NOS CAMPOS FALTANTES!'

    def delete_prod(self):
        Produto_ORM.delete_one_prod(self.tree)
        self.message['text'] = 'PRODUTO DELETADO COM SUCESSO !'

    def edit_prod(self):
        if(len(self.name3.get()) != 0):
            Produto_ORM.edit_prod_nome(self.tree,self.name3.get())
        if(len(self.price.get()) != 0):
            Produto_ORM.edit_prod_price(self.tree,self.price.get())
        if(len(self.quant.get()) != 0):
            Produto_ORM.edit_prod_quant(self.tree,self.quant.get())
        Produto_ORM.get_prod_all(self.tree)
