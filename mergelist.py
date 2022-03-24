
from singlyLinkedList import Node,LinkedList
def mergeLists(firstList,secondList,mergedList):
    currentFirst=firstList.head
    currentSecond=secondList.head
    while True:
        if currentFirst is None:
            mergedList.insertEnd(currentSecond)
            break
        if currentSecond is None:
            mergedList.insertEnd(currentFirst)
            break
        if currentFirst.data<currentSecond.data:
            currentFirstNext=currentFirst.next
            currentFirst.next=None
            mergedList.insertEnd(currentFirst)
            currentFirst.insertEnd(currentFirst)
        else:
            currentSecondNext=currentSecond.next
            currentSecond.next=None
            mergedList.insertEnd(currentSecond)
            currentSecond=currentSecondNext

nodeOne=Node(1)
nodeTwo=Node(3)
nodeThree=Node(4)
firstList=LinkedList()
firstList.insertEnd(nodeOne)
firstList.insertEnd(nodeTwo)
firstList.insertEnd(nodeThree)

# secondlist
nodeFour=Node(2)
nodeFive=Node(7)
nodeSix=Node(9)
secondList=LinkedList()
secondList.insertEnd(nodeFour)
secondList.insertEnd(nodeFive)
secondList.insertEnd(nodeSix)

print("Printin first list")
firstList.printList()
print("printin second list")
secondList.printList()

mergedList=LinkedList()

mergeLists(firstList,secondList,mergedList)
del firstList

del secondList
print("printing merged List")
mergedList.printList()
