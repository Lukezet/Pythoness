
def read():
    numbers=[]
    with open("./Files/numbers.txt", "r" , encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)

def write():
    route="./Files/"
    nfile=input("ingrese el nombre del archivo")
    froute=route+nfile+".txt"
    names=["Soronging","Lucas","Agustin","Facundo","Rocío"]
    with open(froute, "w" ) as f:
        for name in names:
            f.write(name)
            f.write("\n")
    

def run():
    write()

if __name__=="__main__":
    run()