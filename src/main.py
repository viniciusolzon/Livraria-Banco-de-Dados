# adding tables folder to the system path
# import sys
# sys.path.insert(0, '../tables')

# from usuario import PersonTable
 
from initializer import tables

def main():
    for row in tables['usuario'].query("SELECT * FROM usuario"):
        print(row)
    
    

if __name__ == "__main__":
    main()
