import csv
import pickle


def isAdmin(username, password):
    with open("logins.csv", "r") as adminFile:
        adminRead = csv.DictReader(adminFile)
        isValid = False

        for line in adminRead:
            if (line['Username'] == username) and (line['Password'] == password):
                isValid = True
                break

        return isValid


def addAdmin(username, password):
    with open("logins.csv", "a", newline='') as adminFile:
        adminWrite = csv.DictWriter(adminFile, ['Username', 'Password'])
        adminWrite.writerow({'Username': username, 'Password': password})


def checkStock():
    with open("stock.dat", "rb") as stockFile:
        stockDict = pickle.load(stockFile)
    return stockDict


def checkVehicles():
    with open("vehicles.dat", "rb") as vehicleFile:
        vehicles = pickle.load(vehicleFile)
    return vehicles


def outOfStockCheck():
    outOfStock = False
    stockDict = checkStock()
    itemsOutOfStock = []

    for key in stockDict.keys():
        if stockDict[key] == 0:
            outOfStock = True
            itemsOutOfStock.append(key)

    if outOfStock:
        print("ALERT! Following items are currently out of stock: ", itemsOutOfStock)


def tooMuchStockCheck():
    maxCapacity = 1000
    stockDict = checkStock()
    totalStock = 0

    for value in stockDict.values():
        totalStock += value

    if totalStock >= 0.9 * maxCapacity:
        print("ALERT! Warehouse nearing capacity. Ship some stock soon. Max capacity: ", maxCapacity,
              " and current stock: ", totalStock)


def updatePrices():
    with open("prices.dat", "rb") as pricesFile:
        pricesDict = pickle.load(pricesFile)

    print("Current prices are:", pricesDict)
    product = str(input("Which product to update price of? "))
    newPrice = int(input("What should be the new price? "))
    pricesDict[product] = newPrice

    with open("prices.dat", "wb") as pricesFile:
        pickle.dump(pricesDict, pricesFile)


def addStock():
    stockDict = checkStock()
    print("The products are: ", stockDict)

    product = str(input("Which product to update stock from? "))
    add = int(input("How much stock to add? "))
    stockDict[product] += add

    with open("stock.dat", "wb") as stockFile:
        pickle.dump(stockDict, stockFile)

    print("Stock successfully updated!")


def addVehicles():
    with open("vehicles.dat", "rb") as vehicleFile:
        vehicles = pickle.load(vehicleFile)

    print("There are currently", vehicles, "vehicles.")
    addedVehicles = int(input("How many vehicles have come back? "))
    vehicles += addedVehicles

    with open("vehicles.dat", "wb") as vehicleFile:
        pickle.dump(vehicles, vehicleFile)

    print("Vehicles successfully updated!")


def removeStock():
    stockDict = checkStock()
    vehicles = checkVehicles()
    print("The products are: ", stockDict)

    product = str(input("Which product to update stock from? "))
    remove = int(input("How much cargo to ship? "))

    if remove <= stockDict[product] and vehicles > 0:
        stockDict[product] -= remove

        print("Stock successfully updated! Shipped cargo using 1 vehicle.")

        with open("stock.dat", "wb") as stockFile:
            pickle.dump(stockDict, stockFile)

        with open("vehicles.dat", "wb") as vehicleFile:
            pickle.dump(vehicles - 1, vehicleFile)

        with open("prices.dat", "rb") as pricesFile:
            pricesDict = pickle.load(pricesFile)

            print()
            print("--SALES INVOICE--")
            print("Product: ", product)
            print("Price per unit: ", pricesDict[product])
            print("Quantity sold: ", remove)
            print("-----------------")
            print("Total: ", (pricesDict[product] * remove))
            print()

    elif vehicles == 0:
        print("Cannot ship this cargo: There are no vehicles to ship it with")

    else:
        print("Cannot ship this cargo: Not enough stock")


def workerStatus():
    absentWorkerList = []
    minHours = 24
    maxHours = 0

    with open('workerlog.dat', 'rb') as workerFile:
        workerRead = pickle.load(workerFile)

        for key in workerRead.keys():
            if workerRead[key] == 0:
                absentWorkerList.append(key)

            elif workerRead[key] < minHours:
                minHours = workerRead[key]
                minWorker = key

            elif workerRead[key] > maxHours:
                maxHours = workerRead[key]
                maxWorker = key

    print('List of absent workers today is: ', absentWorkerList)
    print('The worker who has worked the most today is: ', maxWorker)
    print('The worker who has worked the least today is: ', minWorker)


def workerUpdate():
    with open('workerlog.dat', 'rb') as workerFile:
        workerRead = pickle.load(workerFile)

    with open('workerlog.dat', 'wb') as workerFile:
        workerWrite = {}

        for key in workerRead.keys():
            inputPrompt = "Enter the number of hours worked for employee " + key + ": "
            hours = int(input(inputPrompt))
            workerWrite[key] = hours

        pickle.dump(workerWrite, workerFile)


def workerWages():
    hourlyRate = float(input("Enter the hourly rate to be paid: "))

    with open('workerlog.dat', 'rb') as workerFile:
        workerRead = pickle.load(workerFile)

        for key in workerRead.keys():
            if workerRead[key] == 0:
                print(key, "was absent")
            else:
                print(key, "is to be paid", (hourlyRate * workerRead[key]))


continueLoop = True

print('----- LOGIN SCREEN -----')
print()
usernameInput = str(input("Enter username: "))
passwordInput = str(input("Enter password: "))
print()

if isAdmin(usernameInput, passwordInput):
    print('Access granted.')
    outOfStockCheck()
    tooMuchStockCheck()

    while continueLoop:
        print()
        print('1. Add a new login account')
        print()
        print('2. View worker status and today\'s statistics')
        print('3. Update today\'s worker attendance')
        print('4. Calculate today\'s worker wages')
        print()
        print('5. Check and update price of stock')
        print('6. Check current warehouse stock')
        print('7. Received shipment (add stock)')
        print('8. Ship cargo and generate invoice (remove stock)')
        print('9. Check and add vehicles (if vehicles have completed journey and returned)')
        print()
        print('0. Log out')
        print()
        choiceA = int(input('Enter your choice (0-9): '))

        if choiceA == 1:
            print()
            uname = str(input("Enter the new user's username: "))
            passwd = str(input("Enter the new user's password: "))
            addAdmin(uname, passwd)
            print("Adding new user", uname, "successful.")

            print("Enter any key to continue")
            input()

        elif choiceA == 2:
            print()
            workerStatus()

            print("Enter any key to continue")
            input()

        elif choiceA == 3:
            print()
            workerUpdate()

            print("Enter any key to continue")
            input()

        elif choiceA == 4:
            print()
            workerWages()

            print("Enter any key to continue")
            input()

        elif choiceA == 5:
            print()
            updatePrices()

            print("Enter any key to continue")
            input()

        elif choiceA == 6:
            print()
            print("Current stock is: ", checkStock())

            print("Enter any key to continue")
            input()

        elif choiceA == 7:
            print()
            addStock()

            print("Enter any key to continue")
            input()

        elif choiceA == 8:
            print()
            removeStock()

            print("Enter any key to continue")
            input()

        elif choiceA == 9:
            print()
            addVehicles()

            print("Enter any key to continue")
            input()

        elif choiceA == 0:
            continueLoop = False

        else:
            print('Invalid input. The program will now exit.')

else:
    print('Wrong username and/or password. The program will now exit.')
