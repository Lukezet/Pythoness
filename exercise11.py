#dict_comprehension={i : (i**3) for i in range(1,101) if i%3!=0}
#print(dict_comprehension)
"""
def run():

    dicc={i : round(i**0.5,2) for i in range(1,11)}
    print(dicc)
if __name__=="__main__":
    run()

listita=[1,2,3,4,5]
listap=[i**2 for i in listita]
print(listap)"""
listita=[1,2,3,4,5]
listap=[]
for i in listita:
    listap.append(i**2)
print(listap)