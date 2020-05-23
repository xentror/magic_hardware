mov r0, r1
mov r1, r0

mov acc1, r0
mov acc1, r1
mov acc1, r2
mov acc1, r3

add r0
add r1
add r2
add r3

xor r0
xor r1
xor r2
xor r3

or r0
or r1
or r2
or r3

AND r0
and r1
and r2
and r3

jump $3
jump $255
jump 0x3

mov r1, 0xFF
mov r2, $255
mov r1, 0xAF
mov r2, $123

store 0xFF, R1

load r2, 0xFF
