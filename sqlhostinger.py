import mysql.connector

# use person;
# CREATE TABLE person(id INT NOT NULL AUTO_INCREMENT,name CHAR(255) NOT NULL,PRIMARY KEY (id)deafult charactet set= utf8);
# CREATE TABLE person(id INT NOT NULL AUTO_INCREMENT,name CHAR(255) NOT NULL,PRIMARY KEY (id));  ## Works
# show tables;

# create table person int auto_increment primary key, name varchar(255)default character set utf-8; #some wrongs
# desc person;
# show databases;
# use person;
# alter, ändra
# insert into tablename set name="Kalle karlsson";
# update tablename add column email varchar(255)

# connector - connect.py
# DBconnector - connect.py
"""
michelskoglund@hotmail.se


MySQL server hostname is: sql150.main-hosting.eu.
DATABASE                USERNAME
u209758462_miskb	u209758462_misk7
host: sql150.main-hosting.eu.

Email: michelskoglund@hotmail.se

"""

__author__ = 'Michel Skoglund'


def sqlhostingConnector():
    root = Tk()
    root.title("sqlhostingConnector")
    root.geometry("400x100")
    try:
        connect = mysql.connector.connect(
            user='u209758462_misk7',
            passwd='mi235277sk',
            host='sql150.main-hosting.eu',
            db='')
        label = Label(root, text=str(
            2 * '\n') + "Det Funkar!! Du har lyckats att koppla Dig till Din databas! på hosting.eu" + str(
            2 * '\n'))
        label.pack()

    except mysql.connector.Error as e:

        if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            label = Label(root,
                          text=str(
                              2 * '\n') + "Kopplingen fungerar inte!\n hosting.eu" + str(
                              2 * '\n'))
            label.pack()


        elif e.errno == errorcode.ER_BAD_DB_ERROR:
            label = Label(root, text=str(
                2 * '\n') + "Databas namn hittades inte!! \nhosting.eu" + str(2 * '\n'))
            label.pack()


        else:
            label = Label(root, text='\n' + str(e))
            label.pack()

    root.mainloop()


# SQl create Database # Cant create database at db4free  No Privileges
def sqlhostingCreateDatabase():
    root = Tk()
    root.title("sqlhostingCreateDatabase")
    root.geometry("400x100")
    try:
        connection = mysql.connector.connect(user='u209758462_misk7',
                                             passwd='mi235277sk',
                                             host='sql150.main-hosting.eu',
                                             db='')

        sql_insert_query = ''' CREATE DATABASE u209758462_miskb;  '''

        cursor = connection.cursor()
        result = cursor.execute(sql_insert_query)
        connection.commit()

        label = Label(root, text="Databasen skapades hosting.eu.")
        label.pack()

    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        label = Label(root, text="Databasen skapades misslyckades hosting.eu." + str(error))
        label.pack()
    finally:
        # closing database connection.
        if connection.is_connected():
            cursor.close()
            connection.close()
            label = Label(root, text="hosting.eu. MySQL koppling nerkopplad")
            label.pack()
    root.mainloop()


# SQl DROP DATABASE


def sqlhostingDropDatabase():
    root = Tk()
    root.title("sqlhostingDropDatabase")
    root.geometry("400x100")
    try:
        connection = mysql.connector.connect(user='u209758462_misk7',
                                             passwd='mi235277sk',
                                             host='sql150.main-hosting.eu',
                                             db='u209758462_miskb')

        sql_insert_query = ''' DROP DATABASE u209758462_miskb;  '''

        cursor = connection.cursor()
        result = cursor.execute(sql_insert_query)
        connection.commit()

        label = Label(root, text="Databasen deleted hosting.eu.")
        label.pack()

    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        label = Label(root, text="Databasen delete misslyckades {} hosting.eu.".format(error))
        label.pack()
    finally:
        # closing database connection.
        if connection.is_connected():
            cursor.close()
            connection.close()
            label = Label(root, text="hosting.eu. MySQL koppling nerkopplad")
            label.pack()
    root.mainloop()


# Sql create Tables -
def sqlhostingCreateTables():
    root = Tk()
    root.title("sqlhostingCreateTables")
    root.geometry("400x100")
    try:
        connection = mysql.connector.connect(user='u209758462_misk7',
                                             passwd='mi235277sk',
                                             host='sql150.main-hosting.eu',
                                             db='u209758462_miskb')

        sql_insert_query = ''' 
CREATE  TABLE profiles
( first_name VARCHAR(30) NOT NULL,
last_name VARCHAR(30) NOT NULL,
email VARCHAR(60) NOT NULL,
age VARCHAR(15) NOT NULL,
yrke VARCHAR(30)NOT NULL,
country VARCHAR(30)NOT NULL,
hobbies VARCHAR(30)NOT NULL,
lenght VARCHAR(30)NOT NULL,
sex ENUM('M','F','O') NOT NULL,
date_entered TIMESTAMP,
profiles_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY)
default character set= utf8;
  '''

        cursor = connection.cursor()
        result = cursor.execute(sql_insert_query)
        connection.commit()

        label = Label(root, text="CREATED TABLE profiles skapades {} hosting.eu.".format(sql_insert_query))
        label.pack()

    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        label = Label(root, text="CREATED TABLE profiles misslyckades {} hosting.eu.".format(error))
        label.pack()
    finally:
        # closing database connection.
        if connection.is_connected():
            cursor.close()
            connection.close()
            label = Label(root, text="hosting.eu. MySQL koppling nerkopplad")
            label.pack
    root.mainloop()


# DROP TABLE
def sqlhostingDropTables():
    root = Tk()
    root.title("sqlhostingDropTables")
    root.geometry("400x100")
    try:
        connection = mysql.connector.connect(user='u209758462_misk7',
                                             passwd='mi235277sk',
                                             host='sql150.main-hosting.eu',
                                             db='u209758462_miskb')

        sql_insert_query = ''' 
DROP TABLE profiles;
  '''

        cursor = connection.cursor()
        result = cursor.execute(sql_insert_query)
        connection.commit()

        label = Label(root, text="DROP TABLE profiles lyckades {} hosting.eu.".format(sql_insert_query))
        label.pack()

    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        label = Label(root, text="DROP TABLE misslyckades {} hosting.eu.".format(error))
        label.pack()
    finally:
        # closing database connection.
        if connection.is_connected():
            cursor.close()
            connection.close()
            label = Label(root, text="hosting.eu. MySQL koppling nerkopplad ")
            label.pack

    root.mainloop()


# SQl insert -  insert.py


def sqlhostingInsertQuery():
    root = Tk()
    root.title("sqlhostingInsertQuery")
    root.geometry("400x100")
    try:
        connection = mysql.connector.connect(user='u209758462_misk7',
                                             passwd='mi235277sk',
                                             host='sql150.main-hosting.eu',
                                             db='u209758462_miskb')

        sql_insert_query = ''' INSERT INTO profiles VALUE 
('Michel','skoglund','michelskoglund@hotmail.com','41','student','sweden','gitarrer','178','M',NOW(),NULL); '''

        cursor = connection.cursor()
        result = cursor.execute(sql_insert_query)
        connection.commit()

        label = Label(root, text="profiles VALUE  har lagrats i tabellen hosting.eu.")
        label.pack()

    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        label = Label(root, text="Lagring i profiles misslyckades {} hosting.eu.".format(error))
        label.pack()
    finally:
        # closing database connection.
        if connection.is_connected():
            cursor.close()
            connection.close()
            label = Label(root, text="hosting.eu. MySQL koppling nerkopplad")
            label.pack()

    root.mainloop()


# SQl show databases -  show databases.py


def sqlhostingShowDb():
    root = Tk()
    root.title("sqlhostingShowDb")
    root.geometry("400x100")
    try:
        connection = mysql.connector.connect(user='u209758462_misk7',
                                             passwd='mi235277sk',
                                             host='sql150.main-hosting.eu',
                                             db='')

        sql_insert_query = ''' show databases; '''

        cursor = connection.cursor()

        cursor.execute(sql_insert_query)
        for row in cursor.fetchall():
            label = Label(root, text=row)
            label.pack()
        connection.commit()

        label = Label(root, text="SHOW databases körs hosting.eu.")
        label.pack()

    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        label = Label(root, text="SHOW databases misslyckades {} db4free.nethosting.eu.")
    finally:
        # closing database connection.
        if connection.is_connected():
            cursor.close()
            connection.close()
            label = Label(root, text="hosting.eu. MySQL koppling nerkopplad")
            label.pack()


# USE  database miskdb

def sqlhostingUsedatabase():
    root = Tk()
    root.title("sqlhostingUsedatabase")
    root.geometry("400x100")
    try:
        connection = mysql.connector.connect(user='u209758462_misk7',
                                             passwd='mi235277sk',
                                             host='sql150.main-hosting.eu',
                                             db='u209758462_miskb')

        sql_insert_query = ''' USE u209758462_miskb	; '''

        cursor = connection.cursor()
        result = cursor.execute(sql_insert_query)
        connection.commit()

        label = Label(root, text="Database changed, USE miskdb now hosting.eu.")
        label.pack()

    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        label = Label(root, text="USE Database miskdb misslyckades {} hosting.eu.".format(error))
        label.pack()
    finally:
        # closing database connection.
        if connection.is_connected():
            cursor.close()
            connection.close()
            label = Label(root, text="hosting.eu.MySQL koppling nerkopplad")
            label.pack()
    root.mainloop()


def sqlhostingSelectDB():


    root = Tk()
    root.title("sqlhostingSelectDB")
    root.geometry("400x100")

    try:
        connection = mysql.connector.connect(user='u209758462_misk7',
                                             passwd='mi235277sk',
                                             host='sql150.main-hosting.eu',
                                             db='u209758462_miskb')

        sql_insert_query = ''' SELECT DATABASE (); '''

        cursor = connection.cursor()
        result = cursor.execute(sql_insert_query)
        for row in cursor.fetchall():
            label = Label(root, text=row)
            label.pack()
        connection.commit()
        choices = ['GB', 'MB', 'KB']
        variable = StringVar(root)
        variable.set('GB')

        w = Checkbutton(root, values=choices)
        w.pack();

        label = Label(root, text="SELECT DATABASE miskdb hosting.eu.")
        label.pack()

    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        label = Label(root, text="SELECT DATABASE miskdb misslyckades {} hosting.eu.".format(error))
        label.pack()
    finally:
        # closing database connection.
        if connection.is_connected():
            cursor.close()
            connection.close()
            label = Label(root, text="hosting.eu. MySQL koppling nerkopplad")
            label.pack()
    root.mainloop()


def sqlhostingDescribeTable():
    root = Tk()
    root.title("sqlhostingReadFromDB")
    root.geometry("400x100")
    try:
        connection = mysql.connector.connect(user='u209758462_misk7',
                                             passwd='mi235277sk',
                                             host='sql150.main-hosting.eu',
                                             db='u209758462_miskb')

        sql_insert_query = ''' DESCRIBE profiles; '''

        cursor = connection.cursor()
        result = cursor.execute(sql_insert_query)
        for row in cursor.fetchall():
            label = Label(root, text=row)
            label.pack()
        connection.commit()

        label = Label(root, text="DESCRIBE profile db4free.net")
        label.pack()

    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        label = Label(root, text="DESCRIBE profiles misslyckades {} hosting.eu.".format(error))
        label.pack()
    finally:
        # closing database connection.
        if connection.is_connected():
            cursor.close()
            connection.close()
            label = Label(root, text="hosting.eu. MySQL koppling nerkopplad")
            label.pack()
    root.mainloop()


# Read from Ddatabase
def sqlhostingReadFromDB():
    root = Tk()
    root.title("sqlhostingReadFromDB")
    root.geometry("400x100")
    try:
        connection = mysql.connector.connect(user='u209758462_misk7',
                                             passwd='mi235277sk',
                                             host='sql150.main-hosting.eu',
                                             db='u209758462_miskb')

        sql_insert_query = ''' SELECT * FROM profiles '''

        cursor = connection.cursor()
        result = cursor.execute(sql_insert_query)
        for row in cursor.fetchall():
            label = Label(root, text=row)
            label.pack()
        connection.commit()

        for row in cursor.fetchall():
            label = Label(root, text=str(row))
            label.pack()

            label = Label(root, text="Reading profiles now dhosting.eu.")
            label.pack()

    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        label = Label(root, text="Reading profiles misslyckades {} hosting.eu.".format(error))
        label.pack()
    finally:
        # closing database connection.
        if connection.is_connected():
            cursor.close()
            connection.close()
            label = Label(root, text="hosting.eu. MySQL koppling nerkopplad")
            label.pack()


###########################
"""
MySQL server hostname is: sql150.main-hosting.eu.
DATABASE                USERNAME
u209758462_miskb	u209758462_misk7
host: sql150.main-hosting.eu.

Email: michelskoglund@hotmail.se

"""

# SQL MANUAL  LOCAL  INSERT INTO profiles  VALUES
from tkinter import *
import mysql
import mysql.connector
import time
from mysql.connector import errorcode
import sqlite3


def hostingerdatabase():
    _firstName = firstName.get()
    _lastName = lastName.get()
    _email = email.get()
    _age = age.get()
    _yrke = yrke.get()
    _country = country.get()
    _hobbies = hobbies.get()
    _lenght = lenght.get()
    _sex = sex.get()
    _date = date.get()
    _profileid = profileid.get()
    connection = mysql.connector.connect(user='u209758462_misk7',
                                         passwd='mi235277sk',
                                         host='sql150.main-hosting.eu',
                                         db='u209758462_miskb')

    cursor = connection.cursor()

    # sql_insert_query = ''' CREATE DATABASE profiles IF NOT EXISTS profiles;'''
    """sql_insert_query = '''CREATE  TABLE  IF NOT EXISTS profiles
    ( first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    email VARCHAR(60) NOT NULL,
    age VARCHAR(15) NOT NULL,
    yrke VARCHAR(30)NOT NULL,
    country VARCHAR(30)NOT NULL,
    hobbies VARCHAR(30)NOT NULL,
    lenght VARCHAR(30)NOT NULL,
    sex ENUM('M','F','O') NOT NULL,
    date_entered TIMESTAMP,
    profiles_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY)
    default character set= utf8;
        '''
        """
    sql_insert_query = '''INSERT INTO profiles  VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}',NOW(),NULL);'''.format(
        _firstName, _lastName, _email, _age, _yrke, _country, _hobbies, _lenght, _sex, _date, _profileid)
    print('Manuel Value inset')
    cursor = connection.cursor()
    result = cursor.execute(sql_insert_query)
    connection.commit()

    # def manuelInsert():


def hostingerguidb():
    root = Tk()
    root.geometry('500x500')
    root.title('manual Insert into profiles\nHostinger')

    global firstName
    firstName = StringVar()
    global lastName
    lastName = StringVar()
    global email
    email = StringVar()
    global age
    age = IntVar()
    global yrke
    yrke = StringVar()
    global country
    country = StringVar()
    global hobbies
    hobbies = StringVar()
    global lenght
    lenght = IntVar()
    global sex
    sex = IntVar()
    global date
    date = IntVar()
    global profileid
    profileid = IntVar()

    labeltitle = Label(root, text="Insert Manual Values into profiles\nHostinger", width=30, font=('bold', 20))
    labeltitle.place(x=50, y=53)

    labelFirstName = Label(root, text="First Name", width=20, font=('bold', 10))
    labelFirstName.place(x=80, y=130)
    entryFirstName = Entry(root, text=firstName)
    entryFirstName.place(x=240, y=130)

    labelLastName = Label(root, text="Last Name", width=20, font=('bold', 10))
    labelLastName.place(x=75, y=150)
    entryLastName = Entry(root, text=lastName)
    entryLastName.place(x=240, y=150)

    labelemail = Label(root, text="Email", width=20, font=('bold', 10))
    labelemail.place(x=70, y=170)
    entrylabelemail = Entry(root, text=email)
    entrylabelemail.place(x=240, y=170)

    labelage = Label(root, text="Age", width=20, font=('bold', 10))
    labelage.place(x=50, y=210)
    entryage = Entry(root, text=age)
    entryage.place(x=240, y=210)

    labelyrke = Label(root, text="yrke", width=20, font=('bold', 10))
    labelyrke.place(x=50, y=230)
    entryyrke = Entry(root, text=yrke)
    entryyrke.place(x=240, y=230)

    labelcountry = Label(root, text="country", width=20, font=('bold', 10))
    labelcountry.place(x=50, y=250)
    # entrycountry = Entry(root, text=country)
    # entrycountry.place(x=240, y=250)
    listett = ['Sverige', 'Finland', 'Norge', 'Danrmark', 'Island']
    droplist = OptionMenu(root, country, *listett)
    droplist.configure(background="gold", width=10)
    country.set('Välj ditt land')
    droplist.place(x=240, y=250)

    labelhobbies = Label(root, text="hobbies", width=20, font=('bold', 10))
    labelhobbies.place(x=50, y=270)
    entryhobbies = Entry(root, text=hobbies)
    entryhobbies.place(x=240, y=270)

    labellenght = Label(root, text="lenght", width=20, font=('bold', 10))
    labellenght.place(x=50, y=290)
    entrylenght = Entry(root, text=lenght)
    entrylenght.place(x=240, y=290)

    labelsex = Label(root, text="sex", width=20, font=('bold', 10))
    labelsex.place(x=50, y=310)
    # entrysex = Entry(root, text=sex)
    # entrysex.place(x=240, y=310)
    Radiobutton(root, text='Male', padx=5, variable=sex, value=1).place(x=200, y=310)
    Radiobutton(root, text='Female', padx=5, variable=sex, value=2).place(x=260, y=310)
    Radiobutton(root, text='Other', padx=5, variable=sex, value=3).place(x=330, y=310)

    labeldate = Label(root, text="date", width=20, font=('bold', 10))
    labeldate.place(x=50, y=330)
    entrydate = Entry(root, text=date)
    entrydate.place(x=240, y=330)

    labelprofiles_id = Label(root, text="profiles_id", width=20, font=('bold', 10))
    labelprofiles_id.place(x=50, y=350)
    entryprofiles_id = Entry(root, text=profileid)
    entryprofiles_id.place(x=240, y=350)

    Button(root, text='Submit', width=20, bg='green', fg='white', command=hostingerdatabase).place(x=270, y=370)

    root.mainloop()


hostingerguidb()
