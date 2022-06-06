- Author: Pratik Antoni Patekar
- About: This is a Python 3 script implementing minimax algorithm with alpha beta pruning for playing max connect 4 game. 
- References: 
	1. Basic script structure written by Chris Conly which is based on C++ code provided by Dr. Vassilis Athitsos.
	2. Lecture material of Artificial Intelligence 1 course by Prof. Vamsikrishna Gopiskrishna
- Python version used to write code: 3.9.7
- Command line commands to be used:
	1. One move mode: python one-move [input_filename] [output_filename] [depth] 
		example: python maxconnect4.py one-move input2.txt output2.txt 5 
	2. Interactive mode: python interactive [input_filename] [computer-next/ human-next] [depth]
		example: python maxconnect4.py interactive input2.txt computer-next 5

- Description:

The python file 'maxconnect4.py' implements minimax algorithm using alpha beta pruning depending upon the values such as depth 
provided in the input command. The basic operation of aiPlay() function is as follows:
	1. aiPlay() function calls the function game_minimax() which returns the column number to be played by ai using minimax algorithm.
	2. In game_minimax() function performs two things. First is creation of tree with calculated eval scores and second is perform 
	alpha beta pruning.
	3. The first part from above is performed using function create_child() function [to create tree] and get_leaf_values() function 
	to calculate evaluation scores for all possible boards after (depth-1) moves.
	4. The second part is performed using AlphaBetaDecision() function which performs alpha beta pruning by recursive call to MaxValue()
	and MinValue() function. These functions: AlphaBetaDecision(), MaxValue() and MinValue() are loosly based on the function descriptions
	given by Prof. Vamsikrishna during the lecture.
	5. The AlphaBetaDecision() function determines the action i.e. column number to be played next and returns it to the game_minimax()
In interactive mode, the program also asks for your player name in input so that it can print whose turn is going on currently.

- Evaluation function:

The evaluation function used here is computationally expensive but it is better at determining the next move compared to other functions that I used. 
The eval function is implemented as eval_func(). 

This eval_func() performs 3 operations:
	1. It creates dummy gameboard and replaces current player pieces with 1, zeros with 0 and opponent pieces with -1.
	2. It then applies multiple masks (around 70 masks in gen_masks() func) to dummy gameboard and sums up the resultant scores for each mask applied gameboard. 
	Each mask checks if the current player can get a score at that a particular set of 4 positions.
	3. After applying all masks, it also checks who is winning at that particular gameboard config using eval_func2() which just finds score
	of current player minus score of the opponent and our main eval func adds it to final score as well.

More information about mask application to gameboard is present in sheet 2 of excel file containing time required for different depth values.

- Observation: The above eval_func() performs better even at blocking opponents pieces. For example: If the opponent is having 3 pieces in
a row and after AI's move opponent can score. Then this eval function detects that as well and blocks that accordingly provided that AI is
not having any other better move or score.