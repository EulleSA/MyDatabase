from View.MainWindow import *
from pony.orm import *



if __name__ == "__main__":
    db = Database()
    db.bind(provider='sqlite', filename='database.sqlite', create_db=True)
    db.generate_mapping(create_tables=True)

    root = Tk()
        
    MainWindow(root)
    root.mainloop()
    
