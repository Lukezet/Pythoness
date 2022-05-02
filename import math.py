"""def simple_list(numbers):
    duplicates = list()
    simples = list()

    for number in numbers:

        if number not in duplicates:
            #print(simples)
            #print(duplicates)
            duplicates.append(number)

    return duplicates
lista_a = [1, 2, 3, 2, 10, 20, 10, 2, 3, 4, 5, 2, 2]
print(simple_list(lista_a))"""
def simple_list(n):
    duplicates=[]
    
    for element in n:
        if element not in duplicates:
            duplicates.append(element)
    return duplicates
d1={"a":1,"b":2}
d2={"c":3,"d":4}
d3=d1|d2
print(d3)
lista = [1, 2, 3, 2, 10, 20, 10, 2, 3, 4, 5, 23, 2]
print(simple_list(lista))
