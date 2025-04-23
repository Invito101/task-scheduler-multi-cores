from processor import MIPSCore
from scheduler import (
	round_robin_scheduler,
	shortest_first_scheduler,
	longest_first_scheduler
)
from simulation import simulate
from program_loader import load_programs
import copy

import os

if __name__ == "__main__":
	os.makedirs("results", exist_ok=True)
	# Load the original programs from the directory
	original_programs = load_programs("programs")

	# Create a list of schedulers to test
	schedulers = [
		("round_robin", round_robin_scheduler),
		("shortest_first", shortest_first_scheduler),
		("longest_first", longest_first_scheduler),
	]

	# Iterate through each scheduler and simulate the execution of the programs
	for name, scheduler in schedulers:
		programs = copy.deepcopy(original_programs)
		assignments = scheduler(programs, num_cores=4)
		with open(f"results/{name}.md", "w") as f:
			f.write(f"# Scheduling With {name} Scheduler\n")
			simulate(assignments, output=f)
