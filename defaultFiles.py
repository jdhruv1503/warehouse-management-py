import pickle

fileO = open("workerlog.dat", "wb")
dicta = {'Om Shinde': 7, 'Shivansh Raj': 9, 'Vishwa Patel': 0, 'Atharva Deshmukh': 3, 'Alika Ramchandran': 0,
         'Janvee Jerukar': 4, 'Ranghunadan Sreenidhi': 5}
pickle.dump(dicta, fileO)
fileO.close()

fileO = open("prices.dat", "wb")
dicta = {'GPU': 14499, 'RAM': 7599, 'HDD': 3599, 'Monitor': 13679, 'Printer': 8099, 'Mouse': 799, 'Keyboard': 549,
         'Router': 6999, 'UPS': 12999}
pickle.dump(dicta, fileO)
fileO.close()

fileO = open("stock.dat", "wb")
dicta = {'GPU': 118, 'RAM': 109, 'HDD': 0, 'Monitor': 57, 'Printer': 92, 'Mouse': 209, 'Keyboard': 255, 'Router': 0,
         'UPS': 56}
pickle.dump(dicta, fileO)
fileO.close()

fileO = open("vehicles.dat", "wb")
intA = 4
pickle.dump(intA, fileO)
fileO.close()

fileO = open("logins.dat", "wb")
dicta = {'Akash': 'warehouse.password@admin1', 'Bhumika': 'whm.pass_admin2', 'Anant': 'Anant_pass', 'aa': 'aa'}
pickle.dump(dicta, fileO)
fileO.close()
