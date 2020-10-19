from random import choice
# Importing choice so I can choose from a list of answers later

answers = ("It is certain.", "Yes.", "Most likely.", "Ask again later.", "Reply hazy, try again.",
           "Cannot predict now.", "My sources say no.", "Very doubtful.", "Outlook not so good.")
# List of possible answers

while True:
    input("What do you want to ask the Magic 8 Ball? ")
    # Letting them ask a question
    print("Please wait a moment...")
    # In progress message
    print(choice(answers))
    # Giving them a random answer
    resume = input("Do you want to ask another question? (Type 'Continue' or 'Quit') ")
    # Asking them if they want to continue
    if resume.strip().lower() == "quit":
        print("I hope to see you again!")
        break
    # If they type "quit", the loop ends, ending the program
    elif resume.strip().lower() == "continue":
        pass
    # If they type "continue", the loop will continue
    else:
        print("I'll just take that as a yes.")
    # If they type anything other than "quit" or "continue", the loop continues
