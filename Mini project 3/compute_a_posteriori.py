# -*- coding: utf-8 -*-
"""
Created on Wed May  4 16:33:28 2022

@author: Pratik Antoni Patekar
UTA id: 1001937948
Programming language used: Python 3.9.6
"""

# Function to calculate the probability after the observation
def cal_prob_after_obs(ph, qch):
    q_is_c = 0
    
    for i in range(5):
        q_is_c = q_is_c + (ph[i] * qch[i])
    
    return q_is_c, (1 - q_is_c)


# Main function starts from here
import sys

if len(sys.argv) == 1:
    print("NOTE: The observation argument is missing in the command line argument.")
    print("The format for command line execution is follows:")
    print("'python compute_a_posteriori observation' where observation is string of any combination of C's and L's.")
    print("Proceeding assuming that there are no observations made.")
    x = ''
elif len(sys.argv) > 2:
    print("ERROR: The number of arguments provided are more than expected.")
    print("NOTE: The format for command line execution is follows:")
    print("'python compute_a_posteriori observation' where observation is string of any combination of C's and L's.")
    sys.exit(0)
else:
    x = sys.argv[1]

# Variable value initialisation
prior_h = [0.1, 0.2, 0.4, 0.2, 0.1]
q_c_h = [1, 0.75, 0.5, 0.25, 0]
q_l_h = [0, 0.25, 0.5, 0.75, 1]
q_is_c = 0
q_is_l = 0

# Calculate the probability that next object selected is cherry and lime 
for i in range(5):
    q_is_c = q_is_c + (prior_h[i] * q_c_h[i])
q_is_l = 1 - q_is_c

print("Observation sequence Q: " + x)
print("Length of Q: " + str(len(x)))
print("")
cal_h = prior_h
if len(x) == 0:
    print("Printing the probabilities for no observations made:")
    print(f"P(h1 | Q) = {cal_h[0]}")
    print(f"P(h2 | Q) = {cal_h[1]}")
    print(f"P(h3 | Q) = {cal_h[2]}")
    print(f"P(h4 | Q) = {cal_h[3]}")
    print(f"P(h5 | Q) = {cal_h[4]}")
    
# Calculate the posterior probability using the formula covered in lecture
count = 1
for i in x:
    if i == 'C':
        for j in range(5):
            cal_h[j] = (cal_h[j] * q_c_h[j])/q_is_c
        print("After Observation " + str(count) + " = " + i)
        #print(cal_h)
        print(f"P(h1 | Q) = {cal_h[0]}")
        print(f"P(h2 | Q) = {cal_h[1]}")
        print(f"P(h3 | Q) = {cal_h[2]}")
        print(f"P(h4 | Q) = {cal_h[3]}")
        print(f"P(h5 | Q) = {cal_h[4]}")
        
        q_is_c, q_is_l = cal_prob_after_obs(cal_h, q_c_h)
        #print(q_is_c, q_is_l)
        print(f"Probability that the next candy we pick will be C, given Q: {q_is_c}")
        print(f"Probability that the next candy we pick will be L, given Q: {q_is_l}")
        print("")
    else:
        for j in range(5):
            cal_h[j] = (cal_h[j] * q_l_h[j])/q_is_l
        #print(cal_h)
        print("After Observation " + str(count) + " = " + i)
        #print(cal_h)
        print(f"P(h1 | Q) = {cal_h[0]}")
        print(f"P(h2 | Q) = {cal_h[1]}")
        print(f"P(h3 | Q) = {cal_h[2]}")
        print(f"P(h4 | Q) = {cal_h[3]}")
        print(f"P(h5 | Q) = {cal_h[4]}")
        q_is_l, q_is_c = cal_prob_after_obs(cal_h, q_l_h)
        #print(q_is_c, q_is_l)
        print(f"Probability that the next candy we pick will be C, given Q: {q_is_c}")
        print(f"Probability that the next candy we pick will be L, given Q: {q_is_l}")
        print("")
    count += 1