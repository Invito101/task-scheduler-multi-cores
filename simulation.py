from processor import MIPSCore

#Function to simulate the execution of MIPS programs on multiple cores
def simulate(assignments, output=None):
    if output is None:
        import sys
        output = sys.stdout

    num_cores = len(assignments)
    cores = [MIPSCore(i) for i in range(num_cores)]

    # Load programs into the cores
    for i, prog_list in enumerate(assignments):
        for prog_name, instrs in prog_list:
            cores[i].load_program(prog_name, instrs)

    clock = 0
    # Main simulation loop
    while not all(core.is_done() for core in cores):
        for core in cores:
            if not core.is_done():
                core.step(output=output)
        clock += 1

    # Print the final state of each core in the output file
    print(f"\nTotal simulation time: {clock} clock cycles", file=output)
    for core in cores:
        names = '+ '.join(set(p for p, _ in core.instructions))
        print(f"Core {core.core_id} ({names}): {core.cycles} cycles", file=output)

