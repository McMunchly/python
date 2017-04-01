# figure out which year somebody will turn 100

from datetime import date

name = input("Input your name: ")

age = int(input("Input your age: "))
currYear = date.today().year

birthday = input("Has your birthday happened this year? y/n: ")

birthInt = 0

if(birthday !="y"):
    birthInt += 1
print(currYear)
year = str((currYear - age - birthInt) + 100)

sentence = name + " will turn 100 in year " + year
print(sentence)
count = int(input("Now input how many times to repeat that: "))

while count > 0:
    print(sentence)
    count -= 1
