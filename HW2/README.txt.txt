Yilin Yang
Data Structures & Algorithms HW2

#EXECUTION INSTRUCTIONS

The code submitted was written using Python 3.

You will need the matplotlib python library 
to run the code provided in Q2, Q4, and Q5.


To install, run the following commands in
 linux terminal.



sudo apt install python3-pip

pip3 install matplotlib

pip3 install python3-tk



Then you may run a program using the example notation: 

python3 ./filename.py


If you absolutely cannot use the matplotlib library,
 delete or comment out the contents of any functions

named "plotter" as these are responsible for using 
the library. New graphs will not be made for you

automatically, however the results will still be 
written to text files which you can use to plot 
graphs manually.



#SUBMISSION DETAILS
Five folders are included containing code and results for questions 1-5. A sixth folder is included
containing the input data provided for the assignment from Sakai. Solutions will print
their results into external text documents, to the terminal, or both. There is no code associated
with question 6; it is answered in the report.

To test different data sets from the ones provided, put the file in the "data" folder. 
Each solution for each question has a function which runs the program given a string of the
data file's name. Simply modify an existing string variable for a file name, or create a new
string and create a new function call.

#FOR QUESTION 1

The solution for question 1 does not print the final sorted data (for visual brevity).
If you wish to confirm that the data is indeed sorted correctly, please uncomment the
"printlist" function call in the "runshellsort" function or "runinsertsort" function to
view the sorted list.