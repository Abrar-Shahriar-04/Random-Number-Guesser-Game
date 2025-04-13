import random


def play_game():
  number = random.randint(1, 10)
  print("\nI'm thinking of a number between 1 and 10.")

  while True:
    try:
      guess = int(input("Your guess: "))
    except ValueError:
      print("Please enter a valid number.")
      continue

    if guess < number:
      print("Too low! Try a higher number.")
    elif guess > number:
      print("Too high! Try a lower number.")
    else:
      print("Correct! You guessed it!")
      break


def main():
  print("=== Welcome to the Random Number Guesser Game ===")

  while True:
    play_game()

    while True:
      print("\nDo you want to play again? (yes/no):")
      play_again = input()

      play_again = play_again.strip().lower()

      if play_again == 'yes' or play_again == 'y':
        break
      elif play_again == 'no' or play_again == 'n':
        print("Thanks for playing! Goodbye!")
        return
      else:
        print("Please only enter 'yes' or 'no'.")


main()
