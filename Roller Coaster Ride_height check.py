# intro
import time

print("Starting", end="", flush=True)  # no newline, flush immediately
time.sleep(1)
print(".", end="", flush=True)
time.sleep(1)
print(".", end="", flush=True)
time.sleep(1)
print(".", flush=True)
print(" ")

input("Press enter to continue...")

print("Welcome to the roller coaster ride!")
height =int(input("Please enter your height in cm: "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))

    if (age < 6 and height > 130) or (age < 10 and height > 160) or (age < 15 and height > 190):
        answer = input(
            "Hmm... that height doesn't quite match your age. Are you sure you're telling the truth? (yes/no): ").lower()

        if answer == "yes":
            print("Alright... we'll trust you this time!")
        else:
            age = int(input("Please enter your real age: "))
            print(f"Thanks for being honest. Updated age: {age}")

    if age < 12:
        bill = 5
        print("Child tickets are free!")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $8!")
    else:
        bill = 12
        print("Adult tickets are $20!")


else:
    print("Sorry, you have to grow taller before you can ride.")
