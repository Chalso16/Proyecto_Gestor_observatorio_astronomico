#Apartado 3
#Comprobacion codigo con fallo
class InventarioConFallo:
    def __init__(self, nombre:str, productos:list[str] = []) -> None:
        self.nombre = nombre
        self.productos = productos

    def anadir(self, producto: str) -> None:
        self.productos.append(producto)

#Comprobacion codigo SIN fallo
class Inventario:
    def __init__(self, nombre:str, productos: list[str] | None = None) -> None:
        self.nombre = nombre
        self.productos = [] if productos is None else productos.copy()

    def anadir(self, producto:str) -> None:
        self.productos.append(producto)

def main() -> None:
    inv1 = InventarioConFallo("Equipo A")
    inv2 = InventarioConFallo("Equipo B")
    inv1.anadir("Filtro solar")
    print("ANTES DEL ARREGLO")
    print("inv1.productos:", inv1.productos)
    print("inv2.productos:", inv2.productos)
    print("id(inv1.productos):", id(inv1.productos))
    print("id(inv2.productos):", id(inv2.productos))
    print("Misma lista:", inv1.productos is inv2.productos)
    assert inv1.productos is inv2.productos

    inv1 = Inventario("Equipo A")
    inv2 = Inventario("Equipo B")
    inv1.anadir("Filtro solar")
    print("DESPUÉS DEL ARREGLO")
    print("inv1.productos:", inv1.productos)
    print("inv2.productos:", inv2.productos)
    print("id(inv1.productos):", id(inv1.productos))
    print("id(inv2.productos):", id(inv2.productos))
    print("Misma lista:", inv1.productos is inv2.productos)
    assert inv1.productos == ["Filtro solar"]
    assert inv2.productos == []
    assert inv1.productos is not inv2.productos

if __name__ == "__main__":
    main()