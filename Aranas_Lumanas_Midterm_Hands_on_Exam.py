print ("Welcome to Grade school math problem generator")

playing = input("Do you want to test your knowledge in math? ")

if playing != "yes" "Yes":
    print("Okay lets play! \n\nNOTE: The answers should be integers only\n")

import random

def check_answer(user_answer, correct_answer):
    return user_answer == correct_answer

def main():
    total_questions = 4
    correct_answers = 0

    # Addition
    addition_1 = random.randint(1, 99)
    addition_2 = random.randint(1, 99)
    print("What is ", addition_1, "+", addition_2, "?")
    addition_answer_input = int(input("="))
    addition_answer_eval = addition_1 + addition_2
    addition_result = addition_answer_eval
    print(addition_result)

    is_correct = check_answer(addition_answer_input, addition_result)

    if is_correct:
        print(f"{addition_1} + {addition_2} = {addition_answer_input}")
        print("Your answer is correct!\n")
        correct_answers += 1
    else:
        print(f"{addition_1} + {addition_2} = {addition_result}")
        print("Your answer is incorrect!\n")

    # Subtraction
    subtraction_1 = random.randint(1, 99)
    subtraction_2 = random.randint(1, 99)
    print("What is ", subtraction_1, "-", subtraction_2, "?")
    subtraction_answer = int(input("="))
    subtraction_answer_eval = subtraction_1 - subtraction_2
    subtraction_result = subtraction_answer_eval
    print(subtraction_result)

    is_correct = check_answer(subtraction_answer, subtraction_result)

    if is_correct:
        print(f"{subtraction_1} - {subtraction_2} = {subtraction_answer}")
        print("Your answer is correct!\n")
        correct_answers += 1
    else:
        print(f"{subtraction_1} - {subtraction_2} = {subtraction_result}")
        print("Your answer is incorrect!\n")

    # Multiplication
    multiplication_1 = random.randint(1, 99)
    multiplication_2 = random.randint(1, 99)
    print("What is ", multiplication_1, "x", multiplication_2, "?")
    multiplication_answer = int(input("="))
    multiplication_answer_eval = multiplication_1 * multiplication_2
    multiplication_result = multiplication_answer_eval
    print(multiplication_result)

    is_correct = check_answer(multiplication_answer, multiplication_result)

    if is_correct:
        print(f"{multiplication_1} x {multiplication_2} = {multiplication_answer}")
        print("Your answer is correct!\n")
        correct_answers += 1
    else:
        print(f"{multiplication_1} x {multiplication_2} = {multiplication_result}")
        print("Your answer is incorrect!\n")

    # Division
    division_1 = random.randint(1, 99)
    division_2 = random.randint(1, 99)
    print("What is ", division_1, "/", division_2, "?")
    division_answer = int(input("="))
    division_answer_eval = division_1 // division_2
    division_result = division_answer_eval
    print(division_result)

    is_correct = check_answer(division_answer, division_result)

    if is_correct:
        print(f"{division_1} / {division_2} = {division_answer}")
        print("Your answer is correct!\n")
        correct_answers += 1
    else:
        print(f"{division_1} / {division_2} = {division_result}")
        print("Your answer is incorrect!\n")

    print(f"You answered {correct_answers} out of {total_questions} questions correctly.")

main()
