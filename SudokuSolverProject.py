#class that takes sudoku board and solves
#Class assumes that the input sudoku board has total boxes = number of rows = number of columns = integer that is a perfect square
import random
class SodokuSolver:
    def __init__(self,Puzzle_Board=[]):
        self.board = Puzzle_Board
        self.board_size = len(self.board) #contains number of row and columns assumes there is same num of row/columns
        self.box_size = int(self.board_size ** 0.5) #contains the demensions of the boxes
        self.found=0

    # prints out any valid sodoku board
    def print_sudoku_board(self):
        board_size=len(self.board)
        for i in range(self.board_size):
            if (i != 0 and i % (self.box_size) == 0):
                for j in range(self.board_size):
                    print("- - ",end="")
                print("")
            for k in range(self.board_size):
                if (k == self.board_size-1):
                    print(f" {self.board[i][k]} \n",end="")
                elif (k != 0 and k % (self.box_size) == 0):
                    print(f" | {self.board[i][k]} ",end="")
                else:
                    print(f" {self.board[i][k]} ",end="")
        print("Printed^\n")

    #Finds an empty square and reutrns in form (row,column)
    def find_empty(self):
        for i in range (self.board_size):
            for j in range (self.board_size):
                if self.board[i][j] == 0 :
                    return(i,j)
        return None
    
    def create_empty(self,size):
        self.board_size = int(size*size) #contains number of row and columns assumes there is same num of row/columns
        self.box_size = size #contains the demensions of the boxes
        for i in range (self.board_size):
            temp=[]
            for k in range (self.board_size):
                temp.append(0)
            self.board.append(temp)

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
    
    def create_random(self,size):
        self.create_empty(size)       
        return self.fill_random()

    def fill_random(self):       
        current_cord = self.find_empty() 
        valuelist = []
        for i in range (1,self.board_size+1):
            valuelist.append(i)
        random.shuffle(valuelist)
        if current_cord == None:
            return True       
        for value in valuelist:
            if self.is_valid(current_cord,value):
                self.board[current_cord[0]][current_cord[1]]=value
                if self.fill_random():
                    return True
                self.board[current_cord[0]][current_cord[1]] = 0
        return False
    
    def only_one(self,initial=True):
        current_cord = self.find_empty()
        if initial == True:
            self.found = 0 
        if current_cord == None:
            self.found += 1
            if self.found==2:
                return True   
            else:
                return False   
        for value in range (1,self.board_size+1):
            if self.is_valid(current_cord,value):
                self.board[current_cord[0]][current_cord[1]]=value
                if self.only_one(False):
                    self.board[current_cord[0]][current_cord[1]] = 0
                    if initial == True:
                        return False
                    else:
                        return True
                self.board[current_cord[0]][current_cord[1]] = 0
        if initial == True and self.found == 1:
            return True
        return False
        
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

    def set_difficulty(self,difficulty):
        nonemptyboxes=[]
        givens=0#count is how many givens remain on board
        totalsquares = self.board_size*self.board_size
        for row in range(self.board_size):
            for column in range(self.board_size):
                if self.board[row][column] != 0:
                    nonemptyboxes.append([row,column])
                    givens += 1
        random.shuffle(nonemptyboxes)
        test=0
        for cordinate in nonemptyboxes:

            temp = self.board[cordinate[0]][cordinate[1]]
            self.board[cordinate[0]][cordinate[1]]=0
            testign = self.only_one()
            test+=1
            print(test, testign, givens)
            if testign == False:
                self.board[cordinate[0]][cordinate[1]]=temp
            else:
                #print(cordinate)
                givens -= 1
            if givens == difficulty:
                return True
        return False                      

        
SudokuBoardE = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
]
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
    [4,1,0,3],
    [2,3,1,4],
    [1,4,3,2],
    [3,2,4,1],
]
SudokuBoard3 = [
    [1]
]
myPuzzle = SodokuSolver()
#print(f"Initial")
#myPuzzle.create_empty(2)
#myPuzzle.print_sudoku_board()
#print(f"random")
#myPuzzle.print_sudoku_board()
#myPuzzle.set_difficulty(0)
#print(f"Level: 0")
#myPuzzle.print_sudoku_board()
#print(myPuzzle.only_one( ))
#myPuzzle.set_difficulty(17)

myPuzzle.create_random(4)
myPuzzle.set_difficulty(145)

#print(f"{myPuzzle.board}")
myPuzzle.print_sudoku_board()
#myPuzzle.set_difficulty(2)
#print(f"Level: 2")
#myPuzzle.print_sudoku_board()