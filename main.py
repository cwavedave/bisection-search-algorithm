# In this problem, you'll create a program that guesses a secret number!
#
# The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive).
# The computer makes guesses, and you give it input - is its guess too high or too low? Using bisection search,
# the computer will guess the user's secret number!

l = 0
h = 100
c = False

print("Please think of a number between 0 and 100!")
while c == False:
    m = (l+h) // 2

    print("Is your secret number", str(m),"?")
    test = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly")
    if test == "l":
        l = m
        m = (l + h) // 2
    elif test == "h":
        h = m
        m = (l + h) // 2
    elif test == "c":
        c = True
    else:
        print("Sorry, I did not understand your input.")

print("Game over. Your secret number was:", str(m))