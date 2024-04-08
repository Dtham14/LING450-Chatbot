from chatterbot import ChatBot
import time 
from chatterbot.trainers import ListTrainer

from chatterbot.trainers import ChatterBotCorpusTrainer


time.clock = time.time

CORPUS_FILE = "./corpus.txt"

chatbot = ChatBot(
    "LING 450 ChatBot",
)

trainer = ListTrainer(chatbot)

trainer.train(CORPUS_FILE)

exit_conditions = (":e", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    elif query.endswith("?"):
        print(f" Of Course! {chatbot.get_response(query)}")
    else:
        print(f" {chatbot.get_response(query)}")