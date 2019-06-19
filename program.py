import random
print('----------------------------')
print('  GUESS THAT NUMBER GAME')
print('----------------------------')
print('')

the_number = random.randint(0, 100)
name = input('Hey, what`s your name? ')
guess = -1

while guess != the_number:
    guess_text = input('Guess a number from 0 to 100: ')
    guess = int(guess_text)
    if guess < the_number:
        #print('Your guess of ' + guess + 'is TOO LOW')
        print('{1}, Your guess of {0} is TOO LOW'.format(guess, name))
    elif guess > the_number:
        #print('Your guess of ' + guess + 'is TOO HIGH')
        print('{1}, Your guess of {0} is TOO HIGH'.format(guess, name))
    else:
        print('Great {}!! You WON. The number was {}'.format(name, guess))

print('Done')

print('The right number was {}'.format(the_number))