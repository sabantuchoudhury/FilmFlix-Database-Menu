import readFilms
import addFilms
import deleteFilms
import updateFilms
import searchQueries

separator = "--------------------------------------------------"

def crudMenu():
    options = 0
    while options not in ["1","2","3","4","5"]:
        print(" FilmFlix\nCRUD Options")
        print(separator)
        print("Enter:\n1. Add a record.\n2. Delete a record.\n3. Amend a record.\n4. Print all records.\n5. Back.")
        print(separator)
        options = input("Enter an option from the menu choices above: ")
        if options not in ["1","2","3","4","5"]:
            print(f"{options} is not a valid number.")
    return options

def reportMenu():
    options = 0
    while options not in ["1","2","3","4","5"]:
        print(" FilmFlix\nReport Options")
        print(separator)
        print("Enter:\n1. Show details for a film.\n2. Show all films in a specified genre.\n3. Show all films in a specified year.\n4. Show all films of a specified rating.\n5. Back.")
        print(separator)
        options = input("Enter an option from the menu choices above: ")
        if options not in ["1","2","3","4","5"]:
            print(f"{options} is not a valid number.")
    return options

def crudMenuOption():
    mainProgram = True
    while mainProgram:
        print(separator)
        mainMenu = crudMenu()
        if mainMenu == "1":
            addFilms.insertFilms()
        elif mainMenu == "2":
            deleteFilms.delete()
        elif mainMenu == "3":
            updateFilms.update()
        elif mainMenu == "4":
            readFilms.read()
        else:
            mainProgram = False

def reportMenuOption():
    mainProgram = True
    while mainProgram:
        print(separator)
        mainMenu = reportMenu()
        if mainMenu == "1":
            searchQueries.searchName()
        elif mainMenu == "2":
            searchQueries.searchGenre()
        elif mainMenu == "3":
            searchQueries.searchYear()
        elif mainMenu == "4":
            searchQueries.searchRating()
        else:
            mainProgram = False

mainProgram = True
while mainProgram:
    print(separator)
    print("1. CRUD Options.\n2. Report Options.\n3. Exit.")
    print(separator)
    mainMenu = input("Select which menu you would like to access: ")
    if mainMenu == "1":
        crudMenuOption()
    elif mainMenu == "2":
        reportMenuOption()
    else:
        mainProgram = False

