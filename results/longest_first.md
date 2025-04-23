# Scheduling With longest_first Scheduler
Core 0 (100.txt): 100.txt :Executing 'add $t0, $zero, $zero'

Core 0: PC = 0, Latency = 0, Cycles = 1

Core 1 (3.txt+ 25.txt+ 10.txt): 25.txt :Executing 'MUL R1, R2, R3'

Core 1: PC = 0, Latency = 0, Cycles = 1

Core 2 (1.txt+ 20.txt+ 12.txt+ 5.txt): 20.txt :Executing 'ADD R1, R1, R1'

Core 2: PC = 0, Latency = 0, Cycles = 1

Core 3 (15.txt+ 17.txt+ 8.txt): 17.txt :Executing 'LOAD R1, 0(R2)'

Core 3: PC = 0, Latency = 2, Cycles = 1

Core 0 (100.txt): 100.txt :Executing 'add $t1, $zero, $zero'

Core 0: PC = 1, Latency = 0, Cycles = 2

Core 1 (3.txt+ 25.txt+ 10.txt): 25.txt :Executing 'DIV R4, R5, R6'

Core 1: PC = 1, Latency = 1, Cycles = 2

Core 2 (1.txt+ 20.txt+ 12.txt+ 5.txt): 20.txt :Executing 'SUB R2, R2, R2'

Core 2: PC = 1, Latency = 0, Cycles = 2

Core 0 (100.txt): 100.txt :Executing 'add $t2, $zero, $zero'

Core 0: PC = 2, Latency = 0, Cycles = 3

Core 2 (1.txt+ 20.txt+ 12.txt+ 5.txt): 20.txt :Executing 'MUL R3, R3, R3'

Core 2: PC = 2, Latency = 0, Cycles = 3

Core 0 (100.txt): 100.txt :Executing 'add $t3, $zero, $zero'

Core 0: PC = 3, Latency = 0, Cycles = 4

Core 1 (3.txt+ 25.txt+ 10.txt): 25.txt :Executing 'ADD R7, R8, R9'

Core 1: PC = 2, Latency = 0, Cycles = 4

Core 2 (1.txt+ 20.txt+ 12.txt+ 5.txt): 20.txt :Executing 'DIV R4, R4, R4'

Core 2: PC = 3, Latency = 1, Cycles = 4

Core 3 (15.txt+ 17.txt+ 8.txt): 17.txt :Executing 'STORE R1, 4(R3)'

Core 3: PC = 1, Latency = 2, Cycles = 4

Core 0 (100.txt): 100.txt :Executing 'add $t4, $zero, $zero'

Core 0: PC = 4, Latency = 0, Cycles = 5

Core 1 (3.txt+ 25.txt+ 10.txt): 25.txt :Executing 'SUB R1, R2, R3'

Core 1: PC = 3, Latency = 0, Cycles = 5

Core 0 (100.txt): 100.txt :Executing 'add $t5, $zero, $zero'

Core 0: PC = 5, Latency = 0, Cycles = 6

Core 1 (3.txt+ 25.txt+ 10.txt): 25.txt :Executing 'MUL R4, R5, R6'

Core 1: PC = 4, Latency = 0, Cycles = 6

Core 2 (1.txt+ 20.txt+ 12.txt+ 5.txt): 20.txt :Executing 'ADD R5, R5, R5'

Core 2: PC = 4, Latency = 0, Cycles = 6

Core 0 (100.txt): 100.txt :Executing 'add $t6, $zero, $zero'

Core 0: PC = 6, Latency = 0, Cycles = 7

Core 1 (3.txt+ 25.txt+ 10.txt): 25.txt :Executing 'DIV R7, R8, R9'

Core 1: PC = 5, Latency = 1, Cycles = 7

Core 2 (1.txt+ 20.txt+ 12.txt+ 5.txt): 20.txt :Executing 'SUB R6, R6, R6'

Core 2: PC = 5, Latency = 0, Cycles = 7

Core 3 (15.txt+ 17.txt+ 8.txt): 17.txt :Executing 'LOAD R4, 8(R5)'

Core 3: PC = 2, Latency = 2, Cycles = 7

Core 0 (100.txt): 100.txt :Executing 'add $t7, $zero, $zero'

Core 0: PC = 7, Latency = 0, Cycles = 8

Core 2 (1.txt+ 20.txt+ 12.txt+ 5.txt): 20.txt :Executing 'MUL R7, R7, R7'

Core 2: PC = 6, Latency = 0, Cycles = 8

Core 0 (100.txt): 100.txt :Executing 'add $t8, $zero, $zero'

Core 0: PC = 8, Latency = 0, Cycles = 9

Core 1 (3.txt+ 25.txt+ 10.txt): 25.txt :Executing 'ADD R1, R2, R3'

Core 1: PC = 6, Latency = 0, Cycles = 9

Core 2 (1.txt+ 20.txt+ 12.txt+ 5.txt): 20.txt :Executing 'DIV R8, R8, R8'

Core 2: PC = 7, Latency = 1, Cycles = 9

Core 0 (100.txt): 100.txt :Executing 'add $t9, $zero, $zero'

Core 0: PC = 9, Latency = 0, Cycles = 10

Core 1 (3.txt+ 25.txt+ 10.txt): 25.txt :Executing 'SUB R4, R5, R6'

Core 1: PC = 7, Latency = 0, Cycles = 10

Core 3 (15.txt+ 17.txt+ 8.txt): 17.txt :Executing 'STORE R6, 12(R7)'

Core 3: PC = 3, Latency = 2, Cycles = 10

Core 0 (100.txt): 100.txt :Executing 'add $s0, $zero, $zero'

Core 0: PC = 10, Latency = 0, Cycles = 11

Core 1 (3.txt+ 25.txt+ 10.txt): 25.txt :Executing 'MUL R7, R8, R9'

Core 1: PC = 8, Latency = 0, Cycles = 11

Core 2 (1.txt+ 20.txt+ 12.txt+ 5.txt): 20.txt :Executing 'ADD R9, R9, R9'

Core 2: PC = 8, Latency = 0, Cycles = 11

Core 0 (100.txt): 100.txt :Executing 'add $s1, $zero, $zero'

Core 0: PC = 11, Latency = 0, Cycles = 12

Core 1 (3.txt+ 25.txt+ 10.txt): 25.txt :Executing 'DIV R1, R2, R3'

Core 1: PC = 9, Latency = 1, Cycles = 12

Core 2 (1.txt+ 20.txt+ 12.txt+ 5.txt): 20.txt :Executing 'SUB R0, R0, R0'

Core 2: PC = 9, Latency = 0, Cycles = 12

Core 0 (100.txt): 100.txt :Executing 'add $s2, $zero, $zero'

Core 0: PC = 12, Latency = 0, Cycles = 13

Core 2 (1.txt+ 20.txt+ 12.txt+ 5.txt): 20.txt :Executing 'LOAD R1, 0(R1)'

Core 2: PC = 10, Latency = 2, Cycles = 13

Core 3 (15.txt+ 17.txt+ 8.txt): 17.txt :Executing 'LOAD R8, 16(R9)'

Core 3: PC = 4, Latency = 2, Cycles = 13

Core 0 (100.txt): 100.txt :Executing 'add $s3, $zero, $zero'

Core 0: PC = 13, Latency = 0, Cycles = 14

Core 1 (3.txt+ 25.txt+ 10.txt): 25.txt :Executing 'ADD R4, R5, R6'

Core 1: PC = 10, Latency = 0, Cycles = 14

Core 0 (100.txt): 100.txt :Executing 'add $s4, $zero, $zero'

Core 0: PC = 14, Latency = 0, Cycles = 15

Core 1 (3.txt+ 25.txt+ 10.txt): 25.txt :Executing 'SUB R7, R8, R9'

Core 1: PC = 11, Latency = 0, Cycles = 15

Core 0 (100.txt): 100.txt :Executing 'add $s5, $zero, $zero'

Core 0: PC = 15, Latency = 0, Cycles = 16

Core 1 (3.txt+ 25.txt+ 10.txt): 25.txt :Executing 'NOP'

Core 1: PC = 12, Latency = 0, Cycles = 16

Core 2 (1.txt+ 20.txt+ 12.txt+ 5.txt): 20.txt :Executing 'STORE R2, 4(R2)'

Core 2: PC = 11, Latency = 2, Cycles = 16

Core 3 (15.txt+ 17.txt+ 8.txt): 17.txt :Executing 'NOP'

Core 3: PC = 5, Latency = 0, Cycles = 16

Core 0 (100.txt): 100.txt :Executing 'add $s6, $zero, $zero'

Core 0: PC = 16, Latency = 0, Cycles = 17

Core 1 (3.txt+ 25.txt+ 10.txt): 25.txt :Executing 'NOP'

Core 1: PC = 13, Latency = 0, Cycles = 17

Core 3 (15.txt+ 17.txt+ 8.txt): 17.txt :Executing 'LOAD R1, 20(R2)'

Core 3: PC = 6, Latency = 2, Cycles = 17

Core 0 (100.txt): 100.txt :Executing 'add $s7, $zero, $zero'

Core 0: PC = 17, Latency = 0, Cycles = 18

Core 1 (3.txt+ 25.txt+ 10.txt): 25.txt :Executing 'NOP'

Core 1: PC = 14, Latency = 0, Cycles = 18

Core 0 (100.txt): 100.txt :Executing 'add $a0, $zero, $zero'

Core 0: PC = 18, Latency = 0, Cycles = 19

Core 1 (3.txt+ 25.txt+ 10.txt): 25.txt :Executing 'LOAD R1, 0(R2)'

Core 1: PC = 15, Latency = 2, Cycles = 19

Core 2 (1.txt+ 20.txt+ 12.txt+ 5.txt): 20.txt :Executing 'NOP'

Core 2: PC = 12, Latency = 0, Cycles = 19

Core 0 (100.txt): 100.txt :Executing 'add $a1, $zero, $zero'

Core 0: PC = 19, Latency = 0, Cycles = 20

Core 2 (1.txt+ 20.txt+ 12.txt+ 5.txt): 20.txt :Executing 'NOP'

Core 2: PC = 13, Latency = 0, Cycles = 20

Core 3 (15.txt+ 17.txt+ 8.txt): 17.txt :Executing 'STORE R1, 24(R3)'

Core 3: PC = 7, Latency = 2, Cycles = 20

Core 0 (100.txt): 100.txt :Executing 'add $a2, $zero, $zero'

Core 0: PC = 20, Latency = 0, Cycles = 21

Core 2 (1.txt+ 20.txt+ 12.txt+ 5.txt): 20.txt :Executing 'NOP'

Core 2: PC = 14, Latency = 0, Cycles = 21

Core 0 (100.txt): 100.txt :Executing 'add $a3, $zero, $zero'

Core 0: PC = 21, Latency = 0, Cycles = 22

Core 1 (3.txt+ 25.txt+ 10.txt): 25.txt :Executing 'STORE R3, 4(R4)'

Core 1: PC = 16, Latency = 2, Cycles = 22

Core 2 (1.txt+ 20.txt+ 12.txt+ 5.txt): 20.txt :Executing 'NOP'

Core 2: PC = 15, Latency = 0, Cycles = 22

Core 0 (100.txt): 100.txt :Executing 'add $v0, $zero, $zero'

Core 0: PC = 22, Latency = 0, Cycles = 23

Core 2 (1.txt+ 20.txt+ 12.txt+ 5.txt): 20.txt :Executing 'NOP'

Core 2: PC = 16, Latency = 0, Cycles = 23

Core 3 (15.txt+ 17.txt+ 8.txt): 17.txt :Executing 'LOAD R4, 28(R5)'

Core 3: PC = 8, Latency = 2, Cycles = 23

Core 0 (100.txt): 100.txt :Executing 'add $v1, $zero, $zero'

Core 0: PC = 23, Latency = 0, Cycles = 24

Core 2 (1.txt+ 20.txt+ 12.txt+ 5.txt): 20.txt :Executing 'ADD R3, R3, R3'

Core 2: PC = 17, Latency = 0, Cycles = 24

Core 0 (100.txt): 100.txt :Executing 'add $t1, $t1, $t0'

Core 0: PC = 24, Latency = 0, Cycles = 25

Core 1 (3.txt+ 25.txt+ 10.txt): 25.txt :Executing 'LOAD R5, 8(R6)'

Core 1: PC = 17, Latency = 2, Cycles = 25

Core 2 (1.txt+ 20.txt+ 12.txt+ 5.txt): 20.txt :Executing 'DIV R4, R4, R4'

Core 2: PC = 18, Latency = 1, Cycles = 25

Core 0 (100.txt): 100.txt :Executing 'add $t0, $t0, $t1'

Core 0: PC = 25, Latency = 0, Cycles = 26

Core 3 (15.txt+ 17.txt+ 8.txt): 17.txt :Executing 'STORE R6, 32(R7)'

Core 3: PC = 9, Latency = 2, Cycles = 26

Core 0 (100.txt): 100.txt :Executing 'sub $t2, $t0, $t1'

Core 0: PC = 26, Latency = 0, Cycles = 27

Core 2 (1.txt+ 20.txt+ 12.txt+ 5.txt): 20.txt :Executing 'NOP'

Core 2: PC = 19, Latency = 0, Cycles = 27

Core 0 (100.txt): 100.txt :Executing 'mul $t3, $t0, $t1'

Core 0: PC = 27, Latency = 0, Cycles = 28

Core 1 (3.txt+ 25.txt+ 10.txt): 25.txt :Executing 'STORE R7, 12(R8)'

Core 1: PC = 18, Latency = 2, Cycles = 28

Core 2 (1.txt+ 20.txt+ 12.txt+ 5.txt): 12.txt :Executing 'MUL R1, R2, R3'

Core 2: PC = 20, Latency = 0, Cycles = 28

Core 0 (100.txt): 100.txt :Executing 'div $t3, $t1'

Core 0: PC = 28, Latency = 0, Cycles = 29

Core 2 (1.txt+ 20.txt+ 12.txt+ 5.txt): 12.txt :Executing 'DIV R4, R1, R2'

Core 2: PC = 21, Latency = 1, Cycles = 29

Core 3 (15.txt+ 17.txt+ 8.txt): 17.txt :Executing 'LOAD R8, 36(R9)'

Core 3: PC = 10, Latency = 2, Cycles = 29

Core 0 (100.txt): 100.txt :Executing 'beq $t0, $t1, equal'

Core 0: PC = 29, Latency = 0, Cycles = 30

Core 0 (100.txt): 100.txt :Executing 'add $s0, $t0, $t2'

Core 0: PC = 30, Latency = 0, Cycles = 31

Core 1 (3.txt+ 25.txt+ 10.txt): 25.txt :Executing 'NOP'

Core 1: PC = 19, Latency = 0, Cycles = 31

Core 2 (1.txt+ 20.txt+ 12.txt+ 5.txt): 12.txt :Executing 'ADD R5, R6, R7'

Core 2: PC = 22, Latency = 0, Cycles = 31

Core 0 (100.txt): 100.txt :Executing 'add $s1, $s0, $t1'

Core 0: PC = 31, Latency = 0, Cycles = 32

Core 1 (3.txt+ 25.txt+ 10.txt): 25.txt :Executing 'ADD R1, R1, R1'

Core 1: PC = 20, Latency = 0, Cycles = 32

Core 2 (1.txt+ 20.txt+ 12.txt+ 5.txt): 12.txt :Executing 'SUB R8, R9, R0'

Core 2: PC = 23, Latency = 0, Cycles = 32

Core 3 (15.txt+ 17.txt+ 8.txt): 17.txt :Executing 'NOP'

Core 3: PC = 11, Latency = 0, Cycles = 32

Core 0 (100.txt): 100.txt :Executing 'add $s2, $s1, $t1'

Core 0: PC = 32, Latency = 0, Cycles = 33

Core 1 (3.txt+ 25.txt+ 10.txt): 25.txt :Executing 'SUB R2, R2, R2'

Core 1: PC = 21, Latency = 0, Cycles = 33

Core 2 (1.txt+ 20.txt+ 12.txt+ 5.txt): 12.txt :Executing 'LOAD R2, 0(R3)'

Core 2: PC = 24, Latency = 2, Cycles = 33

Core 3 (15.txt+ 17.txt+ 8.txt): 17.txt :Executing 'NOP'

Core 3: PC = 12, Latency = 0, Cycles = 33

Core 0 (100.txt): 100.txt :Executing 'add $s3, $s2, $t2'

Core 0: PC = 33, Latency = 0, Cycles = 34

Core 1 (3.txt+ 25.txt+ 10.txt): 25.txt :Executing 'MUL R3, R3, R3'

Core 1: PC = 22, Latency = 0, Cycles = 34

Core 3 (15.txt+ 17.txt+ 8.txt): 17.txt :Executing 'NOP'

Core 3: PC = 13, Latency = 0, Cycles = 34

Core 0 (100.txt): 100.txt :Executing 'sub $s4, $s3, $t1'

Core 0: PC = 34, Latency = 0, Cycles = 35

Core 1 (3.txt+ 25.txt+ 10.txt): 25.txt :Executing 'DIV R4, R4, R4'

Core 1: PC = 23, Latency = 1, Cycles = 35

Core 3 (15.txt+ 17.txt+ 8.txt): 17.txt :Executing 'STORE R2, 40(R1)'

Core 3: PC = 14, Latency = 2, Cycles = 35

Core 0 (100.txt): 100.txt :Executing 'sub $s5, $s4, $t0'

Core 0: PC = 35, Latency = 0, Cycles = 36

Core 2 (1.txt+ 20.txt+ 12.txt+ 5.txt): 12.txt :Executing 'NOP'

Core 2: PC = 25, Latency = 0, Cycles = 36

Core 0 (100.txt): 100.txt :Executing 'mul $s6, $s5, $t1'

Core 0: PC = 36, Latency = 0, Cycles = 37

Core 1 (3.txt+ 25.txt+ 10.txt): 25.txt :Executing 'NOP'

Core 1: PC = 24, Latency = 0, Cycles = 37

Core 2 (1.txt+ 20.txt+ 12.txt+ 5.txt): 12.txt :Executing 'NOP'

Core 2: PC = 26, Latency = 0, Cycles = 37

Core 0 (100.txt): 100.txt :Executing 'div $s6, $t2'

Core 0: PC = 37, Latency = 0, Cycles = 38

Core 1 (3.txt+ 25.txt+ 10.txt): 10.txt :Executing 'ADD R1, R1, R1'

Core 1: PC = 25, Latency = 0, Cycles = 38

Core 2 (1.txt+ 20.txt+ 12.txt+ 5.txt): 12.txt :Executing 'STORE R3, 4(R4)'

Core 2: PC = 27, Latency = 2, Cycles = 38

Core 3 (15.txt+ 17.txt+ 8.txt): 17.txt :Executing 'LOAD R3, 44(R4)'

Core 3: PC = 15, Latency = 2, Cycles = 38

Core 0 (100.txt): 100.txt :Executing 'beq $s6, $t3, label1'

Core 0: PC = 38, Latency = 0, Cycles = 39

Core 1 (3.txt+ 25.txt+ 10.txt): 10.txt :Executing 'SUB R2, R2, R2'

Core 1: PC = 26, Latency = 0, Cycles = 39

Core 0 (100.txt): 100.txt :Executing 'equal:'

Core 0: PC = 39, Latency = 0, Cycles = 40

Core 1 (3.txt+ 25.txt+ 10.txt): 10.txt :Executing 'MUL R3, R3, R3'

Core 1: PC = 27, Latency = 0, Cycles = 40

Core 0 (100.txt): 100.txt :Executing 'add $a0, $zero, $t0'

Core 0: PC = 40, Latency = 0, Cycles = 41

Core 1 (3.txt+ 25.txt+ 10.txt): 10.txt :Executing 'DIV R4, R4, R4'

Core 1: PC = 28, Latency = 1, Cycles = 41

Core 2 (1.txt+ 20.txt+ 12.txt+ 5.txt): 12.txt :Executing 'MUL R5, R5, R5'

Core 2: PC = 28, Latency = 0, Cycles = 41

Core 3 (15.txt+ 17.txt+ 8.txt): 17.txt :Executing 'NOP'

Core 3: PC = 16, Latency = 0, Cycles = 41

Core 0 (100.txt): 100.txt :Executing 'add $a1, $a0, $t1'

Core 0: PC = 41, Latency = 0, Cycles = 42

Core 2 (1.txt+ 20.txt+ 12.txt+ 5.txt): 12.txt :Executing 'ADD R6, R6, R6'

Core 2: PC = 29, Latency = 0, Cycles = 42

Core 3 (15.txt+ 17.txt+ 8.txt): 15.txt :Executing 'MUL R1, R2, R3'

Core 3: PC = 17, Latency = 0, Cycles = 42

Core 0 (100.txt): 100.txt :Executing 'sub $a2, $a1, $t2'

Core 0: PC = 42, Latency = 0, Cycles = 43

Core 1 (3.txt+ 25.txt+ 10.txt): 10.txt :Executing 'LOAD R5, 0(R5)'

Core 1: PC = 29, Latency = 2, Cycles = 43

Core 2 (1.txt+ 20.txt+ 12.txt+ 5.txt): 12.txt :Executing 'DIV R7, R7, R7'

Core 2: PC = 30, Latency = 1, Cycles = 43

Core 3 (15.txt+ 17.txt+ 8.txt): 15.txt :Executing 'MUL R4, R1, R2'

Core 3: PC = 18, Latency = 0, Cycles = 43

Core 0 (100.txt): 100.txt :Executing 'mul $a3, $a2, $t3'

Core 0: PC = 43, Latency = 0, Cycles = 44

Core 3 (15.txt+ 17.txt+ 8.txt): 15.txt :Executing 'MUL R5, R4, R1'

Core 3: PC = 19, Latency = 0, Cycles = 44

Core 0 (100.txt): 100.txt :Executing 'div $a3, $t1'

Core 0: PC = 44, Latency = 0, Cycles = 45

Core 2 (1.txt+ 20.txt+ 12.txt+ 5.txt): 12.txt :Executing 'NOP'

Core 2: PC = 31, Latency = 0, Cycles = 45

Core 3 (15.txt+ 17.txt+ 8.txt): 15.txt :Executing 'DIV R6, R5, R2'

Core 3: PC = 20, Latency = 1, Cycles = 45

Core 0 (100.txt): 100.txt :Executing 'beq $a3, $zero, label2'

Core 0: PC = 45, Latency = 0, Cycles = 46

Core 1 (3.txt+ 25.txt+ 10.txt): 10.txt :Executing 'STORE R6, 8(R6)'

Core 1: PC = 30, Latency = 2, Cycles = 46

Core 2 (1.txt+ 20.txt+ 12.txt+ 5.txt): 5.txt :Executing 'MUL R1, R2, R3'

Core 2: PC = 32, Latency = 0, Cycles = 46

Core 0 (100.txt): 100.txt :Executing 'label1:'

Core 0: PC = 46, Latency = 0, Cycles = 47

Core 2 (1.txt+ 20.txt+ 12.txt+ 5.txt): 5.txt :Executing 'DIV R4, R1, R2'

Core 2: PC = 33, Latency = 1, Cycles = 47

Core 3 (15.txt+ 17.txt+ 8.txt): 15.txt :Executing 'DIV R7, R6, R1'

Core 3: PC = 21, Latency = 1, Cycles = 47

Core 0 (100.txt): 100.txt :Executing 'add $v0, $s0, $s1'

Core 0: PC = 47, Latency = 0, Cycles = 48

Core 0 (100.txt): 100.txt :Executing 'sub $v0, $v0, $s2'

Core 0: PC = 48, Latency = 0, Cycles = 49

Core 1 (3.txt+ 25.txt+ 10.txt): 10.txt :Executing 'NOP'

Core 1: PC = 31, Latency = 0, Cycles = 49

Core 2 (1.txt+ 20.txt+ 12.txt+ 5.txt): 5.txt :Executing 'NOP'

Core 2: PC = 34, Latency = 0, Cycles = 49

Core 3 (15.txt+ 17.txt+ 8.txt): 15.txt :Executing 'ADD R8, R8, R8'

Core 3: PC = 22, Latency = 0, Cycles = 49

Core 0 (100.txt): 100.txt :Executing 'mul $v0, $v0, $s3'

Core 0: PC = 49, Latency = 0, Cycles = 50

Core 1 (3.txt+ 25.txt+ 10.txt): 10.txt :Executing 'ADD R7, R8, R9'

Core 1: PC = 32, Latency = 0, Cycles = 50

Core 2 (1.txt+ 20.txt+ 12.txt+ 5.txt): 5.txt :Executing 'ADD R5, R5, R5'

Core 2: PC = 35, Latency = 0, Cycles = 50

Core 3 (15.txt+ 17.txt+ 8.txt): 15.txt :Executing 'SUB R9, R9, R9'

Core 3: PC = 23, Latency = 0, Cycles = 50

Core 0 (100.txt): 100.txt :Executing 'div $v0, $s4'

Core 0: PC = 50, Latency = 0, Cycles = 51

Core 1 (3.txt+ 25.txt+ 10.txt): 10.txt :Executing 'MUL R9, R0, R1'

Core 1: PC = 33, Latency = 0, Cycles = 51

Core 2 (1.txt+ 20.txt+ 12.txt+ 5.txt): 5.txt :Executing 'STORE R1, 4(R6)'

Core 2: PC = 36, Latency = 2, Cycles = 51

Core 3 (15.txt+ 17.txt+ 8.txt): 15.txt :Executing 'MUL R0, R0, R0'

Core 3: PC = 24, Latency = 0, Cycles = 51

Core 0 (100.txt): 100.txt :Executing 'beq $v0, $s5, label3'

Core 0: PC = 51, Latency = 0, Cycles = 52

Core 1 (3.txt+ 25.txt+ 10.txt): 10.txt :Executing 'NOP'

Core 1: PC = 34, Latency = 0, Cycles = 52

Core 3 (15.txt+ 17.txt+ 8.txt): 15.txt :Executing 'DIV R1, R1, R1'

Core 3: PC = 25, Latency = 1, Cycles = 52

Core 0 (100.txt): 100.txt :Executing 'label2:'

Core 0: PC = 52, Latency = 0, Cycles = 53

Core 1 (3.txt+ 25.txt+ 10.txt): 3.txt :Executing 'LOAD R1, 0(R2)'

Core 1: PC = 35, Latency = 2, Cycles = 53

Core 0 (100.txt): 100.txt :Executing 'add $t4, $t4, $t0'

Core 0: PC = 53, Latency = 0, Cycles = 54

Core 2 (1.txt+ 20.txt+ 12.txt+ 5.txt): 1.txt :Executing 'ADD R1, R2, R3'

Core 2: PC = 37, Latency = 0, Cycles = 54

Core 3 (15.txt+ 17.txt+ 8.txt): 15.txt :Executing 'ADD R2, R2, R2'

Core 3: PC = 26, Latency = 0, Cycles = 54

Core 0 (100.txt): 100.txt :Executing 'add $t5, $t5, $t1'

Core 0: PC = 54, Latency = 0, Cycles = 55

Core 3 (15.txt+ 17.txt+ 8.txt): 15.txt :Executing 'SUB R3, R3, R3'

Core 3: PC = 27, Latency = 0, Cycles = 55

Core 0 (100.txt): 100.txt :Executing 'sub $t6, $t5, $t4'

Core 0: PC = 55, Latency = 0, Cycles = 56

Core 1 (3.txt+ 25.txt+ 10.txt): 3.txt :Executing 'ADD R3, R1, R2'

Core 1: PC = 36, Latency = 0, Cycles = 56

Core 3 (15.txt+ 17.txt+ 8.txt): 15.txt :Executing 'NOP'

Core 3: PC = 28, Latency = 0, Cycles = 56

Core 0 (100.txt): 100.txt :Executing 'mul $t7, $t6, $t4'

Core 0: PC = 56, Latency = 0, Cycles = 57

Core 1 (3.txt+ 25.txt+ 10.txt): 3.txt :Executing 'SUB R4, R3, R1'

Core 1: PC = 37, Latency = 0, Cycles = 57

Core 3 (15.txt+ 17.txt+ 8.txt): 15.txt :Executing 'NOP'

Core 3: PC = 29, Latency = 0, Cycles = 57

Core 0 (100.txt): 100.txt :Executing 'div $t8, $t7'

Core 0: PC = 57, Latency = 0, Cycles = 58

Core 3 (15.txt+ 17.txt+ 8.txt): 15.txt :Executing 'NOP'

Core 3: PC = 30, Latency = 0, Cycles = 58

Core 0 (100.txt): 100.txt :Executing 'beq $t8, $t6, label4'

Core 0: PC = 58, Latency = 0, Cycles = 59

Core 3 (15.txt+ 17.txt+ 8.txt): 15.txt :Executing 'ADD R4, R4, R4'

Core 3: PC = 31, Latency = 0, Cycles = 59

Core 0 (100.txt): 100.txt :Executing 'label3:'

Core 0: PC = 59, Latency = 0, Cycles = 60

Core 3 (15.txt+ 17.txt+ 8.txt): 8.txt :Executing 'MUL R1, R2, R3'

Core 3: PC = 32, Latency = 0, Cycles = 60

Core 0 (100.txt): 100.txt :Executing 'add $s6, $t0, $t1'

Core 0: PC = 60, Latency = 0, Cycles = 61

Core 3 (15.txt+ 17.txt+ 8.txt): 8.txt :Executing 'DIV R4, R1, R2'

Core 3: PC = 33, Latency = 1, Cycles = 61

Core 0 (100.txt): 100.txt :Executing 'sub $s7, $s6, $t2'

Core 0: PC = 61, Latency = 0, Cycles = 62

Core 0 (100.txt): 100.txt :Executing 'mul $a0, $s7, $t3'

Core 0: PC = 62, Latency = 0, Cycles = 63

Core 3 (15.txt+ 17.txt+ 8.txt): 8.txt :Executing 'NOP'

Core 3: PC = 34, Latency = 0, Cycles = 63

Core 0 (100.txt): 100.txt :Executing 'div $a1, $a0'

Core 0: PC = 63, Latency = 0, Cycles = 64

Core 3 (15.txt+ 17.txt+ 8.txt): 8.txt :Executing 'ADD R5, R5, R5'

Core 3: PC = 35, Latency = 0, Cycles = 64

Core 0 (100.txt): 100.txt :Executing 'beq $a1, $s7, label5'

Core 0: PC = 64, Latency = 0, Cycles = 65

Core 3 (15.txt+ 17.txt+ 8.txt): 8.txt :Executing 'STORE R1, 4(R6)'

Core 3: PC = 36, Latency = 2, Cycles = 65

Core 0 (100.txt): 100.txt :Executing 'label4:'

Core 0: PC = 65, Latency = 0, Cycles = 66

Core 0 (100.txt): 100.txt :Executing 'add $s0, $s1, $s2'

Core 0: PC = 66, Latency = 0, Cycles = 67

Core 0 (100.txt): 100.txt :Executing 'sub $s1, $s0, $s3'

Core 0: PC = 67, Latency = 0, Cycles = 68

Core 0 (100.txt): 100.txt :Executing 'mul $s2, $s1, $s4'

Core 0: PC = 68, Latency = 0, Cycles = 69

Core 0 (100.txt): 100.txt :Executing 'div $s3, $s2'

Core 0: PC = 69, Latency = 0, Cycles = 70

Core 0 (100.txt): 100.txt :Executing 'beq $s3, $s4, end'

Core 0: PC = 70, Latency = 0, Cycles = 71

Core 0 (100.txt): 100.txt :Executing 'label5:'

Core 0: PC = 71, Latency = 0, Cycles = 72

Core 0 (100.txt): 100.txt :Executing 'add $a2, $a3, $v0'

Core 0: PC = 72, Latency = 0, Cycles = 73

Core 0 (100.txt): 100.txt :Executing 'sub $a3, $a2, $v1'

Core 0: PC = 73, Latency = 0, Cycles = 74

Core 0 (100.txt): 100.txt :Executing 'mul $v0, $a3, $t0'

Core 0: PC = 74, Latency = 0, Cycles = 75

Core 0 (100.txt): 100.txt :Executing 'div $v1, $v0'

Core 0: PC = 75, Latency = 0, Cycles = 76

Core 0 (100.txt): 100.txt :Executing 'beq $v1, $a2, end'

Core 0: PC = 76, Latency = 0, Cycles = 77

Core 0 (100.txt): 100.txt :Executing 'end:'

Core 0: PC = 77, Latency = 0, Cycles = 78

Core 0 (100.txt): 100.txt :Executing 'add $zero, $zero, $zero'

Core 0: PC = 78, Latency = 0, Cycles = 79

Core 0 (100.txt): 100.txt :Executing 'add $zero, $zero, $zero'

Core 0: PC = 79, Latency = 0, Cycles = 80

Core 0 (100.txt): 100.txt :Executing 'add $zero, $zero, $zero'

Core 0: PC = 80, Latency = 0, Cycles = 81

Core 0 (100.txt): 100.txt :Executing 'add $zero, $zero, $zero'

Core 0: PC = 81, Latency = 0, Cycles = 82

Core 0 (100.txt): 100.txt :Executing 'add $zero, $zero, $zero'

Core 0: PC = 82, Latency = 0, Cycles = 83

Core 0 (100.txt): 100.txt :Executing 'add $zero, $zero, $zero'

Core 0: PC = 83, Latency = 0, Cycles = 84

Core 0 (100.txt): 100.txt :Executing 'add $zero, $zero, $zero'

Core 0: PC = 84, Latency = 0, Cycles = 85

Core 0 (100.txt): 100.txt :Executing 'add $zero, $zero, $zero'

Core 0: PC = 85, Latency = 0, Cycles = 86

Core 0 (100.txt): 100.txt :Executing 'add $zero, $zero, $zero'

Core 0: PC = 86, Latency = 0, Cycles = 87

Core 0 (100.txt): 100.txt :Executing 'add $zero, $zero, $zero'

Core 0: PC = 87, Latency = 0, Cycles = 88


Total simulation time: 88 clock cycles
Core 0 (100.txt): 88 cycles
Core 1 (3.txt+ 25.txt+ 10.txt): 57 cycles
Core 2 (1.txt+ 20.txt+ 12.txt+ 5.txt): 54 cycles
Core 3 (15.txt+ 17.txt+ 8.txt): 67 cycles
