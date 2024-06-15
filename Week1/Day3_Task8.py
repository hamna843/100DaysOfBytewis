class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self) :
        self.head=None
    def Reversal(self):
        prev=None
        current=self.head
        while (current is not None):
            next=current.next
            current.next=prev
            prev=current
            current=next
        self.head= prev
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 
    def printList(self): 
        temp = self.head 
        while(temp): 
            print (temp.data,end=" ") 
            temp = temp.next
List1 = LinkedList() 
List1.push(1) 
List1.push(2) 
List1.push(3) 
List1.push(4) 
List1.push(5) 

print ("foward list") 
List1.printList() 
List1.Reversal() 
print ("\n Reversed Linked List") 
List1.printList() 
