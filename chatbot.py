from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer  # Potentially useful for larger datasets
import os

def init():
    global chatbot
    chatbot = ChatBot('Charlie', logic_adapters=['chatterbot.logic.BestMatch'])
    trainer = ListTrainer(chatbot)

    # Train with initial greetings
    trainer.train(['Hi!', 'Hey there, I am Charlie!'])
    trainer.train(['Ingolstadt', 'City in Bavaria, Germany.'])

    # --- New part: Training from a .txt file ---
    file_path = './app/trainset'  # Replace with the actual path to your .txt file
    files = os.listdir(file_path)
    for l in files:
        with open(file_path + '/' + l, 'r') as f:
            Answer = f.readline().strip()
            print(Answer)
            question = f.readline().strip()
            print(question)
            trainer.train([question, Answer])

    # Process the lines for training
    # This assumes your .txt file has one conversation pair per two lines,
    # or one statement per line to be used as a simple list.
    # You might need to adapt this based on the format of your .txt file.

def get_answer(question):
    global chatbot
    response = chatbot.get_response(question)
    return str(response)
