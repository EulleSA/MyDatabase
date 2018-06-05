import Model.Models
from pony.orm import *



class Funcionario_ORM:

    @db_session
    def add_funcionario(nome,cpf,sexo,anoNascimento):
        Model.Models.Funcionario(nome=nome, cpf=cpf, sexo=sexo, anoNascimento=anoNascimento)
    

    @db_session
    def get_fuc_all(tree):
        records = tree.get_children()
        for elements in records:
            tree.delete(elements)
        funcionario = Model.Models.Funcionario.select_by_sql('SELECT * FROM Funcionario')
        print(funcionario[1].nome)
        

class Fornecedor_ORM:
    @db_session
    def add_fornecedor(nome,cnpj):
        Model.Models.Fornecedor(nome=nome,cnpj=cnpj)



class Produto_ORM:
    @db_session
    def add_produto(nome,preco,quantidade):
        Model.Models.Produto(nome=nome,preco=preco,quantidade=quantidade)