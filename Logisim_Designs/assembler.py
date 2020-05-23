import re
import sys

empty = re.Scanner([
    (r'\s+', None),
])

# scanner of all the possible string in IS of the assembly
mov_reg2reg = re.Scanner([
    (r'mov r0, r1', '1100'),
    (r'mov r0, r2', '1200'),
    (r'mov r0, r3', '1300'),

    (r'mov r1, r0', '1500'),
    (r'mov r1, r2', '1600'),
    (r'mov r1, r3', '1700'),

    (r'mov r2, r0', '1800'),
    (r'mov r2, r1', '1900'),
    (r'mov r2, r3', '1B00'),

    (r'mov r3, r0', '1C00'),
    (r'mov r3, r1', '1D00'),
    (r'mov r3, r2', '1E00'),
])

mov_acc2reg = re.Scanner([
    (r'mov acc1, r0', '3000'),
    (r'mov acc1, r1', '3100'),
    (r'mov acc1, r2', '3200'),
    (r'mov acc1, r3', '3300'),

    (r'mov acc2, r0', '4000'),
    (r'mov acc2, r1', '4100'),
    (r'mov acc2, r2', '4200'),
    (r'mov acc2, r3', '4300'),
])

add_2reg = re.Scanner([
    (r'add r0', '5000'),
    (r'add r1', '5400'),
    (r'add r2', '5800'),
    (r'add r3', '5C00'),
])

xor_2reg = re.Scanner([
    (r'xor r0', '6000'),
    (r'xor r1', '6400'),
    (r'xor r2', '6800'),
    (r'xor r3', '6C00'),
])

or_2reg = re.Scanner([
    (r'or r0', '7000'),
    (r'or r1', '7400'),
    (r'or r2', '7800'),
    (r'or r3', '7C00'),
])

and_2reg = re.Scanner([
    (r'and r0', '7000'),
    (r'and r1', '7400'),
    (r'and r2', '7800'),
    (r'and r3', '7C00'),
])

def hexa_immed(scanner, token): return "%s" % token.replace("0x", "")
def dec_immed(scanner, token): return "%s" % str(hex(int(token.replace("$", "")))).replace("0x", "")

jump = re.Scanner([
    (r'0x\d+', hexa_immed),
    (r'\$\d+', dec_immed),
    (r'jump ', 'jump'),
    (r'\s*,\s*', 'comma'),
])

mov_immed2reg = re.Scanner([
    (r'0x[0-9a-f]+', hexa_immed),
    (r'\$\d+', dec_immed),
    (r'mov ', '2'),
    (r'r0', '0'),
    (r'r1', '4'),
    (r'r2', '8'),
    (r'r3', 'C'),
    (r'\s*,\s*', 'comma'),
])

scanners = [
        empty,

        # Regs
        mov_reg2reg,
        mov_acc2reg,
        mov_immed2reg,

        # ALU
        add_2reg,
        xor_2reg,
        or_2reg,
        and_2reg,

        #Jumps
        jump

        #Ram
]

file = open(str(sys.argv[1]), "r")
lines = file.readlines()

print("")
for line in lines:
    #line = line.replace(" ", "")
    line = line.lower()

    for scanner in scanners:

        token, pattern = scanner.scan(line)
        if len(token) != 0:
            print("assembly: " + line[:-1])
            print("hexa: " + str(token) + "\n")
            break;
