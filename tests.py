'''
    Team 4 - Ben Duggan & Connor Altic
    12/9/18
    Script used to test different AIs and output there data
'''

import time, csv
from Cube import *
from AIs import *
from Heuristic import *

# Test BFS
def BFS_Test(n, scramble_length, tests, outputs, output_name, time_out):
	print('Testing BFS: n=' + str(n) + ', scramble_length: ' + str(scramble_length) + ', tests: ' + str(tests))

	results = [['Trial', 'scrambleLength', 'scramblePattern', 'scrambleHash', 'obviousSolution', 'correct', 'solvedTime(sec)', 'aiPath']]

	for i in range(tests):
		c = Cube(n)
		scramble_pattern = c.trueScramble(scramble_length)
		scramble_hash = c.__hash__()
		obvious_solution = Cube.obviousSolution(scramble_pattern)
		ai = BFS(c)
		start_time = time.time()
		try:
			ai_path = ai.solve(time_out)

			# Run didn't time out!
			run_time = time.time() - start_time
			correct = ai_path[-1][1].isSolved()
			print(ai_path[-1][1].state)
			better_ai_path = []
			for j in ai_path:
				better_ai_path.append((j[0], j[1].state, j[1].__hash__()))
		except Exception as e:
			run_time = 'timed out (>' + str(time_out) + ' secs)'
			better_ai_path = []
			correct = False
			print('Timed out')
		

		print('\tTrial ' + str(i+1) + ': scramble_length: ' + str(scramble_length) + '; scramble_pattern: ' + str(scramble_pattern) + '; correct: ' + str(correct) + '; solved time: ' + str(run_time) + ' sec; ai_length: ' + str(len(better_ai_path)) + '; ai_path: ' + str(better_ai_path))

		results.append([i+1, scramble_length, scramble_pattern, scramble_hash, obvious_solution, correct, run_time, better_ai_path])

	if 'csv' in outputs:
		file = open(output_name+'.csv', 'w', newline='')  
		with file:  
		   writer = csv.writer(file)
		   writer.writerows(results)

# Test better BFS
def Better_BFS_Test(n, scramble_length, tests, outputs, output_name, time_out):
	print('Testing BBFS: n=' + str(n) + ', scramble_length: ' + str(scramble_length) + ', tests: ' + str(tests))

	results = [['Trial', 'scrambleLength', 'scramblePattern', 'scrambleHash', 'obviousSolution', 'correct', 'solvedTime(sec)', 'aiPath']]

	for i in range(tests):
		c = Cube(n)
		scramble_pattern = c.trueScramble(scramble_length)
		scramble_hash = c.__hash__()
		obvious_solution = Cube.obviousSolution(scramble_pattern)
		ai = Better_BFS(c)
		start_time = time.time()
		try:
			ai_path = ai.solve(time_out)

			# Run didn't time out!
			run_time = time.time() - start_time
			correct = ai_path[-1][1].isSolved()
			better_ai_path = []
			for j in ai_path:
				better_ai_path.append((j[0], j[1].state, j[1].__hash__()))
		except Exception as e:
			run_time = 'timed out (>' + str(time_out) + ' secs)'
			better_ai_path = []
			correct = False
			print('Timed out')
		
		print('\tTrial ' + str(i+1) + ': scramble_length: ' + str(scramble_length) + '; scramble_pattern: ' + str(scramble_pattern) + '; correct: ' + str(correct) + '; solved time: ' + str(run_time) + ' sec; ai_length: ' + str(len(better_ai_path)) + '; ai_path: ' + str(better_ai_path))

		results.append([i+1, scramble_length, scramble_pattern, scramble_hash, obvious_solution, correct, run_time, better_ai_path])

	if 'csv' in outputs:
		file = open(output_name+'.csv', 'w', newline='')  
		with file:  
		   writer = csv.writer(file)
		   writer.writerows(results)

# Test A*
def A_star_Test(n, scramble_length, tests, outputs, output_name, time_out, heuristic):
	print('Testing A*: n=' + str(n) + ', scramble_length: ' + str(scramble_length) + ', tests: ' + str(tests))

	results = [['Trial', 'scrambleLength', 'scramblePattern', 'scrambleHash', 'obviousSolution', 'correct', 'solvedTime(sec)', 'aiPath']]

	for i in range(tests):
		c = Cube(n)
		scramble_pattern = c.trueScramble(scramble_length)
		scramble_hash = c.__hash__()
		obvious_solution = Cube.obviousSolution(scramble_pattern)
		ai = A_Star(c, heuristic)
		start_time = time.time()
		try:
			ai_path = ai.solve(time_out)

			# Run didn't time out!
			run_time = time.time() - start_time
			correct = ai_path[-1][1].isSolved()
			better_ai_path = []
			for j in ai_path:
				better_ai_path.append((j[0], j[1].state, j[1].__hash__()))
		except Exception as e:
			run_time = 'timed out (>' + str(time_out) + ' secs)'
			better_ai_path = []
			correct = False
			print('Timed out')
		
		print('\tTrial ' + str(i+1) + ': scramble_length: ' + str(scramble_length) + '; scramble_pattern: ' + str(scramble_pattern) + '; correct: ' + str(correct) + '; solved time: ' + str(run_time) + ' sec; ai_length: ' + str(len(better_ai_path)) + '; ai_path: ' + str(better_ai_path))

		results.append([i+1, scramble_length, scramble_pattern, scramble_hash, obvious_solution, correct, run_time, better_ai_path])

	if 'csv' in outputs:
		file = open(output_name+'.csv', 'w', newline='')  
		with file:  
		   writer = csv.writer(file)
		   writer.writerows(results)

# Test IDA*
def IDA_star_Test(n, scramble_length, tests, outputs, output_name, time_out, heuristic):
	print('Testing IDA*: n=' + str(n) + ', scramble_length: ' + str(scramble_length) + ', tests: ' + str(tests))

	results = [['Trial', 'scrambleLength', 'scramblePattern', 'scrambleHash', 'obviousSolution', 'correct', 'solvedTime(sec)', 'aiPath']]

	for i in range(tests):
		c = Cube(n)
		scramble_pattern = c.trueScramble(scramble_length)
		scramble_hash = c.__hash__()
		obvious_solution = Cube.obviousSolution(scramble_pattern)
		ai = IDA_Star(c, heuristic)
		start_time = time.time()
		try:
			ai_path = ai.solve(time_out)

			print(ai_path)

			# Run didn't time out!
			run_time = time.time() - start_time
			correct = ai_path[-1][1].isSolved()
			better_ai_path = []
			for j in ai_path:
				better_ai_path.append((j[0], j[1].state, j[1].__hash__()))
		except Exception as e:
			run_time = 'timed out (>' + str(time_out) + ' secs)'
			better_ai_path = []
			correct = False
			print('Timed out')
		
		print('\tTrial ' + str(i+1) + ': scramble_length: ' + str(scramble_length) + '; scramble_pattern: ' + str(scramble_pattern) + '; correct: ' + str(correct) + '; solved time: ' + str(run_time) + ' sec; ai_length: ' + str(len(better_ai_path)) + '; ai_path: ' + str(better_ai_path))

		results.append([i+1, scramble_length, scramble_pattern, scramble_hash, obvious_solution, correct, run_time, better_ai_path])

	if 'csv' in outputs:
		file = open(output_name+'.csv', 'w', newline='')  
		with file:  
		   writer = csv.writer(file)
		   writer.writerows(results)

# Test Mini
def Mini_Test(n, scramble_length, tests, outputs, output_name, time_out, heuristic, depth):
	print('Testing Mini: n=' + str(n) + ', scramble_length: ' + str(scramble_length) + ', tests: ' + str(tests))

	results = [['Trial', 'scrambleLength', 'scramblePattern', 'scrambleHash', 'obviousSolution', 'correct', 'solvedTime(sec)', 'aiPath']]

	for i in range(tests):
		c = Cube(n)
		scramble_pattern = c.trueScramble(scramble_length)
		scramble_hash = c.__hash__()
		obvious_solution = Cube.obviousSolution(scramble_pattern)
		ai = Mini(c, heuristic)
		start_time = time.time()
		try:
			ai_path = ai.solve(depth, time_out)

			# Run didn't time out!
			run_time = time.time() - start_time
			correct = ai_path[-1][1].isSolved()
			better_ai_path = []
			for j in ai_path:
				better_ai_path.append((j[0], j[1].state, j[1].__hash__()))
		except Exception as e:
			run_time = 'timed out (>' + str(time_out) + ' secs)'
			better_ai_path = []
			correct = False
			print('Timed out')
		
		print('\tTrial ' + str(i+1) + ': scramble_length: ' + str(scramble_length) + '; scramble_pattern: ' + str(scramble_pattern) + '; correct: ' + str(correct) + '; solved time: ' + str(run_time) + ' sec; ai_length: ' + str(len(better_ai_path)) + '; ai_path: ' + str(better_ai_path))

		results.append([i+1, scramble_length, scramble_pattern, scramble_hash, obvious_solution, correct, run_time, better_ai_path])

	if 'csv' in outputs:
		file = open(output_name+'.csv', 'w', newline='')  
		with file:  
		   writer = csv.writer(file)
		   writer.writerows(results)


if __name__ == '__main__':
	tests = ['bfs', 'bbfs', 'a*', 'ida*', 'mini'] # Which tests do you want to perform
	n = 2 # Cube size
	start_scramble = 0 # Starting scramble 
	end_scramble = 14 # Ending scramble
	num_tests = 5 # How many tests to run
	output_types = ['csv'] # Output types (csv only option)
	output_name = 'test1' # Name of the output file
	start_depth = 1 # Mini start depth
	end_depth = 5 # Mini end depth

	if 'bfs' in tests:
		print('BFS tests')
		for i in range(start_scramble, end_scramble+1):
			BFS_Test(n, i, num_tests, output_types, 'tests/BFS/'+str(n)+'x'+str(n)+'_scramble('+str(i)+')_'+output_name, 10*60)

	if 'bbfs' in tests:
		print('BBFS tests')
		for i in range(start_scramble, end_scramble+1):
			Better_BFS_Test(n, i, num_tests, output_types, 'tests/BBFS/'+str(n)+'x'+str(n)+'_scramble('+str(i)+')_'+output_name, 5*60)

	if 'a*' in tests:
		print('A* tests')
		for i in range(start_scramble, end_scramble+1):
			A_star_Test(n, i, num_tests, output_types, 'tests/A_Star/'+str(n)+'x'+str(n)+'_scramble('+str(i)+')_'+output_name, 5*60, Heuristic.hammingDistance)

	if 'ida*' in tests:
		print('IDA* tests')
		for i in range(start_scramble, end_scramble+1):
			IDA_star_Test(n, i, num_tests, output_types, 'tests/IDA_Star/'+str(n)+'x'+str(n)+'_scramble('+str(i)+')_'+output_name, 10*60, Heuristic.manhattanDistance)

	if 'mini' in tests:
		print('Mini tests')
		for i in range(start_scramble, end_scramble+1):
			for j in range(start_depth, end_depth+1):
				Mini_Test(n, i, num_tests, output_types, 'tests/Mini/'+str(n)+'x'+str(n)+'_scramble('+str(i)+')_depth('+str(j)+')_'+output_name, 10*60, Heuristic.manhattanDistance, j)