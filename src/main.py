import sys
# adding tables folder to the system path
sys.path.insert(1, '../tables')

from person import PersonTable
 

def main():
    tables = {}

    tables['person'] = PersonTable()

    tables['person'].insert("Vinicius", 20, "M")
    tables['person'].insert("Victor Mororo", 21, "M")
    
    print(tables['person'].query("SELECT * FROM person"))


if __name__ == "__main__":
    main()
