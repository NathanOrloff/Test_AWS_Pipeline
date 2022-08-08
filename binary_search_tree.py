from queue_array import Queue




class TreeNode:
    def __init__(self, key, data, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

class BinarySearchTree:

    def __init__(self): # Returns empty BST
        self.root = None

    def is_empty(self): # returns True if tree is empty, else False
        if self.root: # checks to see if there is a root
            return False
        return True





    def search(self, key): # returns True if key is in a node of the tree, else False
        if self.root: #checks is empty
            return self._search(key, self.root) #calls helper function
        else:
            return False



    def _search(self,key,currentNode):
        if key < currentNode.key: #if key is less than the current key
            if currentNode.left:
                return self._search(key, currentNode.left) #search on left sub-tree
            else:
                return False #if there is no leaf to search return false
        elif key > currentNode.key: #if key is greater than the current key
            if currentNode.right:
                return self._search(key, currentNode.right) #search on right sub-tree
            else:
                return False #if there is no leaf to search return false
        else:
            return True #keys are equal return true



    def insert(self, key, data=None): # inserts new node w/ key and data
        # If an item with the given key is already in the BST, 
        # the data in the tree will be replaced with the new data
        if self.root: #check if empty
            self._insert(key,data,self.root) #calls helper function
        else:
            self.root = TreeNode(key,data)
    
    def _insert(self, key, data, currentNode):
        if key < currentNode.key: #if key is less than current key 
            if currentNode.left:
               self._insert(key,data,currentNode.left) #call insert on left sub-tree
            else:
               currentNode.left = TreeNode(key,data) #if there is no leaf to call insert on, create TreeNode with data and add to the tree
        elif (key > currentNode.key): #if the key is greater than the current key
            if currentNode.right:
               self._insert(key,data,currentNode.right) #call insert on right sub-tree
            else:
               currentNode.right = TreeNode(key,data) #if there is no leaf to call insert on, create TreeNode with data and key and add to the tree
        else:
            currentNode.data = data #if key is equal to the current node key, replace the data
        
        
        
        
        
    
    def find_min(self): # returns a tuple with min key and data in the BST
        # returns None if the tree is empty
        if self.root: #check if empty
            return self._find_min(self.root) #calls helper function
        else:
            return None

    
    def _find_min(self,currentNode):
        if currentNode.left: #if there is another node with key value less than current
            return self._find_min(currentNode.left) #call find min on left sub-tree
        else:
            return (currentNode.key, currentNode.data) #if at left most leaf return
    



    def find_max(self): # returns a tuple with max key and data in the BST
        # returns None if the tree is empty
        if self.root: #check if empty
            return self._find_max(self.root) #calls helper function
        else:
            return None


    def _find_max(self, currentNode):
        if currentNode.right: #if there is another node with key value greater than current
            return self._find_max(currentNode.right) #call find max on right sub-tree
        else:
            return (currentNode.key, currentNode.data) #if at right most leaf return



    def tree_height(self): # return the height of the tree
        # returns None if tree is empty
        if self.root: #check if empty
            return self._tree_height(self.root) #calls helper function
        else: 
            return None


    def _tree_height(self, currentNode):
        rightHeight = -2 #create right and left height variables with value that will be thrown out
        leftHeight = -2
        if currentNode.right: 
            rightHeight = self._tree_height(currentNode.right) #calls tree height on right sub-tree and assigns value to rightHeight
        if currentNode.left:
            leftHeight = self._tree_height(currentNode.left) #calls tree height on left sub-tree and assigns value to leftHeight
        
        if((currentNode.right == None) and (currentNode.left == None)): #if bottom of tree return 0
            return 0
        
        if (rightHeight > leftHeight): #if the right height is greater than the left, add one and return the height
            return rightHeight + 1
        else: 
            return leftHeight + 1 #else add one to leftheight and return
        


    def inorder_list(self): # return Python list of BST keys representing in-order traversal of BST
        if self.root: #check if empty
            return self._inorder_list(self.root) #call helper function
        else:
            return []


    def _inorder_list(self, currentNode):
        if currentNode is not None: #if not None
            left = self._inorder_list(currentNode.left) #call function on left side
            center = currentNode.key #get current key
            right = self._inorder_list(currentNode.right) #get function on right side
            return left + [center] + right #adds them to list and returns
        else:
            return [] #bottom case
    
    


    def preorder_list(self):  # return Python list of BST keys representing pre-order traversal of BST
        if self.root: #check if empty
            return self._preorder_list(self.root) #call helper function
        else:
            return []
        
        
    def _preorder_list(self, currentNode):
        if currentNode is not None: #if not None
            center = currentNode.key #get current key
            left = self._preorder_list(currentNode.left) #get function on left side
            right = self._preorder_list(currentNode.right) #get function on right side
            return [center] + left + right #return list
        else:
            return [] #bottom case
    
    
    
    
    def level_order_list(self):  # return Python list of BST keys representing level-order traversal of BST
        # You MUST use your queue_array data structure from lab 3 to implement this method
        q = Queue(25000) # Don't change this!
        if self.root: #check if empty
            q.enqueue(self.root) #add root to queue
            lst = [] #create return list
            while(q.size() > 0): #while something is in the queue
                node = q.dequeue() #dequeue node to be processed
                lst += [node.key] #add the key to the list
                if node.left:
                    q.enqueue(node.left) #enqueue left child
                if node.right:
                    q.enqueue(node.right) #enqueue right child
                
            return lst  #return
        else:
            return [] 
        
        
    







