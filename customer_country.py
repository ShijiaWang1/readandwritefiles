import csv

customers = open("customers.csv", "r")

customers_file = csv.reader(customers, delimiter=",")

countryfile = csv.writer(open("customer_country.csv", "w"), delimiter=",")


for record in customers_file:
    countryfile.writerow((record[1], record[2], record[4]))

row_count = len(record)
print(row_count)
