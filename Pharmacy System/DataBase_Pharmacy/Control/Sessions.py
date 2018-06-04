
import Model.Models
from pony.orm import *


class Funcionario_ORM:

    @db_session
    def add_funcionario(self,nome,cpf,sexo,anoNascimento):
        Model.Models.Funcionario(nome=self.nome, cpf=self.cpf, sexo=self.sexo, anoNascimento=self.anoNascimento)