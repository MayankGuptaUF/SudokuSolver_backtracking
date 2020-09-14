# SudokuSolver_backtracking
README:

Language- Python (version 3.5+)

Library Used - 
1) sys( used to import file)
2) math ( used to calculate the Qoutient)
NOTE- Both of these are standard python libraries that you do not need to install.

OS - Ubuntu 16.04


To execute the program: python3 HW1.py [filename]
For eg- python3 HW1.py sudoku1.txt

NOTE- If file is not in the same directory enter the full path name.

All the function are in the Solver class.

1) io(filenam)- The function io is a file handling function which is used to import the text file and then convert it to a nested list so that it can mimic a matrix. It takes the text file as an input.
2) possible(rows,columns,placement)- This is a private function that can only be called inside the Class Solver, this function is used to see whether the input 'placement' can be placed at the particular cell denoted by the rows and columns.
3) fill_values(): fill_values does not take any input, it is used to make changes to the global variable Sudoku. In this function, the Sodoku grid is recursively traversed till we are able to fill out all the cells.
4) checkerf(rows,columns): This is a private function. It takes the position of the cell and checks if the Sodoku puzzle is valid or not.In case there is a violation, this function also returns the positions where the violations have occured.
5) test(): The test function is the driver function for checkerf() and iteratively checks the validity for all 81 possible values.


Algorithm-

In this approach, first the function io() is called to import the Sudoku to a global variable called Sudoku, Next the test() function is called to check the validity of the puzzle.If the initial placement is valid, we proceed to the fill_values() function, this function iteratively places a number in a particular cell which ensuring that it does not violate the rules which is ensured through the possible() function.But, it might happen that because not all cells are filled in the starting, we might have multiple valid numbers up until that iteration. In that case,after some recursions, we would encounter a position where none of the 1-9 are able to be valid , that means that a number previously entered that seemed like a likely fit was incorrect and we back track our approach until we find that position where the incorrect value was filled and change that value.This continues until none of the cells are empty.
