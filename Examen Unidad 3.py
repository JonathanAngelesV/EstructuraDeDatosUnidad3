class Nodo:
    def __init__(self,datoInicial):
        self.dato = datoInicial
        self.siguiente = None
        self.anterior = None

    def obtenerDato(self):
        return self.dato

    def obtenerSiguiente(self):
        return self.siguiente

    def obtenerAnterior(self):
        return self.anterior

    def asignarDato(self,nuevodato):
        self.dato = nuevodato

    def asignarSiguiente(self,nuevosiguiente):
        self.siguiente = nuevosiguiente

    def asignarAnterior(self,nuevoanterior):
        self.anterior = nuevoanterior


class ListaDoblementeEnlazada:

    def __init__(self):
        self.cabeza = None
        self.final = None
        
    def estaVacia(self):
        return self.cabeza == None

    def agregar(self,item):
        #item = input("Introduzca un elemento: ")
        actual = self.cabeza
        previo = None
        detenerse = False
        while actual != None and not detenerse:
            if actual.obtenerDato() > item:
                detenerse = True
            else:
                previo = actual
                actual = actual.obtenerSiguiente()

        temp = Nodo(item)
        if previo == None:
            temp.asignarSiguiente(self.cabeza)
            temp.asignarAnterior(None)
            self.cabeza = temp
        else:
            temp.asignarSiguiente(actual)
            temp.asignarAnterior(previo)
            previo.asignarSiguiente(temp)
            self.final = temp
            
    
    def buscar(self,item):
        #item = input("Que elemento desea buscar?: ")
        actual = self.cabeza
        Nante = None
        NSig = None
        ejemplo = None
        contador = 0
        encontrado = False
        while actual != None and not encontrado:
            if actual.obtenerDato() == item:
                encontrado = True
                print("El elemento se encuentra en el nodo: " + str(contador))
                print("El nodo anterior es: ")
                
                #Manda a llamar los nodos a un lado del nodo deseado
                Nante = actual.obtenerAnterior()
                NSig = actual.obtenerSiguiente()
                #Regresa Nodo Anterior
                if Nante != None:
                    print(Nante.obtenerDato())
                else:
                    print("El nodo anterior es vacio")
                #Regresa Nodo Siguiente
                print("El nodo siguiente es: ")
                if NSig != None:
                    print(NSig.obtenerDato())
                else:
                    print("El nodo siguiente es vacio")
            else:
                actual = actual.obtenerSiguiente()
                contador += 1
        if encontrado == False:
            print("No existe")

    def leerRaiz(self):
        raiz = self.cabeza
        return raiz.obtenerDato()
    
    def leerFinal(self):
        final = self.final
        #Imprime el lado izquierdo
        Izquierda = final.obtenerAnterior()
        if Izquierda == None:
            print("Esta vacio el lado izquierdo")
        else:
            print("Lado Izquierdo")
            print(Izquierda.obtenerDato())
        #Imprime el lado derecho
        Derecha = final.obtenerSiguiente()
        if Derecha == None:
            print("Esta vacio el lado derecho")
        else:
            print("Lado Derecho")
            print(Derecha.obtenerDato())
    
    def printlista(self):
        print("Leer Lista de izquierda a derecha: 1")
        print("Leer Lista de derecha a izquierda: 2")
        decision = 0
        decision = input("Que desea realizar?: ")
        #Imprime la lista izquierda a derecha
        if decision == "1":
            actual = self.cabeza
            elemento = 0
            if(actual != None):
                while actual != None:
                    elemento = actual.obtenerDato()
                    actual = actual.obtenerSiguiente()
                    print(elemento)
            else:
                print("No existen nodos!")
        #Imprime la lista derecha a izquierda
        elif decision == "2":
            actual = self.final
            elemento = 0
            if(actual != None):
                while actual != None:
                    elemento = actual.obtenerDato()
                    actual = actual.obtenerAnterior()
                    print(elemento)
            else:
                print("No existen nodos!")
        

    def remover(self,item):
        #item = input("Que nodo desea eliminar?: ")
        actual = self.cabeza
        previo = None
        encontrado = False
        while not encontrado:
            if actual.obtenerDato() == item:
                encontrado = True
            else:
                previo = actual
                actual = actual.obtenerSiguiente()

        if previo == None:
            self.cabeza = actual.obtenerSiguiente()
        else:
            previo.asignarSiguiente(actual.obtenerSiguiente())
            
lista = ListaDoblementeEnlazada()
#Conjunto de Datos 1-9
lista.agregar(1)
lista.agregar(2)
lista.agregar(3)
lista.agregar(4)
lista.agregar(5)
lista.agregar(6)
lista.agregar(7)
lista.agregar(8)
lista.agregar(9)
#Imprime la Lista Doblemente Enlazada
lista.printlista()
#Agrega 10,11,13
lista.agregar(10)
lista.agregar(11)
lista.agregar(13)
#Elimina 8 y 1
lista.remover(8)
lista.remover(1)
#Leer la raiz
lista.leerRaiz()
#Leer el final
lista.leerFinal()
#Busca los numeros 0,7,8 y 1
lista.buscar(0)
lista.buscar(7)
lista.buscar(8)
lista.buscar(1)
