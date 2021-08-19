import csv


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


def isWorker(username, password):
    with open("workers.csv", "r") as workerFile:
        workerRead = csv.DictReader(workerFile)
        isValid = False

        for line in workerRead:
            if (line['Username'] == username) and (line['Password'] == password):
                isValid = True
                break

        return isValid


def addWorker(username, password):
    with open("workers.csv", "a", newline='') as workerFile:
        workerWrite = csv.DictWriter(workerFile, ['Username', 'Password'])
        workerWrite.writerow({'Username': username, 'Password': password})


def workerstatus():

    l=[]
    minHours = 24
    maxHours = 0

    with open('workerlog.csv','r') as workerFile:
        workerRead = csv.DictReader(workerFile)

        for line in workerRead:
            if line['workerHours'] == '0':
                a=line['workerName']
                l.append(a)

            elif ( int(line['workerHours']) < minHours ):
                minHours = int(line['workerHours'])
                minWorker = line['workerName']

            elif ( int(line['workerHours']) > maxHours ):
                maxHours = int(line['workerHours'])
                maxWorker = line['workerName']

        print('List of absent workers today is: ',l)
        print('The worker who has worked the most today is: ', maxWorker)
        print('The worker who has worked the least today is: ', minWorker)

#-------------------------------------------------------------------------------------------------------

print('----- LOGIN SCREEN -----')
print('---Enter your choice:---')
print()
print('1. Administrator Login')
print('2. Worker Login')
print()
choice = int(input('Enter your choice (1/2): '))

if choice == 1:

    print()
    print('----- ADMIN LOGIN -----')
    username = str(input("Enter username: "))
    password = str(input("Enter password: "))
    print()

    if isAdmin(username, password):
        # ADMINISTRATOR FUNCTIONS
        print('Access granted.')
        print()
        print('1. Add an Administrator account')
        print('2. Add a Worker account')
        print('3. View worker status and today\'s statistics')
        print()
        choiceA = int(input('Enter your choice (1/2/3): '))

        if choiceA == 1:
            uname = str(input("Enter the new user's username: "))
            passwd = str(input("Enter the new user's password: "))
            addAdmin(uname, passwd)

        elif choiceA == 2:
            uname = str(input("Enter the new user's username: "))
            passwd = str(input("Enter the new user's password: "))
            addWorker(uname, passwd)

        elif choiceA == 3:
            workerstatus()

    else:
        print('Wrong username and/or password. The program will now exit.')

elif choice == 2:

    print()
    print('----- WORKER LOGIN ----')
    username = str(input("Enter username: "))
    password = str(input("Enter password: "))
    print()

    if isWorker(username, password):
        print('Access granted.')
        # HERE is where the fun begins. This is where we will add all worker functions, warehouse and vehicle management

    else:
        print('Wrong username and/or password. The program will now exit.')

else:
    print("Invalid input. Program will now exit.")
