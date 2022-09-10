from BinaryTree import *
from BinaryTree import BinaryTree

BinTree = BinaryTree()
BinTree.populateTree(BinTree)



#Encode function
def encode(encode_text):
  
    

   lst=[] 
   for letter in encode_text:  
       letter=letter.upper()
       if BinTree.inOrderPre(BinTree.root,letter,lst):
            lst.append(BinTree.inOrderPre(BinTree.root,letter,lst)) 
      

   return ' '.join(lst)







#Decode function
def decode(text):
    lst=[]
    
    cur=BinTree.getRoot()
    Counter = 0
    for letter in text:
        
        if letter== ".":
            cur=cur.dot

        if letter=="-":
            cur=cur.dash
        
        if letter == " " or Counter== (len(text)-1):        
            
            lst.append(cur.value)
            cur=BinTree.getRoot() 
        
                    
        
        Counter+=1
    return ''.join(lst)
    


