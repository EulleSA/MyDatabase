
from View.MainWindow import *
from pymongo import *

if __name__ == "__main__":
    
    client = MongoClient('mongodb://localhost:27017/')
    banco = client.Pharmacy
    produto = banco.produto
    funcionario = banco.funcionario
    fornecedor = banco.fornecedor

    root = Tk()
        
    MainWindow(root)
    root.mainloop()



