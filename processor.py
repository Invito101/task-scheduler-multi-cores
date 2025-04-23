LATENCY_TABLE = {
	"ADD": 1,
	"SUB": 1,
	"MUL": 1,
	"DIV": 1,
	"LOAD": 1,
	"STORE": 1,
	"NOP": 1,
	"BEQ": 1,
}

class MIPSCore:
	def __init__(self, core_id):
		self.core_id = core_id
		self.instructions = []
		self.pc = 0
		self.cycles = 0
		self.current_latency = 0
		self.label_map = {}


	# Load a program into the core
	def load_program(self, program_name, instructions):
		self.instructions.extend([(program_name, instr) for instr in instructions])

		# Create a label map for branch instructions
		for i, (_, instr) in enumerate(self.instructions):
			if ':' in instr:
				label = instr.split(':')[0].strip()
				self.label_map[label] = i

	# Reset the core state
	def step(self, output=None):
		if output is None:
			import sys
			output = sys.stdout

		if self.pc >= len(self.instructions):
			if self.current_latency > 0:
				self.current_latency -= 1
				self.cycles += 1
				return True
			return False

		if self.current_latency > 0:
			self.current_latency -= 1
			self.cycles += 1
			return True

		# Fetch the instruction
		program_name, instr = self.instructions[self.pc]
		op = instr.split()[0].replace(":", "")
		latency = LATENCY_TABLE.get(op, 1)
		self.current_latency = latency - 1
		self.cycles += 1

		# Print the instruction being executed
		print(f"Core {self.core_id} ({'+ '.join(set(p for p, _ in self.instructions))}): {program_name} :Executing '{instr}'\n", file=output)
		print(f"Core {self.core_id}: PC = {self.pc}, Latency = {self.current_latency}, Cycles = {self.cycles}\n", file=output)

		# Handle branch instructions
		if op == "BEQ":
			parts = instr.replace(",", "").split()
			label = parts[-1]
			if label in self.label_map:
				self.pc = self.label_map[label]
				return True

		self.pc += 1
		return True

	# Check if the program is done
	def is_done(self):
		return self.pc >= len(self.instructions) and self.current_latency == 0