import datetime
year_now = datetime.datetime.now().year

def character_input():
    name = str(input("Please enter your name: "))
    age = int(input("Please enter your age: "))
    year = (year_now - age) + 100

    print(f"Hello {name} you are {age} years old and in the year {year} you'll be 100 years old")

character_input()