# Import the random module for generating random numbers and operators
import random




# Function to generate a random integer within a given range
def function_O(MINIMUM, MAXIMUM):
    """
    Random integer.
    """
    return random.randint(MINIMUM, MAXIMUM)


# Function to generate a random arithmetic operator (+, -, *)
def function_M():
    """
    Generates a random arithmetic operator (+, -, *).
    """
    return random.choice(['+', '-', '*'])


# Function to perform a math operation based on the provided numbers and operator
def function_G(n1, n2, op):
    number1 = n1
    number2 = n2
    operator = op


    if op == '+':
        result = n1 + n2
    elif op == '-':
        result = n1 - n2
    else:
        result = n1 * n2
    return result


# Function for the math quiz game
def math_quiz():
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    # Loop through the number of questions specified
    for _ in range(total_questions):
        # Generate random numbers and operator for the current question
        n1 = function_O(1, 10)
        n2 = function_O(1, 10)
        o = function_M()

        # Calculate the correct answer for the current question
        CORRECT_ANSWER = function_G(n1, n2, o)

        # Display the question to the user
        print(f"\nQuestion: {n1} {o} {n2}")

        try:
            # Get the user's answer as input
            user_answer = input("Your answer: ")
            user_answer = int(user_answer)
        except ValueError:
            print("Invalid input, please enter a valid integer")

        # Check if the user's answer is correct
        if user_answer == CORRECT_ANSWER:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {CORRECT_ANSWER}.")

    # Display the final score
    print(f"\nGame over! Your score is: {score}/{total_questions}")


# Execute the math quiz game if the script is executed directly
if __name__ == "__main__":
    math_quiz()
