from connect import *
import readFilms
import time

def searchName():
    genreName = input("Enter the name of the film you want to search for: ").title()

    cursor.execute(f"SELECT * FROM tblFilms WHERE title = '{genreName}'")
    row = cursor.fetchall()
    for record in row:
        print(record)
    time.sleep(3)

def searchGenre():
    genreName = input("Enter the genre you want to search for: ").title()

    cursor.execute(f"SELECT * FROM tblFilms WHERE genre = '{genreName}'")
    row = cursor.fetchall()
    for record in row:
        print(record)
    time.sleep(3)

def searchYear():
    year = input("Enter the year you want to search for: ").title()

    cursor.execute(f"SELECT * FROM tblFilms WHERE yearReleased = '{year}'")
    row = cursor.fetchall()
    for record in row:
        print(record)
    time.sleep(3)

def searchRating():
    rating = input("Enter the rating you want to search for: ").upper()

    cursor.execute(f"SELECT * FROM tblFilms WHERE rating = '{rating}'")
    row = cursor.fetchall()
    for record in row:
        print(record)
    time.sleep(3)
 
if __name__ == "__main__":
    searchName()
    searchGenre()
    searchYear()
    searchRating()