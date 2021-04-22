class Lista():
		head = None

class Node():
		value = None
		nextNode = None

def VerLista(Lista):
		currentnode = Lista.head
		while currentnode != None:
				print(currentnode.value,' ',end='')
				currentnode=currentnode.nextNode
		print('')

def lengthLista(Lista):
		currentnode = Lista.head
		contador = 0
		while currentnode != None:
				contador+=1
				currentnode = currentnode.nextNode
		return(contador)

def add (Lista,value1):
		NodeNew = Node()
		NodeNew.value = value1
		NodeNew.nextNode = Lista.head
		Lista.head = NodeNew