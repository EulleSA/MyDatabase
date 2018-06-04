from Pharmacy import *
import datetime


class Funcionario(db.Entity):
    nome = Required(str)
    cpf = Required(str)
    sexo = Required(str)
    anoNascimento = Required(str)


class Produto(db.Entity):
    nome = Required(str)
    preco = Required(float)
    quantidade = Required(int)
    dataValidade = Required(datetime)
    dataFabricacao = Required(datetime)


class Fornecedor(db.Entity):
    nome = Required(str)
    cnpj = Required(int)
