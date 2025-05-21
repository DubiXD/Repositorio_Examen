from abc import ABC, abstractmethod

# Clase abstracta para representar una receta
class Receta(ABC):
    def __init__(self, nombre, ingredientes, pasos):
        self.nombre = nombre  # nombre
        self.ingredientes = ingredientes  # ingredientes
        self.pasos = pasos  # pasos

    @abstractmethod
    def mostrar(self):
        print(f"Receta: {self.nombre}")
        print("Ingredientes:")
        for ing in self.ingredientes:
            print(f"- {ing}")
        print("Pasos:")
        for paso in self.pasos:
            print(f"{paso}")


# Clase para recetas vegetarianas
class RecetaVegetariana(Receta):
    def __init__(self, nombre, ingredientes, pasos):
        super().__init__(nombre, ingredientes, pasos)

# Clase para recetas no vegetarianas
class RecetaNoVegetariana(Receta):
    def __init__(self, nombre, ingredientes, pasos):
        super().__init__(nombre, ingredientes, pasos)

# Clase con utilidades del restaurante
class Utilidades(Receta):
    @staticmethod
    def imprimir_receta(receta):
        print("====================================")
        receta.mostrar()
        print("====================================")

    @staticmethod
    def mostrar_lista_ingredientes(lista):
        for l in lista:
            print(f"* {l}")

def crear_receta():
    nombre_receta = input("Que tipo de receta quieres crear?: ")
    ingredientes_receta = []
    print("Dime los ingredientes que vas a usar (Escribe fin para terminar): ")
    while True:
        ing = input("")
        if ing.lower() == "fin":
            break
        ingredientes_receta.append(ing)
    pasos_receta = []
    print("Introduce los pasos (Escribe fin para terminar): ")
    while True:
        paso = input("")
        if paso.lower() == "fin":
            break
        pasos_receta.append(paso)
    return nombre_receta, ingredientes_receta, pasos_receta

# Función principal
def principal():        #Hay una incidencia y es que no sale del bulce de la función de crear_receta, posiblemente sea un fallo de ahi
    
    nombre_receta, ingredientes_receta, pasos_receta = crear_receta()
    tipo_receta = input("Que tipo de receta quieres hacer? ")

    if tipo_receta == "vegetariana":
        print("== Crear receta (vegetariana) ==")
        apta_para_veganos = input("Dime si es apta para veganos: ")
        receta1 = RecetaVegetariana(nombre_receta, ingredientes_receta, pasos_receta, apta_para_veganos)
        Receta.mostrar(receta1)
    elif tipo_receta == "no vegetariana":
        print("== Crear receta (con carne) ==")
        tipo_carne = input("Indica el tipo de carne: ")
        receta2 = RecetaNoVegetariana(nombre_receta, ingredientes_receta, pasos_receta, tipo_carne)
        Receta.mostrar(receta2)
    else:
        print("El tipo de receta no existe o no es válido")
        
# Ejecutar el programa
if __name__ == "__main__":
    principal()
