import random
import os
def presentation():
    os.system('clear')
    vidas=7
    start=input("************* Welcome to the Hangman GAME ************\n Please press enter for start the GAME!\n Press anything else for exit")
    if start=="":
        print("COMPLETE THE NEXT LINES AND \n__________________¡GUESS THE WORD!__________________")

def read_random():
    wordlist=[]
    with open("./hangman_ahorcado/data.txt", "r" , encoding="utf-8") as f:
        for line in f:
            wordlist.append(line.rstrip("\n"))
        ramword=random.choice(wordlist)
        new_sentence = ramword.maketrans('áéíóú', 'aeiou')
        n_sentence = ramword.translate(new_sentence)
        ramword=n_sentence.upper
        return ramword




def run():
    pal_aleatoria=read_random()
    r=presentation()


if __name__=="__main___":
    run()
