# User's guide to Warehouse Management System
This Warehouse Management software is used to track inventory, worker attendance, wages, vehicles and to generate tax invoices for a warehouse. When this program is run in Python, the first thing to be seen is the login screen. Here, you need to enter a correct username and password to login. 

## Logging in
The logins' default values are:

|Username|Password|
|--------|--------|
|Akash|warehouse.password@admin1|
|Bhumika|whm.pass_admin2|
|Anant|Anant_pass|

After logging in with one of these three credentials, the program can be used.

## Usage

|Input number|Description|Function called|
|------------|-----------|---------------|
|1|Add a new login account|`addAdmin()`|
|2|View worker status and today's statistics|`workerStatus()`|
|3|Update today's worker attendance|`workerUpdate()`|
|4|Calculate today\'s worker wages|`workerWages()`|
|5|Check and update price of stock|`updatePrices()`|
|6|Check current warehouse stock|`checkStock()`|
|7|Received shipment (add stock)|`addStock()`|
|8|Ship cargo and generate invoice (remove stock)|`removeStock()`|
|9|Check and add vehicles (if vehicles have completed journey and returned)|`addVehicles()`|

## Default warehouse values

### Worker names and hours: `workerlog.dat`

Stores a dictionary with default value `{'Om Shinde': 7, 'Shivansh Raj': 9, 'Vishwa Patel': 0, 'Atharva Deshmukh': 3, 'Alika Ramchandran': 0, 'Janvee Jerukar': 4, 'Ranghunadan Sreenidhi': 5}`

### Stock prices: `prices.dat`

Stores a dictionary with default value `{'GPU': 14499, 'RAM': 7599, 'HDD': 3599, 'Monitor': 13679, 'Printer': 8099, 'Mouse': 799, 'Keyboard': 549, 'Router': 6999, 'UPS': 12999}`

### Stock inventory: `stock.dat`

Stores a dictionary with default value `{'GPU': 118, 'RAM': 109, 'HDD': 0, 'Monitor': 57, 'Printer': 92, 'Mouse': 209, 'Keyboard': 255, 'Router': 0, 'UPS': 56}`

### Number of vehicles: `vehicles.dat`

Stores an integer with default value `4`

### Login credentials: `logins.csv`

Stores the following data in CSV form:

|Username|Password|
|--------|--------|
|Akash|warehouse.password@admin1|
|Bhumika|whm.pass_admin2|
|Anant|Anant_pass|