from random import randint
number = randint(1,100)
attempts = 0
print('----- WELCOME TO THE GUESSING GAME -----')
print('----- COMPUTER IS CHOOSING THE NUMBER -----')
print('----- COMPUTER CHOOSE THE NUMBER : ?? -----')
print("----- NOW IT'S YOUR TURN -----")
print('----- GOOD LUCK ----- ')
print('-----ENTER EXIT TO EXIT THE GAME-----')
print('-----SOLVE THIS GAME IN 7ATTEMPTS-----')
while number > 0:
    guess = input("ENTER YOUR GUESS BETWEEN 1-100: \n")
    if guess.lower() == "exit":
        print("Thanks for playing!")
        break
    attempts+=1
    print('number of attempts : ',attempts)
    if attempts == 7:
        print('----YOU RAN OUT OF ATTEMPTS-----')
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
