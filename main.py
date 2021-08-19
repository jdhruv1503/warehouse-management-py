import csv
import pickle


def isAdmin(username, password):
    with open("admins.csv", "r") as adminFile:
        adminRead = csv.DictReader(adminFile)
        isValid = False

        for line in adminRead:
            if (line['Username'] == username) and (line['Password'] == password):
                isValid = True
                break

        return isValid


def addAdmin(username, password):
    with open("admins.csv", "a", newline='') as adminFile:
        adminWrite = csv.DictWriter(adminFile, ['Username', 'Password'])
        adminWrite.writerow({'Username': username, 'Password': password})


def checkStock():
    with open("stock.dat", "rb") as stockFile:
        stockDict = pickle.load(stockFile)
    return stockDict

def outOfStockCheck():
    outOfStock = False
    stockDict = checkStock()
    itemsOutOfStock = []

    for key in stockDict.keys():
        if stockDict[key]==0:
            outOfStock = True
            itemsOutOfStock.append(key)

    if outOfStock:
        print("ALERT! Following items are currently out of stock: ",itemsOutOfStock)

def tooMuchStockCheck():
    maxCapacity = 1000
    stockDict = checkStock()
    totalStock = 0

    for value in stockDict.values():
        totalStock += value

    if totalStock >= 0.9*maxCapacity:
        print("ALERT! Warehouse nearing capacity. Ship some stock soon. Max capacity: ",maxCapacity," and current stock: ",totalStock)

def addStock():
    maxCapacity = 1000
    stockDict = checkStock()
    print("The products are: ", stockDict)

    product = str(input("Which product to update stock from? "))
    add = int(input("How much stock to add? "))
    stockDict[product] += add

    with open("stock.dat", "wb") as stockFile:
        pickle.dump(stockDict, stockFile)

    print("Stock successfully updated!")


def removeStock():
    stockDict = checkStock()
    print("The products are: ", stockDict)

    product = str(input("Which product to update stock from? "))
    remove = int(input("How much cargo to ship? "))

    if remove <= stockDict[product]:
        stockDict[product] -= remove
        print("Stock successfully updated!")
        with open("stock.dat", "wb") as stockFile:
            pickle.dump(stockDict, stockFile)

    else:
        print("Cannot ship this cargo: Not enough stock")


def workerStatus():
    l = []
    minHours = 24
    maxHours = 0

    with open('workerlog.csv', 'r') as workerFile:
        workerRead = csv.DictReader(workerFile)

        for line in workerRead:
            if line['workerHours'] == '0':
                a = line['workerName']
                l.append(a)

            elif int(line['workerHours']) < minHours:
                minHours = int(line['workerHours'])
                minWorker = line['workerName']

            elif int(line['workerHours']) > maxHours:
                maxHours = int(line['workerHours'])
                maxWorker = line['workerName']

        print('List of absent workers today is: ', l)
        print('The worker who has worked the most today is: ', maxWorker)
        print('The worker who has worked the least today is: ', minWorker)


# -------------------------------------------------------------------------------------------------------

continueLoop = True

print('----- LOGIN SCREEN -----')
print()
username = str(input("Enter username: "))
password = str(input("Enter password: "))
print()

if isAdmin(username, password):
    print('Access granted.')
    outOfStockCheck()
    tooMuchStockCheck()

    while continueLoop:
        print()
        print('1. Add a new login account')
        print('2. View worker status and today\'s statistics')
        print('3. Check current warehouse stock')
        print('4. Received shipment (add stock)')
        print('5. Ship cargo (remove stock)')
        print('9. Log out')
        print()
        choiceA = int(input('Enter your choice (1-9): '))

        if choiceA == 1:
            print()
            uname = str(input("Enter the new user's username: "))
            passwd = str(input("Enter the new user's password: "))
            addAdmin(uname, passwd)
            print("Adding new user \'", uname, "\' successful.")

        elif choiceA == 2:
            print()
            workerStatus()

        elif choiceA == 3:
            print()
            print("Current stock is: ", checkStock())

        elif choiceA == 4:
            print()
            addStock()

        elif choiceA == 5:
            print()
            removeStock()

        elif choiceA == 9:
            continueLoop = False

        else:
            print('Invalid input. The program will now exit.')

else:
    print('Wrong username and/or password. The program will now exit.')
