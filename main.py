import node, AstarF, math
from problem import *

def estcostmisplaced(nodeLayout, probLayout): #probLayout is a list
    cnt = 0
    for r in range(3):
        for c in range(3):
            if nodeLayout[r][c] != probLayout[r][c]:
                cnt += 1
    if cnt > 0:
        cnt -= 1
    return cnt #cnt should be less than 8

def estcosteuclidean(nodeLayout, probLayout): #probLayout is a list
    diffx = 0
    diffy = 0
    mapofPuzzle = {}  
    result = 0

    for r in range(3):
        for c in range(3):
            mapofPuzzle.update({probLayout[r][c] : (r,c)})
    
    for r in range(3):
        for c in range(3):
            if nodeLayout[r][c] == 0:
                continue
            (pr, pc) = mapofPuzzle[nodeLayout[r][c]] #mapofPuzzle[0] is location of 0 (r,c)
            diffr = pr - r
            diffc = pc - c
            result += math.sqrt(diffr**2 + diffc**2)

    return math.floor(result) #diff should be less than 8

def estcostuniform(nodeLayout, probLayout):
    return 0

def main():
    print("Welcome to sjawa006 8 puzzle solver.\nType '1' to use a default puzzle, or '2' to enter your own puzzle.")
    puzzletype = input() #input
    puzzle = [[],[],[]]
    
    if puzzletype == '1':
        puzzle = [[1,2,3], [4,5,6], [8,7,0]]
        #puzzle = [[8,7,1], [6,0,2], [5,4,3]] #oh boy puzzle
        #puzzle = [[0,1,2], [4,5,3], [7,8,6]] #doable
        #puzzle = [[1,2,0], [4,5,3], [7,8,6]] #easy
        #puzzle = [[1,2,3], [4,5,6], [7,0,8]] #very easy
        #puzzle = [[1,2,3], [4,5,6], [7,8,0]] #very easy

        print("There are no default puzzles.") #pick an existing puzzle
    elif puzzletype == '2':
        print("Enter your puzzle, use a zero to represent the blank\nEnter the first row, use space or tabs between numbers")
        x = input() #input
        puzzle[0] = list(map(int, x.split()))
        print("Enter the first row, use space or tabs between numbers")
        x = input() #input
        puzzle[1] = list(map(int, x.split()))
        print("Enter the first row, use space or tabs between numbers")
        x = input() #input
        puzzle[2] = list(map(int, x.split()))
    else:
        print("Invalid number. Please type either '1' or '2'.")
    
    print("\nEnter your choice of algorithm\nUniform Cost Search\nA* with the Misplace Tile heuristic\nA* with the Euclidean distance heuristic\n")
    algotype = input() #input
    if algotype == '1':
        prob = Problem(puzzle) # check type of everything involved with Problem
        ucs = AstarF.Astar(prob, estcostuniform)
        print("reached main from uniformcost", ucs)
    elif algotype == '2':
        prob = Problem(puzzle) # check type of everything involved with Problem
        Am = AstarF.Astar(prob, estcostmisplaced)
        print("reached main from Amisplaced", Am)
    elif algotype == '3':
        prob = Problem(puzzle) # check type of everything involved with Problem
        Ae = AstarF.Astar(prob, estcosteuclidean)
        print("reached main from Aeuclid", Ae)
    else:
        print("Invalid number. Reminder, valid algorithm numbers are '1', '2', or '3'.")
    return


if __name__ == "__main__":
    main()
