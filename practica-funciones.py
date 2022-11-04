''' Práctica en Lenguaje Python
===================================
Se compone de funciones,constructores y encapsulamiento para llamar a las mismas
Autor: Alexis Bruce Barrios Echalar'''

#Variables y otras estructuras
frutasdicp = {'manzana ':15, 'durazno ':20 , 'pera ':10, 'banana ':5}
fruta=('manzana', 'durazno', 'pera', 'banana')
kilousuario=(5, 2, 8, 2)

def add (a, b):
    " Retorna la suma de a y b"
    print ('a={} , b={} , retornando a+b ={} '. format (a,b,a+b))
    return a+b

'''Añadir una función buyLotsOfFruit(orderList) que tome como parametro una lista de tuplas
(fruta, kilo) y retorne el costo de la lista'''
def BUYlotsoffruit():
    nombre= input("Ingrese el nombre de la fruta:")
    nrokilos=float(input("Ingrese cuántos kilos necesita: "))
    return (nombre, nrokilos)

'''Complete la función shopSmart(order, shops) que recibe un orderList y una lista de objetos FruitShop
y retorne el objeto FruitShop que posea el menor costo total'''

for i in range(0, len(kilousuario)):
    sum(item["manzana", "durazno", "pera", "banana"]*kilousuario(i) for item in frutasdicp)


if __name__ == '__main__':
    run()