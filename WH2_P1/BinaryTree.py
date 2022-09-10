from TreeNode import TreeNode
class BinaryTree:
    
    
    def __init__(self):
        self.root=None

    def getRoot(self):
        return self.root


    #Inserting root
    def put(self,ke, v):
        if self.root:
            self._put(ke, v,self.root)
        else:
            self.root = TreeNode(ke, v)
    #Inserting other nodes
    def _put(self, ke, v,currentNode):
        keList = [k for k in ke]
        Counter= 0
        for item in  keList:
            if item == '.':
                if currentNode.dot == None:
                    currentNode.dot = TreeNode ("","",parent=currentNode)
                currentNode = currentNode.dot
                
            if item == '-':
                if currentNode.dash == None:
                    currentNode.dash = TreeNode ("","",parent=currentNode)
                currentNode = currentNode.dash
            Counter +=1
            
            if Counter == len(keList):
                currentNode.value= v
                currentNode.key= ke

    #Populating the tree
    def populateTree(bt,self):
        bt.put("root","root")
        bt._put(".--.","P",bt.root)
        bt._put(".","E",bt.root)
        bt._put("..","I",bt.root)
        bt._put("...","S",bt.root)
        bt._put("....","H",bt.root)
        bt._put("...-","V",bt.root)
        bt._put("..-.","F",bt.root)
        bt._put("..-","U",bt.root)
        bt._put( ".-..","L",bt.root)
        bt._put( ".-.","R",bt.root)
        bt._put( ".-","A",bt.root)
        bt._put( ".--.","P",bt.root)
        bt._put( ".---","J",bt.root)
        bt._put( ".--","W",bt.root)
        bt._put( "-","T",bt.root)
        bt._put( "-...","B",bt.root)
        bt._put( "-..","D",bt.root)
        bt._put( "-.","N",bt.root)
        bt._put( "--..","Z",bt.root)
        bt._put( "--.","G",bt.root)
        bt._put( "---","O",bt.root)
        bt._put( "--","M",bt.root)
        bt._put( "--.-","Q",bt.root)
        bt._put( "-----","0",bt.root)
        bt._put( "----.","9",bt.root)
        bt._put("---..","8",bt.root)
        bt._put( "--...","7",bt.root)
        bt._put( "-....","6",bt.root)
        bt._put( "-...-","=",bt.root)
        bt._put( "-..-.","/",bt.root)
        bt._put( ".----","1",bt.root)
        bt._put( "..---","2",bt.root)
        bt._put( "...--","3",bt.root)
        bt._put( "....-","4",bt.root)
        bt._put( ".....","5",bt.root)
        #Puntation and other useful symbols
        bt._put(". .-.-.-",".",bt.root)
        bt._put("-.--.","(",bt.root)
        bt._put(".-.-.","+",bt.root)
        bt._put("..-.-","¿",bt.root)
        bt._put("--..--",",",bt.root)
        bt._put("-.--.-",")",bt.root)
        bt._put("-....-","-",bt.root)
        bt._put("--...-","¡ ",bt.root)
        bt._put("..--.","?",bt.root)
        bt._put(".-...","&",bt.root)
        bt._put("..--.-","_",bt.root)
        bt._put(".----.","’",bt.root)
        bt._put("---...",":",bt.root)
        bt._put(".-..-.","”",bt.root)
        bt._put("-.-.--","!",bt.root)
        bt._put("-.-.-.",";",bt.root)
        bt._put("...-..-","$",bt.root)




        
    #search function 
    def search(self, cur, value):
        
        if cur==None or cur.getValue()==value:
            return cur
        elif value > cur.getValue():
            return self.search(cur.getRight(),value)
        else:
            return self.search(cur.getLeft(), value) 



    #delete function
    def delete(self, value):
        
        if self.root == None:
            print("The tree is empty or the current root is None.")
        else:
            par = self.root
            cur = self.root
            pos = 0 # 0 for left and 1 for right
                               
            while cur != None:
                
                if value > cur.getValue():
                    par = cur
                    pos = 1
                    cur = cur.getRight()
                elif value < cur.getValue():
                    par = cur
                    pos = 0
                    cur = cur.getLeft()
                else:
                    break
            
            # after the search  
                   
            if cur==None:
                print("The value isn't included in the tree.")
            else:
                #found the node                
                #case1 and case2: no child or one child
                if not (cur.getLeft()!=None and cur.getRight()!=None):
                    if cur == self.root:
                        self.root = self.next(cur)
                    elif par.getLeft() == cur:
                        par.setLeft(self.next(cur))
                    else:
                        par.setRight(self.next(cur)) 
                else:
                #case 3: two children
                    pre, parpre = self.inOrderPre(cur)
                    #delete pre
                    if parpre.getLeft()==pre:
                            parpre.setLeft(None)
                    else:
                        parpre.setRight(None)
                    
                    cur.setValue(pre.getValue())





    #traversal for the tree 
    def inOrderPre(self,cur,letter,lst):
        
        if cur == None:
            return 
        self.inOrderPre(cur.dot,letter,lst)
        if cur.value==letter and cur is not None:    
            lst.append(cur.key)
            return lst
        self.inOrderPre(cur.dash,letter,lst)


    


