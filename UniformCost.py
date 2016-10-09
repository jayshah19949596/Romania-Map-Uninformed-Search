# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 12:49:48 2016

@author: jaysh
"""

#This is Uniform Cost search
# It is implemented by a priority queue where the node with the minimum value is always selected


def graph_search(start,goal,problem):
    explored = []   #Represents the states which has been already explored
    g        = {}  #Represents the nodes and one of the nodes will be explored
    path = []   #Represents the path of the graph
    current_state=''       #Represents the current state 
    path_cost=0  #Represents the cost of the path
    flag=True
    parent = {}
    frontier,parent=intialise_frontier(start,problem,parent)
    
    path.append(start)
    explored.append(start)
    
    
    
    
    
    while frontier:
        minimum,frontier,minimum_key,minimum_value,last_key=first_update_frontier(frontier,path)
        
        path.append(last_key)
        print("\n Path VALUE : "+", ".join(path))
    
        current_state= path[-1]
        print ('\n The value of current state = '+current_state)
        blank = []
        for keys in frontier:
            split = keys.split(" ")
            blank.append(split[1])
        print ('\n frontier bfore updation = ')
        print(blank)
        explored.append(current_state)
        print ('\n explored states :'+", ".join(explored))
       
        if(test_goal(current_state,goal) == False):
            print ("\n The curent state is NOT the goal state ")
            
            g,path_cost,flag,parent=expand_node(g,problem,current_state,path_cost,goal,flag,parent)
            update_frontier(g,explored,frontier,minimum_value)
            blank = []
            for keys in frontier:
                split = keys.split(" ")
                blank.append(split[1])                
            print ('\n frontier after updation = ')
            print (blank)
        else:
            print ("\n the current state is the goal state ")      
            break
        
        g={}
    print(frontier)
    print(parent)
    reverse_path = [goal]
    child=goal
    cost=0
    

    

    while start not in reverse_path:
        for elem in parent :
            elements = elem.split(" ")
            if elements[1]==child:
                reverse_path.append(elements[0])
                cost = cost + parent[elem]                
                child=elements[0]
            
                
    print("\n")    
    print(reverse_path)
    actual_path = reverse_path[::-1]
    final_path = ', '.join(actual_path)      
    final_explored = ', '.join(explored)
    print("\n FINAL OUTPUT -------------------------------------------------------------")

    print("\n The Final Explored states are :"+final_explored)

    print ("\n The Uniform Cost from Arad to Bucharest is :"+ str(minimum_value))

    print ("\n The Path from Arad to Bucharest using Uniform Cost Search :\n "+final_path)

    print("\n FINAL OUTPUT ------------------------------------------------------------")
    
    
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
#This fucntion updates frontier by 
#inserting those nodes in the frontier 
#which are present in g but they are not explored
#Basically froniter is the union of the list g and explored      
def update_frontier(g,explored,frontier,minimum_value):
    for element in g:
        a = element.split(" ")
        if a[1] not in explored:

            frontier.update({element:g[element]+minimum_value})
        
        else :
            for key in frontier:
                if key == a[1] and g[element]+minimum_value < frontier[key]+minimum_value  :
                    frontier[key] = g[element]+minimum_value
                    
    return frontier    
            
            
#This fucntion Expands the current state
# It shows all the possibility that can be explored from the current state
# and it also shows the cost of that possibility              
def expand_node(g,problem,s,path_cost,goal,flag,parent):   
    for keys in problem :
        
        a = (keys.split(' '))
        
        if a[0] == s:
            present = {keys:problem[keys]}
            g.update(present)
            parent.update(present)
            if a[1] == goal:
                
                flag = False
            path_cost=path_cost+problem[keys]
    
    return g,path_cost,flag,parent

#This function initialises the frontier node to the start node
def intialise_frontier(start,problem,parent):
   # frontier = {"hey "+start:0}
    frontier = {}
    for keys in problem :
        a = keys.split(" ")
        if a[0] == start:
            present = {keys:problem[keys]}
            frontier.update(present)
            parent.update(present)
            
    return frontier ,parent

#It finds the dictionary which is to be appended to the frontier dictionary
def finding_dicitonary(frontier,problem):
    
    d1 = {}
    d2={}
    i=0
    j=0
    
    for ele in frontier:
        b = ele.split(" ")
        
        for key in problem:
            a = key.split(" ")
            
            if a[0] == b[1]:
                d1={key:problem[key]}
                d2.update(d1)
                j=j+1
            i=i+1
    
    
    return d2

#This function updates the frontier dictionary 
# it calculates the state with minimum cost which will be explored
def first_update_frontier(frontier,path):
    minimum_value = 1000000
    for keys in frontier:
        if(frontier[keys]<minimum_value):
            minimum_key=keys
            minimum_value=frontier[keys]
        

    
    
    
    print("\n The Action is to expand : "+minimum_key.split(" ")[1]+" because it has the lowest cost "+str(minimum_value))
    print("\n The Parent node of "+minimum_key.split(" ")[1]+" is "+path[-1] )
    print("\n minimum value ="+str(minimum_value))
    print(frontier)
    
    
    del frontier[minimum_key]
            
            
        
    print(frontier)
    minimum = {minimum_key:minimum_value}
    
    a = minimum_key.split(" ")
    
    return minimum,frontier,minimum_key,minimum_value,a[1]


#This function compares the current node with the goal node
#if the current node is the goal node than it sends True else it sends False         
def test_goal(s,goal):
    if (s==goal):
        return True
    return False
    
    

problem = { 'Arad Zerind':75 , 'Arad Timisoara':118,'Arad Sibiu':140, 'Zerind Oradea':71, 'Oradea Sibiu':151, 'Timisoara Lugoj':111,
	     'Lugoj Mehadia':70, 'Mehadia Drobeta':75, 'Drobeta Craiova':120, 'Craiova Rimnicu-Vilcea':146, 'Craiova Pitesti':138,
	     'Sibiu Fagaras':99, 'Sibiu Rimnicu-Vilcea':80, 'Rimnicu-Vilcea Pitesti':97, 'Fagaras Bucharest':211, 'Pitesti Bucharest':101,
	     'Bucharest Urziceni':85, 'Bucharest Giurgiu':90, 'Urziceni Vaslui':142, 'Vaslui Iasi':92, 'Iasi Neamt':87, 'Urziceni Hirsova':98,
	     'Hirsova Eforie':86}
 

start = "Arad"     
goal = "Bucharest"
graph_search(start,goal,problem)