
from View.MainWindow import *
from Dao.DAOFactory import *
from pymongo import *
import psycopg2

class Pharmacy:
    def __init__(self):
        self.conn = psycopg2.connect(host='localhost', database='postgres',user='postgres', password='postgres')
        self.conn.set_session(autocommit=True)
        self.database = self.conn.cursor()

        root = Tk()

        self.dao_factory = DAOFactory(self.database)
        MainWindow(root,self.dao_factory)
        root.mainloop()

if __name__ == "__main__":

    phm = Pharmacy()
    phm.conn.close()


  



