from connect import *
import readFilms
import time

def update():
    idField = input("Enter the filmID of the record to be updated: ")
    fieldName = input("Enter field name (Title/yearReleased/Rating/Duration/Genre): ").title()

    newFieldValue = input(f"Enter the value for the {fieldName} field: ")
    newFieldValue = "'" + newFieldValue+ "'"

    cursor.execute(f"UPDATE tblFilms SET {fieldName} = {newFieldValue} WHERE filmID = {idField}")
    conn.commit()

    print(f"Record {idField} updated in the films table.")
    time.sleep(3)

    readFilms.read()
 
if __name__ == "__main__":
    update()