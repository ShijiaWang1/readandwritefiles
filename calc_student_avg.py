import csv
from fileinput import close

score = open("Student_Scores.csv", "r",encoding="utf-8")

score_file = csv.reader(score)

scorefile = csv.writer(open("student_avg.csv", "w",encoding="utf-8", newline=""))

for row in score_file:
    avg = round((int(row[1])+int(row[2])+int(row[3]))/3,2)
    scorefile.writerow(("student name: ",row[0]," average grade: ",avg))

score.close