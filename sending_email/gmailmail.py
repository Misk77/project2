import smtplib
from tkinter import *



def sendmail():
    root = Tk()
    email_sender = 'michelskoglund@gmail.com'
    email_receiver = 'michelskoglund@gmail.com'

    labelsender = Label(root, text="email_sender = 'michelskoglund@gmail.com'").pack()

    labelrecive = Label(root, text="'email_receiver = 'michelskoglund@gmail.com'").pack()

    connection = smtplib.SMTP('smtp.gmail.com', 587)
    connection.starttls()
    connection.login(email_sender, 'cde123VFR456')
    connection.sendmail(email_sender, email_receiver, 'Michel sending from python to gmail TO gmail..')
    connection.quit()
    root.mainloop()

