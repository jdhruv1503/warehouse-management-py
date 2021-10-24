from tkinter import *
import csv
import pickle


# ------------------------------- FUNCTIONS OF MAIN BUTTONS ------------------------------------

# A dummy function, debug only

def dummyFunc():
    pass


# Some generic prompts used throughout the program

def successPrompt(message):
    successPopup = Tk()
    successPopup.title('Success!')
    invalidLabel = Label(successPopup, text=message).grid(row=0, column=0)
    okButton = Button(successPopup, text="OK", command=successPopup.destroy).grid(row=1, column=0)
    successPopup.mainloop()


def failurePrompt(message):
    failPopup = Tk()
    failPopup.title('Error!')
    invalidLabel = Label(failPopup, text=message).grid(row=0, column=0)
    okButton = Button(failPopup, text="OK", command=failPopup.destroy).grid(row=1, column=0)
    failPopup.mainloop()


# ADD AN ACCOUNT

def addAccountPrompt():
    addAccWindow = Tk()
    addAccWindow.title('Add a user account')

    addAccWindow.grid_columnconfigure(0, weight=1)
    addAccWindow.grid_columnconfigure(1, weight=1)
    addAccWindow.grid_rowconfigure(0, weight=1)
    addAccWindow.grid_rowconfigure(1, weight=1)
    addAccWindow.grid_rowconfigure(2, weight=1)
    addAccWindow.grid_rowconfigure(3, weight=1)

    usernameAddLabel = Label(addAccWindow, text="Username").grid(row=0, column=0)
    usernameAdd = StringVar(addAccWindow)
    usernameAddEntry = Entry(addAccWindow, textvariable=usernameAdd).grid(row=0, column=1)

    passwordAddLabel = Label(addAccWindow, text="Password").grid(row=1, column=0)
    passwordAdd = StringVar(addAccWindow)
    passwordAddEntry = Entry(addAccWindow, textvariable=passwordAdd, show='*').grid(row=1, column=1)

    passwordConfirmLabel = Label(addAccWindow, text="Confirm password").grid(row=2, column=0)
    password2Add = StringVar(addAccWindow)
    passwordConfirmEntry = Entry(addAccWindow, textvariable=password2Add, show='*').grid(row=2, column=1)

    addButton = Button(addAccWindow, text="Add a new account",
                       command=lambda: addAccount(usernameAdd, passwordAdd, password2Add)).grid(row=3,
                                                                                                column=0)

    addAccWindow.mainloop()


def addAccount(usernameAddArg, passwordAddArg, password2AddArg):
    if passwordAddArg.get() == password2AddArg.get():

        with open("logins.csv", "a", newline='') as adminFile:
            adminWrite = csv.DictWriter(adminFile, ['Username', 'Password'])
            adminWrite.writerow({'Username': usernameAddArg.get(), 'Password': passwordAddArg.get()})

        successPrompt("User has been added!")

    else:
        failurePrompt("Passwords do not match!")


# VIEW WORKER STATUS

def viewWorkerPrompt():
    absentWorkerList = []
    maxWorkerList = []
    minWorkerList = []
    minHours = 24
    maxHours = 0

    with open('workerlog.dat', 'rb') as workerFile:
        workerRead = pickle.load(workerFile)

        for key in workerRead.keys():
            if workerRead[key] == 0:
                absentWorkerList.append(key)

            elif workerRead[key] < minHours:
                minHours = workerRead[key]

            elif workerRead[key] > maxHours:
                maxHours = workerRead[key]

        for key in workerRead.keys():
            if workerRead[key] == minHours:
                minWorkerList.append(key)
            elif workerRead[key] == maxHours:
                maxWorkerList.append(key)

    message1 = "The workers absent today are: \n" + str(absentWorkerList)
    message2 = "The worker(s) who have worked the least today are: \n" + str(minWorkerList)
    message3 = "The worker(s) who have worked the most today are: \n" + str(maxWorkerList)

    workerStatWindow = Tk()
    workerStatWindow.title('Worker status')
    label1 = Label(workerStatWindow, text=message1).grid(row=0, column=0)
    label2 = Label(workerStatWindow, text=message2).grid(row=1, column=0)
    label3 = Label(workerStatWindow, text=message3).grid(row=2, column=0)
    okButton = Button(workerStatWindow, text="OK", command=workerStatWindow.destroy).grid(row=3, column=0)
    workerStatWindow.mainloop()


# WORKER UPDATING

def updateWorker(keysArg, valuesArg):
    intsList = []

    for val in valuesArg:
        intsList.append(int(val.get()))

    newDict = dict(zip(keysArg, intsList))

    with open('workerlog.dat', 'wb') as workerFile:
        pickle.dump(newDict, workerFile)

    successPrompt("Worker values have been updated!")


def updateWorkerPrompt():
    with open('workerlog.dat', 'rb') as workerFile:
        workerRead = pickle.load(workerFile)

        updWorkerWindow = Tk()
        updWorkerWindow.title("Update worker status")

        n = 0
        labels = []
        texts = []
        textValues = []

        # Mechanism to procedurally generate a window and populate it with values of worker hours

        for key in workerRead.keys():
            textValues.append(StringVar(updWorkerWindow))
            textValues[n].set(workerRead[key])

            labels.append(Label(updWorkerWindow, text=key).grid(row=n, column=0))
            texts.append(Entry(updWorkerWindow, textvariable=textValues[n]).grid(row=n, column=1))

            n += 1

    updateWorkerButton = Button(updWorkerWindow, text="Update values",
                                command=lambda: updateWorker(workerRead.keys(), textValues)).grid(row=n + 1, column=0)
    updWorkerWindow.mainloop()

# WORKER WAGES

def workerWagePrompt():
    hourlyRateWindow = Tk()
    hourlyRateWindow.geometry('300x100')
    hourlyRateWindow.title('Enter hourly wages')

    hourlyRateWindow.grid_columnconfigure(0, weight=1)
    hourlyRateWindow.grid_columnconfigure(1, weight=1)
    hourlyRateWindow.grid_rowconfigure(0, weight=1)
    hourlyRateWindow.grid_rowconfigure(1, weight=1)

    rateLabel = Label(hourlyRateWindow, text="Enter the hourly rate:").grid(row=0, column=0)
    rate = StringVar(hourlyRateWindow)
    rateLabel = Entry(hourlyRateWindow, textvariable=rate).grid(row=0, column=1)

    hourlyRateButton = Button(hourlyRateWindow, text="OK", command=lambda: workerWageDisplay(rate.get())).grid(row=1, column=0)
    hourlyRateWindow.mainloop()

def workerWageDisplay(rateValue):
    with open('workerlog.dat', 'rb') as workerFile:
        workerRead = pickle.load(workerFile)

        wageWindow = Tk()
        wageWindow.title("View worker wages")

        n = 0
        labels = []
        labels2 = []

        for key in workerRead.keys():
            labels.append(Label(wageWindow, text=key + ":").grid(row=n, column=0))
            labels2.append(Label(wageWindow, text=str(workerRead[key]*int(rateValue)) + " rupees").grid(row=n, column=1))

            n += 1

    workerWageButton = Button(wageWindow, text="OK",
                                command=wageWindow.destroy).grid(row=n + 1, column=0)
    wageWindow.mainloop()

# PRICE UPDATING (identical syntax as that of updating worker values above)

def updatePrices(keysArg, valuesArg):
    intsList = []

    for val in valuesArg:
        intsList.append(int(val.get()))

    newDict = dict(zip(keysArg, intsList))

    with open('prices.dat', 'wb') as priceFile:
        pickle.dump(newDict, priceFile)

    successPrompt("Price values have been updated!")


def updatePricePrompt():
    with open('prices.dat', 'rb') as priceFile:
        priceRead = pickle.load(priceFile)

        updPriceWindow = Tk()
        updPriceWindow.title("Update stock price")

        n = 0
        labels = []
        texts = []
        textValues = []

        for key in priceRead.keys():
            textValues.append(StringVar(updPriceWindow))
            textValues[n].set(priceRead[key])

            labels.append(Label(updPriceWindow, text=key).grid(row=n, column=0))
            texts.append(Entry(updPriceWindow, textvariable=textValues[n]).grid(row=n, column=1))

            n += 1

    updateWorkerButton = Button(updPriceWindow, text="Update values",
                                command=lambda: updatePrices(priceRead.keys(), textValues)).grid(row=n + 1, column=0)
    updPriceWindow.mainloop()


# Stock view values

def viewStockPrompt():
    with open('stock.dat', 'rb') as stockFile:
        stockRead = pickle.load(stockFile)

        viewStockWindow = Tk()
        viewStockWindow.title("View stock")

        n = 0
        labels = []
        labels2 = []

        for key in stockRead.keys():
            labels.append(Label(viewStockWindow, text=key + ":").grid(row=n, column=0))
            labels2.append(Label(viewStockWindow, text=str(stockRead[key]) + " units").grid(row=n, column=1))

            n += 1

    updateWorkerButton = Button(viewStockWindow, text="OK",
                                command=viewStockWindow.destroy).grid(row=n + 1, column=0)
    viewStockWindow.mainloop()


# ------------------------------- MAIN MENU ------------------------------------

def initializeMainMenu():
    mainMenu = Tk()
    mainMenu.geometry('500x500')
    mainMenu.title('Warehouse Management')
    mainMenu.grid_columnconfigure(0, weight=1)

    for rowCounter in range(0, 16):
        mainMenu.grid_rowconfigure(rowCounter, weight=1)

    button1 = Button(mainMenu, text="Add an account", command=addAccountPrompt).grid(row=0, column=0)
    spacer1 = Label(mainMenu, text="  ").grid(row=1, column=0)
    button2 = Button(mainMenu, text="View worker status", command=viewWorkerPrompt).grid(row=2, column=0)
    button3 = Button(mainMenu, text="Update worker attendance", command=updateWorkerPrompt).grid(row=3, column=0)
    button4 = Button(mainMenu, text="Calculate worker wages", command=workerWagePrompt).grid(row=4, column=0)
    spacer2 = Label(mainMenu, text="  ").grid(row=5, column=0)
    button5 = Button(mainMenu, text="Update price of stock", command=updatePricePrompt).grid(row=6, column=0)
    button6 = Button(mainMenu, text="Check current stock", command=viewStockPrompt).grid(row=7, column=0)
    button7 = Button(mainMenu, text="Received shipment (add stock)", command=dummyFunc).grid(row=8, column=0)
    button8 = Button(mainMenu, text="Ship cargo and generate invoice (remove stock)", command=dummyFunc).grid(row=9,
                                                                                                              column=0)
    spacer3 = Label(mainMenu, text="  ").grid(row=10, column=0)
    button9 = Button(mainMenu, text="Check and add vehicles (if vehicles have completed journey and returned)",
                     command=dummyFunc).grid(row=11, column=0)
    spacer4 = Label(mainMenu, text="  ").grid(row=12, column=0)
    button10 = Button(mainMenu, text="Log out", command=mainMenu.destroy).grid(row=13, column=0)

    #  implement out of stock and too much stock checks here and add lines of text!

    mainMenu.mainloop()


# ------------------------------- LOGIN AUTHORIZATION------------------------------------

def loginAuth(usernameArg, passwordArg):
    with open("logins.csv", "r") as adminFile:
        adminRead = csv.DictReader(adminFile)
        isValid = False

        for line in adminRead:
            if (line['Username'] == usernameArg.get()) and (line['Password'] == passwordArg.get()):
                isValid = True
                break

        if isValid:
            loginWindow.destroy()
            initializeMainMenu()

        else:
            failurePrompt("Invalid credentials!")


# MAIN BODY, Basically the login window only. It calls the main menu when authorized, which in turn calls all other functions.

loginWindow = Tk()
loginWindow.geometry('250x125')
loginWindow.title('Login')

loginWindow.grid_columnconfigure(0, weight=1)
loginWindow.grid_columnconfigure(1, weight=1)
loginWindow.grid_rowconfigure(0, weight=1)
loginWindow.grid_rowconfigure(1, weight=1)
loginWindow.grid_rowconfigure(2, weight=1)
loginWindow.grid_rowconfigure(3, weight=1)

usernameLabel = Label(loginWindow, text="Username").grid(row=0, column=0)
username = StringVar(loginWindow)
usernameEntry = Entry(loginWindow, textvariable=username).grid(row=0, column=1)

passwordLabel = Label(loginWindow, text="Password").grid(row=1, column=0)
password = StringVar(loginWindow)
passwordEntry = Entry(loginWindow, textvariable=password, show='*').grid(row=1, column=1)

loginButton = Button(loginWindow, text="Login", command=lambda: loginAuth(username, password)).grid(row=3, column=0)

loginWindow.mainloop()