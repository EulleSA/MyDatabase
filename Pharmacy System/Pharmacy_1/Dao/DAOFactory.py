from sys import path
path.append("..")
from Dao import *


class DAOFactory:
    def __init__(self,db):
        self.db = db
    
    def get_FuncionarioDAO(self):
        return PostgresqlDAO.FuncionarioDAO(self.db)
