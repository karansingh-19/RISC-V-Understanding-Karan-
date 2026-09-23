# RISC-V-Understanding-Karan-
This repository contains notes of my basic understanding of RISK-V. 

Basically RISK-V is an Instruction Set Architecture (ISA) that defines the instructions and rules that a compatible processor understands. It also defines the language between CPU and Software (How instructions get fetch-decode-encode-execute). 

It is just a set of instructions from memory and registers that tells what logical and arithmetic operations are to be performed. 

Registers :- Generally RISK-V contains fixed number of 32-bits base registers memory (x0-x31). It has several Advantages:

• decoding simpler
• instruction fetch predictable
• alignment easier
• pipeline design simpler

Some basic registers widely used for operations are :- 
1) x0 = It is always 0
2) x1 = Also known as ra (return address)
3) x2 = Also known as sp (stack pointer)
4) x10 = a0
5) x11 = a1

Load Words :-
1) lw(load from memory)
lw x3, 0(x1)
Memory → Register

Store Word:-
sw x3, 0(x1)
