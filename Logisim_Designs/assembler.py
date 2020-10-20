import re
import sys

# scanner of all the possible string in IS of the assembly
mov_reg2reg = re.Scanner([
    (r'\s*mov\s*r0,\s*r1\s*', '1100'),
    (r'\s*mov\s*r0,\s*r2\s*', '1200'),
    (r'\s*mov\s*r0,\s*r3\s*', '1300'),

    (r'\s*mov\s*r1,\s*r0\s*', '1500'),
    (r'\s*mov\s*r1,\s*r2\s*', '1600'),
    (r'\s*mov\s*r1,\s*r3\s*', '1700'),

    (r'\s*mov\s*r2,\s*r0\s*', '1800'),
    (r'\s*mov\s*r2,\s*r1\s*', '1900'),
    (r'\s*mov\s*r2,\s*r3\s*', '1B00'),

    (r'\s*mov\s*r3,\s*r0\s*', '1C00'),
    (r'\s*mov\s*r3,\s*r1\s*', '1D00'),
    (r'\s*mov\s*r3,\s*r2\s*', '1E00'),
])

mov_acc2reg = re.Scanner([
    (r'\s*mov\s*acc1,\s*r0\s*', '3000'),
    (r'\s*mov\s*acc1,\s*r1\s*', '3100'),
    (r'\s*mov\s*acc1,\s*r2\s*', '3200'),
    (r'\s*mov\s*acc1,\s*r3\s*', '3300'),
    (r'\s*mov\s*acc2,\s*r0\s*', '4000'),
    (r'\s*mov\s*acc2,\s*r1\s*', '4100'),
    (r'\s*mov\s*acc2,\s*r2\s*', '4200'),
    (r'\s*mov\s*acc2,\s*r3\s*', '4300'),
])

add_2reg = re.Scanner([
    (r'\s*add\s*r0\s*', '5000'),
    (r'\s*add\s*r1\s*', '5400'),
    (r'\s*add\s*r2\s*', '5800'),
    (r'\s*add\s*r3\s*', '5C00'),
])

xor_2reg = re.Scanner([
    (r'\s*xor\s*r0\s*', '6000'),
    (r'\s*xor\s*r1\s*', '6400'),
    (r'\s*xor\s*r2\s*', '6800'),
    (r'\s*xor\s*r3\s*', '6C00'),
])

or_2reg = re.Scanner([
    (r'\s*or\s*r0\s*', '7000'),
    (r'\s*or\s*r1\s*', '7400'),
    (r'\s*or\s*r2\s*', '7800'),
    (r'\s*or\s*r3\s*', '7C00'),
])

and_2reg = re.Scanner([
    (r'\s*and\s*r0\s*', '7000'),
    (r'\s*and\s*r1\s*', '7400'),
    (r'\s*and\s*r2\s*', '7800'),
    (r'\s*and\s*r3\s*', '7C00'),
])

def hexa_immed(scanner, token): return "%s" % format(int(token, 16), "02X")
def dec_immed(scanner, token): return "%s" % format(int(token.replace("$", "")), "02X").replace("0x", "")

jump = re.Scanner([
    (r'0x\d+', hexa_immed),
    (r'\$\d+', dec_immed),
    (r'\s*jump\s*', '90'),
    (r'\s*,\s*', ''),
])

mov_immed2reg = re.Scanner([
    (r'0x[0-9a-f]+', hexa_immed),
    (r'\$\d+', dec_immed),
    (r'\s*mov\s*', '2'),
    (r'\s*r0_s*', '0'),
    (r'\s*r1\s*', '4'),
    (r'\s*r2\s*', '8'),
    (r'\s*r3\s*', 'c'),
    (r'\s*,\s*', ''),
])

store = re.Scanner([
    (r'0x[0-9a-f]+', hexa_immed),
    (r'\$\d+', dec_immed),
    (r'r0', '0'),
    (r'r1', '1'),
    (r'r2', '2'),
    (r'r3', '3'),
    (r'\s*,\s*', ''),
    (r'store\s*', 'a')
])

load = re.Scanner([
    (r'0x[0-9a-f]+', hexa_immed),
    (r'\$\d+', dec_immed),
    (r'load\s*r0,\s*', 'b0'),
    (r'load\s*r1,\s*', 'b1'),
    (r'load\s*r2,\s*', 'b2'),
    (r'load\s*r3,\s*', 'b3'),
])

cmp = re.Scanner([
    (r'\s*cmp\s*', 'c000'),
])

scanners = [
        # Regs
        mov_reg2reg,
        mov_acc2reg,
        mov_immed2reg,

        # ALU
        add_2reg,
        xor_2reg,
        or_2reg,
        and_2reg,
        cmp,

        #Jumps
        jump,

        #Ram
        store,
        load,
]

file = open(str(sys.argv[1]), "r")
modulo = int(sys.argv[2])
lines = file.readlines()

print("v2.0 raw")
cpt = 0
separator = ''
for line in lines:
    line = line.lower()

    for scanner in scanners:
        token, pattern = scanner.scan(line)

        if len(token) != 0:
            if token[0] == 'a':
                swap = token[1]
                token[1] = token[-1]
                token[-1] = swap

            token = separator.join(token)
            # print(line[:-1].ljust(15, ' ') + ": " + str(token))

            if cpt >= modulo:
                cpt = 0
                print("")
            else:
                cpt += 1
            print(str(token) + ' ', end  = '');
            break;
