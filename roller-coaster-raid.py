print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? \n"))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("your bill is $5.")
    elif age <= 18:
        bill =7
        print("your bill is $7.")
    else:
        bill = 12
        print("your bill is $12.")
    wanted_photo=input(str("you want photo, press y for YES or press n for NO \n"))
    if wanted_photo == "y":
        bill+=3
    print(f"your bill is ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
