import os
from load import *
from search_authors import *


def create_conn(port):
    client = MongoClient(f"mongodb://localhost:{port}")

    db = client['291db']
    dblp = db["dblp"]
    return dblp

def search_articles():
    clearTerminal()
    print("search_articles")

def search_authors(dblp):
    # clearTerminal()
    search_for_authors(dblp)

def list_venues():
    clearTerminal()
    print()

def add_article():
    clearTerminal()
    print()

def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the system terminal to look cleaner

def menu(dblp):

    menu = "User Session\n1. Search for articles\n2. Search for authors \n3. List the venues\n4. Add an article \n5. Terminate the Program"
    while True:
        print(menu)

        # Ensure the expected input is provided and unexpected behaviour is elimated
        user_option = input(str("Please enter an option #: "))
        while (user_option not in ["1", "2", "3", "4", "5"]):
            clearTerminal()
            print(menu)
            user_option = input(str("Invalid option entered. Please enter an option #: "))

        if user_option == "1":
            search_articles()

        elif user_option == "2":
            clearTerminal()
            search_authors(dblp)

        elif user_option == "3":
            list_venues()

        elif user_option == "4":
            add_article()

        elif user_option == "5":
            print("Going to Quit")
            quit()

        else:
            print("Please enter a valid Option #")

def user_input():
    port_num = input("Port: ")
    print("See Port: "+port_num)
    port_num = int(port_num)
    dblp = create_conn(port_num)
    return dblp


def main():
    dblp = user_input()
    pprint(dblp)
    menu(dblp)

if __name__ == "__main__":
    main()
