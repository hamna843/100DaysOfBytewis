class Tree:
    def __init__(self,val=None):
      
        self.value = val

        if self.value:
            self.left = Tree()
            self.right = Tree()
        else:
          
            self.left = None
            self.right = None

    def isempty(self):
        return (self.value == None)
    

    def insert(self,data):    #insert fucntion
      

        if self.isempty():
            self.value = data
            
            self.left = Tree()
            self.right = Tree()
            print("{} is inserted successfully".format(self.value))
            

        elif data < self.value:
            self.left.insert(data)
            return
        
        elif data > self.value:
            self.right.insert(data)
            
        elif data == self.value:
            return
    def isleaf(self):
       
        if self.left.left == None and self.right.right == None:
            return True
        else:
            return False
    def Search(self, v):
        if self.isempty():
            
            print("{} is not found".format(v))
            return False
        if self.value == v:
            
            print("{} is found".format(v))
            return True
        if v < self.value:
            
            return self.left.Search(v)
        else:
           
            return self.right.Search(v)
    # def inorder(self):
    #     if self.isempty():
    #         # If the tree is empty, return an empty list
    #         return []
    #     else:
    #         # Return the inorder traversal of the tree (left subtree, root, right subtree)
    #         return self.left.inorder() + [self.value] + self.right.inorder()
    def isleaf(self):
        # Check if the node is a leaf node (no children)
        if self.left == None and self.right == None:
            return True
        else:
            return False
    def delete(self, v):
        # Delete a value from the Tree
        if self.isempty():
            return
        if v < self.value:
            self.left.delete(v)
            return
        if v > self.value:
            self.right.delete(v)
            return
        if v == self.value:
            if self.isleaf():
                self.value = None
                self.left = None
                self.right = None
                return
            elif self.left.isempty():
                self.value = self.right.value
                self.left = self.right.left
                self.right = self.right.right
                return
            else:
                self.value = self.left.maxval()
                self.left.delete(self.left.maxval())
                return
    def Traversal(self):
     
        if self.isempty():
            return ([])
        else:
        
            return ([self.value] + self.left.Traversal() + self.right.Traversal())
t = Tree(15)

t.insert(11)
t.insert(20)
t.Search(11)
t.delete(20)
print(t.Traversal())