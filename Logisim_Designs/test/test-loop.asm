mov r1, $10
mov r2, $0
mov r3, $1
mov acc1, r3
mov acc2, r2
add r2
store 0x0, r2
mov acc1, r2
mov acc2, r1
cmp
jumpeq 0xA
jump 0x3
