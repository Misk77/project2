import smtplib
from tkinter import *

root = Tk()


def sendmail():
    email_sender = 'michelskoglund@hotmail.se'
    email_receiver = 'michelskoglund@hotmail.se'

    labelsender = Label(root, text="email_sender = 'michelskoglund@hotmail.se'").pack()

    labelrecive = Label(root, text="'email_receiver = 'michelskoglund@hotmail.se'").pack()

    connection = smtplib.SMTP('smtp-mail.outlook.com', 995)
    connection.starttls()
    connection.login(email_sender, 'Kalleanka2018')
    connection.sendmail(email_sender, email_receiver, 'Michel sending from python to hotmail TO hotmail..')
    connection.quit()


buttonWebSite = Button(text="Sending mail", command=sendmail)
buttonWebSite.bind("<Return>", lambda event: sendmail())
buttonWebSite.pack()
root.mainloop()
