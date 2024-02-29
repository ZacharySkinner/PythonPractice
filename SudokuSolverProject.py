#class that takes sudoku board and solves
#Class assumes that the input sudoku board has total boxes = number of rows = number of columns = integer that is a perfect square
class SodokuSolver:
    def __init__(self,Puzzle_Board):
        self.board = Puzzle_Board
        self.board_size = len(self.board) #contains number of row and columns assumes there is same num of row/columns
        self.box_size = int(self.board_size ** 0.5) #contains the demensions of the boxes

    # prints out any valid sodoku board with total boxes = number of rows = number of columns = integer that is a perfect square
    def print_sudoku_board(self):

        board_size=len(self.board)
        for i in range(self.board_size):
            if (i != 0 and i % (self.box_size) == 0):
                for j in range(self.board_size):
                    print("- ",end="")
                print("")
            for k in range(self.board_size):
                if (k == self.board_size-1):
                    print(f"{self.board[i][k]} \n",end="")
                elif (k != 0 and k % (self.box_size) == 0):
                    print(f" | {self.board[i][k]}",end="")
                else:
                    print(f"{self.board[i][k]}",end="")
        print("")

    #Finds an empty square and reutrns in form (row,column)
    def find_empty(self):
        for i in range (len(self.board)):
            for j in range (self.board_size):
                if self.board[i][j] == 0 :
                    return(i,j)
        return None
    
    def is_valid(self, cord, num):
        #checks the Column
        for i in range(self.board_size):
            if  (i != cord[0] and self.board[i][cord[1]] == num):
                return False

        #checks the Row    
        for i in range(self.board_size):
            if  (i != cord[1] and self.board[cord[0]][i] == num):
                return False
        
        #checks box
        box_cord_x = cord[1] // self.box_size
        box_cord_y = cord[0] // self.box_size
        for column in range(box_cord_x*self.box_size, box_cord_x*self.box_size+self.box_size):
            for row in range(box_cord_y*self.box_size, box_cord_y*self.box_size+self.box_size):
                if (((row,column) != cord) and (self.board[row][column]==num)):
                    return False
        return True
    
    #Solve the puzzle using backtracking
    def solve_board(self):
        current_cord = self.find_empty() 
        # return true if puzzle is fully solved
        if current_cord == None:
            return True       
        for value in range (1,self.board_size+1):
            if self.is_valid(current_cord,value):
                self.board[current_cord[0]][current_cord[1]]=value
                if self.solve_board():
                    return True
                self.board[current_cord[0]][current_cord[1]] = 0
        return False


SudokuBoard = [
    [0,1,6,7,0,5,3,0,0],
    [4,0,0,0,6,0,0,0,0],
    [2,0,0,0,0,0,0,0,1],
    [6,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,3,0,8,0],
    [0,9,7,0,5,0,0,0,4],
    [0,2,0,0,0,0,0,0,0],
    [0,0,0,9,0,0,4,0,0],
    [0,5,1,0,7,0,0,0,9]
]
SudokuBoard2 = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],

    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],

    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],

    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]
SudokuBoard3 = [
    [1]
]
myPuzzle = SodokuSolver(SudokuBoard2)
myPuzzle.print_sudoku_board()
myPuzzle.solve_board()
#print(myPuzzle.is_valid((0,3),4))
#print(myPuzzle.find_empty())
myPuzzle.print_sudoku_board()

