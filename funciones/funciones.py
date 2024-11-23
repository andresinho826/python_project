"""
funciones definidas por el usuario
"""

def greet():
    print("hola python")

greet()

# funcion con retorno

def return_greet():
    return "hola python con return"

greet = return_greet()
print(greet)


#funcion con parametro

def arg_greet(name):
    print(f"hola, {name}")

arg_greet("andres")
def arg_greets(greet, name):
    print(f"{greet}, {name}")

arg_greets("hello", "castillo")

#ingresarlos en orden
arg_greets(name="castillo", greet="ola___")


# con argumentos predefininido
def default_arg_greet(name="python"):
    print(f"hola, {name}")

default_arg_greet()
default_arg_greet("moreno")

