import csv

students = []

with open("/Users/gabi/Desktop/phyton/names_house_v2.csv") as file:
    reader = csv.reader(file)
    for name, home in reader:
        students.append({"name": name, "home": home})