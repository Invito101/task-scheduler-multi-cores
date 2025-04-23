# Scheduling With round_robin Scheduler
Core 0 (1.txt+ 3.txt+ 15.txt): 1.txt :Executing 'ADD R1, R2, R3'

Core 0: PC = 0, Latency = 0, Cycles = 1

Core 1 (17.txt+ 10.txt+ 5.txt): 10.txt :Executing 'ADD R1, R1, R1'

Core 1: PC = 0, Latency = 0, Cycles = 1

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'add $t0, $zero, $zero'

Core 2: PC = 0, Latency = 0, Cycles = 1

Core 3 (25.txt+ 12.txt): 12.txt :Executing 'MUL R1, R2, R3'

Core 3: PC = 0, Latency = 0, Cycles = 1

Core 0 (1.txt+ 3.txt+ 15.txt): 15.txt :Executing 'MUL R1, R2, R3'

Core 0: PC = 1, Latency = 0, Cycles = 2

Core 1 (17.txt+ 10.txt+ 5.txt): 10.txt :Executing 'SUB R2, R2, R2'

Core 1: PC = 1, Latency = 0, Cycles = 2

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'add $t1, $zero, $zero'

Core 2: PC = 1, Latency = 0, Cycles = 2

Core 3 (25.txt+ 12.txt): 12.txt :Executing 'DIV R4, R1, R2'

Core 3: PC = 1, Latency = 1, Cycles = 2

Core 0 (1.txt+ 3.txt+ 15.txt): 15.txt :Executing 'MUL R4, R1, R2'

Core 0: PC = 2, Latency = 0, Cycles = 3

Core 1 (17.txt+ 10.txt+ 5.txt): 10.txt :Executing 'MUL R3, R3, R3'

Core 1: PC = 2, Latency = 0, Cycles = 3

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'add $t2, $zero, $zero'

Core 2: PC = 2, Latency = 0, Cycles = 3

Core 0 (1.txt+ 3.txt+ 15.txt): 15.txt :Executing 'MUL R5, R4, R1'

Core 0: PC = 3, Latency = 0, Cycles = 4

Core 1 (17.txt+ 10.txt+ 5.txt): 10.txt :Executing 'DIV R4, R4, R4'

Core 1: PC = 3, Latency = 1, Cycles = 4

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'add $t3, $zero, $zero'

Core 2: PC = 3, Latency = 0, Cycles = 4

Core 3 (25.txt+ 12.txt): 12.txt :Executing 'ADD R5, R6, R7'

Core 3: PC = 2, Latency = 0, Cycles = 4

Core 0 (1.txt+ 3.txt+ 15.txt): 15.txt :Executing 'DIV R6, R5, R2'

Core 0: PC = 4, Latency = 1, Cycles = 5

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'add $t4, $zero, $zero'

Core 2: PC = 4, Latency = 0, Cycles = 5

Core 3 (25.txt+ 12.txt): 12.txt :Executing 'SUB R8, R9, R0'

Core 3: PC = 3, Latency = 0, Cycles = 5

Core 1 (17.txt+ 10.txt+ 5.txt): 10.txt :Executing 'LOAD R5, 0(R5)'

Core 1: PC = 4, Latency = 2, Cycles = 6

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'add $t5, $zero, $zero'

Core 2: PC = 5, Latency = 0, Cycles = 6

Core 3 (25.txt+ 12.txt): 12.txt :Executing 'LOAD R2, 0(R3)'

Core 3: PC = 4, Latency = 2, Cycles = 6

Core 0 (1.txt+ 3.txt+ 15.txt): 15.txt :Executing 'DIV R7, R6, R1'

Core 0: PC = 5, Latency = 1, Cycles = 7

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'add $t6, $zero, $zero'

Core 2: PC = 6, Latency = 0, Cycles = 7

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'add $t7, $zero, $zero'

Core 2: PC = 7, Latency = 0, Cycles = 8

Core 0 (1.txt+ 3.txt+ 15.txt): 15.txt :Executing 'ADD R8, R8, R8'

Core 0: PC = 6, Latency = 0, Cycles = 9

Core 1 (17.txt+ 10.txt+ 5.txt): 10.txt :Executing 'STORE R6, 8(R6)'

Core 1: PC = 5, Latency = 2, Cycles = 9

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'add $t8, $zero, $zero'

Core 2: PC = 8, Latency = 0, Cycles = 9

Core 3 (25.txt+ 12.txt): 12.txt :Executing 'NOP'

Core 3: PC = 5, Latency = 0, Cycles = 9

Core 0 (1.txt+ 3.txt+ 15.txt): 15.txt :Executing 'SUB R9, R9, R9'

Core 0: PC = 7, Latency = 0, Cycles = 10

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'add $t9, $zero, $zero'

Core 2: PC = 9, Latency = 0, Cycles = 10

Core 3 (25.txt+ 12.txt): 12.txt :Executing 'NOP'

Core 3: PC = 6, Latency = 0, Cycles = 10

Core 0 (1.txt+ 3.txt+ 15.txt): 15.txt :Executing 'MUL R0, R0, R0'

Core 0: PC = 8, Latency = 0, Cycles = 11

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'add $s0, $zero, $zero'

Core 2: PC = 10, Latency = 0, Cycles = 11

Core 3 (25.txt+ 12.txt): 12.txt :Executing 'STORE R3, 4(R4)'

Core 3: PC = 7, Latency = 2, Cycles = 11

Core 0 (1.txt+ 3.txt+ 15.txt): 15.txt :Executing 'DIV R1, R1, R1'

Core 0: PC = 9, Latency = 1, Cycles = 12

Core 1 (17.txt+ 10.txt+ 5.txt): 10.txt :Executing 'NOP'

Core 1: PC = 6, Latency = 0, Cycles = 12

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'add $s1, $zero, $zero'

Core 2: PC = 11, Latency = 0, Cycles = 12

Core 1 (17.txt+ 10.txt+ 5.txt): 10.txt :Executing 'ADD R7, R8, R9'

Core 1: PC = 7, Latency = 0, Cycles = 13

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'add $s2, $zero, $zero'

Core 2: PC = 12, Latency = 0, Cycles = 13

Core 0 (1.txt+ 3.txt+ 15.txt): 15.txt :Executing 'ADD R2, R2, R2'

Core 0: PC = 10, Latency = 0, Cycles = 14

Core 1 (17.txt+ 10.txt+ 5.txt): 10.txt :Executing 'MUL R9, R0, R1'

Core 1: PC = 8, Latency = 0, Cycles = 14

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'add $s3, $zero, $zero'

Core 2: PC = 13, Latency = 0, Cycles = 14

Core 3 (25.txt+ 12.txt): 12.txt :Executing 'MUL R5, R5, R5'

Core 3: PC = 8, Latency = 0, Cycles = 14

Core 0 (1.txt+ 3.txt+ 15.txt): 15.txt :Executing 'SUB R3, R3, R3'

Core 0: PC = 11, Latency = 0, Cycles = 15

Core 1 (17.txt+ 10.txt+ 5.txt): 10.txt :Executing 'NOP'

Core 1: PC = 9, Latency = 0, Cycles = 15

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'add $s4, $zero, $zero'

Core 2: PC = 14, Latency = 0, Cycles = 15

Core 3 (25.txt+ 12.txt): 12.txt :Executing 'ADD R6, R6, R6'

Core 3: PC = 9, Latency = 0, Cycles = 15

Core 0 (1.txt+ 3.txt+ 15.txt): 15.txt :Executing 'NOP'

Core 0: PC = 12, Latency = 0, Cycles = 16

Core 1 (17.txt+ 10.txt+ 5.txt): 17.txt :Executing 'LOAD R1, 0(R2)'

Core 1: PC = 10, Latency = 2, Cycles = 16

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'add $s5, $zero, $zero'

Core 2: PC = 15, Latency = 0, Cycles = 16

Core 3 (25.txt+ 12.txt): 12.txt :Executing 'DIV R7, R7, R7'

Core 3: PC = 10, Latency = 1, Cycles = 16

Core 0 (1.txt+ 3.txt+ 15.txt): 15.txt :Executing 'NOP'

Core 0: PC = 13, Latency = 0, Cycles = 17

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'add $s6, $zero, $zero'

Core 2: PC = 16, Latency = 0, Cycles = 17

Core 0 (1.txt+ 3.txt+ 15.txt): 15.txt :Executing 'NOP'

Core 0: PC = 14, Latency = 0, Cycles = 18

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'add $s7, $zero, $zero'

Core 2: PC = 17, Latency = 0, Cycles = 18

Core 3 (25.txt+ 12.txt): 12.txt :Executing 'NOP'

Core 3: PC = 11, Latency = 0, Cycles = 18

Core 0 (1.txt+ 3.txt+ 15.txt): 15.txt :Executing 'ADD R4, R4, R4'

Core 0: PC = 15, Latency = 0, Cycles = 19

Core 1 (17.txt+ 10.txt+ 5.txt): 17.txt :Executing 'STORE R1, 4(R3)'

Core 1: PC = 11, Latency = 2, Cycles = 19

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'add $a0, $zero, $zero'

Core 2: PC = 18, Latency = 0, Cycles = 19

Core 3 (25.txt+ 12.txt): 25.txt :Executing 'MUL R1, R2, R3'

Core 3: PC = 12, Latency = 0, Cycles = 19

Core 0 (1.txt+ 3.txt+ 15.txt): 3.txt :Executing 'LOAD R1, 0(R2)'

Core 0: PC = 16, Latency = 2, Cycles = 20

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'add $a1, $zero, $zero'

Core 2: PC = 19, Latency = 0, Cycles = 20

Core 3 (25.txt+ 12.txt): 25.txt :Executing 'DIV R4, R5, R6'

Core 3: PC = 13, Latency = 1, Cycles = 20

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'add $a2, $zero, $zero'

Core 2: PC = 20, Latency = 0, Cycles = 21

Core 1 (17.txt+ 10.txt+ 5.txt): 17.txt :Executing 'LOAD R4, 8(R5)'

Core 1: PC = 12, Latency = 2, Cycles = 22

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'add $a3, $zero, $zero'

Core 2: PC = 21, Latency = 0, Cycles = 22

Core 3 (25.txt+ 12.txt): 25.txt :Executing 'ADD R7, R8, R9'

Core 3: PC = 14, Latency = 0, Cycles = 22

Core 0 (1.txt+ 3.txt+ 15.txt): 3.txt :Executing 'ADD R3, R1, R2'

Core 0: PC = 17, Latency = 0, Cycles = 23

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'add $v0, $zero, $zero'

Core 2: PC = 22, Latency = 0, Cycles = 23

Core 3 (25.txt+ 12.txt): 25.txt :Executing 'SUB R1, R2, R3'

Core 3: PC = 15, Latency = 0, Cycles = 23

Core 0 (1.txt+ 3.txt+ 15.txt): 3.txt :Executing 'SUB R4, R3, R1'

Core 0: PC = 18, Latency = 0, Cycles = 24

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'add $v1, $zero, $zero'

Core 2: PC = 23, Latency = 0, Cycles = 24

Core 3 (25.txt+ 12.txt): 25.txt :Executing 'MUL R4, R5, R6'

Core 3: PC = 16, Latency = 0, Cycles = 24

Core 1 (17.txt+ 10.txt+ 5.txt): 17.txt :Executing 'STORE R6, 12(R7)'

Core 1: PC = 13, Latency = 2, Cycles = 25

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'add $t1, $t1, $t0'

Core 2: PC = 24, Latency = 0, Cycles = 25

Core 3 (25.txt+ 12.txt): 25.txt :Executing 'DIV R7, R8, R9'

Core 3: PC = 17, Latency = 1, Cycles = 25

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'add $t0, $t0, $t1'

Core 2: PC = 25, Latency = 0, Cycles = 26

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'sub $t2, $t0, $t1'

Core 2: PC = 26, Latency = 0, Cycles = 27

Core 3 (25.txt+ 12.txt): 25.txt :Executing 'ADD R1, R2, R3'

Core 3: PC = 18, Latency = 0, Cycles = 27

Core 1 (17.txt+ 10.txt+ 5.txt): 17.txt :Executing 'LOAD R8, 16(R9)'

Core 1: PC = 14, Latency = 2, Cycles = 28

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'mul $t3, $t0, $t1'

Core 2: PC = 27, Latency = 0, Cycles = 28

Core 3 (25.txt+ 12.txt): 25.txt :Executing 'SUB R4, R5, R6'

Core 3: PC = 19, Latency = 0, Cycles = 28

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'div $t3, $t1'

Core 2: PC = 28, Latency = 0, Cycles = 29

Core 3 (25.txt+ 12.txt): 25.txt :Executing 'MUL R7, R8, R9'

Core 3: PC = 20, Latency = 0, Cycles = 29

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'beq $t0, $t1, equal'

Core 2: PC = 29, Latency = 0, Cycles = 30

Core 3 (25.txt+ 12.txt): 25.txt :Executing 'DIV R1, R2, R3'

Core 3: PC = 21, Latency = 1, Cycles = 30

Core 1 (17.txt+ 10.txt+ 5.txt): 17.txt :Executing 'NOP'

Core 1: PC = 15, Latency = 0, Cycles = 31

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'add $s0, $t0, $t2'

Core 2: PC = 30, Latency = 0, Cycles = 31

Core 1 (17.txt+ 10.txt+ 5.txt): 17.txt :Executing 'LOAD R1, 20(R2)'

Core 1: PC = 16, Latency = 2, Cycles = 32

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'add $s1, $s0, $t1'

Core 2: PC = 31, Latency = 0, Cycles = 32

Core 3 (25.txt+ 12.txt): 25.txt :Executing 'ADD R4, R5, R6'

Core 3: PC = 22, Latency = 0, Cycles = 32

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'add $s2, $s1, $t1'

Core 2: PC = 32, Latency = 0, Cycles = 33

Core 3 (25.txt+ 12.txt): 25.txt :Executing 'SUB R7, R8, R9'

Core 3: PC = 23, Latency = 0, Cycles = 33

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'add $s3, $s2, $t2'

Core 2: PC = 33, Latency = 0, Cycles = 34

Core 3 (25.txt+ 12.txt): 25.txt :Executing 'NOP'

Core 3: PC = 24, Latency = 0, Cycles = 34

Core 1 (17.txt+ 10.txt+ 5.txt): 17.txt :Executing 'STORE R1, 24(R3)'

Core 1: PC = 17, Latency = 2, Cycles = 35

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'sub $s4, $s3, $t1'

Core 2: PC = 34, Latency = 0, Cycles = 35

Core 3 (25.txt+ 12.txt): 25.txt :Executing 'NOP'

Core 3: PC = 25, Latency = 0, Cycles = 35

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'sub $s5, $s4, $t0'

Core 2: PC = 35, Latency = 0, Cycles = 36

Core 3 (25.txt+ 12.txt): 25.txt :Executing 'NOP'

Core 3: PC = 26, Latency = 0, Cycles = 36

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'mul $s6, $s5, $t1'

Core 2: PC = 36, Latency = 0, Cycles = 37

Core 3 (25.txt+ 12.txt): 25.txt :Executing 'LOAD R1, 0(R2)'

Core 3: PC = 27, Latency = 2, Cycles = 37

Core 1 (17.txt+ 10.txt+ 5.txt): 17.txt :Executing 'LOAD R4, 28(R5)'

Core 1: PC = 18, Latency = 2, Cycles = 38

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'div $s6, $t2'

Core 2: PC = 37, Latency = 0, Cycles = 38

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'beq $s6, $t3, label1'

Core 2: PC = 38, Latency = 0, Cycles = 39

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'equal:'

Core 2: PC = 39, Latency = 0, Cycles = 40

Core 3 (25.txt+ 12.txt): 25.txt :Executing 'STORE R3, 4(R4)'

Core 3: PC = 28, Latency = 2, Cycles = 40

Core 1 (17.txt+ 10.txt+ 5.txt): 17.txt :Executing 'STORE R6, 32(R7)'

Core 1: PC = 19, Latency = 2, Cycles = 41

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'add $a0, $zero, $t0'

Core 2: PC = 40, Latency = 0, Cycles = 41

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'add $a1, $a0, $t1'

Core 2: PC = 41, Latency = 0, Cycles = 42

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'sub $a2, $a1, $t2'

Core 2: PC = 42, Latency = 0, Cycles = 43

Core 3 (25.txt+ 12.txt): 25.txt :Executing 'LOAD R5, 8(R6)'

Core 3: PC = 29, Latency = 2, Cycles = 43

Core 1 (17.txt+ 10.txt+ 5.txt): 17.txt :Executing 'LOAD R8, 36(R9)'

Core 1: PC = 20, Latency = 2, Cycles = 44

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'mul $a3, $a2, $t3'

Core 2: PC = 43, Latency = 0, Cycles = 44

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'div $a3, $t1'

Core 2: PC = 44, Latency = 0, Cycles = 45

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'beq $a3, $zero, label2'

Core 2: PC = 45, Latency = 0, Cycles = 46

Core 3 (25.txt+ 12.txt): 25.txt :Executing 'STORE R7, 12(R8)'

Core 3: PC = 30, Latency = 2, Cycles = 46

Core 1 (17.txt+ 10.txt+ 5.txt): 17.txt :Executing 'NOP'

Core 1: PC = 21, Latency = 0, Cycles = 47

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'label1:'

Core 2: PC = 46, Latency = 0, Cycles = 47

Core 1 (17.txt+ 10.txt+ 5.txt): 17.txt :Executing 'NOP'

Core 1: PC = 22, Latency = 0, Cycles = 48

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'add $v0, $s0, $s1'

Core 2: PC = 47, Latency = 0, Cycles = 48

Core 1 (17.txt+ 10.txt+ 5.txt): 17.txt :Executing 'NOP'

Core 1: PC = 23, Latency = 0, Cycles = 49

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'sub $v0, $v0, $s2'

Core 2: PC = 48, Latency = 0, Cycles = 49

Core 3 (25.txt+ 12.txt): 25.txt :Executing 'NOP'

Core 3: PC = 31, Latency = 0, Cycles = 49

Core 1 (17.txt+ 10.txt+ 5.txt): 17.txt :Executing 'STORE R2, 40(R1)'

Core 1: PC = 24, Latency = 2, Cycles = 50

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'mul $v0, $v0, $s3'

Core 2: PC = 49, Latency = 0, Cycles = 50

Core 3 (25.txt+ 12.txt): 25.txt :Executing 'ADD R1, R1, R1'

Core 3: PC = 32, Latency = 0, Cycles = 50

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'div $v0, $s4'

Core 2: PC = 50, Latency = 0, Cycles = 51

Core 3 (25.txt+ 12.txt): 25.txt :Executing 'SUB R2, R2, R2'

Core 3: PC = 33, Latency = 0, Cycles = 51

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'beq $v0, $s5, label3'

Core 2: PC = 51, Latency = 0, Cycles = 52

Core 3 (25.txt+ 12.txt): 25.txt :Executing 'MUL R3, R3, R3'

Core 3: PC = 34, Latency = 0, Cycles = 52

Core 1 (17.txt+ 10.txt+ 5.txt): 17.txt :Executing 'LOAD R3, 44(R4)'

Core 1: PC = 25, Latency = 2, Cycles = 53

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'label2:'

Core 2: PC = 52, Latency = 0, Cycles = 53

Core 3 (25.txt+ 12.txt): 25.txt :Executing 'DIV R4, R4, R4'

Core 3: PC = 35, Latency = 1, Cycles = 53

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'add $t4, $t4, $t0'

Core 2: PC = 53, Latency = 0, Cycles = 54

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'add $t5, $t5, $t1'

Core 2: PC = 54, Latency = 0, Cycles = 55

Core 3 (25.txt+ 12.txt): 25.txt :Executing 'NOP'

Core 3: PC = 36, Latency = 0, Cycles = 55

Core 1 (17.txt+ 10.txt+ 5.txt): 17.txt :Executing 'NOP'

Core 1: PC = 26, Latency = 0, Cycles = 56

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'sub $t6, $t5, $t4'

Core 2: PC = 55, Latency = 0, Cycles = 56

Core 1 (17.txt+ 10.txt+ 5.txt): 5.txt :Executing 'MUL R1, R2, R3'

Core 1: PC = 27, Latency = 0, Cycles = 57

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'mul $t7, $t6, $t4'

Core 2: PC = 56, Latency = 0, Cycles = 57

Core 1 (17.txt+ 10.txt+ 5.txt): 5.txt :Executing 'DIV R4, R1, R2'

Core 1: PC = 28, Latency = 1, Cycles = 58

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'div $t8, $t7'

Core 2: PC = 57, Latency = 0, Cycles = 58

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'beq $t8, $t6, label4'

Core 2: PC = 58, Latency = 0, Cycles = 59

Core 1 (17.txt+ 10.txt+ 5.txt): 5.txt :Executing 'NOP'

Core 1: PC = 29, Latency = 0, Cycles = 60

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'label3:'

Core 2: PC = 59, Latency = 0, Cycles = 60

Core 1 (17.txt+ 10.txt+ 5.txt): 5.txt :Executing 'ADD R5, R5, R5'

Core 1: PC = 30, Latency = 0, Cycles = 61

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'add $s6, $t0, $t1'

Core 2: PC = 60, Latency = 0, Cycles = 61

Core 1 (17.txt+ 10.txt+ 5.txt): 5.txt :Executing 'STORE R1, 4(R6)'

Core 1: PC = 31, Latency = 2, Cycles = 62

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'sub $s7, $s6, $t2'

Core 2: PC = 61, Latency = 0, Cycles = 62

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'mul $a0, $s7, $t3'

Core 2: PC = 62, Latency = 0, Cycles = 63

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'div $a1, $a0'

Core 2: PC = 63, Latency = 0, Cycles = 64

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'beq $a1, $s7, label5'

Core 2: PC = 64, Latency = 0, Cycles = 65

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'label4:'

Core 2: PC = 65, Latency = 0, Cycles = 66

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'add $s0, $s1, $s2'

Core 2: PC = 66, Latency = 0, Cycles = 67

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'sub $s1, $s0, $s3'

Core 2: PC = 67, Latency = 0, Cycles = 68

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'mul $s2, $s1, $s4'

Core 2: PC = 68, Latency = 0, Cycles = 69

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'div $s3, $s2'

Core 2: PC = 69, Latency = 0, Cycles = 70

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'beq $s3, $s4, end'

Core 2: PC = 70, Latency = 0, Cycles = 71

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'label5:'

Core 2: PC = 71, Latency = 0, Cycles = 72

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'add $a2, $a3, $v0'

Core 2: PC = 72, Latency = 0, Cycles = 73

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'sub $a3, $a2, $v1'

Core 2: PC = 73, Latency = 0, Cycles = 74

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'mul $v0, $a3, $t0'

Core 2: PC = 74, Latency = 0, Cycles = 75

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'div $v1, $v0'

Core 2: PC = 75, Latency = 0, Cycles = 76

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'beq $v1, $a2, end'

Core 2: PC = 76, Latency = 0, Cycles = 77

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'end:'

Core 2: PC = 77, Latency = 0, Cycles = 78

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'add $zero, $zero, $zero'

Core 2: PC = 78, Latency = 0, Cycles = 79

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'add $zero, $zero, $zero'

Core 2: PC = 79, Latency = 0, Cycles = 80

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'add $zero, $zero, $zero'

Core 2: PC = 80, Latency = 0, Cycles = 81

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'add $zero, $zero, $zero'

Core 2: PC = 81, Latency = 0, Cycles = 82

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'add $zero, $zero, $zero'

Core 2: PC = 82, Latency = 0, Cycles = 83

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'add $zero, $zero, $zero'

Core 2: PC = 83, Latency = 0, Cycles = 84

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'add $zero, $zero, $zero'

Core 2: PC = 84, Latency = 0, Cycles = 85

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'add $zero, $zero, $zero'

Core 2: PC = 85, Latency = 0, Cycles = 86

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'add $zero, $zero, $zero'

Core 2: PC = 86, Latency = 0, Cycles = 87

Core 2 (20.txt+ 8.txt+ 100.txt): 100.txt :Executing 'add $zero, $zero, $zero'

Core 2: PC = 87, Latency = 0, Cycles = 88

Core 2 (20.txt+ 8.txt+ 100.txt): 20.txt :Executing 'ADD R1, R1, R1'

Core 2: PC = 88, Latency = 0, Cycles = 89

Core 2 (20.txt+ 8.txt+ 100.txt): 20.txt :Executing 'SUB R2, R2, R2'

Core 2: PC = 89, Latency = 0, Cycles = 90

Core 2 (20.txt+ 8.txt+ 100.txt): 20.txt :Executing 'MUL R3, R3, R3'

Core 2: PC = 90, Latency = 0, Cycles = 91

Core 2 (20.txt+ 8.txt+ 100.txt): 20.txt :Executing 'DIV R4, R4, R4'

Core 2: PC = 91, Latency = 1, Cycles = 92

Core 2 (20.txt+ 8.txt+ 100.txt): 20.txt :Executing 'ADD R5, R5, R5'

Core 2: PC = 92, Latency = 0, Cycles = 94

Core 2 (20.txt+ 8.txt+ 100.txt): 20.txt :Executing 'SUB R6, R6, R6'

Core 2: PC = 93, Latency = 0, Cycles = 95

Core 2 (20.txt+ 8.txt+ 100.txt): 20.txt :Executing 'MUL R7, R7, R7'

Core 2: PC = 94, Latency = 0, Cycles = 96

Core 2 (20.txt+ 8.txt+ 100.txt): 20.txt :Executing 'DIV R8, R8, R8'

Core 2: PC = 95, Latency = 1, Cycles = 97

Core 2 (20.txt+ 8.txt+ 100.txt): 20.txt :Executing 'ADD R9, R9, R9'

Core 2: PC = 96, Latency = 0, Cycles = 99

Core 2 (20.txt+ 8.txt+ 100.txt): 20.txt :Executing 'SUB R0, R0, R0'

Core 2: PC = 97, Latency = 0, Cycles = 100

Core 2 (20.txt+ 8.txt+ 100.txt): 20.txt :Executing 'LOAD R1, 0(R1)'

Core 2: PC = 98, Latency = 2, Cycles = 101

Core 2 (20.txt+ 8.txt+ 100.txt): 20.txt :Executing 'STORE R2, 4(R2)'

Core 2: PC = 99, Latency = 2, Cycles = 104

Core 2 (20.txt+ 8.txt+ 100.txt): 20.txt :Executing 'NOP'

Core 2: PC = 100, Latency = 0, Cycles = 107

Core 2 (20.txt+ 8.txt+ 100.txt): 20.txt :Executing 'NOP'

Core 2: PC = 101, Latency = 0, Cycles = 108

Core 2 (20.txt+ 8.txt+ 100.txt): 20.txt :Executing 'NOP'

Core 2: PC = 102, Latency = 0, Cycles = 109

Core 2 (20.txt+ 8.txt+ 100.txt): 20.txt :Executing 'NOP'

Core 2: PC = 103, Latency = 0, Cycles = 110

Core 2 (20.txt+ 8.txt+ 100.txt): 20.txt :Executing 'NOP'

Core 2: PC = 104, Latency = 0, Cycles = 111

Core 2 (20.txt+ 8.txt+ 100.txt): 20.txt :Executing 'ADD R3, R3, R3'

Core 2: PC = 105, Latency = 0, Cycles = 112

Core 2 (20.txt+ 8.txt+ 100.txt): 20.txt :Executing 'DIV R4, R4, R4'

Core 2: PC = 106, Latency = 1, Cycles = 113

Core 2 (20.txt+ 8.txt+ 100.txt): 20.txt :Executing 'NOP'

Core 2: PC = 107, Latency = 0, Cycles = 115

Core 2 (20.txt+ 8.txt+ 100.txt): 8.txt :Executing 'MUL R1, R2, R3'

Core 2: PC = 108, Latency = 0, Cycles = 116

Core 2 (20.txt+ 8.txt+ 100.txt): 8.txt :Executing 'DIV R4, R1, R2'

Core 2: PC = 109, Latency = 1, Cycles = 117

Core 2 (20.txt+ 8.txt+ 100.txt): 8.txt :Executing 'NOP'

Core 2: PC = 110, Latency = 0, Cycles = 119

Core 2 (20.txt+ 8.txt+ 100.txt): 8.txt :Executing 'ADD R5, R5, R5'

Core 2: PC = 111, Latency = 0, Cycles = 120

Core 2 (20.txt+ 8.txt+ 100.txt): 8.txt :Executing 'STORE R1, 4(R6)'

Core 2: PC = 112, Latency = 2, Cycles = 121


Total simulation time: 123 clock cycles
Core 0 (1.txt+ 3.txt+ 15.txt): 24 cycles
Core 1 (17.txt+ 10.txt+ 5.txt): 64 cycles
Core 2 (20.txt+ 8.txt+ 100.txt): 123 cycles
Core 3 (25.txt+ 12.txt): 55 cycles
