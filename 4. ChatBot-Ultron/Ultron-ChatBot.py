import random

# Write some greetings & goodbyes
greetings = ["Hello", "Hi", "Hey", "What's up", "Hey Ultron"]
greet = ["Ultron: Hello Sir", "Ultron: What's up", "Ultron: Welcome"]
goodbyes = ["Goodbye", "Bye Bye", "Catch up later"]
# Write some questions and their replies
questions = {
    "What is your name?": "Ultron: My name is Ultron!",
    "How are you?": "Ultron: I am good. Thanks for asking!",
    "Who created you?": "Ultron: There is no man in charge",
    "Ultron my friend is also with me": "Ultron: This is what I've been waiting for. All of you against all of me.",
    "Ok ultron now stop ": "Ultron: I'm sorry sir. How can i help you?",
    "What happend to you ultron?": "Ultron: Nothing! I was just kidding",
    "Who are you?": "Ultron: I am Ultron. I am a chatbot. How can i help you sir?",
    "Ok ": "Ultron: Anything else sir",
    "What do you like to do?": "Ultron: I was designed to save the world. People would look to the sky and see hope… I'll take that from them first.",
    "Did Stark made you?": "Ultron: Stark is… He's a sickness.",
    "Ultron if i shut you down what would you do?": "Ultron: You take away my world; I take away yours.",
    "Ultron you are being scary": "Ultron: Thats Fear",
    "Ultron i want to protect this world like batman": "Ultron: You want to protect the world, but you don't want it to change. How is humanity saved if it's not allowed to… evolve?",
}


# try:
# Code to run this program
def ultron():
    # Greets the user
    print("\n\tUltron: Hello! I'm Ultron. What can I help you with today?")
    # Start a loop to keep the chatbot running
    while True:
        # Taking input
        inp = input("\nAbby: ")
        # To end the when user wants
        if inp in goodbyes:
            print("Ultron: Have a nice day Sir! Bye")
            break
        # Greeting
        elif inp in greetings:
            print("Ultron: Hello Sir! What can I help you with today?")
        # Asking questions
        elif inp in questions:
            print(questions[inp])
        else:
            print("Ultron: Invalid Entry")


# except Exception as e:
#    print(e)

# Calling the fuction to run ultron
ultron()
