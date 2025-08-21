class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None
    
    def insertar(self, valor):
        nuevo_nodo = Nodo(valor)
        if(self.raiz == None):
            self.raiz = nuevo_nodo
        
        else:
            actual = self.raiz
            while actual != None:
                padre = actual
                if valor < actual.valor:
                    actual = actual.izquierdo
                else:
                    actual = actual.derecho
            
            if valor < padre.valor:
                padre.izquierdo = nuevo_nodo
            else:
                padre.derecho = nuevo_nodo
    def inorder(self, nodo):
        if(nodo == None):
            return
        else:
            self.inorder(nodo.izquierdo)
            print(nodo.valor)
            self.inorder(nodo.derecho)
    
    def preorder(self, nodo):
        if(nodo == None):
            return
        else:
           print(nodo.valor)
           self.preorder(nodo.izquierdo)
           self.preorder(nodo.derecho)

    def postorder(self, nodo):
        if(nodo == None):
            return
        else:
            self.postorder(nodo.izquierdo)
            self.postorder(nodo.derecho)
            print(nodo.valor)

    def busqueda(self, nodo, valor):
        if(nodo == None):
            return
        else:
           if(nodo.valor == valor):
                print(f"el valor {nodo.valor} fue encontrado")
                return
           self.busqueda(nodo.izquierdo, valor)
           self.busqueda(nodo.derecho, valor)

    

            

arbol = ArbolBinario()
arbol.insertar(6)
arbol.insertar(4)
arbol.insertar(1)
arbol.insertar(5)
arbol.insertar(8)
arbol.insertar(9)

#print("Inorder")
#arbol.inorder(arbol.raiz)

print("Preorden")
arbol.preorder(arbol.raiz)
arbol.busqueda(arbol.raiz, 8)

#print("Postorder")
#arbol.postorder(arbol.raiz)