from connect import *
import readFilms
import time

def insertFilms():
    films = []
    
    title = input("Enter film title: ").title()
    releaseYear = input("Enter the year the film released: ")
    rating = input("Enter film rating: ").upper()
    duration = input("Enter film duration: ")
    genre = input("Enter film genre: ").title()

    films.append(title)
    films.append(releaseYear)
    films.append(rating)
    films.append(duration)
    films.append(genre)

    cursor.execute("INSERT INTO tblFilms VALUES(NULL, ?,?,?,?,?)", films)
    conn.commit()

    print(f"Title {title} inserted into the films table.")
    time.sleep(3)
    readFilms.read()
 
if __name__ == "__main__":
    insertFilms()
