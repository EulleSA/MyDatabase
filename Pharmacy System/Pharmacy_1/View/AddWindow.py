 
from .MainWindow import *
from sys import path
path.append("..")
import tkinter.ttk as ttk
from Dao.PostgresqlDAO import *
#from Control.Controller import *
#from Control.Sessions import *
#from Model.Models import *

class Funcionario_Window:
    def __init__(self,dao_factory):

        self.dao_factory = dao_factory

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
        self.tree.heading('#0',text='Nome',anchor=W)
        self.tree.heading('#1',text='CPF',anchor=W)
        self.tree.heading('#2',text='Sexo',anchor=W)

        Button(self.janela,text='Deletar',command=self.delete_func).grid(row=7,column=0)
        Button(self.janela,text='Editar', command=self.edit_func).grid(row=7,column=1)

        self.get_funcs()

        self.janela.mainloop()

    def add_func(self):
        nome = self.name.get()
        cpf =  self.cpf.get()
        sexo = self.sexo.get()
        anoNascimento = self.anoNascimento.get()
        if(len(self.name.get()) != 0 and len(self.cpf.get()) != 0 and len(self.sexo.get()) != 0 and len(self.anoNascimento.get())!=0):
            
            #Linha 65 deverá ser tratada no arquivo control
            func = Funcionario(nome,cpf,sexo,anoNascimento)
            funcDAO = self.dao_factory.get_FuncionarioDAO()
            funcDAO.insert_func(func)
            
            self.message['text'] = 'Funcionario {} ADICIONADO COM SUCESSO '.format(self.name.get())
            self.name.delete(0,END)
            self.cpf.delete(0,END)
            self.sexo.delete(0,END)
            self.anoNascimento.delete(0,END)
            #FuncionarioDAO.create_table(self.dao_factory)
            
            #Não precisa mudar da linha 78-84     
            self.get_funcs()
            
        else:
            self.message['text'] = 'POR FAVOR, INSIRA VALORES NOS CAMPOS FALTANTES!'
            

    def get_funcs(self):

        funcDAO = self.dao_factory.get_FuncionarioDAO()

        records = self.tree.get_children()
        for elements in records:
            self.tree.delete(elements)

        get_func = funcDAO.get_func_all(self.dao_factory)
        for row in get_func:
            self.tree.insert('','end',text=row.nome,values=(row.cpf,row.sexo))

    def delete_func(self):

        curItem = self.tree.focus()
        contents = (self.tree.item(curItem))
        selecteditem = contents['text']
        
        funcDAO = self.dao_factory.get_FuncionarioDAO()
        funcDAO.delete_one_func(selecteditem)
        self.tree.delete(curItem)

        self.message['text'] = 'FUNCIONARIO DELETADO COM SUCESSO ! '



    def edit_func(self):

        funcDAO = self.dao_factory.get_FuncionarioDAO()
    
        if(len(self.name.get()) != 0):
            curItem = self.tree.focus()
            contents = (self.tree.item(curItem))
            selecteditem = contents['text']
            funcDAO.edit_func_nome(self.name.get(), selecteditem)
            self.get_func()
            self.message['text'] = 'NOME DO FUNCIONÁRIO ATUALIZADO COM SUCESSO !'

        elif(len(self.cpf.get()) != 0):
            curItem = self.tree.focus()
            contents = (self.tree.item(curItem))
            selecteditem = contents['text']
            funcDAO.edit_func_cpf(self.cpf.get(),selecteditem)
            self.get_func()
            self.message['text'] = 'CPF DO FUNCIONÁRIO ATUALIZADO COM SUCESSO !'

        elif(len(self.sexo.get()) != 0):
            curItem = self.tree.focus()
            contents = (self.tree.item(curItem))
            selecteditem = contents['text']
            funcDAO.edit_func_sexo(self.sexo.get(),selecteditem)
            self.get_func()
            self.message['text'] = 'SEXO DO FUNCIONÁRIO ATUALIZADO COM SUCESSO !'

        elif(len(self.anoNascimento.get()) != 0):
            curItem = self.tree.focus()
            contents = (self.tree.item(curItem))
            selecteditem = contents['text']
            funcDAO.edit_func_sexo(self.anoNascimento.get(),selecteditem)
            self.get_func()
            self.message['text'] = 'ANO DE NASCIMENTO DO FUNCIONÁRIO ATUALIZADO COM SUCESSO !'
        


class Fornecedor_Window:
    def __init__(self,dao_factory):

        self.dao_factory = dao_factory

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

        Label(frame2,text='Funcionario').grid(row=3,column=1)
        self.func = Entry(frame2)
        self.func.grid(row=3,column=2)

        Button(frame2,text='Adicionar',command=self.add_forn).grid(row=4,column=2)
        self.message = Label(self.janela2,text='',font=('arial',8),fg='red')
        self.message.grid(row=4,column=1)
        
        self.tree = ttk.Treeview(self.janela2,height=10,columns=('Id','Nome'))
        self.tree.grid(row=5,column=0,columnspan=3)
        self.tree.heading('#0',text='Nome',anchor=W)
        self.tree.heading('#1',text='CNPJ',anchor=W)
        #self.tree.heading('#2',text='CNPJ',anchor=W)

        Button(self.janela2,text='Deletar',command=self.delete_forn).grid(row=6,column=0)
        Button(self.janela2,text='Editar').grid(row=6,column=1)

        #fornDAO = self.dao_factory.get_FornecedorDAO()

        #fornDAO.create_table()

        self.get_forns()

        self.janela2.mainloop()


    def add_forn(self):
        
        nome = self.name2.get()
        cnpj = self.cnpj.get()
        func = self.func.get()

        if(len(self.name2.get()) != 0 and len(self.cnpj.get()) != 0):
            
            funcionario = self.dao_factory.get_FuncionarioDAO().get_from_name(func)

            fornecedor = Fornecedor(nome,cnpj,funcionario)
            fornDAO = self.dao_factory. get_FornecedorDAO()
            fornDAO.insert_forn(fornecedor)

            self.message['text'] = 'FORNECEDOR {} ADICIONADO COM SUCESSO '.format(self.name2.get())
            self.name2.delete(0,END)
            self.cnpj.delete(0,END)
            self.func.delete(0,END)
            
            self.get_forns()

        else:
            self.message['text'] = 'POR FAVOR, INSIRA VALORES NOS CAMPOS FALTANTES!'



    def get_forns(self):

        fornDAO = self.dao_factory.get_FornecedorDAO()

        records = self.tree.get_children()
        for elements in records:
            self.tree.delete(elements)
        get_forn = fornDAO.get_forn_all(self.dao_factory)
        for row in get_forn:
            self.tree.insert('','end',text=row.nome,values=row.cnpj)

    def delete_forn(self):
        curItem = self.tree.focus()
        contents = (self.tree.item(curItem))
        selecteditem = contents['text']
        
        fornDAO = self.dao_factory.get_FornecedorDAO()
        fornDAO.delete_one_forn(selecteditem)
        self.tree.delete(curItem)

        self.message['text'] = 'FORNECEDOR DELETADO COM SUCESSO ! '
 
    def edit_forn(self):
        
        fornDAO = self.dao_factory.get_FornecedorDAO()

        if(len(self.name2.get()) != 0):

            curItem = self.tree.focus()
            contents = (self.tree.item(curItem))
            selecteditem = contents['text']
            fornDAO.edit_forn_nome(self.name2.get(), selecteditem)
            self.get_forns()
            self.message['text'] = 'NOME DO FORNECEDOR ATUALIZADO COM SUCESSO !'

        elif(len(self.cnpj.get()) != 0):
            curItem = self.tree.focus()
            contents = (self.tree.item(curItem))
            selecteditem = contents['text']
            fornDAO.edit_forn_cnpj(self.cnpj.get())
            self.get_func()
            self.message['text'] = 'NOME DO FORNECEDOR ATUALIZADO COM SUCESSO !'
        
        


class Produto_Window:
    def __init__(self,dao_factory):
        self.dao_factory = dao_factory

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
        self.tree.heading('#0',text='Nome',anchor=W)
        self.tree.heading('#1',text='Preco',anchor=W)
        self.tree.heading('#2',text='Quantidade',anchor=W)
        Button(self.janela3,text='Deletar',command=self.delete_prod).grid(row=8,column=0)
        Button(self.janela3,text='Editar',command=self.edit_prod).grid(row=8,column=1)

        #prodDAO = self.dao_factory.get_ProdutoDAO()
        #prodDAO.create_table()

        self.get_prods()

        self.janela3.mainloop()

    def add_prod(self):
        nome = self.name3.get()
        preco = self.price.get()
        quantidade = self.quant.get()
        forn = self.forn.get()
        func = self.func.get()
        if(len(self.name3.get()) != 0 and len(self.price.get()) != 0 and len(self.quant.get()) != 0 ):

            funcionario = self.dao_factory.get_FuncionarioDAO().get_from_name(func)
            fornecedor = self.dao_factory.get_FornecedorDAO().get_from_name(forn)

            produto = Produto(nome,preco,quantidade,fornecedor, funcionario)
            produto_dao = self.dao_factory.get_ProdutoDAO() 
            produto_dao.insert_prod(produto)
            self.get_prods()
            self.message['text'] = 'PRODUTO {} ADICIONADO COM SUCESSO '.format(nome)
            self.name3.delete(0,END)
            self.price.delete(0,END)
            self.quant.delete(0,END)
            self.forn.delete(0,END)
            self.func.delete(0,END)
            
        else:

            self.message['text'] = 'POR FAVOR, INSIRA VALORES NOS CAMPOS FALTANTES!'

    def get_prods(self):

        prodDAO = self.dao_factory.get_ProdutoDAO()

        records = self.tree.get_children()
        for elements in records:
            self.tree.delete(elements)
        get_prod = prodDAO.get_prod_all(self.dao_factory)
        for row in get_prod:
            self.tree.insert('','end',text=row.nome,values=(row.preco,row.quantidade))


    def delete_prod(self):
        curItem = self.tree.focus()
        contents = (self.tree.item(curItem))
        selecteditem = contents['text']
        
        prodDAO = self.dao_factory.get_ProdutoDAO()
        prodDAO.delete_one_prod(selecteditem)
        self.tree.delete(curItem)

        self.message['text'] = 'PRODUTO DELETADO COM SUCESSO !'

    def edit_prod(self):
        prodDAO = self.dao_factory.get_ProdutoDAO()

        if(len(self.name3.get()) != 0):
            curItem = self.tree.focus()
            contents = (self.tree.item(curItem))
            selecteditem = contents['text']
            prodDAO.edit_prod_nome(self.name3.get(), selecteditem)
            self.get_prods()
            self.message['text'] = 'NOME DO PRODUTO ATUALIZADO COM SUCESSO !'

        elif(len(self.price.get()) != 0):
            curItem = self.tree.focus()
            contents = (self.tree.item(curItem))
            selecteditem = contents['text']
            prodDAO.edit_prod_price(self.price.get(),selecteditem)
            self.get_prods()
            self.message['text'] = 'PRECO DO PRODUTO ATUALIZADO COM SUCESSO !'

        elif(len(self.quant.get()) != 0):
            curItem = self.tree.focus()
            contents = (self.tree.item(curItem))
            selecteditem = contents['text']
            prodDAO.edit_prod_quant(self.quant.get(),selecteditem)
            self.get_prods()
            self.message['text'] = 'QUANTIDADE DO FORNECEDOR ATUALIZADO COM SUCESSO !'