"""
Author: Jose Amarante
Purpose: Chatbot
Libraries user: Chatterbot and Chatterbot_corpus
"""

# imports
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from flask import Flask, render_template, request


# Flask display
app = Flask(__name__)

'''
BOT TRAINING START
'''
# Create instance of the class ChatBot
# You can provide read_only=True if you want to disable the bot’s ability to learn after the training
# logic_adapters is the list of adapters used to train the bot.
myBot = ChatBot(name='DEO', read_only=True, logic_adapters=[
                'chatterbot.logic.MathematicalEvaluation','chatterbot.logic.BestMatch'])

# We supply the bot with text to learn from
smallTalk = ['hi there!',
             'hi!',
             'how do you do?',
             'how are you?',
             'i\'m cool.',
             'fine, you?',
             'always cool.',
             'i\'m ok',
             'glad to hear that.',
             'i\'m fine',
             'glad to hear that.',
             'i feel awesome',
             'excellent, glad to hear that.',
             'not so good',
             'sorry to hear that.',
             'what\'s your name?',
             'My name is Robot. ask me a math question, please.',
             'Are you a youtuber?',
             'Yes I am MR Beast',
             'Do you like Deo',
             'Deo is the best!!!!',
             'Hello Deo',
             'How are you?']

mathTalk1 = ['pythagorean theorem',
             'a squared plus b squared equals c squared.']
mathTalk2 = ['law of cosines',
             'c**2 = a**2 + b**2 - 2 * a * b * cos(gamma)']

# We train the both by creating an instance of ListTrainer and supplying it with the text
trainer = ListTrainer(myBot)
for x in (smallTalk, mathTalk1, mathTalk2):
    trainer.train(x)

# we can train the bot using corpus of data
corpusTrainer = ChatterBotCorpusTrainer(myBot)
corpusTrainer.train('chatterbot.corpus.english')

"""
BOT TRAINING DONE
"""