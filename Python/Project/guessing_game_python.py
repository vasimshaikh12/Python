import random

computer = random.randint(1, 100)

status = True
while status:
    user = int(input("Enter your guess: "))
    if user > computer:
        print("Guess Lower Number")
    elif user < computer:
        print("Guess Higher Number")
    else:
        print("Correct guess. Starting level 2")
        status = False

computer2 = random.randint(1, 50)
level2= False
attempt = 1

print("Level 2 started. Guess the number between 1 and 50. You have 7 attempts.")

while attempt <= 7 and not level2:
    user = int(input(f"Attempt {attempt} - Enter your guess: "))
    if user > computer2:
        print("Guess Lower Number")
    elif user < computer2:
        print("Guess Higher Number")
    else:
        print("Correct guess. Starting level 3")
        level2= True
    attempt += 1

if level2:
    computer3 = random.randint(1, 100)
    level3= False
    attempt3 = 1

    print("Level 3 started. Guess the number between 1 and 100. You have 7 attempts.")

    while attempt3 <= 7 and not level3:
        user = int(input(f"Attempt {attempt3} - Enter your guess: "))
        if user > computer3:
            print("Guess Lower Number")
        elif user < computer3:
            print("Guess Higher Number")
        else:
            print("You guessed all levels correctly. Well done!")
            level3 = True
        attempt3 += 1

    if not level3:
        print("You used all attempts in level 3. Game over.")
else:
    print("You used all attempts in level 2. Game over.")
