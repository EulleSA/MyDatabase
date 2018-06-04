import datetime
from pony.orm import *

db = Database()

class Funcionario(db.Entity):
    nome = Required(str)
    cpf = Required(str)
    sexo = Required(str)
    anoNascimento = Required(str)


class Produto(db.Entity):
    nome = Required(str)
    preco = Required(float)
    quantidade = Required(int)

class Fornecedor(db.Entity):
    nome = Required(str)
    cnpj = Required(int)

db.bind(provider='sqlite', filename='database.sqlite', create_db=True)
db.generate_mapping(create_tables=True)