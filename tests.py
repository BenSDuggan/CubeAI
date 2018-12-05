'''
    Team 4 - Ben Duggan & Connor Altic
    12/5/18
    Script used to test different AIs and output there data
'''

import time, csv
from Cube import *
from AIs import *

def BFS_Test(n, scramble_length, tests, outputs, output_name):
	print('Testing BFS:')

	results = [['Trial#', 'scramble_length', 'scramble_pattern', 'correct', 'solved_time(sec)', 'ai_path']]

	for i in range(tests):
		c = Cube(n)
		scramble_pattern = c.scramble(scramble_length)
		scramble_hash = c.__hash__()
		ai = BFS(c)
		start_time = time.time()
		ai_path = ai.solve()
		end_time = time.time()
		correct = ai_path[-1][1].isSolved()

		better_ai_path = []
		for j in ai_path:
			better_ai_path.append((j[0], j[1].state))

		print('\tTrial ' + str(i+1) + ': scramble_length: ' + str(scramble_length) + '; scramble_pattern: ' + str(scramble_pattern) + '; correct: ' + str(correct) + '; solved time: ' + str(end_time-start_time) + ' sec; ai_path: ' + str(better_ai_path))

		results.append([i+1, scramble_length, scramble_pattern, correct, end_time-start_time, better_ai_path])

	if 'latex' in outputs:
		pass

	if 'csv' in outputs:
		file = open(output_name+'.csv', 'w', newline='')  
		with file:  
		   writer = csv.writer(file)
		   writer.writerows(results)


if __name__ == '__main__':
	n = 2
	scramble_length = 2
	tests = 2
	outputs = ['latex', 'csv']
	output_name = 'tests/BFS/test'

	BFS_Test(n, scramble_length, tests, outputs, output_name)