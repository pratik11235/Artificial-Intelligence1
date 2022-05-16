# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 05:19:44 2022
@author: Pratik Patekar
-About this code: The following script performs uninformed and informed state space search 
on the graph provided in text file. 
-References: Lecture material of Artificial Intelligence 1 by Prof. Vamsikrishna Gopiskrishna
-Python version used to write code: 3.9.7
"""

import sys

# Node struct for UCS algorithm
class node_struct:
    def __init__(self, name, pred, cost):
        self.name = name
        self.pred = pred
        self.cost = cost
        
# Function to print the contents of the fringe
def print_fringe(fringe):
    if fringe == []:
        print("\nFringe is empty.")
    else:
        print("\nFringe: ")
        for i in fringe:
            print(f'|{i.name}||{i.cost}|')

# Function to cities that are adjacent to 'city' along with their costs g(n)
def return_city_cost(links, city, closed):
    k = list(links[city.name].keys()) # get the city names adjacent to 'city' 
    return_k = []
    
    # For every adjacent city create a node with the costs and append them to a list
    # return the list of nodes of adjacent cities
    for i in range(len(k)):
        if k[i] not in closed: # check if not in closed
            return_k.append(node_struct(k[i], city, city.cost + links[city.name][k[i]])) # Node creation
    return return_k

# Function to determine node with min cost and pop the same
# Note: There are two ways to find node with minimum cost and pop
# 1. sort the fringe on basis of cost in ascending order and pop the topmost node (Covered in class) TC = O(n.log(n)) OR
# 2. find the node with min cost and pop it (used in the following function) TC = O(2n) = O(n)
def ucs_pop(fringe, closed):
    min_cost = fringe[0].cost    # initialize min_cost to one of the possible values
    return_node = fringe[0]      # initialize variable containing node to be returned or popped
    
    for i in fringe:             # find minimum cost
        if i.cost < min_cost:
            min_cost = i.cost
    print("Min cost:", min_cost) # print min cost
    for i in fringe:             # find the node in fringe with min cost
        if i.cost == min_cost:
            return_node = i
            fringe.remove(i)     # remove the node from fringe
    print("Popped node:", return_node.name) # print node to be popped
    if return_node.name not in closed:
        closed.append(return_node.name)  # add the popped node to closed
    return fringe, closed, return_node # return the node removed from fringe

# Function to perform UCS algorithm
def UCS(fringe, closed, goal, links, pm):
    nodes_expanded = 0
    nodes_generated = 0
    while True:
        # 1. Pop the node from fringe with minimum cost
        fringe, closed, node1 = ucs_pop(fringe, closed) 
        # 2. Check if the popped node is goal or not
        if node1.name == goal:
            # if it is goal then break the loop and goto block after while loop to print path found and return path cost
            print("Goal found!") 
            break
        # 3. If it is not goal then expand that node and add nodes to fringe
        city_cost = return_city_cost(links, node1, closed)  # find adjacent nodes
        nodes_expanded += 1
        for i in city_cost:
            if i.name not in closed:
                nodes_generated += 1
        #nodes_generated += len(city_cost)
        for i in city_cost:
            fringe.append(i) # add to fringe
        print_fringe(fringe) if pm == 1 else None # print fringe and closed list contents
        print("Closed:", closed) if pm == 1 else None 
        
        # if fringe is empty then return to main function and print no path exists
        if fringe == []: 
            return -1
    
    # Trace the path from the predecessors of the nodes
    path = []
    x = node1
    
    path.append(node1.name)
    print("\nPrinting the data found: ")
    while x.pred != None:
        path.append(x.pred.name)
        x = x.pred
    path = path[::-1]
    
    print("No. of nodes expanded: ", nodes_expanded)
    print("No. of nodes generated: ", nodes_generated)
    print(f'Distance: {node1.cost} km')
    # print the path found
    print("Path:")
    for i in range(len(path) - 1):
        print(f'{path[i]} to {path[i+1]}, {links[path[i]][path[i+1]]} km')
    #print("-> ".join(path))
    return node1.cost

def uninformed_search(infile, start, goal):
    print(f"Input file: {infile}")
    print(f"Start city: {start}")
    print(f"Goal city: {goal}\n")
    
    ## Read input file provided
    try:
        input1_txt = open(infile,'r')
    except:
        print("ERROR: Unable to open the file.")
        print("Tip: Check if you have added .txt extension in the command.")
        print("Also make sure that the file is present in the same directory as the script file.")
        return
    x = ''
    contents = []
    count = 1
    prompt_after = 10
    
    while True:
        x = input1_txt.readline().rstrip("\n")
        contents.append(x)
        if x == 'END OF INPUT':
            break 
        count += 1
        if count%prompt_after == 0:
            print(f'{count} lines read. No END OF INPUT found yet...')
            
    input1_txt.close()
    
    print("Completed reading input file...")
    contents.remove('END OF INPUT')
    #print(contents)
    
    ## Creating a dictionary for links between every city combination available
    links = {}
    
    for i in contents:
        temp = i.split(" ")
        #print(temp)
        if temp[0] not in links.keys():
            links[temp[0]] = {temp[1]: int(temp[2])}
        else:
            links[temp[0]][temp[1]] = int(temp[2])
        
        if temp[1] not in links.keys():
            links[temp[1]] = {temp[0]: int(temp[2])}
        else:
            links[temp[1]][temp[0]] = int(temp[2])
                        
    #print(links)
    
    print_mode = -1
    while print_mode != 0 and print_mode != 1:
        try:
            print_mode = int(input("Enter 1 if you want to enter print mode or else 0: "))
        except:
            print("Please enter either either 1 or 0.")
    
    start_node = node_struct(start, None, 0) # Uninformed
    
    fringe = [start_node]        # Fringe with start node
    closed = []                  # empty closed nodes list
    print_fringe(fringe) if print_mode == 1 else None  # Print fringe contents i.e. city names and cost
    print("Closed:", closed) if print_mode == 1 else None # Print closed nodes
    path = UCS(fringe, closed, goal, links, print_mode) #Function call
    if path != -1:
        print(f'The total path cost is {path} km.') # Print path cost of the path found
    else:
        print(f'\nNo path exists between {start} and {goal}.') # Print message if no path found
    
# Node struct for A* algorithm
class node_struct_h:
    def __init__(self, name, pred, cost, heuristics):
        self.name = name
        self.pred = pred
        #self.depth = depth
        self.cost = cost
        self.heuristics = heuristics

# Function to print the contents of the fringe
def print_fringe_h(fringe):
    if fringe == []:
        print("\nFringe is empty.")
    else:
        print("\nFringe: ")
        for i in fringe:
            print(f'|{i.name}||{i.cost}||{i.heuristics}|')

# Function to cities that are adjacent to 'city' along with their costs g(n)
def return_city_cost_h(links, city, closed, heur):
    k = list(links[city.name].keys())
    return_k = []
    for i in range(len(k)):
        if k[i] not in closed:
            # Only additional thing as compared to UCS return_city_cost function is heuristics parameter of node
            # Here heuristics is added to node structure which is f(n) = g(n) + h(n)
            return_k.append(node_struct_h(k[i], city, city.cost + links[city.name][k[i]], city.cost + links[city.name][k[i]] + heur[k[i]]))
    return return_k

# Function to determine node with min cost g(n) + heuristics h(n) and pop the same
# This function works exactly as ucs_pop function. Only difference is here we are considering heuristics parameter of node
# which is f(n) i.e. g(n) + h(n) instead of just cost i.e. g(n)
def ucs_pop_h(fringe, closed):
    min_cost = fringe[0].heuristics
    return_node = fringe[0]
    for i in fringe:
        if i.heuristics < min_cost:
            min_cost = i.heuristics
    print("Min cost:", min_cost)
    for i in fringe:
        if i.heuristics == min_cost:
            return_node = i
            fringe.remove(i)
    print("Popped node:", return_node.name)
    if return_node.name not in closed:
        closed.append(return_node.name)
    return fringe, closed, return_node

# Function to perform A* algorithm
# This function works exactly same as UCS except for one difference. Here we are considering heuristics parameter 
# of node i.e. f(n) instead of just cost i.e. g(n)
def Astar_H(fringe, closed, goal, links, heuristics_dict, pm):
    nodes_expanded = 0
    nodes_generated = 0
    while True:
        fringe, closed, node1 = ucs_pop_h(fringe, closed)
        if node1.name == goal:
            print("Goal found")
            break
        city_cost = return_city_cost_h(links, node1, closed, heuristics_dict)
        nodes_expanded += 1
        for i in city_cost:
            if i.name not in closed:
                nodes_generated += 1
        for i in city_cost:
            fringe.append(i)
        print_fringe_h(fringe) if pm == 1 else None 
        print("Closed:", closed) if pm == 1 else None 
        if fringe == []:
            return -1
        
    path = []
    x = node1
    
    # Find the path by tracing the predecessor
    path.append(node1.name)
    print("\nPrinting the path found: ")
    while x.pred != None:
        path.append(x.pred.name)
        x = x.pred
    
    # Print the path found
    path = path[::-1]
    print("No. of nodes expanded: ", nodes_expanded)
    print("No. of nodes generated: ", nodes_generated)
    print(f'Distance: {node1.cost} km')
    # print the path found
    print("Path:")
    for i in range(len(path) - 1):
        print(f'{path[i]} to {path[i+1]}, {links[path[i]][path[i+1]]} km')
    #print("-> ".join(path))
    return node1.cost

def informed_search(infile, start, goal, hfile):
    print(f"Input file: {infile}")
    print(f"Start city: {start}")
    print(f"Goal city: {goal}")
    print(f"Heuristics file: {hfile}\n")
    ## Read input file provided
    try:
        input1_txt = open(infile,'r')
    except:
        print("ERROR: Unable to open the file.")
        print("Tip: Check if you have added .txt extension in the command.")
        print("Also make sure that the file is present in the same directory as the script file.")
        return
    x = ''
    contents = []
    count = 1
    prompt_after = 10
    
    while True:
        x = input1_txt.readline().rstrip("\n")
        contents.append(x)
        if x == 'END OF INPUT':
            break 
        count += 1
        if count%prompt_after == 0:
            print(f'{count} lines read. No END OF INPUT found yet...')
            
    input1_txt.close()
    
    print("Completed reading input file...")
    contents.remove('END OF INPUT')
    #print(contents)
    
    ## Creating a dictionary for links between every city combination available
    links = {}
    
    for i in contents:
        temp = i.split(" ")
        #print(temp)
        if temp[0] not in links.keys():
            links[temp[0]] = {temp[1]: int(temp[2])}
        else:
            links[temp[0]][temp[1]] = int(temp[2])
        
        if temp[1] not in links.keys():
            links[temp[1]] = {temp[0]: int(temp[2])}
        else:
            links[temp[1]][temp[0]] = int(temp[2])
                        
    #print(links)
    
    ## Reading heuristics file
    try:
        h_kassel_txt = open( hfile,'r')
    except:
        print("ERROR: Unable to open the file.")
        print("Tip: Check if you have added .txt extension in the command.")
        print("Also make sure that the file is present in the same directory as the script file.")
        return
    x = ''
    heur = []
    count = 1
    prompt_after = 10
    
    while True:
        x = h_kassel_txt.readline().rstrip("\n")
        heur.append(x)
        if x == 'END OF INPUT':
            break 
        count += 1
        if count%prompt_after == 0:
            print(f'{count} lines read. No END OF INPUT found yet...')
        
    h_kassel_txt.close()
    
    print("Completed reading heuristics file...")
    heur.remove('END OF INPUT')
    #print(heur)
    heuristics = {}
    
    for i in heur:
        x = i.split(" ")
        heuristics[x[0]] = int(x[1])
        
    #print(heuristics)
    
    print_mode = -1
    while print_mode != 0 and print_mode != 1:
        try:
            print_mode = int(input("Enter 1 if you want to enter print mode or else 0: "))
        except:
            print("Please enter either either 1 or 0.")
    start_node = node_struct_h(start, None, 0, heuristics[start]) # Informed
    fringe = [start_node]        # Fringe with start node
    closed = []                  # empty closed nodes list
    print_fringe_h(fringe) if print_mode == 1 else None # Print fringe contents i.e. city names, cost, cost + h(n)
    print("Closed:", closed) if print_mode == 1 else None # Print closed nodes
    path = Astar_H(fringe, closed, goal, links, heuristics, print_mode) # Function call
    if path != -1:
        print(f'The total path cost is {path} km.') # Print path cost of the path found
    else:
        print(f'\nNo path exists between {start} and {goal}.') # Print message if no path found
    

def main():
    if len(sys.argv) == 4:
        print("Three arguments are provided. Therefore performing uninformed search\n")
        uninformed_search(sys.argv[1], sys.argv[2], sys.argv[3])
    elif len(sys.argv) == 5:
        print("Four arguments are provided. Therefore performing informed search\n")
        informed_search(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        print("ERROR: Number of arguments in the command are either less or more.")
        print("Tip: Check for spaces if added by mistake.")
    

main()


