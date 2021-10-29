from tkinter import *
import pickle

# ------------------- Some UI constants used to style buttons, text, etc. ---------------------

BACKGROUND_COL = '#212630'
FOREGROUND_COL = '#D9D9D9'
BUTTON_COL = '#5939F9'
BUTTON_COL_RED = '#DE2929'
TITLE_FONT = 'Poppins Black'
BODY_FONT = 'Poppins Regular'


# ------------------- Some generic prompts used throughout the program --------------------------

def successPrompt(message):
    successPopup = Tk()
    successPopup.title('Success!')
    successPopup.geometry('600x160')
    successPopup.configure(bg=BACKGROUND_COL)

    successPopup.grid_columnconfigure(0, weight=1)
    successPopup.grid_rowconfigure(0, weight=1)
    successPopup.grid_rowconfigure(1, weight=1)

    textLabel = Label(successPopup, text=message, bg=BACKGROUND_COL, fg=FOREGROUND_COL, font=(BODY_FONT, 20)).grid(
        row=0, column=0)
    okButton = Button(successPopup, text="OK", command=successPopup.destroy, bg=BUTTON_COL, fg=FOREGROUND_COL,
                      font=(BODY_FONT, 15)).grid(row=1, column=0)

    successPopup.mainloop()


def failurePrompt(message):
    failPopup = Tk()
    failPopup.title('Error!')
    failPopup.geometry('600x160')
    failPopup.configure(bg=BACKGROUND_COL)

    failPopup.grid_columnconfigure(0, weight=1)
    failPopup.grid_rowconfigure(0, weight=1)
    failPopup.grid_rowconfigure(1, weight=1)

    textLabel = Label(failPopup, text=message, bg=BACKGROUND_COL, fg=FOREGROUND_COL, font=(BODY_FONT, 20)).grid(row=0,
                                                                                                                column=0)
    okButton = Button(failPopup, text="OK", command=failPopup.destroy, bg=BUTTON_COL, fg=FOREGROUND_COL,
                      font=(BODY_FONT, 15)).grid(row=1, column=0)

    failPopup.mainloop()


# ------------------- Some generic vehicle functions used throughout the program --------------------------

def checkVehicles():
    with open("vehicles.dat", "rb") as vehicleFile:
        vehicles = pickle.load(vehicleFile)
    return vehicles


def removeOneVehicle():
    newVehicles = checkVehicles() - 1

    with open("vehicles.dat", "wb") as vehicleFile:
        pickle.dump(newVehicles, vehicleFile)


# ---------------------------------------- Adding accounts -----------------------------------------

def addAccountPrompt():
    addAccWindow = Tk()
    addAccWindow.title('Add a user account')
    addAccWindow.geometry('500x300')
    addAccWindow.configure(bg=BACKGROUND_COL)

    addAccWindow.grid_columnconfigure(0, weight=1)
    addAccWindow.grid_columnconfigure(1, weight=1)
    addAccWindow.grid_rowconfigure(0, weight=1)
    addAccWindow.grid_rowconfigure(1, weight=1)
    addAccWindow.grid_rowconfigure(2, weight=1)
    addAccWindow.grid_rowconfigure(3, weight=1)

    usernameAddLabel = Label(addAccWindow, text="Username", font=(BODY_FONT,15), bg=BACKGROUND_COL, fg=FOREGROUND_COL).grid(row=0, column=0)
    usernameAdd = StringVar(addAccWindow)
    usernameAddEntry = Entry(addAccWindow, textvariable=usernameAdd, font=(BODY_FONT,15), bg=BACKGROUND_COL, fg=FOREGROUND_COL).grid(row=0, column=1)

    passwordAddLabel = Label(addAccWindow, text="Password", font=(BODY_FONT,15), bg=BACKGROUND_COL, fg=FOREGROUND_COL).grid(row=1, column=0)
    passwordAdd = StringVar(addAccWindow)
    passwordAddEntry = Entry(addAccWindow, textvariable=passwordAdd, show='*', font=(BODY_FONT,15), bg=BACKGROUND_COL, fg=FOREGROUND_COL).grid(row=1, column=1)

    passwordConfirmLabel = Label(addAccWindow, text="Confirm password", font=(BODY_FONT,15), bg=BACKGROUND_COL, fg=FOREGROUND_COL).grid(row=2, column=0)
    password2Add = StringVar(addAccWindow)
    passwordConfirmEntry = Entry(addAccWindow, textvariable=password2Add, show='*', font=(BODY_FONT,15), bg=BACKGROUND_COL, fg=FOREGROUND_COL).grid(row=2, column=1)

    addButton = Button(addAccWindow, text="Add a new account",
                       command=lambda: addAccount(usernameAdd, passwordAdd, password2Add), font=(BODY_FONT, 15), bg=BUTTON_COL, fg=FOREGROUND_COL, bd=0).grid(row=3,
                                                                                                column=0)

    addAccWindow.mainloop()


def addAccount(usernameAddArg, passwordAddArg, password2AddArg):
    if passwordAddArg.get() == password2AddArg.get():

        with open("logins.dat", "rb") as adminFile:
            admins = pickle.load(adminFile)

        with open("logins.dat", "wb") as adminFile:
            admins[usernameAddArg.get()] = passwordAddArg.get()
            pickle.dump(admins, adminFile)

        successPrompt("User has been added!")

    else:
        failurePrompt("Passwords do not match!")


# ----------------------------------------- Remove an account -----------------------------------------

def removeAccountPrompt():
    removeAccWindow = Tk()
    removeAccWindow.title('Remove a user account')
    removeAccWindow.geometry('500x200')
    removeAccWindow.configure(bg=BACKGROUND_COL)

    removeAccWindow.grid_columnconfigure(0, weight=1)
    removeAccWindow.grid_columnconfigure(1, weight=1)
    removeAccWindow.grid_rowconfigure(0, weight=1)
    removeAccWindow.grid_rowconfigure(1, weight=1)
    removeAccWindow.grid_rowconfigure(2, weight=1)
    removeAccWindow.grid_rowconfigure(3, weight=1)

    usernameAddLabel = Label(removeAccWindow, text="Username", font=(BODY_FONT,15), bg=BACKGROUND_COL, fg=FOREGROUND_COL).grid(row=0, column=0)
    usernameAdd = StringVar(removeAccWindow)
    usernameAddEntry = Entry(removeAccWindow, textvariable=usernameAdd, font=(BODY_FONT,15), bg=BACKGROUND_COL, fg=FOREGROUND_COL).grid(row=0, column=1)

    passwordAddLabel = Label(removeAccWindow, text="Password", font=(BODY_FONT,15), bg=BACKGROUND_COL, fg=FOREGROUND_COL).grid(row=1, column=0)
    passwordAdd = StringVar(removeAccWindow)
    passwordAddEntry = Entry(removeAccWindow, textvariable=passwordAdd, show='*', font=(BODY_FONT,15), bg=BACKGROUND_COL, fg=FOREGROUND_COL).grid(row=1, column=1)

    addButton = Button(removeAccWindow, text="Remove account",
                       command=lambda: removeAccount(usernameAdd, passwordAdd), font=(BODY_FONT, 15), bg=BUTTON_COL_RED , fg=FOREGROUND_COL, bd=0).grid(row=3,
                                                                                     column=0)

    removeAccWindow.mainloop()


def removeAccount(usernameAddArg, passwordAddArg):
    with open("logins.dat", "rb") as adminFile:
        admins = pickle.load(adminFile)

    try:
        if admins[usernameAddArg.get()] == passwordAddArg.get():
            admins.pop(usernameAddArg.get())

            with open("logins.dat", "wb") as adminFile:
                pickle.dump(admins, adminFile)

            successPrompt("User has been removed!")

        else:
            failurePrompt("Invalid credentials!")

    except KeyError:
        failurePrompt("User does not exist!")


# ----------------------------------------- View worker status -----------------------------------------

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
    workerStatWindow.configure(bg=BACKGROUND_COL)

    workerStatWindow.grid_columnconfigure(0, weight=1)
    workerStatWindow.grid_rowconfigure(0, weight=1)
    workerStatWindow.grid_rowconfigure(1, weight=1)
    workerStatWindow.grid_rowconfigure(2, weight=1)
    workerStatWindow.grid_rowconfigure(3, weight=1)

    label1 = Label(workerStatWindow, text=message1, font=(BODY_FONT, 15), bg=BACKGROUND_COL, fg=FOREGROUND_COL).grid(
        row=0, column=0)
    label2 = Label(workerStatWindow, text=message2, font=(BODY_FONT, 15), bg=BACKGROUND_COL, fg=FOREGROUND_COL).grid(
        row=1, column=0)
    label3 = Label(workerStatWindow, text=message3, font=(BODY_FONT, 15), bg=BACKGROUND_COL, fg=FOREGROUND_COL).grid(
        row=2, column=0)
    okButton = Button(workerStatWindow, text="OK", command=workerStatWindow.destroy, font=(BODY_FONT, 15),
                      bg=BUTTON_COL, fg=FOREGROUND_COL, bd=0).grid(row=3, column=0)
    workerStatWindow.mainloop()


# ----------------------------------------- Updating workers -----------------------------------------

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
    updWorkerWindow.configure(bg=BACKGROUND_COL)

    n = 0
    labels = []
    entries = []
    textValues = []

    # Mechanism to procedurally generate a window and populate it with values of worker hours, as well as reconfiguring rows

    for key in workerRead.keys():
        textValues.append(StringVar(updWorkerWindow))
        textValues[n].set(workerRead[key])

        labels.append(
            Label(updWorkerWindow, text=key, font=(BODY_FONT, 15), bg=BACKGROUND_COL, fg=FOREGROUND_COL).grid(row=n,
                                                                                                              column=0))
        entries.append(Entry(updWorkerWindow, textvariable=textValues[n], font=(BODY_FONT, 15), bg=BACKGROUND_COL,
                             fg=FOREGROUND_COL).grid(row=n, column=1))

        n += 1

    updateWorkerButton = Button(updWorkerWindow, text="Update values",
                                command=lambda: updateWorker(workerRead.keys(), textValues), font=(BODY_FONT, 15),
                                bg=BUTTON_COL, fg=FOREGROUND_COL, bd=0).grid(row=n + 1, column=0)
    updWorkerWindow.mainloop()


# ----------------------------------------- Calculating worker wages -----------------------------------------

def workerWagePrompt():
    hourlyRateWindow = Tk()
    hourlyRateWindow.geometry('580x150')
    hourlyRateWindow.title('Enter hourly wages')
    hourlyRateWindow.configure(bg=BACKGROUND_COL)

    hourlyRateWindow.grid_columnconfigure(0, weight=1)
    hourlyRateWindow.grid_columnconfigure(1, weight=1)
    hourlyRateWindow.grid_rowconfigure(0, weight=1)
    hourlyRateWindow.grid_rowconfigure(1, weight=1)

    rateItem = Label(hourlyRateWindow, text="Enter the hourly rate:", font=(BODY_FONT, 15), bg=BACKGROUND_COL,
                     fg=FOREGROUND_COL).grid(row=0, column=0)
    rate = StringVar(hourlyRateWindow)
    rateItem = Entry(hourlyRateWindow, textvariable=rate, font=(BODY_FONT, 15), bg=BACKGROUND_COL,
                     fg=FOREGROUND_COL).grid(row=0, column=1)

    rateItem = Button(hourlyRateWindow, text="Calculate wages", command=lambda: workerWageDisplay(rate.get()),
                      font=(BODY_FONT, 15), bg=BUTTON_COL, fg=FOREGROUND_COL, bd=0).grid(row=1,
                                                                                         column=1)
    hourlyRateWindow.mainloop()


def workerWageDisplay(rateValue):
    with open('workerlog.dat', 'rb') as workerFile:
        workerRead = pickle.load(workerFile)

    wageWindow = Tk()
    wageWindow.title("View worker wages")
    wageWindow.configure(bg=BACKGROUND_COL)

    wageWindow.columnconfigure(0, weight=1)
    wageWindow.columnconfigure(1, weight=1)

    n = 0
    labels = []
    labels2 = []

    for key in workerRead.keys():
        labels.append(
            Label(wageWindow, text=key + ":", font=(BODY_FONT, 15), bg=BACKGROUND_COL, fg=FOREGROUND_COL).grid(row=n,
                                                                                                               column=0))
        labels2.append(Label(wageWindow, text=str(workerRead[key] * int(rateValue)) + " rupees", font=(BODY_FONT, 15),
                             bg=BACKGROUND_COL, fg=FOREGROUND_COL).grid(row=n, column=1))

        n += 1

    workerWageButton = Button(wageWindow, text="OK",
                              command=wageWindow.destroy, font=(BODY_FONT, 15), bg=BUTTON_COL, fg=FOREGROUND_COL,
                              bd=0).grid(row=n + 1, column=0)
    wageWindow.mainloop()


# ----------------------------------------- Updating prices (identical syntax as that of updating worker values above)

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
        updPriceWindow.configure(bg=BACKGROUND_COL)

        n = 0
        labels = []
        entries = []
        textValues = []

        for key in priceRead.keys():
            textValues.append(StringVar(updPriceWindow))
            textValues[n].set(priceRead[key])

            labels.append(
                Label(updPriceWindow, text=key, font=(BODY_FONT, 15), bg=BACKGROUND_COL, fg=FOREGROUND_COL).grid(row=n,
                                                                                                                 column=0))
            entries.append(Entry(updPriceWindow, textvariable=textValues[n], font=(BODY_FONT, 15), bg=BACKGROUND_COL,
                                 fg=FOREGROUND_COL).grid(row=n, column=1))

            n += 1

    updPriceButton = Button(updPriceWindow, text="Update values",
                            command=lambda: updatePrices(priceRead.keys(), textValues), font=(BODY_FONT, 15),
                            bg=BUTTON_COL, fg=FOREGROUND_COL, bd=0).grid(row=n + 1, column=0)
    updPriceWindow.mainloop()


# ----------------------------------------- View current stock -----------------------------------------

def viewStockPrompt():
    with open('stock.dat', 'rb') as stockFile:
        stockRead = pickle.load(stockFile)

        viewStockWindow = Tk()
        viewStockWindow.title("View stock")
        viewStockWindow.configure(bg=BACKGROUND_COL)

        n = 0
        labels = []
        amounts = []

        for key in stockRead.keys():
            labels.append(
                Label(viewStockWindow, text=key + ":", font=(BODY_FONT, 15), bg=BACKGROUND_COL, fg=FOREGROUND_COL).grid(
                    row=n, column=0))
            amounts.append(
                Label(viewStockWindow, text=str(stockRead[key]) + " units", font=(BODY_FONT, 15), bg=BACKGROUND_COL,
                      fg=FOREGROUND_COL).grid(row=n, column=1))

            n += 1

    updateWorkerButton = Button(viewStockWindow, text="OK",
                                command=viewStockWindow.destroy, font=(BODY_FONT, 15), bg=BUTTON_COL, fg=FOREGROUND_COL,
                                bd=0).grid(row=n + 1, column=0)
    viewStockWindow.mainloop()


# ----------------------------------------- Add stock -----------------------------------------

def addStock(valuesArg):
    values = []
    for value in valuesArg:
        values.append(value.get())

    with open('stock.dat', 'rb') as stockFile:
        stockRead = pickle.load(stockFile)

        n = 0
        for key in stockRead:
            stockRead[key] += int(values[n])
            n += 1

    with open('stock.dat', 'wb') as stockFile:
        pickle.dump(stockRead, stockFile)

    successPrompt("Stock has been added!")


def addStockPrompt():
    with open('stock.dat', 'rb') as stockFile:
        stockRead = pickle.load(stockFile)

        addStockWindow = Tk()
        addStockWindow.title("Add stock")
        addStockWindow.configure(bg=BACKGROUND_COL)

        n = 0
        labels = []
        entries = []
        textValues = []

        for key in stockRead.keys():
            textValues.append(StringVar(addStockWindow))
            textValues[n].set("0")

            labels.append(
                Label(addStockWindow, text=key + ":", font=(BODY_FONT, 15), bg=BACKGROUND_COL, fg=FOREGROUND_COL).grid(
                    row=n, column=0))
            entries.append(Entry(addStockWindow, textvariable=textValues[n], font=(BODY_FONT, 15), bg=BACKGROUND_COL,
                                 fg=FOREGROUND_COL).grid(row=n, column=1))

            n += 1

    addStockButton = Button(addStockWindow, text="OK",
                            command=lambda: addStock(textValues), font=(BODY_FONT, 15), bg=BUTTON_COL,
                            fg=FOREGROUND_COL, bd=0).grid(row=n + 1, column=0)
    addStockWindow.mainloop()


# ----------------------------------------- Remove stock -----------------------------------------

def removeStock(valuesArg):
    availableVehicles = checkVehicles()
    values = []
    for value in valuesArg:
        values.append(value.get())

    # Checks if enough stock is available, and if a vehicle is available

    with open('stock.dat', 'rb') as stockFile:
        stockRead = pickle.load(stockFile)
        isValidTransaction = True
        vehicleIsAvailable = True
        n = 0

        for key in stockRead:
            if (stockRead[key] < int(values[n])):
                isValidTransaction = False
            n += 1

            if availableVehicles < 1:
                vehicleIsAvailable = False

    if isValidTransaction and vehicleIsAvailable:

        with open('stock.dat', 'rb') as stockFile:
            stockRead = pickle.load(stockFile)
            n = 0
            for key in stockRead:
                stockRead[key] -= int(values[n])
                n += 1

        with open('stock.dat', 'wb') as stockFile:
            pickle.dump(stockRead, stockFile)

        removeOneVehicle()

        successPrompt("Stock has been shipped!\nNow there are " + str(checkVehicles()) + " vehicles available.")

    elif not isValidTransaction:
        failurePrompt("There is not enough stock!")
    elif not vehicleIsAvailable:
        failurePrompt("There are no available vehicles!")


def removeStockPrompt():
    with open('stock.dat', 'rb') as stockFile:
        stockRead = pickle.load(stockFile)

        removeStockWindow = Tk()
        removeStockWindow.title("Ship stock")
        removeStockWindow.configure(bg=BACKGROUND_COL)

        n = 0
        labels = []
        entries = []
        textValues = []

        for key in stockRead.keys():
            textValues.append(StringVar(removeStockWindow))
            textValues[n].set("0")

            labels.append(Label(removeStockWindow, text=key + ":", font=(BODY_FONT, 15), bg=BACKGROUND_COL,
                                fg=FOREGROUND_COL).grid(row=n, column=0))
            entries.append(Entry(removeStockWindow, textvariable=textValues[n], font=(BODY_FONT, 15), bg=BACKGROUND_COL,
                                 fg=FOREGROUND_COL).grid(row=n, column=1))

            n += 1

    removeStockButton = Button(removeStockWindow, text="OK",
                               command=lambda: removeStock(textValues), font=(BODY_FONT, 15), bg=BUTTON_COL,
                               fg=FOREGROUND_COL, bd=0).grid(row=n + 1, column=0)
    removeStockWindow.mainloop()


# ----------------------------------------- Add vehicles -----------------------------------------

def addVehicles(vehiclesToAdd):
    if int(vehiclesToAdd.get()) > 0:
        newVehicles = checkVehicles() + int(vehiclesToAdd.get())

        with open("vehicles.dat", "wb") as vehicleFile:
            pickle.dump(newVehicles, vehicleFile)

        successPrompt("Vehicles have been successfully added!")

    else:
        failurePrompt("No. of vehicles to be added must be non-negative!")


def addVehiclesPrompt():
    displayString = "There are currently " + str(checkVehicles()) + " vehicles available."

    vehicleWindow = Tk()
    vehicleWindow.title('Add vehicles')
    vehicleWindow.geometry('600x290')
    vehicleWindow.configure(bg=BACKGROUND_COL)

    vehicleWindow.grid_columnconfigure(0, weight=1)
    vehicleWindow.grid_rowconfigure(0, weight=1)
    vehicleWindow.grid_rowconfigure(1, weight=1)
    vehicleWindow.grid_rowconfigure(2, weight=1)
    vehicleWindow.grid_rowconfigure(3, weight=1)

    vehiclesLabel = Label(vehicleWindow, text=displayString, font=(BODY_FONT, 20), bg=BACKGROUND_COL,
                          fg=FOREGROUND_COL).grid(row=0, column=0)
    addVehiclesLabel = Label(vehicleWindow, text="How many vehicles to add?", font=(BODY_FONT, 20), bg=BACKGROUND_COL,
                             fg=FOREGROUND_COL).grid(row=1, column=0)

    vehiclesToAdd = StringVar(vehicleWindow)
    vehicleEntry = Entry(vehicleWindow, textvariable=vehiclesToAdd, font=(BODY_FONT, 20), bg=BACKGROUND_COL,
                         fg=FOREGROUND_COL).grid(row=2, column=0)

    vehicleButton = Button(vehicleWindow, text="Add vehicles", font=(BODY_FONT, 20), bg=BUTTON_COL, fg=FOREGROUND_COL,
                           bd=0, command=lambda: addVehicles(vehiclesToAdd)).grid(row=3,
                                                                                  column=0)

    vehicleWindow.mainloop()


# ------------------------------- MAIN MENU ------------------------------------

def initializeMainMenu(usernameArg):
    mainMenu = Tk()
    mainMenu.geometry('1180x760')
    mainMenu.title('Warehouse Management')
    mainMenu.configure(bg=BACKGROUND_COL)

    mainMenu.grid_columnconfigure(0, weight=0)
    mainMenu.grid_columnconfigure(1, weight=1)
    mainMenu.grid_columnconfigure(2, weight=1)
    for rowCounter in range(0, 17):
        mainMenu.grid_rowconfigure(rowCounter, weight=1)

    labelTitle = Label(mainMenu, text="Warehouse Management", font=(TITLE_FONT, 45), bg=BACKGROUND_COL,
                       fg=FOREGROUND_COL).grid(row=0, column=1)

    button1 = Button(mainMenu, text="Add an account", font=(BODY_FONT, 15), bg=BUTTON_COL, fg=FOREGROUND_COL, bd=0,
                     command=addAccountPrompt).grid(row=1, column=1)
    button2 = Button(mainMenu, text="Remove an account", font=(BODY_FONT, 15), bg=BUTTON_COL, fg=FOREGROUND_COL, bd=0,
                     command=removeAccountPrompt).grid(row=2, column=1)

    spacer1 = Label(mainMenu, text="  ", font=(TITLE_FONT, 10), bg=BACKGROUND_COL, fg=FOREGROUND_COL).grid(row=3,
                                                                                                           column=0)
    button3 = Button(mainMenu, text="View worker status", font=(BODY_FONT, 15), bg=BUTTON_COL, fg=FOREGROUND_COL, bd=0,
                     command=viewWorkerPrompt).grid(row=4, column=1)
    button4 = Button(mainMenu, text="Update worker attendance", font=(BODY_FONT, 15), bg=BUTTON_COL, fg=FOREGROUND_COL,
                     bd=0, command=updateWorkerPrompt).grid(row=5, column=1)
    button5 = Button(mainMenu, text="Calculate worker wages", font=(BODY_FONT, 15), bg=BUTTON_COL, fg=FOREGROUND_COL,
                     bd=0, command=workerWagePrompt).grid(row=6, column=1)

    spacer2 = Label(mainMenu, text="  ", font=(TITLE_FONT, 10), bg=BACKGROUND_COL, fg=FOREGROUND_COL).grid(row=7,
                                                                                                           column=0)
    button6 = Button(mainMenu, text="Update price of stock", font=(BODY_FONT, 15), bg=BUTTON_COL, fg=FOREGROUND_COL,
                     bd=0, command=updatePricePrompt).grid(row=8, column=1)
    button7 = Button(mainMenu, text="Check current stock", font=(BODY_FONT, 15), bg=BUTTON_COL, fg=FOREGROUND_COL, bd=0,
                     command=viewStockPrompt).grid(row=9, column=1)
    button8 = Button(mainMenu, text="Received shipment (add stock)", font=(BODY_FONT, 15), bg=BUTTON_COL,
                     fg=FOREGROUND_COL, bd=0, command=addStockPrompt).grid(row=10, column=1)
    button9 = Button(mainMenu, text="Ship cargo and generate invoice (remove stock)", font=(BODY_FONT, 15),
                     bg=BUTTON_COL, fg=FOREGROUND_COL, bd=0, command=removeStockPrompt).grid(
        row=11,
        column=1)

    spacer3 = Label(mainMenu, text="  ", font=(TITLE_FONT, 15), bg=BACKGROUND_COL, fg=FOREGROUND_COL).grid(row=12,
                                                                                                           column=1)
    button10 = Button(mainMenu, text="Check and add vehicles (if vehicles have completed journey and returned)",
                      font=(BODY_FONT, 15), bg=BUTTON_COL, fg=FOREGROUND_COL, bd=0, command=addVehiclesPrompt).grid(
        row=13, column=1)

    spacer4 = Label(mainMenu, text="  ", font=(TITLE_FONT, 10), bg=BACKGROUND_COL, fg=FOREGROUND_COL).grid(row=14,
                                                                                                           column=1)
    labelLogIn = Label(mainMenu, text="Logged in as:", font=(BODY_FONT, 15), bg=BACKGROUND_COL, fg=FOREGROUND_COL).grid(
        row=15, column=0)
    labelLogIn2 = Label(mainMenu, text=usernameArg, font=(BODY_FONT, 15), bg=BACKGROUND_COL, fg=FOREGROUND_COL).grid(
        row=16, column=0)
    button11 = Button(mainMenu, text="Log out", command=mainMenu.destroy, font=(BODY_FONT, 15), bg=BUTTON_COL_RED,
                      fg=FOREGROUND_COL, bd=0).grid(row=15, column=2)

    #  implement out of stock and too much stock checks here and add lines of text!

    mainMenu.mainloop()


# ------------------------------- LOGIN AUTHORIZATION------------------------------------

def loginAuth(usernameArg, passwordArg):
    with open("logins.dat", "rb") as adminFile:
        adminRead = pickle.load(adminFile)

    isValid = False

    for account in adminRead.keys():
        if account == usernameArg.get() and adminRead[account] == passwordArg.get():
            isValid = True
            break

    if isValid:
        loginWindow.destroy()
        initializeMainMenu(usernameArg.get())

    else:
        failurePrompt("Invalid credentials!")


# MAIN BODY, Basically the login window only. It calls the main menu when authorized, which in turn calls all other functions.

loginWindow = Tk()
loginWindow.geometry('425x550')
loginWindow.eval('tk::PlaceWindow . center')
loginWindow.title('Login')
loginWindow.configure(bg=BACKGROUND_COL)

loginWindow.grid_columnconfigure(0, weight=1)
loginWindow.grid_rowconfigure(0, weight=1)
loginWindow.grid_rowconfigure(1, weight=1)
loginWindow.grid_rowconfigure(2, weight=1)
loginWindow.grid_rowconfigure(3, weight=1)
loginWindow.grid_rowconfigure(4, weight=1)
loginWindow.grid_rowconfigure(5, weight=1)
loginWindow.grid_rowconfigure(6, weight=1)
loginWindow.grid_rowconfigure(7, weight=1)

mainLabel = Label(loginWindow, text="Login", font=(TITLE_FONT, 40), bg=BACKGROUND_COL, fg=FOREGROUND_COL).grid(row=0,
                                                                                                               column=0)
spacer1 = Label(loginWindow, text=" ", font=(BODY_FONT, 10), bg=BACKGROUND_COL, fg=FOREGROUND_COL).grid(row=1, column=0)

usernameLabel = Label(loginWindow, text="Username:", font=(BODY_FONT, 20), bg=BACKGROUND_COL, fg=FOREGROUND_COL).grid(
    row=2, column=0)
username = StringVar(loginWindow)
usernameEntry = Entry(loginWindow, textvariable=username, font=(BODY_FONT, 20), bg=BACKGROUND_COL,
                      fg=FOREGROUND_COL).grid(row=3, column=0)

passwordLabel = Label(loginWindow, text="Password:", font=(BODY_FONT, 20), bg=BACKGROUND_COL, fg=FOREGROUND_COL).grid(
    row=4, column=0)
password = StringVar(loginWindow)
passwordEntry = Entry(loginWindow, textvariable=password, show='*', font=(BODY_FONT, 20), bg=BACKGROUND_COL,
                      fg=FOREGROUND_COL).grid(row=5, column=0)

spacer2 = Label(loginWindow, text=" ", font=(BODY_FONT, 10), bg=BACKGROUND_COL, fg=FOREGROUND_COL).grid(row=6, column=0)
loginButton = Button(loginWindow, text="Login", font=(BODY_FONT, 20), bg=BUTTON_COL, fg=FOREGROUND_COL, bd=0,
                     command=lambda: loginAuth(username, password)).grid(row=7, column=0)

loginWindow.mainloop()
