from tkinter import *
from subprocess import Popen
from datetime import datetime
import timeit
import sys


def Matrix():
    root = Tk()
    root.title("Matrix")
    root.geometry("400x100")
    p = Popen("Matrix.bat", cwd=r"C:\Users\miche\PycharmProjects\DevOps-Programmering av Python\vecka42\appett")
    stdout, stderr = p.communicate()
    root.mainloop()


def powershell():
    p = Popen("powershell.exe",
              cwd=r"C:\Users\miche\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Windows PowerShell")
    win = Tk()
    win.mainloop()
    stdout, stderr = p.communicate()


def testScriptTime():
    root = Tk()
    root.title("testScriptTime")
    root.geometry("400x100")
    start = timeit.default_timer()
    # lägg in vilket script att testa tid nedan

    stop = timeit.default_timer()
    total_time = stop - start
    mins, secs = divmod(total_time, 60)
    hours, mins = divmod(mins, 60)

    Label(root,
          text=("Dont forget to input script to test\nTotal running time: %d:%d:%d.\n" % (hours, mins, secs))).pack()

    root.mainloop()


"""

root=Tk()
Frame(root)
command=os.system("ping google.se")
Text(command=os.system("ping google.se")).pack()
startupinfo = None
if os.name == 'nt':
    Label(startupinfo = subprocess.STARTUPINFO()).pack()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
Label(proc = subprocess.Popen(command, startupinfo=startupinfo)).pack()
Label(text=command).pack()
root.mainloop()

"""
