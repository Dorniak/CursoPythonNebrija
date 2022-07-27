# La clase mamífero sera la que usemos como clase base
class Mamifero:  # La clase se define de esta manera
    tipo = 'Mamifero'  # Atributo de clase, significa que todas las instancias de esta clase compartirán este atributo

    def __init__(self, patas=0,
                 especie=''):  # Las funciones que tienen este formato __xxx__
        # son dunder methods o métodos mágicos y estan definidos en el core de python. El método __init__ se llamará
        # automáticamente al crear una instancia de esta clase.
        self.patas = patas  # Atributo de instancia, son aquellos que pueden modificarse en cada instancia
        self.__especie = especie  # Atributo protegido, los atributos/funciones que empiezan por __
        # quedan protegidos y no pueden ser accedidos desde fuera
        self.__posicion = [0, 0]  # Para poder modificar un atributo protegido, se debe hacer desde dentro de la
        # propia clase, mediante un getter y un setter o una funcion que lo modifique

    def mover(self, x, y):  # Así se define un método. Los métodos de clase siempre tienen como primer argumento self
        # aunque no cuenta cuando vamos ha hacer una llamada al método
        try:
            x = float(x)
            y = float(y)
            if -10 <= x <= 10 and -10 <= y <= 1:
                self.__posicion[0] += x
                self.__posicion[1] += y
            else:
                raise ValueError('Out of range')
        except:  # Podemos recoger una cualquier excepción de esta forma, aunque nos saldra un warning
            print('No se ha podido mover el Mamifero')

    def get_position(self):
        return self.__posicion[:]

    # La forma típica de hacer un getter y setter es la siguiente
    def get_patas(self) -> int:
        return self.patas

    def set_patas(self, num_patas):
        self.patas = num_patas

    # Pero también podemos definirlo mediante un Property que se hace de la siguiente manera
    @property
    def especie(self):  # Tener en cuenta que el nombre debe ser igual al del atributo
        print('Getter especie')
        return self.__especie

    @especie.setter  # De esta forma se crea el setter
    def especie(self, value):  # Tener en cuenta que el nombre debe ser igual al del atributo
        print('Setter especie')
        if not isinstance(value, str):
            raise TypeError('Especie debe ser de tipo str')
        self.__especie = value
