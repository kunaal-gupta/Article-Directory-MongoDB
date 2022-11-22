import os

def search_articles():
    clearTerminal()
    print("search_articles")

def search_authors():
    clearTerminal()
    print()

def list_venues():
    clearTerminal()
    print()

def add_article():
    clearTerminal()
    print()

def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the system terminal to look cleaner

def menu():

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
            search_authors()

        elif user_option == "3":
            list_venues()

        elif user_option == "4":
            add_article()

        elif user_option == "5":
            print("Going to Quit")
            quit()

        else:
            print("Please enter a valid Option #")


def main():
    menu()

if __name__ == "__main__":
    main()