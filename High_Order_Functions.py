from functools import reduce
my_list=[1,2,3,4,5]
#Una Funcion de Orden Superior es una funcion que dentro lleva otra funcion, ej:
def saludo(func):
    func()
def hola():
    print("Hola GATOS!!")
def Adios():
    print("Chau perritas")
saludo(hola)
saludo(Adios)

#FUNCION FILTER
my_list=[1,2,3,4,5]
HOF_FILTER=list(filter(lambda x:x%2!=0,my_list))
print(HOF_FILTER)

#FUNCION MAP
HOF_MAP=list(map(lambda x:x**2,my_list))
print(HOF_MAP)

#FUNCION REDUCE
HOF_REDUCE=reduce(lambda a, b: a * b, my_list)
print(HOF_REDUCE)