from chatterbot import ChatBot
import time 
from chatterbot.trainers import ListTrainer

from chatterbot.trainers import ChatterBotCorpusTrainer
import re

time.clock = time.time

# CORPUS_FILE = "./corpus.txt"

train_data = []
chatbot = ChatBot(
    "LING 450 ChatBot",
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'maximum_similarity_threshold': 0.60
        }
    ]
)

with open('./cleaned_corpus3.csv','r', encoding='utf-8') as f_in:

    for line in f_in: 
        train_data.append(line)

trainer = ListTrainer(chatbot)

# run this to retrain
# trainer.train(train_data)


exit_conditions = (":e", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    # addresses the one letter response from learning
    elif len(str(chatbot.get_response(query))) == 1:
        print(f" Oops I'm still learning!")
    elif query.endswith("?"):
        print(f" Hmm... {chatbot.get_response(query)}")
    else:
        print(f" {chatbot.get_response(query)}")