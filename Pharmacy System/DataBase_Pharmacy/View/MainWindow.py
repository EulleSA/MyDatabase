from tkinter import *
from .AddWindow import *
#from pony.orm import *


#https://www.pycursos.com/tkinter-sqlite3/
'''
class Funcionario:
    def __init__(self,nome,cpf,sexo,anoNascimento):
        self.nome = nome
        self.cpf = cpf
        self.sexo = sexo 
        self.anoNascimento = anoNascimento

    def __str__(self):
        return self.nome
'''


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
        Fornecedor_Window()
    
    def tela_produto(self):
        Produto_Window()



'''
# Acesso ao banco
class Funcionario(db.Entity):
    nome = Required(str)
    cpf = Required(int)
    sexo = Required(str)
    anoNascimento = Required(str)


    @db_session
    def add(self):
        Funcionario(nome=self.ed_name.get(),cpf=int(self.ed_cpf.get()),sexo=self.ed_sexo.get(),anoNascimento=self.ed_anoNascimento.get())


# Parte gráfica
def cadastro_funcionario():
    janela = Tk()
    janela.geometry("350x200+100+100")
    janela["bg"] = "pink"
    janela.title("Cadastrar Funcionário")
    
    #WIDGETS

    lb1 = Label(janela,text="Nome",bg="white")
    lb2 = Label(janela,text="CPF",bg="white")
    lb3 = Label(janela,text="Sexo",bg="white")
    lb4 = Label(janela,text="Ano de Nascimento",bg="white")

    ed_name = Entry(janela,)
    ed_cpf = Entry(janela,)
    ed_sexo = Entry(janela,)
    ed_anoNascimento = Entry(janela,)

    btn1 = Button(janela, text="Confirmar",command=add)
    btn2 = Button(janela, text="Cancelar")

    #LAYOUT
    lb1.grid(row=0,column=0)
    lb2.grid(row=1,column=0)
    lb3.grid(row=2,column=0)
    lb4.grid(row=3,column=0)

    ed_name.grid(row=0,column=1)
    ed_cpf.grid(row=1,column=1)
    ed_sexo.grid(row=2,column=1)
    ed_anoNascimento.grid(row=3,column=1)

    btn1.grid(row=6,column=1,sticky=W)
    btn2.grid(row=6,column=1,sticky=E)

    janela.mainloop()



db.bind(provider='sqlite', filename='database.sqlite', create_db=True)
db.generate_mapping(create_tables=True)


janela = Tk()
janela.title("Pharmacy System")


janela.mainloop()
'''