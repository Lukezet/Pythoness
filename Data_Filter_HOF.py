from data_list import DATA

def run():
    all_python_devs=[worker["name"] for worker in DATA if worker["language"]=="python"]
    all_platzi_worker=[worker["name"] for worker in DATA if worker["organization"]=="Platzi"]
    all_oldman_workers=[worker["name"] for worker in DATA if worker["age"]>=60]# Ejercicio de >60 con list_comprehensions 
    adults=list(filter(lambda worker : worker ["age"]>60,DATA))#
    adults=list(map(lambda worker: worker["name"],adults))# Ejercicio de >60 con High order functions

    old_people = list(map(lambda worker: {**worker, **{"old": worker["age"] > 60}}, DATA))# con esta HOF agregamos una nueva llave "old" que nos devuelve true si son mayores de 60
    #RETO clase nro 12
    python_devs=list(filter(lambda worker : worker["language"]=="javascript", DATA))
    python_devs=list(map(lambda worker : worker ["name"],python_devs))
    python_workplace=list(filter(lambda worker : worker["organization"]=="Platzi", DATA))
    python_workplace=list(map(lambda worker : worker ["name"],python_workplace))

    all_oldman_workers=[worker["name"] for worker in DATA if worker["age"]>=60]# Ejercicio de >60 con list_comprehensions
    old_person_list=[{**worker, **{"old": worker["age"] > 60}} for worker in DATA]




    for worker in all_oldman_workers:
        print(worker)
    for worker in old_person_list:
        print(worker)




if __name__=='__main__':
    run()