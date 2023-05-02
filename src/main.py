# adding tables folder to the system path
# import sys
# sys.path.insert(0, '../tables')

# from person import PersonTable
 
from initializer import tables

def main():
    for row in tables['person'].query("SELECT * FROM person"):
        print(row)



if __name__ == "__main__":
    main()
