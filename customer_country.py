import csv
from sqlite3 import Row

customers = open("customers.csv", "r",encoding="utf-8")

customers_file = csv.reader(customers, delimiter=",")

countryfile = csv.writer(open("customer_country.csv", "w",encoding="utf-8", newline=""), delimiter=",")



for record in customers_file:
    countryfile.writerow((record[1], record[2], record[4]))

customers.close