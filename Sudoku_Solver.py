import sys
import math
class Solver():
	def io(filenam): 
		global SIZE		# SIZE 9 represented the no of row and column in 9x9 Sudoku
		SIZE=9
		file = open(filenam, 'r') 
		lise=[]			# This loop is used to import the Sodoku as a List of Lists. 
		for i in range(SIZE):
			line = file.readline().strip()
			list1=list(line.split(','))
			list2=list(map(int,list1))	
			lise.append(list2)
		for i in range(SIZE):	# This prints the unsolved sudoku
			print(lise[i])
		print("\n")
		global sudoku 
		sudoku=lise
	def _possible(rows,columns,placement):	
		global sudoku
		for i in range(SIZE):	# If the number being tested is already present in either row or column it cannot be added.
			if sudoku[rows][i]==placement or sudoku[i][columns]==placement: 
				return False
		columngrid=(math.floor(columns/3))*3 # Check in the 3x3 sub-grid if the number is already present.
		rowgrid=(math.floor(rows/3))*3
		for i in range(3):
			for j in range(3):
				if(sudoku[rowgrid+i][columngrid+j]==placement):
					return False
		return True				# If value is not duplicate, return True.
	def fill_values():
		global sudoku
		for rows in range(SIZE):
			for columns in range(SIZE):
				if sudoku[rows][columns]==0: # If the cell is empty, then proceed further to fill up possible values.
					for placement in range(1,10):
						if(Solver._possible(rows,columns,placement)):
							sudoku[rows][columns]=placement
							Solver.fill_values()	# Using recursion, we call solve again and again until we break out of first if.
							sudoku[rows][columns]=0
					return
		for i in range(9):
			print(sudoku[i])

	def _checkerf(rows,columns):
		global sudoku
		check=sudoku[rows][columns]	# value to be checked using x and y co-ordinate.
		count=0
		listing=[]
		for a in range(SIZE):
			if(sudoku[rows][a]==check): # If value appears in the column more than once, means that the Puzzle is incorrect.
				count+=1
				listing.append([rows+1,a+1])
		if(count>1):
			print(listing)
			return False
		else:
			listing=[]
			count=0
		for b in range(SIZE):
			if(sudoku[b][columns]==check):	# If value appears in row more than once, means that the Puzzle is incorrect.
				count+=1
				listing.append([b+1,columns+1])
		if(count>1):
			print(listing)
			return False
		else:
			listing=[]
			count=0
		columngrid=(math.floor(columns/3))*3
		rowgrid=(math.floor(rows/3))*3
		for i in range(0,3):			# If value appears more than once in the 3x3 grid, means the Puzzle is incorrect.
			for j in range(0,3):
				if(sudoku[rowgrid+i][columngrid+j]==check):
					count+=1
					listing.append([rowgrid+i+1,columngrid+j+1])
		if(count>1):
			print(listing)
			return False
		else:
			listing=[]
			count=0
			return True					# If none of the above conditions fail, means the Puzzle is solvable.
	def test():
		
		global sudoku
		for i in range(9):				# Iterate over the entire 9x9 grid to check validity of Puzzle.
			for j in range(9):
				if(sudoku[i][j]!=0):
					m=Solver._checkerf(i,j)
					if(m==False):
						print("Sudoku Violation!")
						return 0
def main():
	if(len(sys.argv)<2):
			print("\nInvalid Input! Run with Program name followed by Sudoku filename in .txt format.\n")
			exit()
	filenam=sys.argv[1]
	Solver.io(filenam) # import the txt file
	Solver.test()	   # Test if puzzle is valid
	Solver.fill_values()     # Proceed to solve if valid
if __name__ == "__main__":
	main()
