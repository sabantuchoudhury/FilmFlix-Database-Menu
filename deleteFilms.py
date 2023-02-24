from connect import *
import readFilms
import time

def delete():
    idField = input("Enter the filmID of the record to be deleted: ")

    cursor.execute(f"DELETE FROM tblFilms WHERE filmID = {idField}")
    conn.commit()

    print(f"Record {idField} deleted from the films table.")
    time.sleep(3)
    readFilms.read()

if __name__ == "__main__":
    delete()