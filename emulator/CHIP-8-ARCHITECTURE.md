Emulator: reads the original machine code instructions that were assembled for the target machine, interprets them, and then replicates the functionality of the target machine on that host machine

# CHIP-8 Description
> A good starting CPU to work on: 34 instructions, graphics are simple monochrome pixels, and sounds are just a single buzzer tone

- 16 8-bit registers
- 4K Bytes of Memory
    - 0x000-0x1FF
    - 0x050-0x0A0
    - 0x200-0xFFF
- 16-bit Index Register: special register used to store memory addresses for use in operations
- 16-bit Program Counter: is a special register that holds the address of the next instruction to execute. Again, it’s 16 bits because it has to be able to hold the maximum memory address (0xFFF).
- 16-Level Stack: keep track of the order of execution when it calls into functions, can hold 16 different PCs
- 8-bit Stack Pointer: to tell where in the 16 levels of stack the most recent value was placed
- 8-bit Delay Timer: given a value, will decrement at a rate of 60Hz
- 8-bit Sound Timer
- 16-bit Input Keys: match the hex values 0 to F
- 64x32 Monochrome Display Memory

a nibble = half a byte, exactly 4 bits
> CHIP-8 opcodes are 16-bit words typically described in four hex digits
# Fonts
- Characters are examples of sprites
# CPU Cycle
- Fetch the next instruction in the form of an opcode
- Decode the instruction to determine what operation needs to occur
- Execute the instruction

# C++ concepts:
- `typedef`: creates an alias (new name) for an existing data type to make complex types simpler and code more readable
    - example: For instance, `typedef unsigned int uint`; lets you write `uint my_number`; instead of `unsigned int my_number;`
- bitmask: a value (sequence of 0s and 1s) used in programming to perform bitwise operations, allowing efficient storage and manipulation of multiple true/false states or flags within a single integer
    - bitwise OR ( | )
    - bitwise AND ( & )
    - bitwise XOR ( ^ )

- Suffixes in numeric literals in C/C++:
    - __u__ or __U__ makes the literal unsigned int (e.g. 12u)
    - __l__ or __L__ : long, combine with u for unsigned
    - __ll__ or __LL__ : long long, combine with u for _unsigned_
    - __f__ or __F__: float


# Technical Reference
- http://devernay.free.fr/hacks/chip8/C8TECH10.HTM
- https://github.com/mattmikolay/chip-8/wiki/Mastering-CHIP%E2%80%908



