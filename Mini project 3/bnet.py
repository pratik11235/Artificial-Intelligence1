# -*- coding: utf-8 -*-
"""
Created on Wed May  4 23:30:45 2022

@author: Pratik Antoni Patekar
UTA id: 1001937948
Programming language used: Python 3.9.6
"""

import sys

class Node:
    # Class to define the nodes of Bayesian network
    def __init__(self, node_name, pred_count, depends_on, cond_table):
        self.node_name = node_name
        self.pred_count = pred_count
        self.depends_on = depends_on
        self.cond_table = cond_table
    
    # Function to calculate the individual probability using conditional tables 
    # stored in the bayesian network
    def computeProbability(self, nodes, arg):
        # If the node is have no conditional dependency then
        # return the prior probability
        if self.pred_count == 0:
            if arg[self.node_name] == True:
                return self.cond_table[True]
            else:
                return (1 - self.cond_table[True])
        
        # Else return the probability depending on the values of the variables
        # that current variable depends on
        else:
            j = self.cond_table[arg[self.depends_on[0].node_name]]
            for i in range(1, self.pred_count):
                j = j[arg[self.depends_on[i].node_name]]
            if arg[self.node_name] == True:
                return j
            else:
                return 1-j
        return False

# Function to return all possible argument values for the arguments that are not specified
# eg. if there are 3 variables A B and C and A is true and B is true then this function will
# return an array with 2 dictionaries where first contains A, B and C are true and second 
# with A and B true and C being false
def return_args(count, arg, val):
    args = []
    len_val = len(val)
    if count != 2**len(val):
        print("The lengths of passed arguments are different")
    for j in range(count):
        # Generate binary number pattern
        # if val contains 2 unknown variables then following will generate
        # 00, 01, 10 and 11
        x = ('{0:0' + str(len(val)) + 'b}').format(j)
        new_arg = arg.copy()
        
        # Assign True and False values according to the pattern generated above
        for i in range(len_val):
            if x[i] == "1":
                new_arg[val[i]] = True
            else:
                new_arg[val[i]] = False
        
        # Append the generated argument values to args array 
        args.append(new_arg)
    
    return args

# Function to calculate the probability depending on the argument values and 
# the Bayesian network (passed as nodes below)
def calc_final_prob(arg_val, nodes):
    B, E, A, J, M = nodes
    
    # Mapping between the nodes and node names
    get_node_var = {"A": A, "B": B, "E": E, "J": J, "M": M}
    
    # Initializing final output variables
    final_out = 1
    output = 0
    
    # Check if any argument is unassigned
    # If all arguments are having values assigned then calculate the probability using 
    # computeProbability() function defined above
    if None not in arg_val.values():
        for i in arg_val.keys():
            ind_prob = get_node_var[i].computeProbability([B, E, A, J, M], arg_val)
            final_out = final_out * ind_prob
    
    # Else generate the all possible values of arguments using return_args() function
    # defined above and then calculate the probability using the computeProbability() function
    # as done in the above case
    else:
        none_list = []
        
        # Get the variables which are unassigned
        for i in arg_val.keys():
            if arg_val[i] == None:
                none_list.append(i)
        
        # Create all possible values for arguments/ variables
        arg_vals = return_args(2**len(none_list), arg_val, none_list)
        
        # For every possible argument in arg_vals do the same calculation as in  above case 
        # and then sum output of every case to generate the final output
        for arg_val in arg_vals:
            for i in arg_val:
                ind_prob = get_node_var[i].computeProbability([B, E, A, J, M], arg_val)
                final_out = final_out * ind_prob
            #print(final_out)
            output = output + final_out
            final_out = 1
        final_out = output
    return final_out
    
# Main function
def main():
    # Create the Bayesian network
    tab = {True: 0.001}
    B = Node("B", 0, None, tab)       # B node
    tab = {True: 0.002}
    E = Node("E", 0, None, tab)       # E node
    tab = {True: {True: 0.95, False: 0.94}, False: {True: 0.29, False: 0.001}}
    A = Node("A", 2, [B, E], tab)       # A node
    tab = {True: 0.90, False: 0.05}
    J = Node("J", 1, [A], tab)       # J node
    tab = {True: 0.70, False: 0.01}
    M = Node("M", 1, [A], tab)       # M node
    
    # Reading the arguments passed from the command-line
    # ************** starts here *********************
    given_flag = 0   # Flag to indicate if there is any conditional variable argument passed
    arg_val = {"B": None, "E": None, "A": None, "J": None, "M": None}  # Arguments to calculate probability of
    given_val = {"B": None, "E": None, "A": None, "J": None, "M": None} # Given variable arguments
    
    arg_count = 0
    given_count = 0
    
    for i in sys.argv[1:]:
        if i[0] not in ['B', 'E', 'A', 'J', 'M', 'g']:
            print("###################################################################################################")
            print("ERROR: One of the arguments entered contains variable other than B, E, A, J and M.")
            print("Please check the input arguments once and execute the code again.")
            print("###################################################################################################")
            return
        if i == "given":
            given_flag = 1
            continue
        if given_flag == 0:
            arg_count += 1
            if i[1] == 't':
                arg_val[i[0]] = True
            else:
                arg_val[i[0]]= False
        else:
            given_count += 1
            if i[1] == 't':
                given_val[i[0]] = True
            else:
                given_val[i[0]]= False
    
    # Input command line argument validation
    if arg_count < 1 or arg_count > 5:
        print("###################################################################################################")
        print("ERROR: The number of arguments entered is greater than 5 or less than 1.")
        print("Note that the number of arguments entered before the keyword 'given' can not be less than 1 or greater than 5.")
        print("Check if you have repeated any node/ variable name in the command line input and re-run the code.")
        print("###################################################################################################")
        return
    if given_count < 1 and given_flag != 0:
        print("###################################################################################################")
        print("ERROR: The keyword 'given' is used but there are no arguments following it")
        print("Please recheck the input command line statement and re-run the program.")
        print("###################################################################################################")
        return
    if given_count > 4:
        print("###################################################################################################")
        print("ERROR: The number of arguments following the keyword 'given' can not be more than 4.")
        print("Please re-check your input command line statement and re-run the program.")
        print("###################################################################################################")
        return
    
    warn = 0
    for i in given_val.keys():
        if given_val[i] != None:
            if arg_val[i] == None:
                arg_val[i] = given_val[i]
            else:
                warn = 1
                #return
    
    if warn == 1:
        print("###################################################################################################")
        print("WARNING: The arguments entered after the keyword 'given' are mentioned before the keyword as well.")
        print("""A contradicting argument and given argument can lead to wrong probability outputs i.e. sometimes
greater than 1 or sometimes less than 0.""")
        print("Please check the command line input and re-run the code.")
        print("###################################################################################################\n\n")
                
    # ******************** And ends here ********************
    
    # Check if there are any arguments that are given
    # If there are any given arguments then calculate the numerator seperately
    # and the denominator seperately using calc_final_prob() function
    # and return the output as numerator/ denominator
    if given_flag == 1:
        n = calc_final_prob(arg_val, [B, E, A, J, M])
        d = calc_final_prob(given_val, [B, E, A, J, M])
        final_output = n/d
        print("Probability =", final_output)
    
    # else just directly calculate the probability using calc_final_prob() function
    # and return the output
    else:
        final_output = calc_final_prob(arg_val, [B, E, A, J, M])
        print("Probability =", final_output)
    
main()
