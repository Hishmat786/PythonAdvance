import random

def guess_the_number():
    # Define the range for the random number and the maximum number of attempts
    lower_bound = 1
    upper_bound = 10
    max_attempts = 5
    
    # Generate a random number between lower_bound and upper_bound
    number_to_guess = random.randint(lower_bound, upper_bound)
    
    print(f"Welcome to the Guess the Number game!")
    print(f"I'm thinking of a number between {lower_bound} and {upper_bound}.")
    print(f"You have {max_attempts} attempts to guess the number.")
    
    attempts = 0
    
    while attempts < max_attempts:
        # Get the player's guess
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        attempts += 1
        
        # Check the player's guess
        if guess < lower_bound or guess > upper_bound:
            print(f"Please guess a number between {lower_bound} and {upper_bound}.")
        elif guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
            break  # Exit the loop when the guess is correct
        
        # Inform the player of the remaining attempts
        if attempts < max_attempts:
            remaining_attempts = max_attempts - attempts
            print(f"You have {remaining_attempts} attempts left.")
        else:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")

# Call the function to start the game
guess_the_number()
