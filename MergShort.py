from linkedlist import *
		
def OrdenaListas(ListaIzquierda,ListaDerecha): #Dada 2 listas ORDENADAS genera una lista nueva ordenada
		currentnode2 = ListaDerecha.head
		while ListaIzquierda.head!=None:
				currentnode1 = ListaIzquierda.head #Apunta al primer elemento de la lista
				currentnode2Anterior = None

				while currentnode2!=None and currentnode1.value >= currentnode2.value:
						currentnode2Anterior = currentnode2
						currentnode2 = currentnode2.nextNode

				ListaIzquierda.head = ListaIzquierda.head.nextNode
				currentnode1.nextNode = currentnode2

				if currentnode2Anterior == None:
						ListaDerecha.head = currentnode1
				else:
						currentnode2Anterior.nextNode = currentnode1
				currentnode2 = currentnode1

		return(ListaDerecha)

def DivideEn2Listas(ListaDiv):#Dado 1 la divide a la mitad y retorna 2 listas
		LongitudLista = int(lengthLista(ListaDiv)/2)
		currentnode = ListaDiv.head
		for i in range(LongitudLista-1):
				currentnode = currentnode.nextNode
		ListaNew = Lista()
		ListaNew.head = currentnode.nextNode
		currentnode.nextNode = None
		return(ListaDiv,ListaNew)

def MergShort(Lista):
		if Lista.head.nextNode == None: #Si la lista solo tiene un unico nodo
				return(Lista)
		else:
				(ListaUno,ListaDos) = DivideEn2Listas(Lista)
				ListaUno = MergShort(ListaUno)
				ListaDos = MergShort(ListaDos)
				ListaOrdenada = OrdenaListas(ListaUno,ListaDos)
				return(ListaOrdenada)



