import priorityqueue, node

def Astar(problem, estcost):  #returns either a solution or failure
    frontier = priorityqueue.priorityQueue()  #needs to be a priority queue (min heap)
    print("problem.initial_state =", problem.initial_state)
    
    #initialize the frontier using the initial state of problem
    root = node.Node(None, 0, problem.initial_state)
    frontier.push(root) #, root.gn, root.hn)
   
    #initialize the explored set to be empty
    explored = set()

    while True:
        if frontier.isEmpty():
            return "failure" #what will failure look like??
        
        #choose a leaf node and remove it from the frontier
        #   the node with the least g(n) will be removed
        #       how to calculate g(n)??
        nodewithmingn = frontier.popmin()  #initialize nodewithmingn with the first node in current frontier (which should be the node with the minimum g(n))

        print("popped min from frontier", nodewithmingn.currPuzzleLayout, "with a g(n) =", nodewithmingn.gn, "and a h(n) =", nodewithmingn.hn, "and a queue size of", len(frontier.queue))
    
        if nodewithmingn.isGoalState(problem):
            return "found solution" #corresponding solution

        #expand chosen node, creating new nodes.
        #   if any new nodes are in explored set, do nothing:
        #   check if each is in the frontier. if it is, update or add to frontier.
        allnewnodes = []
        newNode = nodewithmingn.goUp() #newNode is a node containing the new puzzle layout
        if newNode is not None:
            newNode.hn = estcost(newNode.currPuzzleLayout, problem.goal_state.currPuzzleLayout)
            allnewnodes.append(newNode) #list of all new nodes adjacent to chosen node

        newNode = nodewithmingn.goDown() 
        if newNode is not None:
            newNode.hn = estcost(newNode.currPuzzleLayout, problem.goal_state.currPuzzleLayout)
            allnewnodes.append(newNode) #list of all new nodes adjacent to chosen node

        newNode = nodewithmingn.goLeft()
        if newNode is not None:
            newNode.hn = estcost(newNode.currPuzzleLayout, problem.goal_state.currPuzzleLayout)
            allnewnodes.append(newNode) #list of all new nodes adjacent to chosen node

        newNode = nodewithmingn.goRight()
        if newNode is not None:
            newNode.hn = estcost(newNode.currPuzzleLayout, problem.goal_state.currPuzzleLayout)
            allnewnodes.append(newNode) #list of all new nodes adjacent to chosen node
        
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

        explored.add(nodewithmingn) #add the node to the explored set
        if len(explored) >= 25000:
            return "but could not find solution in 25000 nodes"
