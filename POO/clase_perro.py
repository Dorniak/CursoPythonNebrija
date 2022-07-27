from Ejercicios.POO.clase_base import Mamifero  # Importamos la clase definida en el otro archivo


class Perro(Mamifero):
    # De esta forma creamos una clase perro que hereda de mamífero con todos sus atributos y metodos
    num = 1  # Atributo de clase que usaremos para controlar el número de perror instanciados

    def __init__(self, nombre=None):
        super().__init__()  # Cuando heredamos de otra clase cuya instancia tiene un init debemos llamarlo en el
        # init de la clase hija
        self.patas = 4
        self.especie = 'can'
        if nombre is None:
            self.nombre = f'Perro {self.num}'
        else:
            self.nombre = nombre
        Perro.num += 1  # De esta forma modificamos la variable de clase

    def __add__(self, other):
        # De esta forma podemos definir el comportamiento de un objeto cuando se le aplica un operador en este caso +
        if isinstance(other, Perro):
            return Jauria(miembros=[self, other])
        else:
            raise TypeError('Not supported operation')

    # El método __repr__ es llamado cuando se imprimer un objeto o se introduce en un format
    def __repr__(self):
        return self.nombre


class Jauria:
    def __init__(self, miembros=None):
        if miembros is None:
            miembros = []
        self.miembros = set(miembros)

    def add_miembro(self, perro: Perro):
        self.miembros.add(perro)

    def __add__(self, other):
        if isinstance(other, Perro):
            return self.miembros.union({other})
        elif isinstance(other, Jauria):
            return self.miembros.union(other.miembros)
        else:
            raise TypeError('Operation not supported')

    def __repr__(self):
        return f'La jauria está compuesta por {self.miembros}'


print('Pruebas sdfhgaafdbg')  # Esto se imprimirá siempre que hagamos un import de este archivo
if __name__ == '__main__':  # Esto solo se ejecutará si hacemos un run de este archivo
    p = Perro()
    print('prueba')
