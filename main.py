print("Basically RISK-V is an Instruction Set Architecture (ISA) that defines the instructions and rules that a compatible processor understands. It also defines the language between CPU and Software (How instructions get fetch-decode-encode-execute). \n")

print("It is just a set of instructions from memory and registers that tells what logical and arithmetic operations are to be performed. \n")

print("Registers :- Generally RISK-V contains fixed number of 32-bits base registers memory (x0-x31). It has several Advantages: \n")

print("•decoding simpler\n")
print("•instruction fetch predictable\n")
print("•alignment easier\n")
print("•pipeline design simpler\n")

print("Some basic registers widely used for operations are :- \n")
print("1 → x0= It is always 0\n")
print("2 → x1 = Also known as ra (return address\n")
print("3 → x2 = Also known as sp (stack pointer)\n")
print("4 → x10 = a0 (argument/return value)\n")
print("5 → x11 = a1 (argument/return value)\n")

print("Load Words :- \n")
print("lw(load from memory)\n")
print("lw x3, 0(x1)\n")
print("Loads data from memory into a register (Memory → Register)\n")

print("Store Word:-\n")
print("sw(store to memory)\n")
print("sw x3, 0(x1)\n")
print("Stores data from a register into memory\n")
print("(Register → Memory)\n")

print("In a Instruction format, there are different fields :-\n")

print("opcode | rd | rs1 | rs2 | funct3 | funct7 | immediate\n")

print("for example :- \n")
print("add x3, x1, x2\n")
print("    ↑    ↑    ↑\n")
print("    rd  rs1 rs2\n")

print("x1 = 2\n")
print("x2 = 3\n")
print("x3 = x1 + x2 = 5\n")

print("Types of Instruction format :-\n")
print("1 → R-type : generally register to register operations\n")
print("2 → I-type : One immediate value is involved\n")