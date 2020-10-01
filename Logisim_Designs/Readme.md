# My first CPU

The purpose of this logisim design was to learn how is working/ design
a simple 8bits CPU.

This CPU execute an instruction in 3 Clock Ticks, driving by a ring counter, wich
switches states each time time main clock tick.

This CPU is based on the Havard model, with the Data Memory and Program
memory are separated. All externs memories are asynchronus which made it
more easy for me, because the result of a read or a write command are
instant in the simulator.

## Rom

The program memory is an asychronous memory which send 2 bytes to the
Instruction Register.
The following will save it during the fetch phase and send it to the
decoder block during the decode phase.

## Ram

The Data memory is an asynchronous memory which send 1 byte into the
main bus of the cpu, which is link to the PC register, registers banks,
and the RAM. That's why a negate door link to the value of the Write Ram
Micro Instruction is here to ensure that the main bus is linked to the
RAM input only when needed.

## ALU

The ALU is here to do all the arithmetic and logic operations. It works
with an Accumulator Register and a specified Register of the Bank register.
That's why you have to put a value inside the accumulator, and then
call an operations between the accumulator and the wanted register.

This increase the number of instruction needed for a simple operations
but made it easier during the design.

## Instruction Set

This CPU has 11 Instructions:
All instruction are on 2bytes and are divided this way:
```
XXXX XXXX XXXX XXXX
|_______| |__| |__|
  Instr   |Dst Src|
  Opcode  |_______|
               |_____ Immediate
```
The first byte is for the intruction type (mov, load, store, ...)
The second byte can be interpreted as a Immediate value or can be
divided into a Dst/Src structure.

### MOV

Mov Dst, Src

Mov Reg, Reg -> 10 \
Mov Reg, Imm -> 11 \
Mov Acc, Imm -> 12 \

### Load

Load Reg, ADDR -> 20

### Store

Store ADDR, Reg -> 30 \
Store ADDR, Imm -> 31 \

### ALU

Add Reg -> 40 \
Xor Reg -> 50 \
And Reg -> 60 \
Or Reg -> 70 \

### Jump

Jump ADDR -> 80

## Tests

A reset signal was integrated at the end, because I found that I needed
one in order to facilitate testing. May be I'll find later a way to do
automatize test in Logisim.

To facilitate the tests, I created a very basic assembler python script
which return the opcodes of a given asembly file. It is based on the
under-use scanner part of the regex Python library.

## CPU Design

![image](magic_cpu_design.png)
