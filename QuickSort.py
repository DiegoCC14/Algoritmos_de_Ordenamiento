from linkedlist import *

def ordenaPunteroPrimerElemento(Lista):#Toma el primer y pone si es menor al principio y mayor lo deja, retorna nodo tomado
		nodoComparador = Lista.head #El nodo que sera comparado
		currentnode = Lista.head.nextNode #El nodo que se compara comienza en el segundo nodo.
		currentnodeAnterior = Lista.head #Apuntamos al segundo elemento
		NodoPrevioAnodoComaparador = Lista.head

		while currentnode!=None:
				if currentnode.value < nodoComparador.value:
						nodoMenor = currentnode
						currentnode = currentnode.nextNode
						currentnodeAnterior.nextNode = currentnode
						nodoMenor.nextNode = Lista.head
						Lista.head = nodoMenor
						if NodoPrevioAnodoComaparador == None:
								NodoPrevioAnodoComaparador = L.head

				else:
						currentnodeAnterior = currentnode
						currentnode = currentnode.nextNode
		return(nodoComparador,NodoPrevioAnodoComaparador)


def QuickSort(Lista):
		if Lista.head.nextNode == None:
				return (Lista.head) #Retornamos el ultimo elemento de la lista
		else:
				nodoDivididor = ordenaPunteroPrimerElemento(Lista)
				ListaDerecha = Lista()
				ListaDerecha.head = nodoDivididor.nextNode
				nodoDivididor.nextNode = None   



L = Lista()
add(L,8)
add(L,9)
add(L,2)
add(L,1)
add(L,10)
add(L,8)

print(ordenaPunteroPrimerElemento(L).value)
VerLista(L)