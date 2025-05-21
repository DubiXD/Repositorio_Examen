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

# Función principal
def principal():
    receta1 = RecetaVegetariana("Ensalada César", ["lechuga", "queso", "pan tostado", "salsa"], ["Lavar", "Mezclar", "Servir"])
    receta2 = RecetaNoVegetariana("Pollo al horno", ["pollo", "patatas", "ajo", "aceite"], ["Preparar", "Hornear", "Servir"])
    
    # Duplicación de código al imprimir
    print("== Mostrar recetas ==")
    Utilidades.imprimir_receta(receta1)
    Utilidades.imprimir_receta(receta2)

    # Código duplicado para mostrar ingredientes
    print("Ingredientes de Ensalada César:")
    for ing in receta1.i:
        print(f"* {ing}")
    
    print("Ingredientes de Pollo al horno:")
    for ing in receta2.i:
        print(f"* {ing}")


# Ejecutar el programa
if __name__ == "__main__":
    principal()
