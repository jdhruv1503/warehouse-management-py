import csv


def isAdmin(username=None, password=None):
    with open("admins.csv", "r") as adminFile:
        adminRead = csv.DictReader(adminFile)
        isValid = False

        for line in adminRead:
            if (line['Username'] == username) and (line['Password'] == password):
                isValid = True
                break

        return isValid


def addAdmin(username=None, password=None):
    with open("admins.csv", "a", newline='') as adminFile:
        adminWrite = csv.DictWriter(adminFile, ['Username', 'Password'])
        adminWrite.writerow({'Username': username, 'Password': password})


def isWorker(username=None, password=None):
    with open("workers.csv", "r") as workerFile:
        workerRead = csv.DictReader(workerFile)
        isValid = False

        for line in workerRead:
            if (line['Username'] == username) and (line['Password'] == password):
                isValid = True
                break

        return isValid


def addWorker(username=None, password=None):
    with open("workers.csv", "a", newline='') as workerFile:
        workerWrite = csv.DictWriter(workerFile, ['Username', 'Password'])
        workerWrite.writerow({'Username': username, 'Password': password})


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
        print('Access granted.')
        # HERE is where the fun begins. This is where we will add all admin functions like addAdmin and addWorker

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
