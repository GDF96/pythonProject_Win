print("Try to guess my name!")
count = 1
name = "guilherme"
guess = input("What is my name? ")
while count < 3 and guess.lower() != name:    # .lower allows things like Guilherme to still match
    print("You are wrong!")
    guess = input("What is my name? ")
    count = count + 1

if guess.lower() != name:
    print("You are wrong!") # this message isn't printed in the third chance, so we print it now
    print("You ran out of chances.")
else:
    print("Yes! My name is", name + "!")

# Example found on: https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3/Boolean_Expressions