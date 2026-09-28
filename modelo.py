#Apartado 1: Definir 4 clases principales con sus constructores
#Apartado 2: Añadir encapsulamiento (getter)
#Apartado 4: Sobrecarga __repr__ (representar obj como texto) y __eq__ (para decidir cuando dos obj son iguales)
#Apartado 6: Uso de tuplas o listas

from types import NotImplementedType

#1. clase1
class ObjetoCeleste:
    #1. constructor, 6. uso de tupla
    def __init__(self, identificador:str, tipo:str, coordenadas:tuple[float,float]) -> None:
        # .strip() quita los espacios
        if not identificador.strip() or not tipo.strip():
            raise ValueError("El identificador y el tipo NO pueden estar vacios")
        if len(coordenadas) != 2 :
            raise ValueError("Se necesitan exactamente 2 coordenadas, AR y declinacion ")
        ar, dec = (float(valor) for valor in coordenadas) #convertir los valores a float
        if ar <0 or ar > 360 or dec <-90 or dec>90 :
            raise ValueError("Coordenadas fuera de rango")

        self._identificador = identificador.strip()
        self._tipo = tipo.strip()
        self.__coordenadas = coordenadas

    # 2. getters (encapsulamiento)
    @property
    def identificador(self) -> str:
        return self._identificador

    @property
    def tipo(self) -> str:
        return self._tipo

    @property
    def coordenadas(self) -> tuple[float, float]:
        return self.__coordenadas

    #sobrecarga representacion como texto
    def __repr__(self) -> str:
        return f"ObjetoCeleste({self.identificador!r}, {self.tipo!r}, {self.coordenadas!r})"

    #sobrecarga equivalente
    def __eq__(self, otro:object) -> bool | NotImplementedType:
        #comprobacion si "otro" es una instancia de ObjetoCeleste
        if not isinstance(otro, ObjetoCeleste):
            return NotImplemented
        #retorno de igualdad por valor
        return (self.identificador, self.tipo, self.coordenadas) == (otro.identificador, otro.tipo, otro.coordenadas)

#1. clase2
class Telescopio :
    UNIDAD_HORAS = 'h'
    #1. constructor
    def __init__(self, nombre:str, horas_uso:int = 0) -> None:
        #usamos el setter
        self.nombre = nombre
        self.horas_uso = horas_uso

    #2. getter (encapsulamiento)
    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def horas_uso(self) -> int:
        return self.__horas_uso


    @nombre.setter
    def nombre(self, nuevo_valor:str)->None:
        if not isinstance(nuevo_valor, str):
            raise TypeError("El nombre tiene que ser un string")
        if not nuevo_valor.strip() :
            raise TypeError("El nombre del telescopio no puede estar vacio")
        self.__nombre = nuevo_valor.strip()

    @horas_uso.setter
    def horas_uso(self, nuevo_valor:int)->None:
        if type(nuevo_valor) is not int :
            raise TypeError("Las horas de uso tienen que ser un int")
        if nuevo_valor < 0 :
            raise TypeError("Las hotas de uso tienen que ser mayor a 0")
        #Aqui se instancia el atributo
        self.__horas_uso = nuevo_valor

#1. clase3
class SesionObservacion:
    #1. constructor
    def __init__(self, fecha:str, telescopio:Telescopio, objetivo:ObjetoCeleste) -> None:
        #instanciar atributos
        self.fecha = fecha
        self.telescopio = telescopio
        self.objetivo = objetivo

    def resumen(self) -> str:
        return (
            f"{self.fecha}: {self.objetivo.identificador} "
            f"con {self.telescopio.nombre}"
        )

#1. clase4
class CatalogoObservatorio:
    #1. constructor, 6. uso de lista
    def __init__(self, nombre:str, objetos_iniciales:list[ObjetoCeleste]) -> None:
        #instanciar atributos
        self.nombre = nombre
        self.objetos = objetos_iniciales
        #capacidad maxima de 24
        self.__capacidad_maxima = len(objetos_iniciales) * 3

    #2. getter (encapsulamiento)
    @property
    def capacidad_maxima(self) -> int:
        return self.__capacidad_maxima

    def anadir(self, objeto:ObjetoCeleste) -> None:
        if len(self.objetos) >= self.capacidad_maxima :
            raise TypeError("Capacidad maxima alcanzada")
        self.objetos.append(objeto)


#Creamos un ejemplo de catalogo
def crear_catalogo_ejemplo() -> CatalogoObservatorio :
    #datos, ar y dec en grados
    #Exactamente 8 elementos como pide el enunciado
    elementos = [
        ObjetoCeleste("Sol", "Estrella", (10.68, 41.27)),
        ObjetoCeleste("Luna", "Luna", (83.82, -5.39)),
        ObjetoCeleste("Sirio", "Estrella", (101.29, -16.72)),
        ObjetoCeleste("Júpiter", "Planeta", (0.0, 0.0)),
        ObjetoCeleste("Saturno", "Planeta", (1.0, 1.0)),
        ObjetoCeleste("Neptuno", "Planeta", (83.63, 22.01)),
        ObjetoCeleste("M45", "Cúmulo", (56.75, 24.12)),
        ObjetoCeleste("Pluton", "Planeta", (88.79, 7.41)),
    ]

    return CatalogoObservatorio("Test Catalogo", elementos)