#MODIFICA INGREDIENTES DE UN PLATO PEDIDO 

def info_plato(): #Ingredientes personalizables del plato
    print ("\n\nEl plato " + plato["Nombre"] + " lleva:", end="")
    for i in range(0, len(plato["Ingred_personalizables"])):
        if 1 == plato["Ingred_iniciales"][i]:
            print (" " + plato["Ingred_personalizables"][i], end="")

    print ("\nPuedes añadirle:", end="")
    for i in range(0, len(plato["Ingred_personalizables"])):
        if 0 == plato["Ingred_iniciales"][i]:
            print (" " + plato["Ingred_personalizables"][i], end="")
    print("\n")

#Modificar plato
def elim_ingred():
    done = 0
    print("¿Qué ingrediente deseas eliminar?", end="")

    #Muestra los ingredientes que se pueden eliminar
    print("\nPuedes eliminar:",end="")
    for i in range(0, len(plato["Ingred_personalizables"])):
        if 1 == plato["Ingred_seleccionados"][i]:
            print (" " + plato["Ingred_personalizables"][i], end="")
    print("\n")
    eliminar = input()

    #Elimina el ingrediente
    for i in range(0, len(plato["Ingred_personalizables"])):
        if eliminar.lower() == plato["Ingred_personalizables"][i].lower():
            print("Hemos eliminado " + plato["Ingred_personalizables"][i])
            done = 1
            plato["Ingred_seleccionados"][i] = 0
    if done == 0:
        print("No se encuentra el ingrediente que has seleccionado.")

def agre_ingred():
    print("¿Qué ingrediente deseas agregar?")
    #Muestra elementos que se pueden agregar
    print("Puedes agregar: ",end="")
    for i in range(0, len(plato["Ingred_personalizables"])):
        if 0 == plato["Ingred_seleccionados"][i]:
            print (" " + plato["Ingred_personalizables"][i],end="")
    print("\n")
    agregar = input()

    #Agrega el ingrediente
    for i in range(0, len(plato["Ingred_personalizables"])):
        if agregar.lower() == plato["Ingred_personalizables"][i].lower():
            print("Hemos agregado " + plato["Ingred_personalizables"][i])
            plato["Ingred_seleccionados"][i] = 1

#Mostrar ingredientes finales
def plato_final():
    print("\nPEDIDO\n")
    print(plato["Nombre"], end="")
    Ingredientes_extra =""
    if compr_pers()==1:
        for i in range(0,len(plato["Ingred_personalizables"])):
            if plato["Ingred_iniciales"][i] < plato["Ingred_seleccionados"][i]:
                Ingredientes_extra=Ingredientes_extra +'\n+ '+ plato["Ingred_personalizables"][i]
            elif plato["Ingred_iniciales"][i] > plato["Ingred_seleccionados"][i]:
                Ingredientes_extra=Ingredientes_extra + "\n- "+ plato["Ingred_personalizables"][i]
        print(Ingredientes_extra)

#Comprobamos si el plato está personalizado
def compr_pers():
    if plato["Ingred_iniciales"] != plato["Ingred_seleccionados"]:
        return 1
    else:
        return 0

personalizado = 0

#Información del plato
plato = {
    "ID": "ID305",
    "Nombre": "Ensalada campera",
    "Descripción": "Ensalada campera realizada al estilo italiano",
    "Intolerancias" : ["Vegetariana", "Sin Gluten"],
    "Ingred_personalizables" : ['Queso','Tomate', 'Lechuga'],
    "Ingred_iniciales"  : [1,0,1],
    "Ingred_seleccionados" : [1,0,1]
}


#MAIN CODE

info_plato()
print("¿Deseas eliminar algún ingrediente?")
preg = input()
if preg.lower() == "si" or preg.lower() == "sí":  
    elim_ingred()
    plato_final()
print("\n¿Deseas agregar algún ingrediente?")
preg = input()
if preg.lower() == "si" or preg.lower() == "sí": agre_ingred()
plato_final()
print("\nGracias por usar nuestros servicios.\n")
