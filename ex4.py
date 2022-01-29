from sys import argv
script, user_name = argv
import random
prompt = ">"
choixsortie = "Nothing"
while choixsortie != "Quit":
    print ("Hi", user_name, "my name is:", script)
    print("Do you want to play a game? yes/no")
    game = input(prompt)
    if game == "yes":
        print("Let's do this!")
        print("Pick a number between 1 and 10")
        number = int(input(prompt))
        if number == random.randint(1,10):
            print("Incredible! You win!")
        else:
            print("Game over human!")
    elif game == "no":
            print("Why are you wasting my time? get out!")
    else:
            print("Are you stupid? I said answer ye sor no!")

    choixsortie = input("Write 'Quit' to quit or click Enter to continue")
