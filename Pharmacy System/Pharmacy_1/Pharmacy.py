
from View.MainWindow import *
from pymongo import *
import psycopg2
if __name__ == "__main__":

    con = psycopg2.connect(host='localhost', database='postgres',user='postgres', password='postgres')
    con.set_session(autocommit=True)
    database = con.cursor()


    root = Tk()

    MainWindow(root)
    root.mainloop()



