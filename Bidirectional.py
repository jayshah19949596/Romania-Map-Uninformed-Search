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

# This is a Bidirectional Search
# The problem of the program is stored in a list
# The program is always complete if the goal is present
# Variable path represents the path from Arad towards Bucharest
# Variable path1 represents the path from bucharest towards Arad
# Variable s represent the current state of the search from Arad towards Bucharest
# Variable s1 represents the current state of the search from Bucharest to Arad
# This Program is implemented by a stack where the last node from the frontier is taken out and the new node is appended in the last of frontier 


#intialise_frontier = This function initialises the frontier nodes to the start node i.e in this case Arad
#choose_node = This function chooses the last state from the frontier its like implementing the half of the stack the last node choosen becomes the current state 
#update_frontier = This fucntion updates frontier by inserting those nodes in the frontier which are present in g but they are not explored Basically froniter is the union of the list g and explored
#test_goal = his function compares the current node with the goal node if the current node is the goal node than it sends True else it sends False   
#expand_node = #This fucntion Expands the current state It shows all the possibility that can be explored from the current state and it also shows the cost of that possibility
#calculate_path_cost = #This function back tracks and calculates the total path cost friom arad to bucharest   
def graph_search(start,start1,goal,goal1,problem):
    explored = []   #Represents the states which has been already explored
    explored1 = []
    g        = [] #Represents the nodes and one of the nodes will be explored from Arad toward Bucharest
    g1  = []        #Represents the nodes and one of the nodes will be explored from Bucharest to Arad
    path = []    #Represents the path of the graph from arad to Bucharest
    path1 = []#Represents the path of the graph from Bucharest to Arad
    current_state_A2B=''        #Represents the current state from Arad towards Bucharest
    current_state_B2A=''#Represents the current state from Bucharest towards Arad
    frontier = [] #Represents the frontier nodes from Arad to Bucharest
    frontier1 = [] #Represents the frontier nodes from  Bucharest to Arad
    
    frontier,frontier1=intialise_frontier(start,start1)
    
    print ('\n Initialisation value of frontier = '+", ".join(frontier))
    print ('\n Initialisation value of frontier1 = '+", ".join(frontier1))

    
    while frontier:
        path.append(choose_node(frontier))
        path1.append(choose_node(frontier1))
        
        print ('\n The value of current state = '+path[-1])        
        print ('\n The value of current state1 = '+path1[-1])        
        
        length_of_path = len(path)
        length_of_path1 = len(path1)
        
        
        
        if(length_of_path > 1):
            print ("\nThe parent node of current state "+path[-1]+" is "+path[-2])
        print ("\n path value= "+", ".join(path))
    
        if(length_of_path1 > 1):
            print ("\nThe parent1 node of current state1 "+path1[-1]+" is "+path1[-2])
        print ("\n path value1= "+", ".join(path1))

   

        current_state_A2B= path[-1]
        current_state_B2A= path1[-1]
        

        print ('\n frontier bfore updation = '+", ".join(frontier))
        print ('\n frontier1 bfore updation = '+", ".join(frontier1))
  
        explored.append(current_state_A2B)
        explored1.append(current_state_B2A)
        print ('\n explored node = '+", ".join(explored))
        print ('\n explored1 node = '+", ".join(explored1))
  
        if(test_stop(current_state_A2B,current_state_B2A,goal,goal1) == False):
            print ("\n The curent state is NOT the goal state ")
            g = expand_node(g,problem,current_state_A2B,goal,start,start1)
            g1 = expand_node(g1,problem,current_state_B2A,goal1,start,start1)

            update_frontier(g,explored,frontier)
            update_frontier(g1,explored1,frontier1)
            print ('\n frontier after updation = '+", ".join(frontier))
            print ('\n frontier1 after updation = '+", ".join(frontier1))
   
        else:
            print ("\n The curent state is the stop state ")   
            break
        g=[]
        g1=[]
    
    
    total_path_cost = calculate_path_cost(path,problem)
    total_path_cost1 = calculate_path_cost1(path1,problem)
    final_path =[]
    final_explored = ', '.join(explored)
    final_explored1 = ', '.join(explored1)
    
    for elements in path:
        if elements not in path1:
            final_path.append(elements)
        else:
            break
    i=1   
    for elements in path1:
        final_path.append(path1[-i])
        i=i+1
        
    
    
    final_path_cost = total_path_cost1 + total_path_cost


    print("\n FINAL OUTPTUT ----------------------------------------------------")
    print("\n The Final Explored states from Arad to Bucharest are :\n "+final_explored)
    
    print("\n The Final Explored states from Bucharest to Arad are :\n "+final_explored1)

    
    
    print ("\n The Path from Arad to Bucharest  Bidirectional  Search : "+', '.join(path))
    print (" Path Cost from Arad To Bucharest = "+str(total_path_cost))
    
    print ("\n The Path from Bucharest to Arad using Bidirectional  Search : \n "+', '.join(path1))
    print (" Path Cost from Bucharest To Arad = "+str(total_path_cost1))
        
    print ("\n The joint from Arad to Bucharest using Bidirectional  Search : \n "+', '.join(final_path))
    
    print ("\n Final Path Cost from Arad To Bucharest = "+str(final_path_cost))
    print("\n FINAL OUTPTUT----------------------------------------------------")

#This function initialises the frontier node to the start node 
def intialise_frontier(start,start1):
    frontier = [start]
    frontier1=[start1]
    return frontier,frontier1       

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
def update_frontier(g,explored,frontier):
    for element in g:
        if element not in explored:
            frontier.append(element)
            
    
    return frontier
  
#This function compares the current node with the goal node
# and also compares the condition whether bot the searches have reached  a common node
#if the current node is the goal node or both the searches have reached a commmon node than it sends True else it sends False     
def test_stop(s,s1,goal,goal1):
    if (s==goal):
        return True
    elif(s1==goal1):
        return True
    elif(s==s1):
        return True
    return False
  
#This function Expands the current state
# It shows all the possibility that can be explored from the current state
# and it also shows the cost of that possibility 
def  expand_node(g,problem,s,goal,start,start1):
    if goal==start1:
        for place_distance_list in problem :
            if place_distance_list[0] == s :
                print ("\n The distance to be explored is :"+place_distance_list[0]+" to "+place_distance_list[1])
                print ("The cost of the above distance to be explored is :"+str(place_distance_list[2]))
                g.append(place_distance_list[1])
    elif goal==start:
        for place_distance_list in problem :
            if place_distance_list[1] == s :
                print ("\n The distance to be explored is :"+place_distance_list[1]+" to "+place_distance_list[0])
                print ("The cost of the above distance to be explored is :"+str(place_distance_list[2]))
                g.append(place_distance_list[0])
    return g    
    

    
#This function back tracks and calculates the 
#total path cost friom arad to bucharest    
def calculate_path_cost(path,problem):
    length_of_path = len(path)
    
    i=0
    path_cost=0
    lister=[]
    while i<length_of_path-1 :
        
        for place_distance_list in problem:
            if path[i] == place_distance_list[0] and path[i+1] == place_distance_list[1]  :
                lister.append(place_distance_list[2])    
        i=i+1
    print (lister)
    
    for ele in lister:
        path_cost=path_cost+ele
    
    return path_cost  

#This function back tracks and calculates the 
#total path cost friom arad to Bucharest to Arad
def calculate_path_cost1(path,problem):
    length_of_path = len(path)
    
    i=0
    path_cost=0
    lister=[]
    while i<length_of_path-1 :
        
        for place_distance_list in problem:
            if path[i] == place_distance_list[1] and path[i+1] == place_distance_list[0]  :
                lister.append(place_distance_list[2])    
        i=i+1
    print (lister)
    
    for ele in lister:
        path_cost=path_cost+ele
    
    return path_cost              
            
        
        
    
    
problem = [ ['Arad','Zerind',75], ['Arad','Timisoara',118], ['Arad','Sibiu',140], ['Zerind','Oradea',71], 
         ['Oradea','Sibiu',151], ['Timisoara','Lugoj',111], ['Lugoj','Mehadia',70], ['Mehadia','Drobeta',75], 
         ['Drobeta','Craiova',120], ['Craiova','Rimnicu-Vilcea',146], ['Craiova','Pitesti',138],
	     ['Sibiu','Fagaras',99], ['Sibiu','Rimnicu-Vilcea',80], ['Rimnicu-Vilcea','Pitesti',97],
         ['Fagaras','Bucharest',211], ['Pitesti','Bucharest',101],['Bucharest','Urziceni',85], 
         ['Bucharest Giurgiu',90], ['Urziceni Vaslui',142], ['Vaslui Iasi',92], ['Iasi Neamt',87],
         ['Urziceni Hirsova',98], ['Hirsova Eforie',86] ]


    
start = "Arad"     
goal = "Bucharest"
start1 = goal
goal1 = start
graph_search(start,start1,goal,goal1,problem)

