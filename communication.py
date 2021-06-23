# IMPORTS BOT FROM MAIN
from main import myBot
import logging
logger = logging.getLogger()
logger.setLevel(logging.CRITICAL)

"""
COMUNICATING WITH BOT START
"""

def main():
    # loops until user does not want to talk anymore
    print("\n\tPython Chat Lobby")
    print("---------------------------------")
    userInput = ''

    while userInput != 'exit' or userInput != 'Exit':
        # displays user input
        userInput = input("You: ")

        # displays bot input
        botInput = myBot.get_response(userInput)
        print(f"\n{myBot.name}: {botInput}\n")

    print("Thank you for talking to me.")


main()

"""
COMUNICATING WITH BOT END
"""
