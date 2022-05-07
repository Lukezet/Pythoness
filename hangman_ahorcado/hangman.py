import random
import os
def read_data():
    data=[]
    with open("./hangman_ahorcado/data.txt", "r" , encoding="utf-8") as f:
        [data.append(line.rstrip("\n")) for line in f]        
        choiceword=random.choice(data)            
        return choiceword
def run():
    
    os.system('clear')
    vidas=7
    print("""
 __    __   ______   __    __   ______   __       __   ______   __    __ 
|  \  |  \ /      \ |  \  |  \ /      \ |  \     /  \ /      \ |  \  |  |
| $$  | $$|  $$$$$$\| $$\ | $$|  $$$$$$\| $$\   /  $$|  $$$$$$\| $$\ | $$
| $$__| $$| $$__| $$| $$$\| $$| $$ __\$$| $$$\ /  $$$| $$__| $$| $$$\| $$
| $$    $$| $$    $$| $$$$\ $$| $$|    \| $$$$\  $$$$| $$    $$| $$$$\ $$
| $$$$$$$$| $$$$$$$$| $$\$$ $$| $$ \$$$$| $$\$$ $$ $$| $$$$$$$$| $$\$$ $$
| $$  | $$| $$  | $$| $$ \$$$$| $$__| $$| $$ \$$$| $$| $$  | $$| $$ \$$$$
| $$  | $$| $$  | $$| $$  \$$$ \$$    $$| $$  \$ | $$| $$  | $$| $$  \$$$
 \$$   \$$ \$$   \$$ \$$   \$$  \$$$$$$  \$$      \$$ \$$   \$$ \$$   \$$

                                +----+          
                                |    |
                                O    |
                               /|\   |
                                |    |
                               / \   |
                                     |
                             ===========                                                                         
                           ===============                                                                      
                        ===================                                                                        
""")
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
        saves_words=[]
        print("Vidas:",vidas)
        print(hidden_word)

#-----------------ingresamos letra--------------------    
    while l!=w and vidas>0:
        if vidas==7:
            print("\n        +----+")
            print("        |    |")
            print("             |")
            print("             |")
            print("             |")
            print("             |")
            print("             |")
            print("     ===========")                                                                         
            print("   ===============")                                                                      
            print(" ===================")  
        elif vidas==6:
            print("\n        +----+")
            print("        |    |")
            print("        O    |")
            print("             |")
            print("             |")
            print("             |")
            print("             |")
            print("     ===========")                                                                         
            print("   ===============")                                                                      
            print(" ===================")
        elif vidas==5:
            print("\n        +----+")
            print("        |    |")
            print("        O    |")
            print("       /     |")
            print("             |")
            print("             |")
            print("             |")
            print("     ===========")                                                                         
            print("   ===============")                                                                      
            print(" ===================")
        elif vidas==4:
            print("\n        +----+")
            print("        |    |")
            print("        O    |")
            print("       /|    |")
            print("             |")
            print("             |")
            print("             |")
            print("     ===========")                                                                         
            print("   ===============")                                                                      
            print(" ===================")
        elif vidas==3:
            print("\n        +----+")
            print("        |    |")
            print("        O    |")
            print("       /|\    |")
            print("             |")
            print("             |")
            print("             |")
            print("     ===========")                                                                         
            print("   ===============")                                                                      
            print(" ===================")
        elif vidas==2:
            print("\n        +----+")
            print("        |    |")
            print("        O    |")
            print("       /|\   |")
            print("        |    |")
            print("             |")
            print("             |")
            print("     ===========")                                                                         
            print("   ===============")                                                                      
            print(" ===================")
        elif vidas==1:
            print("\n        +----+")
            print("        |    |")
            print("        O    |")
            print("       /|\   |")
            print("        |    |")
            print("       /     |")
            print("             |")
            print("     ===========")                                                                         
            print("   ===============")                                                                      
            print(" ===================")

        
        try:
            print("Palabras usadas:","-".join(saves_words))
            choice_letter=input("Ingresa una letra").upper()
            if len(choice_letter)>1 or choice_letter.isnumeric():
                raise Exception
            if choice_letter in saves_words:
                pass
            elif choice_letter not in w:
                vidas-=1
            else:
                pass
            saves_words.append(choice_letter)
            for i in range(0,len(w)):
                if w[i]==choice_letter:
                    l[i]=w[i]
            
            os.system('clear')
            print("Vidas ❤:",vidas)
            print(" ".join(l).upper())
            print("\n")
        except Exception:
            os.system('clear')
            print("Solo está permitido usar una letra!")
    if vidas==0:
        print("\n        +----+")
        print("        |    |")
        print("        O    |")
        print("       /|\   |")
        print("        |    |")
        print("       / \   |")
        print("             |")
        print("     ===========")                                                                         
        print("   ===============")                                                                      
        print(" ===================")
        print(""" ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  |
| |          ||  `/,|
| |          (|\`_.'
| |         .-`--'.
| |        /Y . . ||
| |       // |   |||
| |      //  | . |||
| |     ')   |   | (`
| |          ||'||
| |          || ||
| |          || ||
| |          || ||
| |         / | | |
==========|_`-' `-' |===|
|=|=======\ \       '=|=|
| |        \ \        | |
: :         \ \       : :  sk
. .          `'       . .""")
        print(f"Te has quedado sin vidas, has sido ahorcado.. la palabra era{palabra_aleatoria}")

    else:
        print("""
                                        ,.        ,.      ,.
                                        ||        ||      ||  ()
         ,--. ,-. ,.,-.  ,--.,.,-. ,-.  ||-.,.  ,.|| ,-.  ||-.,. ,-. ,.,-.  ,--.
        //`-'//-||||/|| //-||||/`'//-|| ||-'||  ||||//-|| ||-'||//-||||/|| ((`-'
        ||   || |||| ||||  ||||   || || ||  || /|||||| || ||  |||| |||| ||  ``.
        ||,-.||-//|| || ||-||||   ||-|| ||  ||//||||||-|| ||  ||||-//|| || ,-.))
         `--' `-' `' `'  `-,|`'    `-^-``'  `-' `'`' `-^-``'  `' `-' `' `' `--'
                          //           .--------.
                      ,-.//          .: : :  :___`.
                      `--'         .'!!:::::  ||_| `.
                              : . /%O!!::::::::||_|. |
                             [""]/%%O!!:::::::::  : . |
                             |  |%%OO!!::::::::::: : . |
                             |  |%%OO!!:::::::::::::  :|
                             |  |%%OO!!!::::::::::::: :|
                    :       .'--`.%%OO!!!:::::::::::: :|
                  : .:     /`.__.'\%%OO!!!::::::::::::/
                 :    .   /        \%OO!!!!::::::::::/
                ,-'``'-. ;          ;%%OO!!!!!!:::::'
                |`-..-'| |   ,--.   |`%%%OO!!!!!!:'
                | .   :| |_.','`.`._|  `%%%OO!%%'
                | . :  | |--'    `--|    `%%%%'
                |`-..-'| ||   | | | |     /__\`-.
                \::::::/ ||)|/|)|)|\|           /
        ---------`::::'--|._ ~**~ _.|----------( -----------------------
                   )(    |  `-..-'  |           \    ______
                   )(    |          |,--.       ____/ /  /\|| ,-._.-'
                ,-')('-. |          |\`;/   .-()___  :  |`.!,-'`'/`-._
               (  '  `  )`-._    _.-'|;,|    `-,    \_\__\`,-'>-.,-._
                `-....-'     ````    `--'      `-._       (`- `-._`-.   """)
        print(f"GANASTE!! Descubriendo la palabra {palabra_aleatoria}")
            


if __name__=="__main__":
    run()
                                                                       
                                                                         
                                                                         
  