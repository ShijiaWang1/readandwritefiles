import csv

customers = open("customers.csv", "r")

customers_file = csv.reader(customers, delimiter=",")

next(customers_file)

for record in customers_file:
    print("Last Name:", record[2])
