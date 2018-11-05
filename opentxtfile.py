import mysql
from mysql.connector import connection
from tkinter import *
import mysql.connector


def create_txtfile():
    filnamn = input("Creating an txtfile: name your file: ")
    with open(filnamn + ".txt", "w") as f:
        print("You\'r file is created: named: {0}".format(filnamn))


def read_txtfile():
    filnamn = input("Wich txtfile you wanna read?:\nProfiles?[j/n] ")
    if filnamn == "j" or filnamn == "J":
        with open('profiles.txt', 'r') as f:
            for line in f:
                line = line.rstrip()
                print(line)

    else:
        print("No access to others files, right now")


def write_totxtfile():
    filnamn = input("Wich txtfile you wanna write to? ")
    with open(filnamn + ".txt", "a+") as f:
        f.writelines(input("\nPress enter to  return to menu\nSkriv in det du vill skriva:\n"))


def dbtextfile():
    root = Tk()
    root.title("dbtextfile")
    root.geometry("400x100")
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='profiles',
                                             user='root',
                                             password='root')

        sql_insert_query = ''' SELECT * FROM profiles '''

        filnamn = input("Wich txtfile you wanna write to? ")
        with open(filnamn + ".txt", "a+") as f:
            f.writelines(input(sql_insert_query))
            cursor = connection.cursor()
        result = cursor.execute(sql_insert_query)
        for row in cursor.fetchall():
            label = Label(root, text=row)
            label.pack()
        connection.commit()

        for row in cursor.fetchall():
            label = Label(root, text=str(row))
            print(filnamn, row[0])
            label.pack()

            label = Label(root, text="Reading Database now")
            label.pack()

    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        label = Label(root, text="Read from Database  misslyckades {}".format(error))
        label.pack()
    finally:
        # closing database connection.
        if connection.is_connected():
            cursor.close()
            connection.close()
            label = Label(root, text="MySQL koppling nerkopplad")
            label.pack()
    connection.close()
    root.mainloop()


def read_about():
    with open('aboutplayground.txt', 'r') as f:
        for line in f:
            line = line.rstrip()
            print(line)
