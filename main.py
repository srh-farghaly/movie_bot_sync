from chatterbot import ChatBot
from chatterbot.conversation import Statement
from chatterbot.trainers import ChatterBotCorpusTrainer
chatbot = ChatBot('MovieBOT')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english.movie")
print('    Hi, i am your Chatbot    ')


while True:
    query = input(">>> ")
    print(chatbot.get_response(Statement(text=query, search_text=query)))
