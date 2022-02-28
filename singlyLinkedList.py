from multiprocessing.dummy import current_process


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def isListEmpty(self):
        if self.head is None:
            return True
        else:
            return False


    def listLength(self):
        currentNode=self.head
        length=0
        while currentNode is not None:
            length+=1
            currentNode=currentNode.next
        return length

    def insertHead(self,newNode):
        # data=>Anusha,next=>None
        temporaryNode=self.head#Ammulu
        self.head=newNode#Anusha
        self.head.next=temporaryNode
        del temporaryNode
    def insertAt(self,newNode,position):
        if position<0 or position>self.listLength():
            print("Invalid position")
            return
        if position is 0:
            self.insertHead(newNode)
            return 
        currentNode=self.head
        currentPosition=0
        while True:
            if currentPosition==position:
                previousNode.next=newNode
                newNode.next=currentNode
                break
            previousNode=currentNode
            currentNode=currentNode.next
            currentPosition+=1



    
    def insertEnd(self,newNode):
        #head=>ammulu=>None
        if self.head is None:
            self.head=newNode
        else:
            lastNode=self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode=lastNode.next
            lastNode.next=newNode

    def deleteHead(self):
        if self.isListEmpty() is False:
            previousHead=self.head
            self.head=self.head.next
            previousHead.next=None
        else:
            print("Linked list is empty.delete failed")
    def deleteAt(self,position):
        if position<0 or position>=self.listLength():
            print("invalid position")
            return 
        # head=>john=>ben=>mathew=>None  // position=>1
        currentNode=self.head
        currentPosition=0
        while True:
            if currentPosition==position:
                previousNode.next=currentNode.next
                currentNode.next=None
    def deleteEnd(self):
        # lastNode=self.head
        if self.isListEmpty() is False:
            if self.head.next is None:
                self.deleteHead()
                return
            lastNode=self.head
        while lastNode.next is not None:
            previousNode=lastNode
            lastNode=lastNode.next
        previousNode.next=None

    def printList(self):
        if self.head is None:
            print("list is empty")
            return
        currentNode=self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode=currentNode.next
firstNode=Node('10')
linkedList=LinkedList()
linkedList.insertEnd(firstNode)

secondNode=Node("20")
# linkedList=LinkedList()
linkedList.insertEnd(secondNode)

thirdNode=Node("15")
linkedList.insertEnd(thirdNode)
linkedList.deleteEnd()

linkedList.printList()


    
