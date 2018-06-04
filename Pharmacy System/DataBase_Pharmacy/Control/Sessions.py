
import Model.Models
from pony.orm import *


class Funcionario_ORM:

    @db_session
    def add_funcionario(nome,cpf,sexo,anoNascimento):
        Model.Models.Funcionario(nome=nome, cpf=cpf, sexo=sexo, anoNascimento=anoNascimento)