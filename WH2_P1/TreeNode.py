class TreeNode: 
    def __init__(self, key,value,parent=None,dot=None,dash=None):
        self.value = value
        self.dot = dot
        self.dash = dash
        self.parent= parent
        self.key=key



    #defining functions that are going to implemented in tree 
    def hasLeftChild(self):
        return self.dot

    def hasRightChild(self):
        return self.dash

    def getKey(self):
        return self.key
    

    def isRoot(self):
        return not self.root

    def getValue(self):
        return self.value
    def getLeft(self):
        return self.dot
    def getRight(self):
        return self.dash