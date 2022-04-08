# def reverse(head):
#     prev=None
#     cur=head
#     nxt=head.next
#     while cur in None:
#         nxt=cur.next
#         cur.next=prev
#         prev=cur
#         cur=nxt
#     head=prev
#     return head
# reverse()

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    
    def insertEnd(self,newNode):
        if self.head is None:
            self.head=newNode
        else:
            lastNode=self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode=lastNode.next
            lastNode.next=newNode