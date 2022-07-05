import random

user_number = 0
guess_counter = 0

number_to_guess = random.randint(1, 9)

while user_number != number_to_guess:
    user_number = input('please guess the number between 1 to 9 (type exit to end game): ')
    if user_number == 'exit':
        break
    elif int(user_number) == number_to_guess:
        print('You guessed exactly right!')
        number_to_guess = random.randint(1, 9)
        guess_counter += 1
    elif int(user_number) < number_to_guess:
        print('You guessed too low')
    elif int(user_number) > number_to_guess:
        print('You guessed too high ')
print(f'you made {guess_counter} correct guesses')
