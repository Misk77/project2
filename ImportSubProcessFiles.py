from tkinter import *
from subprocess import Popen


def Matrix():
    root = Tk()
    p = Popen("Matrix.bat", cwd=r"C:\Users\miche\PycharmProjects\DevOps-Programmering av Python\vecka42\appett")
    root.mainloop()
    stdout, stderr = p.communicate()


def powershell():
    p = Popen("powershell.exe",
              cwd=r"C:\Users\miche\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Windows PowerShell")
    win = Tk()
    win.mainloop()
    stdout, stderr = p.communicate()


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
