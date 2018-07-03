from Dao import *

class ControlFuncionario:
    def __init__(self,dao_factory):
        self.dao_factory = dao_factory


    def verifica_tabela_fornecedor(self):

        fornDAO = self.dao_factory.get_FornecedorDAO()
        if(fornDAO.get_forn_all() == []):
            return True
        else:
            return False

        