import csv

name=input("What's your name?")
home=input("Where is your home?")

with open("/Users/gabi/Desktop/phyton/students_home.csv", "a") as file:
    #writer = csv.writer(file)
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})