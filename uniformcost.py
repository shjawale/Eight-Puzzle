#function GraphSearch(problem) returns a solution, or failure
#   initialize the frontier using the initial state of problem
#   initialize the explored set to be empty
#   LOOP DO:
#       IF the frontier is empty:
#           return failure
#       choose a leaf node and remove it from the frontier
#       IF the node contains a goal state:
#           return corresponding solution
#       IF choosen node is in the frontier, update node. IF chosen node is in explored set, do nothing:
#           expand the chosen node, adding the resulting node to the frontier
#       add the node to the explored set

# uniform cost search
# dequeue nodes in order of their cost (from initial node), g(n)
#   which is the same as A* = g(n) + h(n) where h(n) = 0

import priorityqueue, node

def uniformcostsearch(problem):  #returns either a solution or failure
    frontier = priorityqueue.priorityQueue()  #needs to be a priority queue (min heap)
    print("problem.initial_state =", problem.initial_state)
    
    #initialize the frontier using the initial state of problem
    root = node.Node(None, 0, 0, problem.initial_state)
    print("root =", root.currPuzzleLayout)
    frontier.push(root) #, root.gn, root.hn)
    print("frontier after pushing root =", frontier.queue[0].currPuzzleLayout)
   
    #uctree = tree.Tree()
    #uctree.source = root

    #initialize the explored set to be empty
    explored = set()
    print("explored =", explored)

    while True:
        print("in while loop")
        if frontier.isEmpty():
            return "failure" #what will failure look like??
        
        #choose a leaf node and remove it from the frontier
        #   the node with the least g(n) will be removed
        #       how to calculate g(n)??
        nodewithmingn = frontier.popmin()  #initialize nodewithmingn with the first node in current frontier (which should be the node with the minimum g(n))

        print("popped min from frontier", nodewithmingn.currPuzzleLayout, "with a g(n) =", nodewithmingn.gn, "and a queue size of", len(frontier.queue))
    
        if nodewithmingn.isGoalState(problem):
            return "found solution" #corresponding solution

        #expand chosen node, creating new nodes.
        #   if any new nodes are in explored set, do nothing:
        #   check if each is in the frontier. if it is, update or add to frontier.
        allnewnodes = []
        print("before possibleOperators call: nodewithmingn.currPuzzleLayout =", nodewithmingn.currPuzzleLayout)
        #possoperators = nodewithmingn.possibleOperators(problem) #returns list of all possible operators starting from chosen node

        print("before loop: allnewnodes =", allnewnodes)
        
        newNode = nodewithmingn.goUp() #newNode is a node containing the new puzzle layout
        if newNode is not None:
            allnewnodes.append(newNode) #list of all new nodes adjacent to chosen node

        newNode = nodewithmingn.goDown() 
        if newNode is not None:
            allnewnodes.append(newNode) #list of all new nodes adjacent to chosen node

        newNode = nodewithmingn.goLeft()
        if newNode is not None:
            allnewnodes.append(newNode) #list of all new nodes adjacent to chosen node

        newNode = nodewithmingn.goRight()
        if newNode is not None:
            allnewnodes.append(newNode) #list of all new nodes adjacent to chosen node
        
        for i in range(len(allnewnodes)):
            print("after loop: allnewnodes[",i, "] =", allnewnodes[i].currPuzzleLayout)

        for n in allnewnodes: #iterate over nodes
            print("n.currPuzzleLayout =", n.currPuzzleLayout)
            if n in explored: #returns bool corresponding to whether given node is in explored set
                print("new node in explored. do nothing")
            elif frontier.find(n): #returns bool corresponding to whether given node is in explored set
                n.update(nodewithmingn, nodewithmingn.gn) #updates node object with  given g(n) value (which should update frontier)
                frontier.update()
                print("updated value of f(n)", n.currPuzzleLayout, "in frontier")
            else:
                frontier.push(n)
                print("pushed", n.currPuzzleLayout, "to frontier")
                #print("frontier.queue[0] =", frontier.queue)



        #for i in frontier.find(node):
        #    if i == nodewithmingn:
        #        print(i,' is in frontier.')
        #        i.updateucs(nodewithmingn) #update reference of i's parent to nodewithmingn's parent and update i's g(n) to nodewithmingn's g(n)
        #        break
        print("explored =", explored) 
        explored.add(nodewithmingn) #add the node to the explored set
            

#def updateucs(self, node): #ucs stands for uniform cost search
#    self.parent = node.parent
#    self.gn = node.g
