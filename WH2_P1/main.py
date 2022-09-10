import morse
from morse import *
from BinaryTree import BinaryTree


# Testing Eleven knows it's Hooper
# if __name__ == "__main__":
#     e = morse.encode('us')
#     print('%s' % e)
#     d = morse.decode(e)
#     print(d)
#     assert morse.encode('us') == '..- ...', "Should be ..-"
#     assert morse.decode('..- ...') == 'US', "Should be us"


#/////////////////////////////////////////////////////////

#Additional test that taking input from user 


decision = input("press '1' to encode, press '2' to decode :")

if decision=='1':
    text=input("Input: ")
    print(encode(text))
elif decision=='2':
    text=input("Input: ")
    print(decode(text))



    
    





    








