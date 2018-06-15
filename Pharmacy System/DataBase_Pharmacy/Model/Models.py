import datetime
from pony.orm import *

db = Database()

class Funcionario(db.Entity):
    nome = Required(str)
    cpf = Required(str,unique=True)
    sexo = Required(str)
    anoNascimento = Required(str)
    produto = Set('Produto')

class Fornecedor(db.Entity):
    nome = Required(str)
    cnpj = Required(int,unique=True)
    produto = Set('Produto')

class Produto(db.Entity):
    nome = Required(str)
    preco = Required(float)
    quantidade = Required(int)
    fornecedor = Required(Fornecedor)
    funcionario = Required(Funcionario)

db.bind(provider='sqlite', filename='database.sqlite', create_db=True)
db.generate_mapping(create_tables=True)