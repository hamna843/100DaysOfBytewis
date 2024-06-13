# class Node:
# 	ReverseList=[]
# 	FowardList=[]
# 	def __init__(self, data):
# 		self.data = data
# 		self.next = None
# def insert(self, data):
        
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return
 
#         current_node = self.head
#         while(current_node.next):
#             current_node = current_node.next
 
#         current_node.next = new_node
# def TraversalFoward(self):
# 	current_node = self.head
# 	while(current_node):
#         Node.FowardList=current_node.data
#         current_node = current_node.next
#     return Node.FowardList
# def TraversalBackword(head):
#     if head == None:
#          return
#     else:
#         TraversalBackword(head.next)
#         Node.ReverseList=head.data
#     return Node.ReverseList
	
# insert(1)
# insert(2)
# insert(3)
# insert(2)
# insert(1)
# TraversalFoward()
# TraversalBackword()
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def PalindromeCheck(self):
        if not self.head:
            return "The linked list is empty."
        Tortise = self.head
        hare = self.head
        stack = []
        while hare and hare.next:
            stack.append(Tortise.data)
            Tortise = Tortise.next
            hare = hare.next.next
        if hare:
            Tortise = Tortise.next
        while Tortise:
            if stack.pop() != Tortise.data:
                return "The linked list is not a palindrome."
            Tortise = Tortise.next
        return "The linked list is a palindrome."

# Example usage:
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(2)
linked_list.append(1)

print(linked_list.PalindromeCheck())  # Output: The linked list is a palindrome.

linked_list1 = LinkedList()
linked_list1.append(1)
linked_list1.append(2)
linked_list1.append(3)
linked_list1.append(4)
linked_list1.append(5)

print(linked_list1.PalindromeCheck())  # Output: The linked list is not a palindrome.