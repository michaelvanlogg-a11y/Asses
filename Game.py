import random

# yes/no function
def yes_no(question):
    while True:
        response = input(question).lower()
        if response in ["yes", "y"]:
            return "yes"
        elif response in ["no", "n"]:
            return "no"
        else:
            print("Please enter yes or no.")

# integer check function
def int_check():
    error = "Please enter an integer greater than or equal to 5."

    while True:
        try:
            response = int(input("How many questions would you like? "))
            if response < 5:
                print(error)
            else:
                return response
        except ValueError:
            print(error)

# Ask for user's name
name = input("Please enter your name: ").strip()
while name == "":
    name = input("Name cannot be empty. Please enter your name: ").strip()

print(f"Welcome to Mathistic, {name}!")

# Instructions
response = yes_no(f"{name}, do you want instructions? (yes/no) ")
if response == "yes":
    print("Try to answer the amount of questions you choose. You can keep going after that if you want!")

# Ask how many questions
game_goal = int_check()
print(f"You chose {game_goal} questions")

print("Let's start!")

score = 0
question_count = 0

# infinite loop
while True:
    question_count += 1

    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operation = random.choice(["+", "-"])

    # avoid negative answers
    if operation == "-" and num2 > num1:
        num1, num2 = num2, num1

    print(f"Question {question_count}: What is {num1} {operation} {num2}?")

    # input checking
    user_input = input("Your answer: ")
    while not user_input.lstrip("-").isdigit():
        print("Please enter a number.")
        user_input = input("Your answer: ")

    user_answer = int(user_input)

    # calculate correct answer
    answer = num1 + num2 if operation == "+" else num1 - num2

    # check answer
    if user_answer == answer:
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect! The correct answer was {answer}.")

    # once they reach their chosen amount, ask to continue
    if question_count >= game_goal:
        continue_game = yes_no("Do you want to keep going? (yes/no) ")
        if continue_game == "no":
            break
        else:
            game_goal += 1  # extend goal so it asks again later

print(f"{name}, your score is {score} out of {question_count}.")
print("Thanks for playing!")