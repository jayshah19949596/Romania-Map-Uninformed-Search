# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 12:21:25 2016

@author: jaysh
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 11:27:08 2016

@author: jaysh
"""

# This is a Depth First Search
# The problem of the program is stored in a List
# The program is always complete if the goal is present
# Variable path represents the path of the Depth First Search
# Variable s represent the current state of the Depth First Search
# This Program is implemented by a stack where the last node from the 
#frontier is taken out and the new node is appended in the last of frontier 


#intialise_frontier = This function initialises the frontier node to the start node i.e in this case Arad
#choose_node = This function chooses the last state from the frontier its like implementing the half of the stack the last node choosen becomes the current state 
#update_frontier = This fucntion updates frontier by inserting those nodes in the frontier which are present in g but they are not explored Basically froniter is the union of the list g and explored
#test_goal = his function compares the current node with the goal node if the current node is the goal node than it sends True else it sends False   
#expand_node = #This fucntion Expands the current state It shows all the possibility that can be explored from the current state and it also shows the cost of that possibility
#calculate_path_cost = #This function back tracks and calculates the total path cost friom arad to bucharest   
def graph_search(start,goal,problem):
    explored = []   #Represents the states which has been already explored
    g        = [] #Represents the nodes and one of the nodes will be explored
    path = []    #Represents the path of the graph
    current_state=''        #Represents the current state 
    parent = [] 
    
    frontier=intialise_frontier(start)
    
    print ('\n Initialisation value of frontier = '+", ".join(frontier))

    
    while frontier:
        path.append(choose_node(frontier))
        
        print ('\n The value of current state = '+path[-1])        
        
        length_of_path = len(path)
        if(length_of_path > 1):
            print ("\nThe parent node of current state "+path[-1]+" is "+path[-2])
        print ("\n path value= "+", ".join(path))
    

   

        current_state= path[-1]
        

        print ('\n frontier bfore updation = '+", ".join(frontier))
  
        explored.append(current_state)
        print ('\n explored node = '+", ".join(explored))
  
        if(test_goal(current_state,goal) == False):
            print ("\n The curent state is NOT the goal state ")
            g = expand_node(g,problem,current_state,parent)


            update_frontier(g,explored,frontier)
            print ('\n frontier after updation = '+", ".join(frontier))
   
        else:
            print ("\n The curent state is the goal state ")   
            break
        g=[]
    
    actual_path,cost = backtracking(start,goal,parent)
    actual_path = actual_path[::-1]

    final_path = ', '.join(actual_path)
    final_explored = ', '.join(explored)
    
    print('\n FINAL OUTPUT --------------------------------------------------------')

    print("\n The Final Explored states are :\n "+final_explored)

    
    
        
    print ("\n The Path from Arad to Bucharest using Depth first Search : \n "+final_path)
    
    print ("\n Final Path Cost from Arad To Bucharest = "+str(cost))
            
    print('\n FINAL OUTPUT --------------------------------------------------------')  

  
#This function back tracks and calculates the 
#total path cost friom arad to bucharest    
       

def backtracking(start,goal,parent):
    reverse_path = [goal]
    child = goal
    cost = 0 
    while start not in reverse_path:
        for elements in parent:
            if elements[1]==child:
                reverse_path.append(elements[0])
                cost = cost + elements[2]
                child=elements[0]
                break
    

    return reverse_path,cost
    
    
#This function initialises the frontier node to the start node i.e in this case Arad
def intialise_frontier(start):
    frontier = [start]
    return frontier       

#This function chooses the first state from the frontier its like 
#implementing the half of the queue
#The first node choosen becomes the current state   
def choose_node(frontier):
    path = frontier.pop()
    return path

#This fucntion updates frontier by 
#inserting those nodes in the frontier 
#which are present in g but they are not explored
#Basically froniter is the union of the list g and explored                   
def update_frontier(g, explored, frontier):
    for element in g:
        if element not in explored:
            frontier.append(element)
    return frontier
  
#This function compares the current node with the goal node
#if the current node is the goal node than it sends True else it sends False     
def test_goal(s,goal):
    if (s==goal):
        return True
    return False
  
#This function Expands the current state
# It shows all the possibility that can be explored from the current state
# and it also shows the cost of that possibility 
def expand_node(g,problem,s,parent):   
    for place_distance_list in problem :
        if place_distance_list[0] == s :
            print ("\n The distance to be explored is :"+place_distance_list[0]+" to "+place_distance_list[1])
            print ("The cost of the above distance to be explored is :"+str(place_distance_list[2]))
            g.append(place_distance_list[1])
            parent.append(place_distance_list)
    return g      
    

  
            
        
        
    
    
problem = [ ['Arad','Zerind',75], ['Arad','Timisoara',118], ['Arad','Sibiu',140], ['Zerind','Oradea',71], 
         ['Oradea','Sibiu',151], ['Timisoara','Lugoj',111], ['Lugoj','Mehadia',70], ['Mehadia','Drobeta',75], 
         ['Drobeta','Craiova',120], ['Craiova','Rimnicu-Vilcea',146], ['Craiova','Pitesti',138],
	     ['Sibiu','Fagaras',99], ['Sibiu','Rimnicu-Vilcea',80], ['Rimnicu-Vilcea','Pitesti',97],
         ['Fagaras','Bucharest',211], ['Pitesti','Bucharest',101],['Bucharest','Urziceni',85], 
         ['Bucharest Giurgiu',90], ['Urziceni Vaslui',142], ['Vaslui Iasi',92], ['Iasi Neamt',87],
         ['Urziceni Hirsova',98], ['Hirsova Eforie',86] ]
         

start = "Arad"     
goal = "Bucharest"
graph_search(start,goal,problem)