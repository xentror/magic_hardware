mov r1, 0xff
mov r2, $1
mov acc1, r1
mov acc2, r2
add r2
cmp
store 0x0, r2
jump $8
