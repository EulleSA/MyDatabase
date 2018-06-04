import Model.Models
from pony.orm import *


class Funcionario_ORM:

    @db_session
    def add_funcionario(nome,cpf,sexo,anoNascimento):
        Model.Models.Funcionario(nome=nome, cpf=cpf, sexo=sexo, anoNascimento=anoNascimento)
    


class Fornecedor_ORM:
    @db_session
    def add_fornecedor(nome,cnpj):
        Model.Models.Fornecedor(nome=nome,cnpj=cnpj)


class Produto_ORM:
    @db_session
    def add_produto(nome,preco,quantidade):
        Model.Models.Produto(nome=nome,preco=preco,quantidade=quantidade)