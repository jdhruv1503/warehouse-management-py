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
    newPrice = abs(int(input("What should be the new price? ")))

    # to make it case insensitive
    for productKey in pricesDict.keys():
        if productKey.lower() == product.lower():
            product = productKey

    pricesDict[product] = newPrice

    with open("prices.dat", "wb") as pricesFile:
        pickle.dump(pricesDict, pricesFile)


def addStock():
    stockDict = checkStock()
    print("The products are: ", stockDict)

    product = str(input("Which product to update stock from? "))
    add = abs(int(input("How much stock to add? ")))

    # to make it case insensitive
    for productKey in stockDict.keys():
        if productKey.lower() == product.lower():
            product = productKey

    stockDict[product] += add

    with open("stock.dat", "wb") as stockFile:
        pickle.dump(stockDict, stockFile)

    print("Stock successfully updated!")


def addVehicles():
    with open("vehicles.dat", "rb") as vehicleFile:
        vehicles = pickle.load(vehicleFile)

    print("There are currently", vehicles, "vehicles.")
    addedVehicles = abs(int(input("How many vehicles have come back? ")))
    vehicles += addedVehicles

    with open("vehicles.dat", "wb") as vehicleFile:
        pickle.dump(vehicles, vehicleFile)

    print("Vehicles successfully updated!")


def removeStock():
    stockDict = checkStock()
    vehicles = checkVehicles()
    print("The products are: ", stockDict)

    product = str(input("Which product to update stock from? "))
    remove = abs(int(input("How much cargo to ship? ")))

    # to make it case insensitive
    for productKey in stockDict.keys():
        if productKey.lower() == product.lower():
            product = productKey

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
            gstRate = abs(int(input("Enter desired GST rate in %: ")))
            print()
            print("--SALES INVOICE--")
            print("Product: ", product)
            print("Price per unit: ", pricesDict[product])
            print("Quantity sold: ", remove)
            print("GST (at", gstRate, "%: ", (pricesDict[product] * remove * gstRate / 100))
            print("-----------------")
            print("Total: ", (pricesDict[product] * remove * (gstRate + 100) / 100))
            print()

    elif vehicles == 0:
        print("Cannot ship this cargo: There are no vehicles to ship it with")

    else:
        print("Cannot ship this cargo: Not enough stock")


def workerStatus():
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

    print('List of absent workers today is: ', absentWorkerList)
    print('The workers who have worked the most today is: ', maxWorkerList)
    print('The workers who have worked the least today is: ', minWorkerList)


def workerUpdate():
    with open('workerlog.dat', 'rb') as workerFile:
        workerRead = pickle.load(workerFile)

    with open('workerlog.dat', 'wb') as workerFile:
        workerWrite = {}

        for key in workerRead.keys():
            inputPrompt = "Enter the number of hours worked for employee " + key + ": "
            hours = min(24,abs(int(input(inputPrompt))))
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
        choiceA = abs(int(input('Enter your choice (0-9): ')))

        if choiceA == 1:
            print()
            uname = str(input("Enter the new user's username: "))
            passwd = str(input("Enter the new user's password: "))
            addAdmin(uname, passwd)
            print("Adding new user", uname, "successful.")

            print("Press Enter to continue")
            input()

        elif choiceA == 2:
            print()
            workerStatus()

            print("Press Enter to continue")
            input()

        elif choiceA == 3:
            print()
            workerUpdate()

            print("Press Enter to continue")
            input()

        elif choiceA == 4:
            print()
            workerWages()

            print("Press Enter to continue")
            input()

        elif choiceA == 5:
            print()
            updatePrices()

            print("Press Enter to continue")
            input()

        elif choiceA == 6:
            print()
            print("Current stock is: ", checkStock())

            print("Press Enter to continue")
            input()

        elif choiceA == 7:
            print()
            addStock()

            print("Press Enter to continue")
            input()

        elif choiceA == 8:
            print()
            removeStock()

            print("Press Enter to continue")
            input()

        elif choiceA == 9:
            print()
            addVehicles()

            print("Press Enter to continue")
            input()

        elif choiceA == 0:
            continueLoop = False

        else:
            print('Invalid input. The program will now exit.')

else:
    print('Wrong username and/or password. The program will now exit.')
