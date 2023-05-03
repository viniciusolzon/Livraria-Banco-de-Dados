from initializer import tables

def main():
    for row in tables['usuario'].read_all():
        print(row)

    print()

    for row in tables['livro'].read_all():
        print(row)

if __name__ == "__main__":
    main()
