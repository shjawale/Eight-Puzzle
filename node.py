import priorityqueue, copy

class Node():
    print('in node class')
    def __init__(self, parent, g, puzzle = None):
        self.parent = parent  #since we create a new node when we still have the parent. we can have parent as an argument
        self.gn = g
        self.hn = 0
        self.currPuzzleLayout = copy.deepcopy(puzzle)  #copy instead of reference

    def isGoalState(self, prob):
        return self.currPuzzleLayout == prob.goal_state.currPuzzleLayout  #goal_state will be a node

    def update(self, parentnode, g):
        self.parent = parentnode
        self.gn = g

    
    #def findBlank(self): #return i, which is index of 0, aka blank space
    #    print("inside findBlank: self.currPuzzleLayout =", self.currPuzzleLayout)
    #    return self.currPuzzleLayout.index(0)

        #for i in range(len(self.currPuzzleLayout)):
        #    if self.currPuzzleLayout[i] == '0':
        #        return i   #return i, which is index of 0, aka blank space
        #return -1

    '''
    def possibleOperators(self, prob):  #returns list of all possible operators starting from chosen node
        operatorList = []
        #allOps = prob.operators
       
        print("inside possibleOperators: self.currPuzzleLayout =", self.currPuzzleLayout)

        #for i in range(len(self.currPuzzleLayout)):
        #    if self.currPuzzleLayout[i] == '0':
        #        break
        #here, i is index of 0, aka blank space
        print("index of blank in", self.currPuzzleLayout, "=", indexofblank)

        if indexofblank >= 0 and indexofblank <= 5:
            operatorList += "d" #goDown()
        if indexofblank >= 3 and indexofblank <= 8:
            operatorList += "u" #goUp()
        if (indexofblank % 3) != 2:
            operatorList += "l" #goLeft()
        if (indexofblank % 3) != 0:
            operatorList += "r" #goRight()
        
        return operatorList
    '''
    def goDown(self): #returns new node with self as parent and new calculated currPuzzle, g(n), h(n)
        adjacentNode = Node(self, self.gn+1, self.currPuzzleLayout) #create newNode and modify 0's position
        for r in (0, 1):
            for c in range(3):
                if adjacentNode.currPuzzleLayout[r][c] == 0:
                    adjacentNode.currPuzzleLayout[r][c] = adjacentNode.currPuzzleLayout[r+1][c]
                    adjacentNode.currPuzzleLayout[r+1][c] = 0
                    return adjacentNode

        return None

    def goUp(self):
        adjacentNode = Node(self, self.gn+1, self.currPuzzleLayout) #create newNode and modify 0's position
        for r in (1, 2):
            for c in range(3):
                if adjacentNode.currPuzzleLayout[r][c] == 0:
                    adjacentNode.currPuzzleLayout[r][c] = adjacentNode.currPuzzleLayout[r-1][c]
                    adjacentNode.currPuzzleLayout[r-1][c] = 0
                    return adjacentNode

        return None
    
    def goLeft(self):
        adjacentNode = Node(self, self.gn+1, self.currPuzzleLayout) #create newNode and modify 0's position
        for c in (1, 2):
            for r in range(3):
                if adjacentNode.currPuzzleLayout[r][c] == 0:
                    adjacentNode.currPuzzleLayout[r][c] = adjacentNode.currPuzzleLayout[r][c-1]
                    adjacentNode.currPuzzleLayout[r][c-1] = 0
                    return adjacentNode

        return None
    
    def goRight(self):
        adjacentNode = Node(self, self.gn+1, self.currPuzzleLayout) #create newNode and modify 0's position
        for c in (0, 1): #column
            for r in range(3): #row
                if adjacentNode.currPuzzleLayout[r][c] == 0:
                    adjacentNode.currPuzzleLayout[r][c] = adjacentNode.currPuzzleLayout[r][c+1]
                    adjacentNode.currPuzzleLayout[r][c+1] = 0
                    return adjacentNode

        return None

    
    def __lt__(self, other): #should only be used by heap. we are deciding which node to keep
        #print("inside __lt__: self g(n) =", self.gn, "self h(n)", self.hn)
        return (self.gn + self.hn) < (other.gn + other.hn)
        
    def __eq__(self, other): #two nodes with the same layout are equal
        #print("inside __lt__: self g(n) =", self.gn, "self h(n)", self.hn)
        return self.currPuzzleLayout == other.currPuzzleLayout


    def __hash__(self):
        #print("inside __hash__: self hash =", hash(self.currPuzzleLayout))
        return hash((tuple(self.currPuzzleLayout[0]), tuple(self.currPuzzleLayout[1]), tuple(self.currPuzzleLayout[2]),))


#newnode = Node(None, 0, [0,1,2])
