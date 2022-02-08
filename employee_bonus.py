import csv
from multiprocessing import BoundedSemaphore

Employee = open("EmployeePay.csv", "r",encoding="utf-8")

Employee_file = csv.reader(Employee)

next(Employee_file)

for row in Employee_file:
    salary_bonus= round(int(row[3])* float(row[4]),2)

    print("ID:", row[0])
    print("First Name:", row[1])
    print("Last Name:", row[2])
    print("Salary",row[3])
    print("Bonus rate",row[4])
    print("Bonus",salary_bonus)
 


