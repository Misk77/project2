import webbrowser
from tkinter import *


def homeConnect(): \
        webbrowser.open('http://michelskoglund.online/', new=2)


def wordPressConnect(): \
        webbrowser.open('http://michelskoglund.online/wordpress/', new=2)


def downloadpage(): \
        webbrowser.open('http://michelskoglund.online/downloads/', new=2)


def googleConnect(): \
        webbrowser.open('https://www.google.com/', new=2)


def slackConnect(): \
        webbrowser.open('https://slack.com/signin', new=2)


def pythonInteractiveConnect(): \
        webbrowser.open('https://www.pythonanywhere.com/user/Misk/consoles/10964195/', new=2)


def guiPthonkConnect(): \
        webbrowser.open('https://www.tutorialspoint.com/python3/python_gui_programming.htm', new=2)


def soloLearnConnect(): \
        webbrowser.open('https://www.sololearn.com/', new=2)


def unofficialWinBIN(): \
        webbrowser.open('https://www.lfd.uci.edu/~gohlke/pythonlibs/', new=2)


# ftp connection
def ftpConnect():
    import ftplib
    root = Tk()
    root.title("ftpConnect")
    root.geometry('500x500')
    server = ftplib.FTP()
    server.connect('185.224.137.146', 21)
    server.login('u209758462', 'mi235277sk')
    server.dir()

    root.mainloop()
