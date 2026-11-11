from random import randint
number = randint(1,100)
print('----- WELCOME TO THE GUESSING GAME -----')
print('----- COMPUTER IS CHOOSING THE NUMBER -----')
print('----- COMPUTER CHOOSE THE NUMBER : ?? -----')
print("----- NOW IT'S YOUR TURN -----")
print('----- GOOD LUCK ----- ')
print('----- ENTER EXIT OR exit TO EXIT THE GAME-----')
guess = int(input('ENTER YOUR GUESS BETWEEN 1-100\n'))
while number > 0:
    guess = input("ENTER YOUR GUESS BETWEEN 1-100: ")
    if guess.lower() == "exit":
        print("Thanks for playing!")
        break
    guess = int(guess)
    if guess <= 0 or guess > 100:
        print('OOPS ENTER NUMBER BETWEEN 1-100')
        break
    if guess > number:
        print('LOWER GUESS AGAIN')
    elif guess < number:
        print('HIGHER GUESS AGAIN')
    else:
        print('YOU GOT IT COMPUTER CHOOSE : ',number)
        break
