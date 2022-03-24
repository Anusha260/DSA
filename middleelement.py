class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linked_List:
    def __init__(self):
        self.head=None
        self.root=None
    
    def print(self):
        temp=self.root
        while(temp):
            print(temp.data)
            temp=temp.next
    
    def push(self,data):
        new=Node(data)
        if(self.head==None):
            self.head=new
            self.root=new
        else:
            self.head.next=new
            self.head=new
    def middle(self):
        i1=i2=self.root
        if(i1 is not None):
            while(i1 is not None and i1.next is not None):
                i1=i1.next.next
                i2=i2.next
            print("Middle is: ",i2.data)
if __name__=="__main__":
    list=Linked_List()
    list.push(1)
    list.push(2)
    list.push(3)
    list.push(4)
    list.push(5)
    list.middle()