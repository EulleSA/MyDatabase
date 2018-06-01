from sys import path
path.append("..")
from .MainWindow import *


class Add_Funcionario_Window:
    def __init__(self):
        self.janela = Tk()
        self.janela.geometry("350x200+100+100")
        self.janela["bg"] = "pink"
        self.janela.title("Cadastrar Funcionário")
        
        #WIDGETS

        self.lb1 = Label(self.janela,text="Nome",bg="white")
        self.lb2 = Label(self.janela,text="CPF",bg="white")
        self.lb3 = Label(self.janela,text="Sexo",bg="white")
        self.lb4 = Label(self.janela,text="Ano de Nascimento",bg="white")

        self.ed_name = Entry(self.janela,)
        self.ed_cpf = Entry(self.janela,)
        self.ed_sexo = Entry(self.janela,)
        self.ed_anoNascimento = Entry(self.janela,)

        self.btn1 = Button(self.janela, text="Confirmar")
        self.btn2 = Button(self.janela, text="Cancelar")

        #LAYOUT
        self.lb1.grid(row=0,column=0)
        self.lb2.grid(row=1,column=0)
        self.lb3.grid(row=2,column=0)
        self.lb4.grid(row=3,column=0)

        self.ed_name.grid(row=0,column=1)
        self.ed_cpf.grid(row=1,column=1)
        self.ed_sexo.grid(row=2,column=1)
        self.ed_anoNascimento.grid(row=3,column=1)

        self.btn1.grid(row=6,column=1,sticky=W,command=self.add)
        self.btn2.grid(row=6,column=1,sticky=E,command=self.cancelar)

        self.janela.mainloop()

    with db_session:
        def add(self):
            Funcionario(nome=self.ed_name.get(),cpf=int(self.ed_cpf.get()),sexo=self.ed_sexo.get(),anoNascimento=self.ed_anoNascimento.get())
            
    def cancelar(self):
        self.janela.destroy()
