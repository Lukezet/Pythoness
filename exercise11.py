#dict_comprehension={i : (i**3) for i in range(1,101) if i%3!=0}
#print(dict_comprehension)
def run():

    dicc={i : (i**3) for i in range(1,11)}
    print(dicc)
if __name__=="__main__":
    run()