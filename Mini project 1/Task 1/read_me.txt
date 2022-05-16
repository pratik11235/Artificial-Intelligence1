- Author: Pratik Antoni Patekar
- About: This is a Python 3 script that performs uninformed and informed state space search on the graph provided in text file.
- References: Lecture material of Artificial Intelligence 1 course by Prof. Vamsikrishna Gopiskrishna
- Python version used to write code: 3.9.7
- Command line commands to be used:
	1. One move mode: python find_route.py [input_textfile] [source_city] [destination_city]
		example: python find_route.py input1.txt Bremen Kassel
	2. Interactive mode: python find_route.py [input_textfile] [source_city] [destination_city] [heuristics_textfile]
		example: python find_route.py input1.txt Bremen Kassel h_kassel.txt

- Description:

The python file 'find_route.py' performs uninformed (UCS) and informed (A star) state space search on the graph provided in input_textfile. 
For informed search, it uses additional file heursitics_textfile which provides heuristics to perform the search.
Following is the basic operation of the code.

Mode 1: Uninformed search:
After executing the command as mentioned above it will ask whether you want to print fringe and closed list after every node 
is popped from the list. If you enter 1 then it will print fringe and closed otherwise it will just print the nodes that are popped.
Next it will perform the UCS using graph search. Depending upon whether a path exists between entered source and destination, the code 
will display the minimum cost path between them or print that no path exists between them.

Mode 2: Informed search:
Works exactly like uninformed search but using heuristics file as well. f(n) = g(n) + h(n)

NOTE: Here (in both modes above) before adding nodes to fringe, program checks whether it is already in closed (in order to save memory). 
If already in closed then it wont be added in fringe itself.

