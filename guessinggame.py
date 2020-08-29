import random

print("----------------------------")
print("       guessing game        ")
print("----------------------------")

print("Guess the number of M&M and you get lunch on the house")
print()

mm_count = random.randint(1, 100)
attempt_limit = 5
attempts = 0

while attempts < attempt_limit:
    guess_text = input("How many M&M are in the jar? ")
    guess = int(guess_text)
    attempts += 1

    if mm_count == guess:
        print(f"GZ! It was {guess}.")
    elif mm_count > guess:
        print("sorry! That's too LOW!")
    else:
        print("thats too HIGH!")

print(f"Bye! You are done in {attempts}!")
