import pickle
import csv

fileO = open("workerlog.dat", "wb")
dicta = {'WorkerA': 0, 'WorkerB': 10, 'WorkerC': 3, 'WorkerD': 0, 'WorkerE': 1, 'WorkerF': 9}
pickle.dump(dicta, fileO)
fileO.close()

fileO = open("prices.dat", "wb")
dicta = {'ProductA': 99, 'ProductB': 129, 'ProductC': 1029, 'ProductD': 999}
pickle.dump(dicta, fileO)
fileO.close()

fileO = open("stock.dat", "wb")
dicta = {'ProductA': 50, 'ProductB': 41, 'ProductC': 10, 'ProductD': 0}
pickle.dump(dicta, fileO)
fileO.close()

fileO = open("vehicles.dat", "wb")
intA = 4
pickle.dump(intA, fileO)
fileO.close()

fileO = open("logins.csv", "w", newline='')
writer = csv.DictWriter(fileO, fieldnames=['Username', 'Password'])
writer.writeheader()
writer.writerow({'Username': 'paras_14', 'Password': 'Paras_ABC'})
writer.writerow({'Username': 'dhruv_15', 'Password': 'Dhruv1503'})
writer.writerow({'Username': 'hitesh_9', 'Password': 'Hitesh@1234'})
fileO.close()
