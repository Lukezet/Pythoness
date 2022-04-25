def run():
    flist=[7, "YAnEZ", True,23.3]
    fdicc={"First Name":"Lucas", "Surname":"Yanez"}
    
    super_list=[
        {"First Name":"Lucas", "Surname":"Yanez"},
        {"First Name":"Angelo", "Surname":"Moriarti"},
        {"First Name":"Vanessa", "Surname":"Suanss"}
    ]
    
    super_dictionary={
        "naturalnum":[1,2,3,4,5],
        "integernum":[-2,-1,0,1,2],
        "letters":["a","b","c","d","e"]
    }
    
    for key, value in super_dictionary.items():
        print(key,"->",value)
    
    print("-"*50)
    
    for diccionario in super_list:
        for key, value in diccionario.items():
            """
            para deshabilitar el salto de línea
            entre los pares de valores,
            se especifica un string de espacio vacío
            a traves del argumento 'end'
            """
            print(value, end=" ")
        """
        el argumento 'sep' indica un separador
        entre los elementos a imprimir, en este
        caso solo se imprime el salto de línea
        para separar los elementos
        de super_list
        """

        print("",sep="\n")


if __name__=="__main__":
    run()
