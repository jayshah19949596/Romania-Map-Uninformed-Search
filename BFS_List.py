# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 12:26:17 2016

@author: jaysh
"""

# -*- coding: utf-8 -*-
"""

"""

# This is a Breadth First Search
# The problem of the program is stored in a list
# The program is always complete if the goal is present
# Variable path represents the path of the Breadth First Search
# Variable s represent the current state of the Breadth First Search
# This Program is implemented by a queue where the first node from the 
#frontier is taken out and the new node is appended in the last of frontier 


#intialise_frontier = This function initialises the frontier node to the start node i.e in this case Arad
#choose_node = This function chooses the first state from the frontier its like implementing the half of the queue the first node3 choosen becomes the current state 
#update_frontier = This fucntion updates frontier by inserting those nodes in the frontier which are present in g but they are not explored Basically froniter is the union of the list g and explored
#test_goal = his function compares the current node with the goal node if the current node is the goal node than it sends True else it sends False   
#expand_node = #This fucntion Expands the current state It shows all the possibility that can be explored from the current state and it also shows the cost of that possibility
def graph_search(start,goal,problem):
    explored = []    #Represents the states which has been already explored
    g        = []   #Represents the nodes and one of the nodes will be explored
    path = []          #Represents the path of the Breadth First Search
    current_state =''               #Represents the current state of the Breadth First Search
    path_cost=0        #calculates the cost of the path from start state to current state
    flag=True
    frontier=intialise_frontier(start)
    parent = []
    print ('\n Initialisation value of the frontier = '+", ".join(frontier))
    i=0
    
    while frontier:
        path.append(choose_node(frontier))
        frontier = frontier[1:]
        length_of_path = len(path)
        if(length_of_path > 1):
            print ("\nThe parent node of current state "+path[-1]+" is "+path[-2])
        print ("\n path value= "+", ".join(path))
        
        current_state= path[-1]
        print ('\n The value of current state = '+current_state)
     
        print ('\n frontier bfore updation = '+", ".join(frontier))
 
        explored.append(current_state)
        print ('\n explored node = '+", ".join(explored))
        if(test_goal(current_state,goal) == False):
            print ("\n The curent state is NOT the goal state ")
            if(flag==True):
                g,path_cost,flag=expand_node(g,problem,current_state,path_cost,goal,flag,parent)
            update_frontier(g,explored,frontier)
            print ('\n frontier after updation = '+", ".join(frontier))
            
        else:
            print ("\n The curent state is NOT the goal state ") 
            break
        g=[]
        i = i+1
        
    actual_path,cost = backtracking(start,goal,parent)
    actual_path = actual_path[::-1]

    final_explored = ', '.join(explored)
    print("\n Final Output --------------------------------------------------------------")
    print("\n The Final Explored states are :\n "+final_explored)
    

    print ("\n The Path from Arad to Bucharest using Breadth First Search : \n"+", ".join(actual_path))

    print("\n The cost from Arad to Bucharest using BFS : "+str(cost))    
    
    print("\n Final Output --------------------------------------------------------------")
      


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
    path = frontier[0]
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
def expand_node(g,problem,s,path_cost,goal,flag,parent):   
    
        for place_distance_list in problem :
            if place_distance_list[0] == s :
                print ("\n The distance to be explored is :"+place_distance_list[0]+" to "+place_distance_list[1])
                print ("The cost of the above distance to be explored is :"+str(place_distance_list[2]))
                print (place_distance_list)
                
                parent.append(place_distance_list)
                print(parent)
                g.append(place_distance_list[1])
                if place_distance_list[0] == goal:
                    flag = False
                path_cost=path_cost+place_distance_list[2]
        return g,path_cost,flag  
         
        
    
    
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