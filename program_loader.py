import os
# This function loads programs from a specified directory.
def load_programs(directory="programs"):
	programs = []
	for filename in sorted(os.listdir(directory)):
		if filename.endswith(".txt"):
			with open(os.path.join(directory, filename)) as f:
				instructions = [line.strip() for line in f if line.strip()]
				programs.append((filename, instructions))
	return programs