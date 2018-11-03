from tkinter import *
import mysql
import mysql.connector
import time
from mysql.connector import errorcode
import sqlite3


def database():


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
    connection = mysql.connector.connect(host='localhost',
                                         database='profiles',
                                         user='root',
                                         password='root')

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


def guidb():
    root = Tk()
    root.geometry('500x500')
    root.title('manual Insert into profiles')

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

    labeltitle = Label(root, text="Insert Manuel into profiles", width=20, font=('bold', 20))
    labeltitle.place(x=90, y=53)

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
    droplist.config(width=10)
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

    Button(root, text='Submit', width=20, bg='green', fg='white', command=database).place(x=270, y=370)

    root.mainloop()


guidb()