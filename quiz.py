# Basic Math Quiz Game

import random
import time

# Step 1: Define the math question function
def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*', '/'])
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    elif operator == '*':
        answer = num1 * num2
    else:
        # Ensure division gives integer answers and avoid division by 0
        num1 = num1 * num2
        answer = num1 // num2
        operator = '/'
    return f"{num1} {operator} {num2}", answer

# Step 2: Main Quiz Game Function
def math_quiz():
    score = 0
    print("\n--- Welcome to the Math Quiz Game! ---")
    print("You will be presented with math problems, and you need to provide the correct answers within the time limit.")
    try:
        rounds = int(input("How many rounds do you want to play? "))
    except ValueError:
        print("Invalid input, using 5 rounds.")
        rounds = 5
    
    for i in range(rounds):
        question, correct_answer = generate_question()
        print(f"\nQuestion {i + 1}: {question}")
        start = time.time()
        try:
            user_answer = int(input("Your answer (You have 15 seconds): "))
        except Exception as e:
            print("No answer given.")
            user_answer = None
        duration = time.time() - start
        if duration > 15:
            print(f"Time's up! The correct answer was: {correct_answer}")
        elif user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {correct_answer}")

    print("\n--- Game Over! ---")
    print(f"Your final score is: {score}/{rounds}")
    if score == rounds:
        print("Congratulations! You got all the questions correct.")
    elif score >= rounds // 2:
        print("Good job! You did well.")
    else:
        print("Keep practicing! You can do better next time.")

# Step 3: Run the Game
math_quiz()
