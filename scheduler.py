#Round Robin Scheduler
def round_robin_scheduler(programs, num_cores):
	assignments = [[] for _ in range(num_cores)]
	# Distribute programs to cores in a round-robin fashion
	for i, (name, instrs) in enumerate(programs):
		assignments[i % num_cores].append((name, instrs))
	return assignments

# Shortest First Scheduler
def shortest_first_scheduler(programs, num_cores):

	# Sort programs by length in ascending order
	sorted_programs = sorted(programs, key=lambda p: len(p[1]))
	
	# Initialize the core programs and their lengths
	core_programs = [[] for _ in range(num_cores)]
	core_lengths = [0] * num_cores

	# Distribute programs to cores based on their lengths
	for prog in sorted_programs:
		min_core_index = core_lengths.index(min(core_lengths))
		core_programs[min_core_index].append(prog)
		core_lengths[min_core_index] += len(prog[1])

	return core_programs

# Longest First Scheduler
def longest_first_scheduler(programs, num_cores):

	# Sort programs by length in descending order
	sorted_programs = sorted(programs, key=lambda p: -len(p[1]))
	core_programs = [[] for _ in range(num_cores)]
	core_lengths = [0] * num_cores

	# Distribute programs to cores based on their lengths
	for prog in sorted_programs:
		min_core_index = core_lengths.index(min(core_lengths))
		core_programs[min_core_index].append(prog)
		core_lengths[min_core_index] += len(prog[1])

	return core_programs


