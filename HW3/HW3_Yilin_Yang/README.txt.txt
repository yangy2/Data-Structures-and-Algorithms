Yilin Yang
Data Structures & Algorithms HW3

#EXECUTION INSTRUCTIONS

The code submitted was written using Python 3.

You may run a program using the example notation: 

python3 ./filename.py



#SUBMISSION DETAILS
#FOR QUESTION 1 & 2
The solution for question 1 is a file with class and function declarations to implement a 2-3 Tree API.
There is nothing to execute for this problem. The solution for question 2 uses this API; the two files 
must be in the same directory. The solution for question 2 will prompt you to specify problem size. The 
maximum size supported is 128000; the program will automatically resize your input if you enter a larger
number. Negative inputs will produce an error.

#FOR QUESTION 3 & 4
To test different data sets than the one included, replace the contents of the "data.txt" folder.
Alternatively include a new file containing the data to use in the same directory as the Python files
and update the string variable "file" to the name of the new file. The solutions for question 3 and 
question 4 both import the "redblack.py" file, which builds a Red Black Tree. The tree is not printed
but can be by uncommenting the "print(self)" call in the "count(self, path)" definition. 

#FOR QUESTION 5
The solution for question 5 does not print the binary search tree (for visual brevity). If you wish to confirm that 
the data is indeed inserted into the tree, please uncomment the "printtree" function near the end of the file.
To search for a different key using rank() and select(), modify the values of the "rank_search" and "select_search"
variables near the end of the file. The input data is the same as question 3 and 4. Modification of the input data
is the same as for those two problems (see above).