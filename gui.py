from tkinter import *
from tkinter import ttk
from sqlLocal import sqlConnector, createDatabase, dropDatabase, insertQuery, showDb, createTables, \
    useProfiles, readFromDB, selectDB, describeTable, dropTables, localguidb
from sqldb4free import sqldb4freeConnector, sqldb4freecreateTables, sqldb4freeCreateDatabase, \
    sqldb4freeDescribeTable, sqldb4freedropDatabase, sqldb4freeInsertQuery, sqldb4freeReadFromDB, sqldb4freeSelectDB, \
    sqldb4freeShowDb, sqldb4freeUsedatabase, sqldb4freedropTables
from sqlhostinger import sqlhostingConnector, sqlhostingCreateDatabase, sqlhostingCreateTables, \
    sqlhostingDescribeTable, sqlhostingDropDatabase, sqlhostingDropTables, sqlhostingInsertQuery, \
    sqlhostingReadFromDB, \
    sqlhostingSelectDB, sqlhostingShowDb, sqlhostingUsedatabase, hostingerguidb
from socketScrips import socket_connect, server, serverUI
from webconnect import homeConnect, wordPressConnect, googleConnect, slackConnect, guiPthonkConnect, \
    soloLearnConnect, \
    unofficialWinBIN, downloadpage, ftpConnect,pythonInteractiveConnect
from cv2showImgVideo import fpsShow, showimagePIL, showimageOsStartfile, showvideo, showimageombyggnad, \
    showaboutplayground
from ImportSubProcessFiles import Matrix, powershell, testScriptTime
from printoutgui import printSomething
from funktioner import on_closing
from sending_email.gmailmail import sendmail
from playingsound.playsound import stringE, a, d, g, b, stringe, lick, showvideoSound
from opentxtfile import read_about

# from appett.guiapp import Appgui

#   TKINTER SETTING  ###########################


root = Tk()
root.configure(background="black")
root.iconbitmap(default="Untitled.ico")
root.title("Michel´s Playground")
root.geometry("1150x600")

# background imgage
frame1 = Frame(root)
frame1 = Frame(root, width=400, height=450)
frame1.place(height=7000, width=4000, x=10, y=100)
frame1.config()

frame1.grid(columnspan=18, rowspan=18)

frame1.grid_rowconfigure(0, weight=1)
frame1.grid_columnconfigure(0, weight=1)

photo = PhotoImage(file=r"C:\Users\miche\PycharmProjects\project2gui\backgroundwebsite.png")
label = Label(root, image=photo)
label.image = photo
label.grid(row=0, column=0, columnspan=21, rowspan=30)

# MIN LABEL
labelett = ttk.Label(text="Michel's Playground")
labelett.grid(row=0, column=0, padx=5, pady=5)
labelett.config(font=("Inconsolata", 20))
ttk.Style().configure("TButton", padding=6, relief="flat",
                      background="#000", foreground='green')
root.style = ttk.Style()

# Entry


menubar = Menu(root)
# Server SOCKET options menu
servermenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Server Options", menu=servermenu)
servermenu.add_command(label="Start server", command=server)
servermenu.add_command(label="Socket connect", command=socket_connect)
servermenu.add_separator()
servermenu.add_command(label="Exit", command=root.quit)

# SQL options menu
sqlmenu = Menu(root, tearoff=0)
menubar.add_cascade(label="Sql menu", menu=sqlmenu)
# LOCAL SQL
sqllocal = Menu(sqlmenu, tearoff=False)
sqlmenu.add_cascade(label="Mysql LOCAL ", menu=sqllocal)
sqllocal.add_command(label="Connect LOCAL ", command=sqlConnector)
sqllocal.add_command(label="Create database profiles LOCAL", command=createDatabase)
sqllocal.add_command(label="Drop database profiles LOCAL", command=dropDatabase)
sqllocal.add_command(label="Insert table  LOCAL", command=insertQuery)
sqllocal.add_command(label="Show database  LOCAL", command=showDb)
sqllocal.add_command(label="Use profiles  LOCAL", command=useProfiles)
sqllocal.add_command(label="Select profiles LOCAL", command=selectDB)
sqllocal.add_command(label="Read database LOCAL", command=readFromDB)
sqllocal.add_command(label="Create table in profiles LOCAL", command=createTables)
sqllocal.add_command(label="Describe table LOCAL", command=describeTable)
sqllocal.add_command(label="DROP TABLE profiles mysql db4free.net", command=dropTables)
sqllocal.add_separator()
sqllocal.add_command(label="Exit", command=root.quit)
# SQL mysql db4free.net
sqldb4free = Menu(sqlmenu, tearoff=False)
sqlmenu.add_cascade(label="mysql db4free.net ", menu=sqldb4free)
sqldb4free.add_command(label="Connect mysql db4free.net ", command=sqldb4freeConnector)
# Create database  CANT be done in db4free.net  No Privileges
sqldb4free.add_command(label="Create database mysql db4free.net", command=sqldb4freeCreateDatabase)
sqldb4free.add_command(label="Drop database mysql db4free.net", command=sqldb4freedropDatabase)
sqldb4free.add_command(label="Insert table mysql db4free.net", command=sqldb4freeInsertQuery)
sqldb4free.add_command(label="Show database mysql db4free.net", command=sqldb4freeShowDb)
sqldb4free.add_command(label="Use Database miskdb mysql db4free.net", command=sqldb4freeUsedatabase)
sqldb4free.add_command(label="Select Database miskdb mysql db4free.net", command=sqldb4freeSelectDB)
sqldb4free.add_command(label="Read database mysql db4free.net", command=sqldb4freeReadFromDB)
sqldb4free.add_command(label="Create table in profiles mysql db4free.net", command=sqldb4freecreateTables)
sqldb4free.add_command(label="Describe table mysql db4free.net", command=sqldb4freeDescribeTable)
sqldb4free.add_command(label="DROP TABLE profiles mysql db4free.net", command=sqldb4freedropTables)
sqldb4free.add_separator()
sqldb4free.add_command(label="Exit", command=root.quit)
# SQL hostinger.com
sqlhosting = Menu(sqlmenu, tearoff=False)
sqlmenu.add_cascade(label="mysql hostinger.com ", menu=sqlhosting)
sqlhosting.add_command(label="Connect mysql hostinger.com ", command=sqlhostingConnector)
# Create database  CANT be done in db4free.net  No Privileges
sqlhosting.add_command(label="Create database mysql hostinger", command=sqlhostingCreateDatabase)
sqlhosting.add_command(label="Drop database mysql hostinger", command=sqlhostingDropDatabase)
sqlhosting.add_command(label="Insert table mysql hostinger", command=sqlhostingInsertQuery)
sqlhosting.add_command(label="Show database mysql hostinger", command=sqlhostingShowDb)
sqlhosting.add_command(label="Use Database miskdb mysql dhostinger", command=sqlhostingUsedatabase)
sqlhosting.add_command(label="Select Database miskdb mysql hostinger", command=sqlhostingSelectDB)
sqlhosting.add_command(label="Read database mysql hostinger", command=sqlhostingReadFromDB)
sqlhosting.add_command(label="Create table in profiles mysql hostinger", command=sqlhostingCreateTables)
sqlhosting.add_command(label="Describe table mysql hostinger", command=sqlhostingDescribeTable)
sqlhosting.add_command(label="DROP TABLE profiles hostinger", command=sqlhostingDropTables)
sqlhosting.add_separator()
sqlhosting.add_command(label="Exit", command=root.quit)

# Web connection options menu
webmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Web connections", menu=webmenu)
webmenu.add_command(label="Search Google ", command=googleConnect)
webmenu.add_command(label="Visit My HomePage", command=homeConnect)
webmenu.add_command(label="Slack", command=slackConnect)
webmenu.add_command(label="FTP Connection", command=ftpConnect)
webmenu.add_command(label="FTP Connection", command=pythonInteractiveConnect)
webmenu.add_command(label="Unofficial Win Binary package", command=unofficialWinBIN)
webmenu.add_separator()
webmenu.add_command(label="Exit", command=root.quit)

# Games options menu
gamemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Game options", menu=gamemenu)
gamemenu.add_command(label="Guessing Game", command=showimageombyggnad)
gamemenu.add_command(label="Game 2", command=showimageombyggnad)
gamemenu.add_command(label="Game 2", command=showimageombyggnad)
gamemenu.add_command(label="Game 2", command=showimageombyggnad)
gamemenu.add_command(label="Game 2", command=showimageombyggnad)
gamemenu.add_command(label="Game 2", command=showimageombyggnad)
gamemenu.add_separator()
gamemenu.add_command(label="Exit", command=root.quit)

# Tuner/sound options menu
tunermenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Tuner options", menu=tunermenu)
tunermenu.add_command(label="Tune E", command=stringE)
tunermenu.add_command(label="Tune A", command=a)
tunermenu.add_command(label="Tune D ", command=d)
tunermenu.add_command(label="Tune G", command=g)
tunermenu.add_command(label="Tune B", command=b)
tunermenu.add_command(label="Tune e", command=stringe)
tunermenu.add_command(label="Play lick", command=lick)
tunermenu.add_separator()
tunermenu.add_command(label="Exit", command=root.quit)

# Programming  options menu
programmingmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Programming", menu=programmingmenu)
programmingmenu.add_command(label="SoloLearn", command=soloLearnConnect)
programmingmenu.add_command(label="Slack", command=slackConnect)
programmingmenu.add_command(label="Python 3 - GUI Programming (Tkinter)", command=guiPthonkConnect)
programmingmenu.add_command(label="Download Page", command=downloadpage)
programmingmenu.add_command(label="Programming 4", command=showimageombyggnad)
programmingmenu.add_command(label="Programming 5", command=showimageombyggnad)
programmingmenu.add_separator()
programmingmenu.add_command(label="Exit", command=root.quit)

# Misc stuff menu
miscmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Misc stuff", menu=miscmenu)
miscmenu.add_command(label="Enter the matrix", command=Matrix)
miscmenu.add_command(label="Poweshell", command=powershell)
miscmenu.add_command(label="Fps test video", command=fpsShow)
miscmenu.add_command(label="SHOW Image Pil ", command=showimagePIL)
miscmenu.add_command(label="SHOW Image OS Startfile", command=showimageOsStartfile)
miscmenu.add_command(label="SHOW avi cvOPEN", command=showvideo)
miscmenu.add_command(label="SHOW avi OS", command=showvideoSound)
miscmenu.add_command(label="Print out gui", command=printSomething)
miscmenu.add_command(label="Send Gmail", command=sendmail)
miscmenu.add_command(label="Connects to FTP", command=sendmail)
miscmenu.add_command(label="Test Script Time", command=testScriptTime)
miscmenu.add_command(label="Programming 5", command=showimageombyggnad)
miscmenu.add_separator()
miscmenu.add_command(label="Exit", command=root.quit)

# Help options
helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="Search Google", command=googleConnect)
helpmenu.add_command(label="Slack", command=slackConnect)
helpmenu.add_command(label="Unofficial Win Binary package", command=unofficialWinBIN)
helpmenu.add_command(label="About playground", command=showaboutplayground)
helpmenu.add_separator()
helpmenu.add_command(label="Exit", command=on_closing)

root.config(menu=menubar)

# Socket STUFF
# Button SERVER socket
buttonServer = ttk.Button(text="SERVER multiserver socket", command=serverUI)
buttonServer.bind("<Return>", lambda event: serverUI())
buttonServer.grid(column=0, row=2)
# Button CLIENT socket
buttonClient = ttk.Button(text="CLIENT multiserver socket", command=socket_connect)
buttonClient.bind("<Return>", lambda event: socket_connect)
buttonClient.grid(column=0, row=3)

#  Web  Connector STUFF   #
# Button visit Misk playgroud
buttonWebSite = ttk.Button(text="Visit My HomePage", command=homeConnect)
buttonWebSite.bind("<Return>", lambda event: homeConnect())
buttonWebSite.grid(column=0, row=5)
# Button visit michels wordpress
buttonWebSite = ttk.Button(text="Visit My Wordpress", command=wordPressConnect)
buttonWebSite.bind("<Return>", lambda event: wordPressConnect())
buttonWebSite.grid(column=0, row=6)
# Button visit DownloadPage
buttonWebSite = ttk.Button(text="Visit My DownloadPage", command=downloadpage)
buttonWebSite.bind("<Return>", lambda event: downloadpage())
buttonWebSite.grid(column=0, row=7)
# Button visit Google
buttonWebSite = ttk.Button(text="Search Google", command=googleConnect)
buttonWebSite.bind("<Return>", lambda event: googleConnect())
buttonWebSite.grid(column=0, row=8)
# Button  Slack
buttonWebSite = ttk.Button(text="Slack", command=slackConnect)
buttonWebSite.bind("<Return>", lambda event: slackConnect())
buttonWebSite.grid(column=0, row=9)
# Button GUI Programming (Tkinter
buttonWebSite = ttk.Button(text="Python 3 - GUI Programming (Tkinter)", command=guiPthonkConnect)
buttonWebSite.bind("<Return>", lambda event: guiPthonkConnect())
buttonWebSite.grid(column=0, row=10)
# Button Unofficial Windows Binaries for Python Extension Packages
buttonWebSite = ttk.Button(text="Unofficial Win Binaries for Python Extension Packages", command=unofficialWinBIN)
buttonWebSite.bind("<Return>", lambda event: unofficialWinBIN())
buttonWebSite.grid(column=0, row=11)
# Button Connect to FTP Hostinger
buttonFtpHostinger = ttk.Button(text="Connect to FTP Hostinger", command=ftpConnect)
buttonFtpHostinger.bind("<Return>", lambda event: ftpConnect())
buttonFtpHostinger.grid(column=0, row=12)
# Button Connect pythonInteractiveConnect
buttonFtpHostinger = ttk.Button(text="Connect to interactive Python ", command=pythonInteractiveConnect)
buttonFtpHostinger.bind("<Return>", lambda event: pythonInteractiveConnect())
buttonFtpHostinger.grid(column=0, row=13)

# SQL STUFF
# SQL LOCAL
# Button Sql CONNECTOR
buttonConnector = ttk.Button(text="Connect SQL Local", command=sqlConnector)
buttonConnector.bind("<Return>", lambda event: sqlConnector())
buttonConnector.grid(column=1, row=2)
# Button Sql CREATE Database
buttoncreateDatabase = ttk.Button(text="SQL Local create Database", command=createDatabase)
buttoncreateDatabase.bind("<Return>", lambda event: createDatabase())
buttoncreateDatabase.grid(column=1, row=3)
# Button Sql Use Person
buttonUsePerson = ttk.Button(text="SQL Local Use profiles", command=useProfiles)
buttonUsePerson.bind("<Return>", lambda event: useProfiles())
buttonUsePerson.grid(column=1, row=4)
# Button Sql SELECT DATABASE()
buttonSelectDatabase = ttk.Button(text="SQL Local Select profiles", command=selectDB)
buttonSelectDatabase.bind("<Return>", lambda event: selectDB())
buttonSelectDatabase.grid(column=1, row=5)
# Button Create Tables
buttonTables = ttk.Button(text="SQL Local create Tables", command=createTables)
buttonTables.bind("<Return>", lambda event: createTables())
buttonTables.grid(column=1, row=6)
# Button Sql INSERT query
buttonInsertQuery = ttk.Button(text="SQL Local Insert Table", command=insertQuery)
buttonInsertQuery.bind("<Return>", lambda event: insertQuery())
buttonInsertQuery.grid(column=1, row=7)
# Button See the SQL SHOW DATABASES
buttonShowDb = ttk.Button(text="SQL Local show databases", command=showDb)
buttonShowDb.bind("<Return>", lambda event: showDb())
buttonShowDb.grid(column=1, row=8)
# Button Sql drop Database
buttonDropDatabase = ttk.Button(text="Sql Local drop Database", command=dropDatabase)
buttonDropDatabase.bind("<Return>", lambda event: dropDatabase())
buttonDropDatabase.grid(column=1, row=9)
# Button Sql READ Database
buttonReadDatabase = ttk.Button(text="Sql Local READ Database", command=readFromDB)
buttonReadDatabase.bind("<Return>", lambda event: readFromDB())
buttonReadDatabase.grid(column=1, row=11)
# Button Sql DESCRIBE tables
buttonDescribeTable = ttk.Button(text="Sql Local DESCRIBE table", command=describeTable)
buttonDescribeTable.bind("<Return>", lambda event: describeTable())
buttonDescribeTable.grid(column=1, row=12)
# Button Sql DROP tables
buttonDropTable = ttk.Button(text="Sql Local DROP table", command=dropTables)
buttonDropTable.bind("<Return>", lambda event: dropTables())
buttonDropTable.grid(column=1, row=10)
# MANUAL INSERT
# Button Sql Local MANUAL INSERT
buttonManINSERT = ttk.Button(text="Local MANUAL INSERT INTO profiles VALUES ", command=localguidb)
buttonManINSERT.bind("<Return>", lambda event: localguidb())
buttonManINSERT.grid(column=1, row=13)
# SQL hostinger.com #########################################################################
# Button Connect SQL db4free.net
buttonConnector = ttk.Button(text="Connect SQL hostinger.com", command=sqlhostingConnector)
buttonConnector.bind("<Return>", lambda event: sqlhostingConnector())
buttonConnector.grid(column=2, row=2)
# Button Sql hostinger.com  CREATE Database CAnt be done on db4free.net NO PRIVIGLES
buttoncreateDatabase = ttk.Button(text="SQL hostinger.com create Database", command=sqlhostingCreateDatabase)
buttoncreateDatabase.bind("<Return>", lambda event: sqlhostingCreateDatabase())
buttoncreateDatabase.grid(column=2, row=3)
# Button Sql hostinger.com  Use Person
buttonUsePerson = ttk.Button(text="SQL hostinger.com Use database miskdb", command=sqlhostingUsedatabase)
buttonUsePerson.bind("<Return>", lambda event: sqlhostingUsedatabase())
buttonUsePerson.grid(column=2, row=4)
# Button Sql hostinger.com SELECT DATABASE()
buttonSelectDatabase = ttk.Button(text="SQL hostinger.com Select profiles", command=sqlhostingSelectDB)
buttonSelectDatabase.bind("<Return>", lambda event: sqlhostingSelectDB())
buttonSelectDatabase.grid(column=2, row=5)
# Button hostinger.com Create  Tables
buttonTables = ttk.Button(text="SQL hostinger.com create Tables", command=sqlhostingCreateTables)
buttonTables.bind("<Return>", lambda event: sqlhostingCreateTables())
buttonTables.grid(column=2, row=6)
# Button Sql hostinger.com INSERT query
buttonInsertQuery = ttk.Button(text="SQL hostinger.com Insert Table", command=sqlhostingInsertQuery)
buttonInsertQuery.bind("<Return>", lambda event: sqlhostingInsertQuery())
buttonInsertQuery.grid(column=2, row=7)
# Button See the SQL SHOW DATABASES
buttonShowDb = ttk.Button(text="SQL hostinger.com show databases", command=sqlhostingShowDb)
buttonShowDb.bind("<Return>", lambda event: sqlhostingShowDb())
buttonShowDb.grid(column=2, row=8)
# Button Sql drop Database
buttonDropDatabase = ttk.Button(text="SQL hostinger.com drop Database", command=sqlhostingDropDatabase)
buttonDropDatabase.bind("<Return>", lambda event: sqlhostingDropDatabase())
buttonDropDatabase.grid(column=2, row=9)
# Button Sql READ Database
buttonReadDatabase = ttk.Button(text="SQL hostinger.com READ Database", command=sqlhostingReadFromDB)
buttonReadDatabase.bind("<Return>", lambda event: sqlhostingReadFromDB())
buttonReadDatabase.grid(column=2, row=11)
# Button Sql DESCRIBE tables
buttonDescribeTable = ttk.Button(text="SQL hostinger.com DESCRIBE table", command=sqlhostingDescribeTable)
buttonDescribeTable.bind("<Return>", lambda event: sqlhostingDescribeTable())
buttonDescribeTable.grid(column=2, row=12)
# Button Sql DROP tables
buttonDropTable = ttk.Button(text="SQL hostinger.com DROP table", command=sqlhostingDropTables)
buttonDropTable.bind("<Return>", lambda event: sqlhostingDropTables())
buttonDropTable.grid(column=2, row=10)
# MANUAL INSERT
# Button Sql MANUAL INSERT
buttonManINSERT = ttk.Button(text="hostinger MANUAL INSERT INTO profiles VALUES ", command=hostingerguidb)
buttonManINSERT.bind("<Return>", lambda event: hostingerguidb())
buttonManINSERT.grid(column=2, row=13)

# Misc STUFF
# Button guess game
buttonGuessingGame = ttk.Button(text="GuessingGame", command=showimageombyggnad)
buttonGuessingGame.bind("<Return>", lambda event: showimageombyggnad())
buttonGuessingGame.grid(column=3, row=2)
# Button See the matrix
buttonMatrix = ttk.Button(text="Enter the MATRIX", command=Matrix)
buttonMatrix.bind("<Return>", lambda event: Matrix())
buttonMatrix.grid(column=3, row=3)
# Button See the Powershell
buttonMatrix = ttk.Button(text="Powershell", command=powershell)
buttonMatrix.bind("<Return>", lambda event: powershell())
buttonMatrix.grid(column=3, row=4)
# Button FPS  testbild
buttonPrintOutGui = ttk.Button(text="FPS test video", command=fpsShow)
buttonPrintOutGui.bind("<Return>", lambda event: fpsShow())
buttonPrintOutGui.grid(column=3, row=5)
# Button SHOW IMAGEPIL
buttonIMAGEPIL = ttk.Button(text="Show ImageWith PIL", command=showimagePIL)
buttonIMAGEPIL.bind("<Return>", lambda event: showimagePIL())
buttonIMAGEPIL.grid(column=3, row=6)
# Button SHOW IMAGE OSstartfile
buttonOSstartfile = ttk.Button(text="Show Image OS startfile", command=showimageOsStartfile)
buttonOSstartfile.bind("<Return>", lambda event: showimageOsStartfile())
buttonOSstartfile.grid(column=3, row=7)
# Button Print out gui
buttonPrintOutGui = ttk.Button(text="Print out gui", command=printSomething)
buttonPrintOutGui.bind("<Return>", lambda event: printSomething())
buttonPrintOutGui.grid(column=3, row=8)
# Button Send gmail
buttonPrintOutGui = ttk.Button(text="Send gmail", command=sendmail)
buttonPrintOutGui.bind("<Return>", lambda event: sendmail())
buttonPrintOutGui.grid(column=3, row=9)
# SHOW avicvOPEN
buttonOSstartfile = ttk.Button(text="SHOW avi cvOPEN NO SOUND", command=showvideo)
buttonOSstartfile.bind("<Return>", lambda event: showvideo())
buttonOSstartfile.grid(column=3, row=10)
# SHOW avicvOPEN        testScriptTime
buttonOSstartfile = ttk.Button(text="SHOW avi OS SOUND", command=showvideoSound)
buttonOSstartfile.bind("<Return>", lambda event: showvideoSound())
buttonOSstartfile.grid(column=3, row=11)
# testScriptTime
buttonOSstartfile = ttk.Button(text="Test Script time", command=testScriptTime)
buttonOSstartfile.bind("<Return>", lambda event: testScriptTime())
buttonOSstartfile.grid(column=3, row=12)
# Button Goodbye exit
buttonGoodbye = Button(root, text="Press to exit", command=on_closing,
                       bg='#000000',
                       fg='#b7f731',
                       relief='flat',
                       width=20)
buttonGoodbye.bind("<Return>", lambda event: on_closing())
buttonGoodbye.grid(row=15)
buttonGoodbye.grid()

# Button Guitar tuner
playE = Radiobutton(root, text='Tune string E', value=1, command=stringE)
playE.configure(foreground='green')
playE.grid(column=4, row=2)
playA = Radiobutton(root, text='Tune string A', value=1, command=a)
playA.configure(foreground='gold')
playA.grid(column=4, row=3)
playD = Radiobutton(root, text='Tune string D', value=1, command=d)
playD.configure(foreground='magenta')
playD.grid(column=4, row=4)
playG = Radiobutton(root, text='Tune string G', value=1, command=g)
playG.configure(foreground='purple')
playG.grid(column=4, row=5)
playB = Radiobutton(root, text='Tune string B', value=1, command=b)
playB.configure(foreground='red')
playB.grid(column=4, row=6)
playe = Radiobutton(root, text='Tune string e', value=1, command=stringe)
playe.configure(foreground='black')
playe.grid(column=4, row=7)
playLick = Radiobutton(root, text='Play lick', value=1, command=lick)
playLick.configure(foreground='blue')
playLick.grid(column=4, row=8)
# Button appgui
# buttonPrintOutGui = ttk.Button(text="app class", command=Appgui)
# buttonPrintOutGui.bind("<Return>", lambda event: Appgui())
# buttonPrintOutGui.grid(column=2, row=13)

# entry button 1
# textentry = Entry(width=20, bg="white")
# textentry.bind("<Return>", '')
# textentry.grid(row=2, column=0, sticky=W)

# root loop
# make Esc exit the program
root.bind('<Escape>', lambda e: root.destroy())
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
# root.protocol("WM_DELETE_WINDOW    ", on_closing)
