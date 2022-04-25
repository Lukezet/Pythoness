def run():
    lista=[1,2,3,4,5,6,7,8,9,10]
    resultado=[]
    pote=0
    for i in lista:
        pote=i**2
        resultado.append(pote)
    print(resultado)
if __name__=="__main__":
    run()