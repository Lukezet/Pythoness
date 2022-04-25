"""def run():

    pote[i**2 for i in range(1,101) if i % 3 != 0]  

    print(pote)

if __name__=="__main__":
    run()"""
def run():
    """pote=[]
    for i in range(1,101):
        if i%3!=0:
            pote.append(i**2)"""
    pote=[i for i in range(1,100000) if (i % 4 == 0 and i % 6 == 0 and i % 9 == 0)]        
    
    print(pote)
if __name__=="__main__":
    run()