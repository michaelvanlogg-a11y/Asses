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

# Ask for user's name first
name = input("Please enter your name: ").strip()
while name == "":
    name = input("Name cannot be empty. Please enter your name: ").strip()

print(f"Welcome to Mathistic, {name}!")

# main program
response = yes_no(f"{name}, do you want instructions? (yes/no) ")
if response == "yes":
    print("Answer the 20 maths questions.")
else:
    print("Let's start!")

score = 0
# ask 20 questions
for i in range(20):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(["+", "-"])
    # avoid negative answers
    if operation == "-" and num2 > num1:
        num1, num2 = num2, num1
    
    print(f"Question {i+1}: What is {num1} {operation} {num2}?")
    
    # input checking
    user_input = input("Your answer: ")
    while not user_input.isdigit():
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

print(f"{name}, your score is {score} out of 20.")
print("Thanks for playing!")