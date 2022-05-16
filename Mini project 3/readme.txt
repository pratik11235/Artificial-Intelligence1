Name: Pratik Antoni Patekar
UTA id: 1001937948
Programming language used: Python 3.9.6



Task 1: Posterior probabilities

Description: Calculate the posterior probabilities given the prior probabilities.

Command line syntax to execute the code:
python compute_a_posteriori.py observations

Here the 'observations' is the string of combination of C's and L's.

For example: python compute_a_posteriori.py LLLLLLLLLLCCCCCCCCCC 


Code explanation:
1. The prior probabilities are stored in the list/ array prior_h
2. Probabilties of getting a cherry and lime are stored in variables q_is_c and q_is_l respectively.
3. The percentage of number of cherries and number of limes in the bag h are stored in list/ array 
q_c_h and q_l_h respectively.
4. After variable initialisation we calculate the probability that the next object picked will be 
cherry and then we also calculate the same for lime (i.e. one minus that of cherry)
5. After this we calculate the posterior probability using the formula covered in class. For this,
I have created a new array named 'cal_h' which stores the new calculated posterior probabilities.
I have also created a function cal_prob_after_obs(ph, qch). This function calculates the posterior
probabilities and returns them to the main function. The argument ph is the list of probabilities 
calculated in the previous iteration for each bag. And the argument qch is the list of percentage 
of the number of cherries in each bag.



Task 2: Bayesian network

Description: Compute and print out the probability of any combination of events given any other 
combination of events

Command line syntax to execute the code:
1. To calculate combination of events X, Y and Z: python bnet.py Xx Yy Zz
2. To calculate conditional probability i.e. P(X = x | Y = y, Z = z): python bnet.py Xx given Yy Zz

Note that here X, Y and Z can be any variable in the Bayesian network and x, y and z can be either
't' if the corresponding variable is True or 'f' if the corresponding variable is False.
The variables in the Bayesian network are as follows:
B - Burglary, E - Earthquake, A - Alarm, J - JohnCalls, M - MaryCalls

For example: 
1. To calculate the probability P(Burglary=true and Alarm=false | MaryCalls=false) the 
command line argument is: python bnet.py Bt Af given Mf
2. To print out the probability P(Alarm=false and Earthquake=true) the command line argument 
is: python bnet.py Af Et


Code explanation:

A. Class Node explanation:

I have created a class named Node which creates Nodes of the Bayesian network given. 
Every instantiated Node contains 4 parameters: 
1. node_name - Name of the node
2. pred_count - Count of nodes that this node depends on
3. depends_on - List/ Array of reference to the nodes in Bayesian network that this node
depends on
4. cond_table - Table of conditional probabilities

This node class also contains a object method that calculates the probability of that node.
The name of the method is computeProbability(nodes, arg). The meaning of the nodes passed are as follows:
1. nodes - The list of nodes in the Bayesian network in specific order i.e. [B, E, A, J, M]
2. arg - These are the values of the arguments passed in the command line input i.e. if in input 
command it is given that python bnet.py Bt Et Af Jt Mt then arg would contain 
{"B": True, "E": True, "A": False, "J": True, "M": True}

Using these, the function calculates the individual probability of the node variable given the value of 
variables in the "arg" dictionary/ table.


B. Function return_args(count, arg, val):

This function returns all possible argument values for the arguments that are not specified
eg. if there are 3 variables A, B and C and the argument contains values as follows:
{"A": True, "B": True, "C": None}
then this function will return an array of all possible combinations of arguments with values:
[{"A": True, "B": True, "C": True},{"A": True, "B": True, "C": False}]

This function is required when there are missing variable in the command line argument.


C. Function calc_final_prob(arg_val, nodes):

This function calculates the final probability for the given set of variable inputs but not 
the conditional probability. The conditional probability is seperately handled in the main function.

There are two arguments for this function:
1. arg_val - This is nothing but the value for every variable in the Bayesian network passed in the 
command line argument. Note that here there can be variables for which the values are unassigned. This
function uses the return_args function to generate all possible arguments values and find their 
product.
2. nodes - The list of nodes in the Bayesian network in specific order i.e. [B, E, A, J, M]


D. Main function:

In this function, the nodes of the Bayesian network i.e. B, E, A, J and Mare created in the beginning.
There are 3 main structures used here. They are as follows:
1. given_flag - Flag to indicate if there is any conditional variable argument passed
2. arg_val - Table/ Dictionary to store the values corresponding to every variable in Bayesian network
and containing values of the arguments passed in command line whose probability has to be calculated.
3. given_val - Table/ Dictionary to store the values of the given variables.

for example: If the given command line input is: python bnet.py Bf At
then the values of the above structures would be:
1. given_flag = 0
2. arg_val - {"B": False, "E": None, "A": True, "J": None, "M": None}
3. given_val - {"B": None, "E": None, "A": None, "J": None, "M": None}

If the given command line input is: python bnet.py Bf At given Jt
then the values of the above structures would be:
1. given_flag = 1
2. arg_val - {"B": False, "E": None, "A": True, "J": None, "M": None}
3. given_val - {"B": None, "E": None, "A": None, "J": True, "M": None}

Now if the given_flag variable is 1 then we need to calculate the conditional probability for which
we calculate the numerator and denominator probabilities seperately using the function calc_final_prob
and print the final output as numerator/denominator.
If the given_flag is 0 then we do not need to calculate the conditional probability and thus directly 
pass the arg_val to calc_final_prob function.

Note: While calculating the conditional probability, the arg_val is updated with the values of the given 
variables since we need to calculate the numerator and denominator seperately. The arg_val is then 
used to calculate the numerator and the given_val is used to calculate the denominator.





