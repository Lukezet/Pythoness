import random
import os
def read_data():
    wordlist=[]
    with open("./hangman_ahorcado/data.txt", "r" , encoding="utf-8") as f:
        for line in f:
            wordlist.append(line.rstrip("\n"))
        choiceword=random.choice(wordlist)
        return choiceword
def run():
    
    os.system('clear')
    vidas=7
    start=input("************* Welcome to the Hangman GAME ************\n Please press enter for start the GAME!\n Press anything else for exit")
    if start=="":
        print("COMPLETE THE NEXT LINES AND \n__________________¡GUESS THE WORD!__________________")

#-------------Obtenemos palabra aleatoria-----------------    

        palabra_aleatoria=read_data()
 
#------------Quitamos Acento de la palabras-----------
        
        new_sentence = palabra_aleatoria.maketrans('áéíóú', 'aeiou')
        n_sentence = palabra_aleatoria.translate(new_sentence)
        palabra_aleatoria=n_sentence.upper()

#------------Pasamos lineas a pantalla----------------
        
        hidden_wordfunc="_"*len(palabra_aleatoria)
        hidden_word="_ "*len(palabra_aleatoria)
        l=list(hidden_wordfunc)
        w=list(palabra_aleatoria)
        print("Vidas:",vidas)
        print(hidden_word)
        print(palabra_aleatoria)

#-----------------ingresamos letra--------------------    
    while l!=w and vidas>0:    

        try:
            choice_letter=input("Ingresa una letra").upper()
            if len(choice_letter)>1 or choice_letter.isnumeric():
                raise Exception
            if choice_letter not in w:
                vidas-=1
            for i in range(0,len(w)):
                if w[i]==choice_letter:
                    l[i]=w[i]
            
            os.system('clear')
            print("Vidas:",vidas)
            print(" ".join(l).upper())
            print("\n")
        except Exception:
            print("Solo está permitido usar una letra!")
    if vidas==0:
        print("Te has quedado sin vidas, has perdido el juego")
    else:
        print(f"GANASTE!! Descubriendo la palabra {palabra_aleatoria}")
            


if __name__=="__main__":
    run()