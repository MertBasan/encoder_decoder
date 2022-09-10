IOT Worksheet 2 (Part1)
////////////////////////////////////////////////////////
Table of Contents
-Personal Experience
-General Info
-Technologies Used
-Features
-Usage 
-Testing 
-Contact
////////////////////////////////////////////////////////

Personal Experience:
I have struggled a bit in the beginning to understand how binary tree works and how to implement it. In the implementation process, the thing I have struggled was the understanding how do we traverse the tree and how do implement the function of encode.  
I have compare my encode function with the online resources, and took the idea. Basically, I learned how encode function works. Implemented for loop inside of it and use it with inOrder traversal mechanism.  

The traverse mechanism in this tree is InOrder traversal. So, implemented some random python codes related with traverse to exercise it. 

I should have implemented a more efficient insert function. I am using two insert functions which are "put" for the root and "_put" for the rest of the nodes. So, it could be just one function that does the same job. Since we are working with letters, I have struggled with the idea of insertation in a tree because could not find a way to compare nodes with eachother, so wrote a new function that allows to populate the tree. 

I can clearly say that learned a lot during especially in implementation such as working with classes, lists, etc...


General Info:
This project is the firts part of worksheet two, module named IOT.
The purpose of this project is converting messages (inputs) to encoded and decoded texts.


Technologies Used:
Python 3.8.10 and Visual Studio Code version 1.65.2 used in this project.


Features:
Different test are included in this project, feel free to test the correctness of code.
The main feature of the project is the converter. (string --> morse) (morse --> string)


Usage:
You have several options to test and use it. 
-Converting your own words in "main.py". That will take your input and convert it to morse or decode. 

-You will also find the test named "Eleven know it's Hooper" in "main.py". 

-Also code contains other tests such as assert tests in "assert_test.py" and unittest in "morseunit.py". 




Contact:
Gitlab profile link: https://gitlab.uwe.ac.uk/m2-basan

