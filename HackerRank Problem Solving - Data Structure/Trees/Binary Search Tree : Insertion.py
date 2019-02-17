### [Challenge Name: Binary Search Tree : Insertion](/challenges/binary-search-tree-insertion)

You are given a pointer to the root of a binary search tree and values to be inserted into the tree. 
Insert the values into their appropriate position in the binary search tree and return the root of 
the updated binary tree.
You just have to complete the function.



#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)

    def insert(self, val):
        #Enter you code here.

        if self.root == None:
            self.root = Node(val)
            return self.root
        
        temp_root = self.root

        while temp_root:
            if temp_root.info > val:
                if temp_root.left:
                    temp_root = temp_root.left
                else:
                    temp_root.left = Node(val)
                    return self.root
            else:
                if temp_root.right:
                    temp_root = temp_root.right
                else:
                    temp_root.right = Node(val)
                    return self.root

