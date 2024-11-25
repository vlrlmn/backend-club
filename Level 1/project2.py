import random

target = random.randint(0, 100)
counter = 0

while True:

    counter += 1

    try:
        num = int(input("Guess a number between 1 and 100: "))
    except ValueError:
        print("Enter valid integer: ")
        continue

    if (num == target):
        print(f"Correct! You guessed the number in {counter} attempts.")
        break
    elif (counter == 10):
        print("Number of attempts were 5! The number was: ", target)
        break
    elif (num > target):
        print("Too high! Try again.")

    elif (num < target):
        print("Too low! Try again.")
