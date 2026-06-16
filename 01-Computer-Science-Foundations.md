# Pillar 1 — Computer Science Foundations

> *"You can't reason about systems you don't understand. You can only guess about them."*

---

## Table of Contents

1. [What Is a Program](#1-what-is-a-program)
2. [Compilation](#2-compilation)
3. [Interpretation](#3-interpretation)
4. [Machine Code](#4-machine-code)
5. [The CPU](#5-the-cpu)
6. [RAM — Random Access Memory](#6-ram)
7. [The Stack](#7-the-stack)
8. [The Heap](#8-the-heap)
9. [Processes](#9-processes)
10. [Threads](#10-threads)
11. [Concurrency](#11-concurrency)
12. [Parallelism](#12-parallelism)
13. [Blocking vs Non-Blocking](#13-blocking-vs-non-blocking)
14. [Synchronous vs Asynchronous](#14-synchronous-vs-asynchronous)
15. [Context Switching](#15-context-switching)
16. [Inter-Process Communication (IPC)](#16-inter-process-communication)

---

## 1. What Is a Program

### Definition

A program is a sequence of instructions stored in memory that a CPU can fetch, decode, and execute. At the machine level, a program is nothing more than a series of binary values arranged such that when fed into a processor, they produce a deterministic change in machine state.

The higher-level concept we call a "program" — the `.js` file, the `.py` file, the compiled binary — is an abstraction layered on top of that fundamental reality.

### Historical Context

In the 1940s, programming meant physically wiring circuits on the ENIAC to represent instructions. Memory and programs were one: the machine itself *was* the program. John von Neumann's 1945 architecture paper introduced the stored-program concept: instructions are data, stored in the same memory as data, fetched and executed sequentially by a central processor. Nearly every computer built since then follows this model.

This is why your JavaScript file, compiled bytecode, and machine instructions are all, at their core, just bits in memory. The abstraction changed; the substrate did not.

### Why It Exists / Problem It Solves

Humans cannot communicate directly with transistors. A program is a translation mechanism: it allows human intent to be expressed in a language that can be mechanically transformed into electrical signals that manipulate hardware.

The layering of abstractions — high-level language → bytecode → machine code → electrical signals → transistor state changes — exists because each layer solves a different problem:

- High-level languages make human reasoning tractable
- Compilers/interpreters make machine translation reliable
- Machine code makes hardware execution possible

### Internal Architecture of a Program in Memory

When a program is loaded and running, the operating system allocates a virtual address space and partitions it:

```
High Address
+---------------------------+
|         Stack             |  ← function call frames, local vars
|           ↓               |
|     (grows downward)      |
+---------------------------+
|                           |
|       (free space)        |
|                           |
+---------------------------+
|           ↑               |
|     (grows upward)        |
|         Heap              |  ← dynamically allocated memory
+---------------------------+
|    BSS Segment            |  ← uninitialized global/static vars
+---------------------------+
|    Data Segment           |  ← initialized global/static vars
+---------------------------+
|    Text Segment           |  ← compiled machine instructions (read-only)
+---------------------------+
Low Address
```

- **Text segment**: The actual compiled instructions. Read-only. If you try to write here, the OS raises a segmentation fault. This is where your functions live after compilation.
- **Data segment**: Global and static variables that have been initialized (`int x = 5;`).
- **BSS segment**: Global/static variables declared but not initialized. The OS zeroes these out.
- **Heap**: Dynamic allocations (`malloc`, `new`, object creation). Grows upward. You manage this manually in C/C++; in garbage-collected languages, the runtime manages it.
- **Stack**: Automatic storage. Grows downward. Holds function frames, return addresses, local variables.

### Step-by-Step: How a Program Runs

```
1. You invoke: `node server.js`

2. The OS creates a new PROCESS:
   - Allocates a virtual address space
   - Loads the Node.js executable into the text segment
   - Sets up stack and heap regions

3. Node.js parses server.js:
   - V8 JIT-compiles your JavaScript to machine code
   - Places compiled code in executable memory

4. The OS's SCHEDULER assigns CPU time to the process

5. The CPU begins the fetch-decode-execute cycle:
   - Fetch: Read next instruction from memory
   - Decode: Determine what instruction it is
   - Execute: Perform the operation
   - Update program counter to next instruction
   - Repeat

6. System calls occur when the program needs OS resources:
   - File read → `read()` syscall
   - Network socket → `socket()` / `accept()` syscalls
   - Memory → `mmap()` / `brk()` syscalls

7. Program terminates:
   - Exit code returned to parent process
   - OS reclaims all allocated memory
   - File descriptors closed
```

### How to Think About It

> Think of a program not as a file that "runs," but as a recipe that the CPU follows one instruction at a time. The CPU is a machine that does exactly one thing extremely fast: reads the next instruction, executes it, advances its internal pointer, and repeats. Everything else — concurrency, abstraction, "running" — is layered on top of that atomic loop.

### How Interviewers Attack This Topic

**Entry question**: "What happens when you run a Node.js script?"

Follow-up chain:
- Where does the code go in memory? → Text segment
- Where do local variables live? → Stack
- Where does `new Object()` go? → Heap
- What creates the isolation between two running Node processes? → Virtual address spaces managed by the OS
- What happens if one process tries to read another process's memory? → OS raises SIGSEGV (segmentation fault); virtual memory prevents this

---

## 2. Compilation

### Definition

Compilation is the process of translating source code written in a high-level language into a lower-level representation — typically machine code or an intermediate bytecode — *before* execution begins.

A **compiler** is a program that takes an entire source file (or set of files), performs multiple transformation passes, and produces an output artifact (binary, bytecode, assembly) that can be executed later.

### Historical Context

The first compiler was written by Grace Hopper in 1952 for the A-0 programming language. Before compilers, programmers wrote in assembly language — a thin mnemonic wrapper over machine code. Compilers made it possible to write in human-readable syntax and have the machine automatically generate machine code. This was considered almost impossible by many engineers at the time: the idea that a program could write programs.

FORTRAN (1957) was the first commercially successful compiled language. Its compiler, developed at IBM, proved that compiled code could be efficient enough for scientific computation — a benchmark that skeptics had considered impossible.

### Internal Architecture of a Compiler

A modern compiler is a multi-stage pipeline:

```
Source Code (.c, .ts, etc.)
         |
         v
+--------------------+
|    LEXER           |  → Tokenizes raw text into tokens
|  (Tokenization)    |     "int x = 5;" → [INT, IDENT(x), EQ, NUM(5), SEMI]
+--------------------+
         |
         v
+--------------------+
|    PARSER          |  → Builds Abstract Syntax Tree (AST)
|  (Syntactic)       |     Tokens → tree of nodes representing grammar
+--------------------+
         |
         v
+--------------------+
|  SEMANTIC ANALYSIS |  → Type checking, scope resolution, symbol table
|                    |     "x + 'hello'" → type error
+--------------------+
         |
         v
+--------------------+
|  IR GENERATION     |  → Intermediate Representation (e.g., LLVM IR)
|                    |     Platform-neutral code
+--------------------+
         |
         v
+--------------------+
|  OPTIMIZATION      |  → Dead code elimination, constant folding,
|                    |     inlining, loop unrolling
+--------------------+
         |
         v
+--------------------+
|  CODE GENERATION   |  → Target machine code (x86, ARM, WASM)
+--------------------+
         |
         v
  Object File (.o)
         |
         v
+--------------------+
|    LINKER          |  → Combines object files, resolves symbols,
|                    |     produces final executable
+--------------------+
         |
         v
  Executable Binary
```

### Why It Exists

Programs written in high-level languages are too far from machine instructions for the CPU to understand directly. The compiler bridges this gap while also performing optimizations that would be impossible to apply at runtime without significant overhead.

Key advantages of ahead-of-time compilation:
1. **Performance**: Optimizations run once at compile time, not every execution
2. **Error detection**: Type errors, undefined symbols, unreachable code detected before runtime
3. **Distribution**: Ship compiled binaries without exposing source code
4. **Platform targeting**: Same source, multiple targets (x86, ARM, WebAssembly)

### Compiler Optimizations (What Actually Happens to Your Code)

Understanding compiler optimizations is critical for reasoning about performance.

**Constant folding**: `int x = 2 * 3 + 1;` → compiler computes `7` at compile time. No multiplication at runtime.

**Dead code elimination**: Code that cannot be reached is removed from the output.

**Inlining**: Small functions are replaced at their call sites with their body. Eliminates function call overhead (stack frame creation, return address push).

**Loop unrolling**: Instead of looping 4 times, emit 4 copies of the body. Reduces branch instructions.

**Register allocation**: Compiler decides which variables live in CPU registers (fastest) vs. stack (slower) vs. memory (slowest).

### Implementation Example 1 — Observing Compilation (TypeScript → JavaScript)

```typescript
// source.ts — TypeScript source

interface User {
  id: number;
  name: string;
}

function greet(user: User): string {
  // TypeScript type annotation — this is compile-time only
  // It will NOT appear in the emitted JavaScript
  const message: string = `Hello, ${user.name}`;
  return message;
}

const result = greet({ id: 1, name: "Harish" });
console.log(result);
```

After TypeScript compilation (`tsc source.ts`):

```javascript
// source.js — Compiled output (type information STRIPPED)
// This is what actually runs

"use strict";

function greet(user) {
  // Notice: no type annotations, no interface
  // The compiler removed all type information
  // TypeScript types ONLY exist at compile time
  const message = `Hello, ${user.name}`;
  return message;
}

const result = greet({ id: 1, name: "Harish" });
console.log(result);
```

This illustrates a crucial concept: **TypeScript's type system does not exist at runtime**. If you pass the wrong type to `greet` at runtime, JavaScript will not catch it — only the TypeScript compiler does, and only when it runs.

### Implementation Example 2 — Understanding What the Compiler Sees (C to Assembly)

```c
// simple.c — A function that adds two numbers
int add(int a, int b) {
    int result = a + b;
    return result;
}

int main() {
    int x = add(3, 4);
    return 0;
}
```

Compiling with `gcc -O0 -S simple.c` (no optimization, output assembly):

```asm
; simple.s — x86-64 Assembly output (simplified)
; This is what the CPU actually understands

add:
    push    rbp              ; Save base pointer (save caller's frame)
    mov     rbp, rsp         ; Set up new stack frame
    mov     DWORD PTR [rbp-4], edi   ; Store argument 'a' on stack
    mov     DWORD PTR [rbp-8], esi   ; Store argument 'b' on stack
    mov     edx, DWORD PTR [rbp-4]   ; Load 'a' into register edx
    mov     eax, DWORD PTR [rbp-8]   ; Load 'b' into register eax
    add     eax, edx         ; Add a + b, result in eax
    mov     DWORD PTR [rbp-12], eax  ; Store result on stack
    mov     eax, DWORD PTR [rbp-12] ; Load result into return register
    pop     rbp              ; Restore caller's frame
    ret                      ; Return (jump to return address on stack)

main:
    push    rbp
    mov     rbp, rsp
    sub     rsp, 16          ; Allocate 16 bytes on stack for locals
    mov     esi, 4           ; Second argument: 4
    mov     edi, 3           ; First argument: 3
    call    add              ; Push return address, jump to add
    mov     DWORD PTR [rbp-4], eax   ; Store return value (x = result)
    mov     eax, 0           ; Return 0 from main
    leave                    ; Restore stack
    ret
```

Every function call creates a stack frame. Every local variable is a position on the stack. The `add eax, edx` line is the actual addition. Understanding this lets you explain why function call overhead exists, what a stack overflow is, and how tail-call optimization works.

### Performance Characteristics

| Aspect | Compiled (C/Go/Rust) | JIT Compiled (Java/V8) | Interpreted (early Python) |
|---|---|---|---|
| Startup time | Near-zero | Slow (JIT warmup) | Fast |
| Peak throughput | Highest | Near-native after warmup | Lowest |
| Memory footprint | Lowest | Medium (JIT metadata) | Variable |
| Portability | Per-target binary | Write once, run anywhere | Write once, run anywhere |
| Debug info | Stripped in release | Available | Available |

### Common Misconceptions

**"JavaScript is interpreted, not compiled."**
False since V8 was released (2008). JavaScript is compiled to machine code by V8's JIT compiler. It goes through parsing → AST → Ignition bytecode → TurboFan optimized machine code. Modern JavaScript execution is not interpretation.

**"Compiled code is always faster."**
Not necessarily. JIT compilers can observe actual runtime behavior (which branches are taken, which types are used) and make optimizations that an ahead-of-time compiler cannot. Java can sometimes outperform C++ for long-running server workloads.

**"TypeScript catches runtime errors."**
TypeScript only catches errors at compile time. After compilation to JavaScript, all type information is gone. A TypeScript program can throw runtime errors that the type system "said" couldn't happen — because the type annotations were lies, or because runtime values came from untyped external sources (JSON from an API, for example).

---

## 3. Interpretation

### Definition

Interpretation is the process of executing source code (or an intermediate form like bytecode) **at runtime**, translating and executing instructions one by one (or in small batches) without producing a separate compiled artifact.

An **interpreter** is a program that reads source code, parses it, and directly executes the semantics described. There is no separate compilation step — or at least, no compilation to native machine code.

### The Compiler-Interpreter Spectrum

The distinction between "compiled" and "interpreted" is not binary. It's a spectrum:

```
Pure Interpretation          Hybrid                    Pure Compilation
      |                         |                              |
      v                         v                              v
Early BASIC             Python (CPython)               C / C++ / Rust
AWK                     Ruby (YARV)                    Go
                        Java (JVM bytecode)
                        JavaScript (V8)
                        Lua
                             |
                             v
                      JIT Compilation
                      (bytecode → machine code at runtime)
                      Java HotSpot, V8 TurboFan, LuaJIT
```

Modern "interpreted" languages almost universally involve:
1. Compilation to bytecode (still faster to interpret than source)
2. JIT compilation of hot paths (frequently executed bytecode → machine code)

### How CPython Interprets Python

CPython (the reference Python implementation) uses a two-phase approach:

```
Python Source (.py)
        |
        v
+------------------+
|    PARSER        |  → Builds AST
+------------------+
        |
        v
+------------------+
|   COMPILER       |  → AST → Bytecode (.pyc)
+------------------+
        |
        v
+------------------+
|    EVAL LOOP     |  → CPython's main loop reads and executes
|  (ceval.c)       |     each bytecode instruction, one at a time
+------------------+
        |
        v
  Results / Side Effects
```

CPython's evaluation loop is literally a `switch` statement in C that dispatches on the opcode of each bytecode instruction. Every Python `for` loop, every `+` operation, every function call passes through this dispatcher. This is why Python is slower than C — not because "Python is slow," but because every operation has an extra layer of dispatch that C does not.

### Implementation Example 1 — What Python Bytecode Looks Like

```python
# source.py

def add(a, b):
    result = a + b
    return result

x = add(3, 4)
```

Examining the bytecode with Python's `dis` module:

```python
import dis

def add(a, b):
    result = a + b
    return result

# Disassemble the add function
dis.dis(add)
```

Output:
```
  3           0 LOAD_FAST                0 (a)
              2 LOAD_FAST                1 (b)
              4 BINARY_ADD
              6 STORE_FAST               2 (result)

  4           8 LOAD_FAST                2 (result)
             10 RETURN_VALUE
```

The Python interpreter's eval loop processes these opcodes in sequence:
- `LOAD_FAST 0`: Push local variable `a` onto the value stack
- `LOAD_FAST 1`: Push local variable `b` onto the value stack
- `BINARY_ADD`: Pop two values, add them, push result
- `STORE_FAST 2`: Pop top of stack, store into local `result`
- `LOAD_FAST 2`: Push `result` onto stack
- `RETURN_VALUE`: Pop top of stack and return it to caller

This is not machine code. This is CPython's virtual machine instruction set. CPython translates these into C function calls, which become machine code. Hence: two levels of indirection compared to compiled C.

### Implementation Example 2 — JavaScript Interpretation vs. JIT (Observing V8)

```javascript
// This code starts interpreted, then gets JIT-compiled

function sumArray(arr) {
  let total = 0;
  for (let i = 0; i < arr.length; i++) {
    total += arr[i];
  }
  return total;
}

// First call: V8 uses Ignition (interpreter/bytecode)
// It collects "type feedback": arr contains numbers
const small = [1, 2, 3];
console.log(sumArray(small));

// After many calls with the same types, V8's TurboFan JIT kicks in
// It compiles sumArray assuming arr contains only numbers
// The compiled version may use SIMD instructions for array summation
const large = new Array(1000000).fill(1);
for (let i = 0; i < 1000; i++) {
  sumArray(large); // V8 sees "hot path", triggers JIT compilation
}

// NOW: if you pass a mixed array, V8 must "deoptimize"
// and fall back to the slower interpreted version
const mixed = [1, "two", 3]; // type violation!
console.log(sumArray(mixed)); // deoptimization occurs here
```

This is why **type consistency in JavaScript is a performance concern**, not just a style concern. V8's JIT compiler makes assumptions about types. Violating those assumptions causes deoptimization — a performance cliff.

### How to Think About It

> Think of an interpreter as an actor who reads a script and performs each line immediately. Think of a compiler as a director who reads the entire script, prepares all blocking and props in advance, and then runs a polished, rehearsed performance. The interpreter is more flexible (it can decide what to do based on what happened earlier in the script), but the compiler's performance is much better because all preparation happened before showtime.

### Tradeoffs: Compilation vs. Interpretation

| Dimension | Compiled | Interpreted |
|---|---|---|
| Startup time | Fast (code is already machine instructions) | Slow (must parse and translate first) |
| Peak speed | Higher | Lower (per-instruction overhead) |
| Type errors | Caught at compile time | Only caught at runtime |
| Development speed | Slower (compile step) | Faster (run immediately) |
| Distribution | Binary (no source required) | Source or bytecode required |
| Debugging | Harder (source mapping required) | Easier (source line known) |
| Portability | Binary is platform-specific | Source runs anywhere with runtime |

### Common Misconceptions

**"Node.js runs JavaScript line by line."**
No. V8 parses the entire script, compiles it to Ignition bytecode, then executes bytecode. Hot functions are JIT-compiled to machine code. There is no "line by line" execution after the initial parse.

**"Python is slow because it's interpreted."**
Python is slower than C because each operation goes through CPython's eval loop dispatcher. This is a form of interpretation overhead, but modern Python (especially PyPy, which has a JIT) can approach C speeds for compute-heavy code. The bottleneck is the architecture, not some inherent property of "interpretation."

---

## 4. Machine Code

### Definition

Machine code is the set of instructions directly executable by a CPU without any further translation. It is expressed as binary values (typically viewed as hexadecimal) where each instruction encodes: an opcode (what operation to perform) and operands (where to find the data).

Machine code is entirely architecture-specific. x86 machine code will not run on an ARM processor and vice versa.

### Why It Exists

CPUs are transistor-based circuits. They understand only electrical signals — high voltage and low voltage, representing 1 and 0. Machine code is the bridge between human-readable operations (add, compare, jump) and the binary patterns that control the CPU's transistors.

Every program that ever ran on any computer ultimately executed as machine code. Every abstraction above it — assembly, C, Python, JavaScript — eventually boils down to machine instructions.

### Internal Architecture: Instruction Set Architecture (ISA)

The set of all instructions a CPU can execute is defined by its **Instruction Set Architecture (ISA)**. Common ISAs:

```
x86-64 (AMD64):  Desktop/server Intel and AMD CPUs
                 Little-endian
                 Complex Instruction Set (CISC)
                 Instructions are variable-length (1–15 bytes)

ARM64 (AArch64): Mobile (iPhone, Android), Apple Silicon (M1/M2)
                 Little-endian (usually)
                 Reduced Instruction Set (RISC)
                 Fixed 32-bit instruction width

RISC-V:          Open ISA, used in embedded systems, growing in HPC
                 Fixed 32-bit or 64-bit instruction width
                 Gaining academic/industry traction

WebAssembly:     NOT native CPU code — a portable binary format
                 Stack-based virtual ISA
                 Translated to native machine code by the browser
```

### Anatomy of an x86-64 Instruction

```
Machine instruction (in hex): 48 01 D8

Decoded:
  48    →  REX.W prefix (indicates 64-bit operand size)
  01    →  ADD opcode (add r/m64, r64)
  D8    →  ModRM byte:
            Mod=11 (register-to-register)
            Reg=011 (rbx — the source register)
            R/M=000 (rax — the destination register)

English: "Add the 64-bit value in register rbx to register rax"
```

### The Fetch-Decode-Execute Cycle in Detail

```
CPU Internal State:
  Program Counter (PC) / Instruction Pointer (IP): points to next instruction
  Registers: rax, rbx, rcx, rdx, rsi, rdi, rbp, rsp, r8-r15 (x86-64)
  Flags Register: Zero, Carry, Overflow, Sign, etc.
  ALU: Arithmetic Logic Unit — performs add, sub, and, or, xor, etc.

Cycle:
  1. FETCH
     - CPU reads bytes at address stored in PC from L1 instruction cache
     - If not in cache: L2 → L3 → RAM (orders of magnitude slower)
     - These bytes are placed in the instruction register

  2. DECODE
     - Instruction decoder circuit determines the opcode and operands
     - For CISC (x86): variable-length instructions make this complex
     - For RISC (ARM): fixed-length makes this simpler

  3. EXECUTE
     - ALU performs the computation (add, subtract, compare)
     - Memory unit accesses RAM if needed (load/store instructions)
     - Jump unit updates PC if it's a branch instruction

  4. WRITE BACK
     - Result is written to destination register or memory
     - Flags register is updated

  5. PC is incremented to next instruction (or set by a jump)
  6. Return to step 1
```

### Memory Hierarchy and Its Impact on Machine Code Performance

Understanding this is critical for senior-level performance discussions:

```
+-------------------+----------+----------+-------+
| Level             | Size     | Latency  | Type  |
+-------------------+----------+----------+-------+
| Registers         | ~1 KB    | 0 cycles | On-die|
| L1 Cache          | 32–64 KB | 4 cycles | On-die|
| L2 Cache          | 256 KB–1 | 12 cycles| On-die|
|                   | MB       |          |       |
| L3 Cache          | 8–32 MB  | 40 cycles| On-die|
| RAM               | 8–64 GB  | 200 cycle| DIMM  |
| SSD (NVMe)        | 1–4 TB   | ~100 µs  | PCIe  |
| HDD               | 1+ TB    | ~10 ms   | SATA  |
+-------------------+----------+----------+-------+
```

A single cache miss that causes a RAM access costs **~200 CPU cycles**. At 3GHz, that's ~66 nanoseconds. A tight loop iterating over an array that fits in L1 cache might run at 1 instruction per cycle. The same loop over data scattered in RAM might run 200x slower — not because the algorithm changed, but because of memory access patterns.

This is why **data locality** is a fundamental optimization principle and why linked lists have worse performance than arrays for sequential access despite identical algorithmic complexity.

### How to Think About It

> Machine code is the only real language. Everything above it — JavaScript, Python, Java, C# — is elaborate machinery whose only purpose is to produce machine code that the CPU can execute. Understanding machine code helps you understand why things that look equivalent in a high-level language can have wildly different performance characteristics. The compiler or runtime sees through the abstraction to the machine code, and so should you.

---

## 5. The CPU

### Definition

A Central Processing Unit (CPU) is the primary circuit in a computer responsible for executing instructions. It coordinates the fetch-decode-execute cycle, manages register state, interfaces with memory, and controls the flow of data through the system.

Modern CPUs are not single sequential processors — they contain multiple cores, instruction pipelines, branch predictors, speculative execution units, and multiple cache levels. Understanding the CPU is understanding why your code runs the way it does.

### Historical Context

Intel's 4004 (1971): 4-bit, single-core, 2300 transistors, 740 KHz.
Intel 8086 (1978): 16-bit, introduced the x86 ISA that still runs today.
Intel Pentium (1993): Superscalar — multiple execution units, pipelining.
AMD Athlon 64 (2003): 64-bit consumer CPUs, x86-64 standard.
Intel Core 2 Duo (2006): First widely used multi-core desktop CPU.
Apple M1 (2020): ARM-based, unified memory architecture, high performance-per-watt.

### Internal Architecture

```
+---------------------------------------------------------------+
|                          CPU DIE                              |
|                                                               |
|  Core 0                    Core 1                            |
|  +-------------------+     +-------------------+             |
|  | Pipeline Stages   |     | Pipeline Stages   |             |
|  | +---------+       |     | +---------+       |             |
|  | | Fetch   |       |     | | Fetch   |       |             |
|  | +---------+       |     | +---------+       |             |
|  | | Decode  |       |     | | Decode  |       |             |
|  | +---------+       |     | +---------+       |             |
|  | | Execute |       |     | | Execute |       |             |
|  | |  (ALU)  |       |     | |  (ALU)  |       |             |
|  | +---------+       |     | +---------+       |             |
|  | | Memory  |       |     | | Memory  |       |             |
|  | +---------+       |     | +---------+       |             |
|  | | Write-  |       |     | | Write-  |       |             |
|  | | Back    |       |     | | Back    |       |             |
|  | +---------+       |     | +---------+       |             |
|  |                   |     |                   |             |
|  | L1 I-Cache 32KB   |     | L1 I-Cache 32KB   |             |
|  | L1 D-Cache 32KB   |     | L1 D-Cache 32KB   |             |
|  | L2 Cache 256KB    |     | L2 Cache 256KB    |             |
|  +-------------------+     +-------------------+             |
|                                                               |
|  Shared L3 Cache (8 MB)                                      |
|                                                               |
|  Memory Controller → RAM Slots                               |
|  PCIe Controller   → GPU, NVMe SSD                          |
+---------------------------------------------------------------+
```

### Pipeline and Superscalar Execution

Modern CPUs do not execute one instruction per clock cycle. They use **pipelining**: breaking instruction execution into stages so multiple instructions can be in-flight simultaneously.

A classic 5-stage pipeline:

```
Clock:  1    2    3    4    5    6    7    8
Inst 1: F    D    E    M    W
Inst 2:      F    D    E    M    W
Inst 3:           F    D    E    M    W
Inst 4:                F    D    E    M    W
Inst 5:                     F    D    E    M   W

F=Fetch, D=Decode, E=Execute, M=Memory, W=WriteBack

At clock 5, all 5 instructions are in different stages simultaneously.
```

Modern out-of-order, superscalar CPUs can execute multiple instructions per clock cycle across multiple execution units. A modern x86 CPU can issue 4–6 instructions per cycle and have hundreds of instructions in flight at once.

### Branch Prediction

When the CPU encounters a conditional branch (`if`/`else`), it doesn't wait to see which direction it goes — it *predicts* and speculatively executes. If the prediction is correct, the work is kept. If wrong (branch misprediction), the speculative work is discarded and the correct path is taken. This is called a **pipeline flush** and costs 15–20 cycles.

```javascript
// This code has predictable branches — the branch predictor succeeds
const arr = new Array(1000000).fill(1);
let sum = 0;
for (let i = 0; i < arr.length; i++) {
  if (arr[i] > 0) {  // Always true — predictor learns this quickly
    sum += arr[i];
  }
}

// This code has unpredictable branches — branch predictor fails frequently
const random = Array.from({length: 1000000}, () => Math.random() > 0.5 ? 1 : -1);
let sum2 = 0;
for (let i = 0; i < random.length; i++) {
  if (random[i] > 0) {  // 50% unpredictable — predictor fails ~50% of time
    sum2 += random[i];
  }
}
// sum2 loop can be significantly slower due to branch mispredictions
```

This is observable in production. Sorted arrays iterate faster than unsorted arrays in branch-heavy code — not because sorting improves the algorithm, but because it makes branch prediction more accurate.

### Speculative Execution and Security (Spectre/Meltdown)

**Speculative execution** is why Spectre (2018) and Meltdown (2018) vulnerabilities exist. The CPU speculatively executes code down a predicted branch and *loads memory* before confirming the branch was correct. By timing cache access patterns, an attacker can read memory the speculative execution loaded — memory they should not have access to.

This is why your browser has been slower since early 2018 — mitigations like site isolation and disabled high-resolution timers were deployed to reduce the attack surface. These mitigations have performance costs.

### How to Think About It

> The CPU is not a simple sequential machine any more. Think of it as a highly parallel, speculative, predictive system that is constantly doing work ahead of time and discarding it if the prediction was wrong. Your code doesn't just *execute* — it races against its own predictions. When you write predictable, cache-friendly code, you are cooperating with the CPU's prefetcher and branch predictor. When you write unpredictable, scattered code, you are fighting those systems.

---

## 6. RAM

### Definition

RAM (Random Access Memory) is volatile, byte-addressable storage that the CPU uses to hold the instructions and data of running programs. "Random access" means any address can be read or written in approximately equal time — unlike a tape drive, which must seek sequentially.

"Volatile" means RAM loses its contents when power is removed.

### Why RAM Exists

Registers (inside the CPU) are extremely fast but extremely limited — typically 16–32 registers, each 8 bytes = ~256 bytes total. RAM provides gigabytes of working space. The tradeoff: RAM is ~200× slower than registers.

RAM is the medium of program execution. Everything that is "running" on a computer lives in RAM: instructions, stack frames, heap objects, OS kernel structures, device driver code.

### Physical Architecture

Modern DDR5 RAM is organized as:

```
RAM Module (DIMM)
  └── Ranks (1–4)
        └── Banks (8–16)
              └── Rows × Columns of capacitors
                    └── Each capacitor = 1 bit
```

Reading from RAM requires:
1. Selecting a row (activating it — charges all capacitors in row)
2. Selecting a column (reading the value)
3. Precharging the row (resetting for next access)

This "row activation" cycle is why sequential memory reads are faster than random reads: reading adjacent addresses in the same row avoids repeated row activation.

### Virtual Memory (Critical for Interview Discussions)

The RAM your program sees is **not** physical RAM. It is **virtual address space** — an abstraction provided by the OS.

```
Program A thinks it has:       Program B thinks it has:
0x0000 to 0xFFFF...            0x0000 to 0xFFFF...
(full 64-bit address space)    (full 64-bit address space)

In reality:
Physical RAM: 16 GB

OS Memory Mapper (MMU):
  Program A virtual 0x7fff0000 → Physical 0x000a3000
  Program B virtual 0x7fff0000 → Physical 0x04f21000
  (completely different physical addresses)
```

This is enforced by the **Memory Management Unit (MMU)**, hardware in the CPU that translates virtual addresses to physical addresses using page tables.

**Key implications**:
- Programs cannot read each other's memory (unless OS explicitly allows it)
- A program can "allocate" more virtual memory than exists as physical RAM (the OS swaps pages to disk)
- A pointer value in your program is a **virtual address**, not a physical location

### How to Think About It

> Think of RAM as an enormous array, indexed by address. Virtual memory means every running program has its own private copy of this array, starting at 0 — but the OS and CPU hardware are secretly translating those indexes to shared physical locations. Programs don't see each other in this array. The OS acts as the translator between each program's private view and the shared physical reality.

---

## 7. The Stack

### Definition

The stack is a region of memory automatically managed by the CPU and OS, used to store function call frames, local variables, return addresses, and saved register values. It operates as a LIFO (Last In, First Out) structure and grows downward in virtual memory.

### Why It Exists

Functions need memory for their local variables. That memory must exist for the duration of the function call and be automatically reclaimed when the function returns. The stack provides this automatically: when a function is called, a **stack frame** is pushed; when it returns, the frame is popped. No manual memory management required.

### Anatomy of a Stack Frame

When `main()` calls `add(3, 4)`:

```
Higher addresses (stack bottom, set at program start)
+---------------------------+
|  OS / Kernel space        |
+---------------------------+
|  main()'s stack frame     |
|  +-----------------------+|
|  | Return address        ||  ← where to jump when main returns
|  | Saved rbp             ||  ← caller's base pointer
|  | Local var: x = ?      ||  ← will receive add's return value
|  +-----------------------+|
+---------------------------+
|  add()'s stack frame      |
|  +-----------------------+|
|  | Return address        ||  ← address in main to jump back to
|  | Saved rbp             ||  ← main's base pointer
|  | Param a = 3           ||
|  | Param b = 4           ||
|  | Local: result = 7     ||
|  +-----------------------+|
+---------------------------+  ← rsp (stack pointer) points here
|      (free stack space)   |
|                           |
Lower addresses (stack grows downward)
```

The **stack pointer (RSP on x86-64)** always points to the top of the current stack. Pushing decrements RSP; popping increments it.

### Implementation: Observing Stack Behavior in JavaScript

```javascript
// JavaScript uses a call stack managed by the V8 engine
// Functionally identical to native stack behavior

function third() {
  // At this point, the call stack contains:
  // [main context] → first() → second() → third()
  console.trace(); // Prints the current call stack
  throw new Error("Stack trace demo");
}

function second() {
  third();
}

function first() {
  second();
}

try {
  first();
} catch (e) {
  console.log(e.stack);
  // Error: Stack trace demo
  //   at third (file.js:4)
  //   at second (file.js:10)
  //   at first (file.js:14)
  //   at Object.<anonymous> (file.js:18)
}
```

### Stack Overflow: The Real Mechanics

```javascript
// This causes a stack overflow
function infinite() {
  return infinite(); // Each call pushes a new frame
  // No base case means frames accumulate until the stack is exhausted
}

try {
  infinite();
} catch (e) {
  console.log(e.message); // "Maximum call stack size exceeded"
}

// Why does this happen?
// Default stack sizes:
//   Browser (Chrome): ~10,000–15,000 frames
//   Node.js: ~10,000–15,000 frames
//   C program: default 8MB stack
//   When exhausted: OS sends SIGSEGV or VM throws RangeError
```

### Stack vs. Heap — The Fundamental Comparison

| Property | Stack | Heap |
|---|---|---|
| Management | Automatic (CPU/compiler) | Manual (C) or GC (JS/Java/Go) |
| Speed | Very fast (just move pointer) | Slower (find free block, bookkeeping) |
| Size | Small (8MB typical) | Large (limited by RAM/virtual space) |
| Lifetime | Limited to function scope | Until explicitly freed or GC'd |
| Fragmentation | None (LIFO) | Yes (holes from allocate/free cycles) |
| Thread sharing | Per-thread (each thread has own stack) | Shared across threads |
| Overflow behavior | Crash (SIGSEGV / RangeError) | `malloc` returns NULL / OOM exception |

### Implementation: Understanding Scope and Stack in Practice

```javascript
// This demonstrates why "var" and "let" behave differently
// regarding scope — which maps to stack frame lifetime

function demonstrateScope() {
  var x = 1; // var: function-scoped — lives for entire function frame
  
  if (true) {
    var y = 2;  // var: ALSO function-scoped — same frame as x
    let z = 3;  // let: block-scoped — conceptually limited to this block's frame
    
    console.log(x, y, z); // 1 2 3
  }
  
  console.log(x, y); // 1 2  ← y is accessible because var = function scope
  // console.log(z); // ReferenceError: z is not defined
  // z was "in" the inner block frame; it's out of scope here
}

// The real mechanism:
// JavaScript engines track binding lifetimes.
// var bindings are hoisted to function scope.
// let/const bindings are NOT hoisted beyond their block.
// The engine doesn't literally create separate stack frames for each block
// in JS (it manages variables in a more complex way),
// but the *semantic* behavior mirrors stack frame lifetime.
```

### How Interviewers Attack This Topic

**Question**: "What is a stack overflow?"

Follow-up chain:
- "What exactly gets put on the stack?" → Return address, saved registers, local variables, function arguments
- "Why does the stack have a size limit?" → OS allocates a fixed virtual memory region for it; growing it requires kernel intervention
- "How does the CPU know a function is done?" → It reads the return address from the top of the current frame, jumps there, then the compiler-generated code restores the stack pointer
- "Can you increase the stack size?" → Yes, in C: `ulimit -s unlimited` or `setrlimit(RLIMIT_STACK, ...)`. In Node.js: `--stack-size=N` flag
- "What's a tail call and why does it matter?" → A tail call is a function call that is the very last operation in a function. The current frame can be *replaced* rather than pushed, preventing stack growth. ES6 specifies tail call optimization; V8 removed support for it due to debuggability concerns.

---

## 8. The Heap

### Definition

The heap is a region of memory used for **dynamic allocation** — memory whose size or lifetime cannot be determined at compile time. Unlike the stack, heap memory is not automatically managed by the CPU; it must be explicitly allocated and freed (in manual memory languages) or managed by a garbage collector (in automatic memory languages).

### Why Dynamic Allocation Exists

Stack allocation works when you know, at compile time, how much memory a function needs. But what about:

- Arrays that grow based on user input
- Objects created based on runtime conditions
- Data that must outlive the function that created it

These cannot go on the stack. The heap provides a large, shared memory pool from which programs can request arbitrary amounts at runtime.

### How Heap Allocation Works

The OS gives the program a large chunk of virtual memory for the heap. The program's **memory allocator** (malloc in C, the V8 heap in Node.js) manages this chunk:

```
Program's heap region (example: 1 GB virtual address space)

+-----------------------------------------------+
|   Allocator Metadata   |  Object A  |  free   |  Object B  |  free  |
|   (free lists, etc.)   |  (100 B)   |  (50B)  |  (200 B)   |  (300B)|
+-----------------------------------------------+
                          ^            ^
                          ptr1         ptr2  ← your pointers point here
```

When you call `new Object()` in JavaScript (or `malloc()` in C):
1. Allocator searches its free list for a block large enough
2. Marks that block as used
3. Returns a pointer to it
4. Updates bookkeeping metadata

When the object is freed (or GC'd):
1. Allocator marks that region as free again
2. May merge adjacent free blocks (coalescing) to reduce fragmentation

### Memory Fragmentation

```
Initial state:  [AAAA][BBBB][CCCC][DDDD][free.........free]

Free B and D:   [AAAA][....][CCCC][....][free.........free]

Now try to allocate 8 bytes (size of B+D combined):
The total free space is 8 bytes, but it's in two separate holes.
A contiguous 8-byte allocation FAILS even though enough total space exists.
This is fragmentation.
```

Garbage collectors in V8, JVM, etc. run **compaction** phases to defragment the heap, sliding all live objects together and creating one large contiguous free region.

### V8 Heap Architecture (Critical for Node.js/JavaScript Interviews)

V8 does not use a simple undivided heap. It uses a **generational garbage collection** model based on the observation that most objects die young (the "generational hypothesis"):

```
V8 Heap Layout:

+------------------+----------------------------------+----------+
|  New Space       |         Old Space                |  Large   |
|  (Young Gen)     |         (Old Gen)                |  Object  |
|                  |                                  |  Space   |
|  [From] [To]     |  [Old Data] [Old Pointer]        |          |
|  Small &         |  Long-lived objects              |  >256 KB |
|  short-lived     |  survived 2+ GC cycles           |  objects |
|  objects start   |                                  |          |
|  here            |                                  |          |
+------------------+----------------------------------+----------+

Also:
  Code Space:     Compiled JIT code
  Map Space:      Object shape descriptors (hidden classes)
  Large Object Space: Objects too big for fixed-size pages
```

**Scavenge GC (Minor GC)**: Runs frequently (~every few MB of allocation). Only processes New Space. Fast because it only looks at new objects.

**Mark-Sweep-Compact GC (Major GC)**: Runs infrequently. Processes Old Space. Pauses the program. The "GC pause" that causes jank in JavaScript applications.

### Implementation: Heap Allocation and Garbage Collection in JavaScript

```javascript
// Example 1: Understanding when objects are allocated on the heap

function processRequest(userId) {
  // This object is allocated on the V8 heap (New Space)
  const user = {
    id: userId,
    timestamp: Date.now(),
    data: new Array(1000).fill(0) // array also heap-allocated
  };

  // The 'user' reference is on the stack (as a local variable)
  // But the object it POINTS TO is on the heap

  return user.data.reduce((sum, x) => sum + x, 0);
  
  // After this function returns:
  // - The local 'user' variable is popped off the stack
  // - If nothing outside this function holds a reference to the object,
  //   it becomes eligible for garbage collection
  // - V8's minor GC will collect it in New Space
}

// This is why the following pattern can cause memory leaks:
const cache = {}; // Global object — lives forever (not GC'd)

function leakyProcess(userId) {
  const user = {
    id: userId,
    data: new Array(1000000).fill(0) // 1M elements!
  };
  
  cache[userId] = user; // We store a reference in a global!
  // Now 'user' will NEVER be garbage collected as long as 'cache' exists
  // This is a memory leak
}

// Call this enough times and your process runs out of memory
for (let i = 0; i < 10000; i++) {
  leakyProcess(i);
}
```

```javascript
// Example 2: Production-style memory management
// Using WeakMap to avoid memory leaks

// Problem: Storing metadata about DOM nodes (or any objects)
// without preventing those objects from being garbage collected

const metadata = new WeakMap(); // Keys are held WEAKLY
// If the key object has no other references, GC can collect it
// AND the WeakMap entry is automatically removed

function attachMetadata(node, data) {
  metadata.set(node, data); // node is the key (held weakly)
}

function getMetadata(node) {
  return metadata.get(node);
}

// Simulated usage
let element = { id: 'button-1', text: 'Click me' }; // Would be a real DOM node
attachMetadata(element, { clickCount: 0, lastClicked: null });

console.log(getMetadata(element)); // { clickCount: 0, lastClicked: null }

element = null; // element is no longer referenced
// GC now can collect the original object
// The WeakMap entry will be automatically removed
// No memory leak!

// Regular Map would hold a strong reference:
const regularMap = new Map();
regularMap.set(element, { clickCount: 0 });
// Even if element = null, regularMap still holds reference
// → memory leak
```

### Garbage Collection Algorithms Deep Dive

**Mark and Sweep** (V8 Old Space, basis of many GC implementations):

```
Phase 1 — MARK:
  Start from "roots" (global variables, stack variables, registers)
  Traverse all reachable objects (BFS or DFS graph traversal)
  Mark each reached object as "live"

  Roots → Object A → Object B → Object D
       → Object C

  Object E has no path from roots → NOT marked (garbage)

Phase 2 — SWEEP:
  Scan entire heap
  Any unmarked object → add its memory to the free list

Phase 3 — COMPACT (optional):
  Move all live objects to one contiguous region
  Update all pointers to reflect new locations
  Eliminate fragmentation
```

**Reference Counting** (used in Python, Swift, Rust Rc<T>):

```
Every object has a reference count.
When a reference to an object is created: count++
When a reference goes out of scope or is reassigned: count--
When count reaches 0: immediately free the object

Problem: CIRCULAR REFERENCES
  A references B, B references A
  Nothing else references A or B
  Both counts are 1, never reach 0
  Memory leak → requires cycle detector
```

JavaScript uses tracing GC (not reference counting) specifically to handle circular references without explicit cycle detection passes.

### How to Think About It

> The heap is a shared pool of memory that multiple parts of your program can borrow from. The allocator is the pool manager: it tracks which chunks are in use and which are free. In manual memory languages (C), you must tell the manager when you're done with a chunk. In GC languages (JavaScript, Java), the manager has a robot (the GC) that periodically surveys the pool, identifies chunks nobody references anymore, and marks them as free. The GC robot's survey takes time — that's the GC pause.

---

## 9. Processes

### Definition

A process is an instance of a running program. It is the operating system's fundamental unit of resource ownership and isolation. A process has: a private virtual address space, one or more threads of execution, file descriptor table, signal handlers, and an associated user and group identity.

The OS is the authority that creates, schedules, and terminates processes. A process cannot exist outside the OS's management.

### Why Processes Exist

In early computing, only one program ran at a time. The CPU was fully devoted to that program. If the program crashed, the entire machine stopped. Processes were invented to solve multiple problems simultaneously:

1. **Isolation**: Programs cannot interfere with each other's memory
2. **Security**: Each process runs under a user identity with specific permissions
3. **Fault containment**: A crashed process doesn't crash others
4. **Multiplexing**: Multiple programs can share one CPU via time-sharing

### How the OS Creates a Process

```
fork() system call (POSIX):

Parent Process             Child Process
+------------------+       +------------------+
| PID: 1234        |       | PID: 5678        |
| Code: [program]  | ───→  | Code: [copy]     |
| Data: [values]   |       | Data: [copy]     |
| Files: [fds]     |       | Files: [copy]    |
| Stack: [frame]   |       | Stack: [copy]    |
+------------------+       +------------------+

fork() returns 0 in child, child's PID in parent
Child is exact copy (with copy-on-write optimization)
```

On Linux, `fork()` uses **copy-on-write (CoW)**: instead of actually copying all pages immediately, the parent and child share the same physical memory pages marked read-only. Only when either process writes to a page does the OS create a real copy. This makes `fork()` very fast even for large processes.

```javascript
// Node.js process example
const { fork } = require('child_process');
const path = require('path');

// Parent process creates a child process
// (Node uses fork() under the hood on Linux)
const child = fork(path.join(__dirname, 'worker.js'));

// The child has its own isolated memory space
// Communication happens via IPC (message passing)
child.send({ type: 'compute', data: [1, 2, 3, 4, 5] });

child.on('message', (result) => {
  console.log('Child computed:', result);
});

child.on('exit', (code) => {
  console.log(`Child exited with code ${code}`);
});
```

```javascript
// worker.js — runs in a separate process with isolated memory
process.on('message', (msg) => {
  if (msg.type === 'compute') {
    const sum = msg.data.reduce((a, b) => a + b, 0);
    process.send({ result: sum });
  }
});
```

### Process State Machine

```
           fork()
             |
             v
         [CREATED]
             |
             v  (scheduled by OS)
         [RUNNING] ←────────────────────────────┐
             |                                   |
    ┌────────┴──────────┐                       |
    |                   |                       |
  I/O request        time slice               (scheduled again)
  or wait()          expires                     |
    |                   |                       |
    v                   v                       |
[BLOCKED/            [READY] ───────────────────┘
 WAITING]
    |
    | I/O completes
    v
  [READY]
    
From any state:
  kill signal → [TERMINATED/ZOMBIE]
  exit() → [TERMINATED/ZOMBIE]
  
A process stays as ZOMBIE until parent calls wait()
to read its exit code. Only then is it fully removed.
```

### Process vs. Thread

| Property | Process | Thread |
|---|---|---|
| Memory space | Private, isolated | Shared within process |
| Creation overhead | High (fork, CoW) | Low |
| Communication | IPC (pipes, sockets, shared memory) | Direct (shared memory) |
| Fault isolation | Crash doesn't affect others | Crash can kill entire process |
| Switching cost | High (full context switch) | Lower (partial context switch) |
| Parallelism | True parallelism possible | True parallelism (multi-core) |
| Security | Strong isolation | Weak (shared state) |
| Node.js analog | `child_process.fork()` | `worker_threads` |

### Implementation: Node.js Cluster Module (Multi-Process Pattern)

```javascript
// server.js — Production-grade multi-process Node.js server
// Uses the Cluster module to spawn one process per CPU core
// Each process independently accepts HTTP connections

const cluster = require('cluster');
const http = require('http');
const os = require('os');

const NUM_CPUS = os.cpus().length;
const PORT = 3000;

if (cluster.isPrimary) {
  // This is the master process
  console.log(`Primary process PID: ${process.pid}`);
  console.log(`Spawning ${NUM_CPUS} workers...`);

  // Spawn one worker per CPU core
  for (let i = 0; i < NUM_CPUS; i++) {
    const worker = cluster.fork();
    
    worker.on('message', (msg) => {
      // Workers can send messages back to primary
      console.log(`Worker ${worker.id}: ${JSON.stringify(msg)}`);
    });
  }

  // Restart crashed workers
  cluster.on('exit', (worker, code, signal) => {
    console.log(`Worker ${worker.id} died (code: ${code}). Restarting...`);
    cluster.fork(); // Replace the dead worker
  });

  // Optional: primary can aggregate stats from all workers
  setInterval(() => {
    const workers = Object.values(cluster.workers);
    workers.forEach(w => w.send({ type: 'stats_request' }));
  }, 30000);

} else {
  // This is a worker process
  // Workers share the same port (OS load-balances)
  
  let requestCount = 0;

  const server = http.createServer((req, res) => {
    requestCount++;
    
    // Each worker handles requests independently
    // No shared state between workers
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({
      worker: cluster.worker.id,
      pid: process.pid,
      requestCount
    }));
  });

  server.listen(PORT, () => {
    console.log(`Worker ${cluster.worker.id} (PID: ${process.pid}) listening on port ${PORT}`);
  });

  // Handle stats requests from primary
  process.on('message', (msg) => {
    if (msg.type === 'stats_request') {
      process.send({ requestCount, pid: process.pid });
    }
  });
}
```

---

## 10. Threads

### Definition

A thread is the smallest unit of execution within a process. Threads within the same process share the same virtual address space (code, heap, global data, file descriptors) but each has its own private call stack, program counter, and register state.

### Why Threads Exist

Processes provide isolation but at high cost. Creating a process requires copying memory structures, setting up new virtual address space, and OS-level bookkeeping. For many workloads, you want concurrent execution within a single program's address space — for example, one thread handling the UI, another fetching data from the network, another computing a hash.

Threads enable **concurrent execution within a process** with lower overhead than multiple processes.

### Thread Stack Layout

```
Process Virtual Address Space
+--------------------------------------------+
|  Text (code)  — SHARED by all threads      |
+--------------------------------------------+
|  Data / BSS   — SHARED by all threads      |
+--------------------------------------------+
|  Heap         — SHARED by all threads      |
+--------------------------------------------+
|  Thread 1 Stack  (8MB by default)          |
+--------------------------------------------+
|  Thread 2 Stack  (8MB by default)          |
+--------------------------------------------+
|  Thread 3 Stack  (8MB by default)          |
+--------------------------------------------+
|  ... (each thread gets its own stack)      |
+--------------------------------------------+
```

Each thread can read and write to the heap directly. This is both the power of threads (easy sharing) and their danger (race conditions).

### The Global Interpreter Lock (GIL) — Python

CPython has a **GIL**: a mutex (mutual exclusion lock) that prevents more than one Python thread from executing Python bytecode at a time. This means Python threads cannot achieve true CPU parallelism for CPU-bound work.

```
Thread 1: ──GIL acquire──EXECUTE──GIL release──GIL acquire──EXECUTE──
Thread 2:                          ──GIL acquire──EXECUTE──GIL release──

Despite multiple threads, only ONE runs Python bytecode at any time.
```

The GIL exists because CPython's memory management (reference counting) is not thread-safe. Removing it would require making all reference counting operations atomic — which has performance costs.

**Why does this matter for interviews?**
- Python threads are useful for I/O-bound concurrency (threads release the GIL during I/O waits)
- Python threads are *not* useful for CPU-bound parallelism (use `multiprocessing` module instead)
- Node.js has no GIL because V8's JavaScript execution model is single-threaded by design

### Node.js and Worker Threads

```javascript
// Node.js Worker Threads — true multi-thread parallelism
// Available in Node.js 10.5+ (stable in 12+)
// Workers have shared memory available, but default is message-passing

const { Worker, isMainThread, parentPort, workerData } = require('worker_threads');

if (isMainThread) {
  // Main thread: delegate CPU-intensive work to workers
  
  function computeInWorker(data) {
    return new Promise((resolve, reject) => {
      // Each Worker is a new V8 isolate sharing the process's OS resources
      // but with its own JS heap (no shared JS objects by default)
      const worker = new Worker(__filename, {
        workerData: data // serialized and passed to worker
      });
      
      worker.on('message', resolve);
      worker.on('error', reject);
      worker.on('exit', (code) => {
        if (code !== 0) reject(new Error(`Worker exited with code ${code}`));
      });
    });
  }

  // Run two CPU-intensive tasks in parallel
  const start = Date.now();
  Promise.all([
    computeInWorker({ array: new Array(10_000_000).fill(1), id: 1 }),
    computeInWorker({ array: new Array(10_000_000).fill(2), id: 2 }),
  ]).then(([result1, result2]) => {
    console.log(`Results: ${result1}, ${result2}`);
    console.log(`Time: ${Date.now() - start}ms`); // ~half the time of sequential!
  });

} else {
  // Worker thread: receives work via workerData, posts result via parentPort
  const { array, id } = workerData;
  
  // This runs in parallel with the main thread and other workers
  const sum = array.reduce((acc, val) => acc + val, 0);
  
  parentPort.postMessage(sum); // Send result back to main thread
}
```

```javascript
// Production pattern: Worker Thread Pool
// Avoid the overhead of creating/destroying workers per request

const { Worker } = require('worker_threads');
const os = require('os');

class WorkerPool {
  constructor(workerPath, size = os.cpus().length) {
    this.workerPath = workerPath;
    this.size = size;
    this.pool = [];       // idle workers
    this.queue = [];      // pending tasks
    
    // Pre-create all workers
    for (let i = 0; i < size; i++) {
      this._createWorker();
    }
  }

  _createWorker() {
    const worker = new Worker(this.workerPath);
    
    worker.on('message', (result) => {
      // Worker finished — invoke callback and return worker to pool
      if (worker._currentTask) {
        worker._currentTask.resolve(result);
        worker._currentTask = null;
      }
      
      // Process next queued task or return to idle pool
      if (this.queue.length > 0) {
        const task = this.queue.shift();
        this._assignTask(worker, task);
      } else {
        this.pool.push(worker); // Return to idle pool
      }
    });

    worker.on('error', (err) => {
      if (worker._currentTask) {
        worker._currentTask.reject(err);
        worker._currentTask = null;
      }
      // Replace dead worker
      this._createWorker();
    });

    this.pool.push(worker);
  }

  _assignTask(worker, task) {
    worker._currentTask = task;
    worker.postMessage(task.data);
  }

  run(data) {
    return new Promise((resolve, reject) => {
      const task = { data, resolve, reject };
      
      if (this.pool.length > 0) {
        // Idle worker available — assign immediately
        const worker = this.pool.pop();
        this._assignTask(worker, task);
      } else {
        // No idle workers — queue the task
        this.queue.push(task);
      }
    });
  }

  terminate() {
    this.pool.forEach(w => w.terminate());
  }
}

// Usage
const pool = new WorkerPool('./compute-worker.js', 4);
const results = await Promise.all([
  pool.run({ type: 'hash', data: 'large string 1' }),
  pool.run({ type: 'hash', data: 'large string 2' }),
  pool.run({ type: 'hash', data: 'large string 3' }),
]);
```

---

## 11. Concurrency

### Definition

Concurrency is the ability of a system to make progress on multiple tasks during overlapping time periods. Critically: concurrency does **not** require simultaneous execution. Multiple tasks can be concurrent by taking turns — interleaving their execution — on a single CPU core.

### The Core Idea

```
Sequential (no concurrency):
  Task A: ████████████████████████████████
  Task B:                                 ████████████████████████

Concurrent (single core, interleaved):
  Task A: ████  ████  ████  ████  ████
  Task B:     ██    ██    ██    ██

Parallel (multiple cores, simultaneous):
  Core 1: Task A: ████████████████████████
  Core 2: Task B: ████████████████████████
```

### Why Concurrency Matters for I/O-Bound Work

Consider a web server handling 1000 requests. Each request involves:
- Reading HTTP headers: 0.1ms CPU
- Database query: 10ms waiting for DB
- Reading HTTP body: 0.1ms CPU
- Sending response: 0.1ms CPU

If handled sequentially: 1000 × (10.3ms) = 10.3 seconds to handle all requests.
If handled concurrently (I/O waiting overlaps): ~10.3ms to handle all requests.

This is why Node.js can handle thousands of concurrent connections on a single core: while one request waits for a database response (I/O), the event loop processes other requests. CPU is barely used; the bottleneck is I/O latency, and concurrency hides that latency.

### Concurrency Problems: Race Conditions

Race conditions occur when the correctness of a program depends on the relative timing of concurrent operations.

```javascript
// Race condition example — simulating what happens in concurrent systems

let counter = 0;

// If two "threads" run this simultaneously:
function increment() {
  // This is NOT atomic — it's three operations:
  // 1. Read counter (load from memory)
  // 2. Add 1 (CPU computation)
  // 3. Write result back (store to memory)
  
  const temp = counter;  // Step 1: Read
  // Imagine a context switch happens HERE
  // Another thread also reads counter (gets same value!)
  counter = temp + 1;    // Step 3: Write (overwrites other thread's write!)
}

// Both threads read 0, both compute 1, both write 1
// Final value: 1 (should be 2!)

// In JavaScript, the event loop prevents this for JS code
// (single-threaded JS execution)
// But in Worker Threads with SharedArrayBuffer, it CAN happen:

const sharedBuffer = new SharedArrayBuffer(4);
const sharedArray = new Int32Array(sharedBuffer);

// In Worker 1:
sharedArray[0]++; // NOT atomic! Can race with Worker 2

// Solution: use Atomics
Atomics.add(sharedArray, 0, 1); // Atomic add — guaranteed race-free
```

### Concurrency Primitives

**Mutex (Mutual Exclusion Lock)**:
```
Thread 1: lock() → CRITICAL SECTION → unlock()
Thread 2:           (waiting for lock)          → lock() → CRITICAL SECTION → unlock()

Only one thread in the critical section at a time.
```

**Semaphore**: Like a mutex but allows N concurrent holders. Used to limit resource access (e.g., max 10 concurrent DB connections).

**Condition Variable**: Lets a thread wait until a condition is true, then be woken by another thread. Used in producer-consumer patterns.

**Channel (Go-style)**: Instead of sharing memory and locking it, threads communicate by passing messages through a channel. "Don't communicate by sharing memory; share memory by communicating."

---

## 12. Parallelism

### Definition

Parallelism is the simultaneous execution of multiple computations. True parallelism requires multiple processors or cores. Parallelism is a specific form of concurrency where the overlap is not just in time-slices but actual simultaneous execution.

### Amdahl's Law — The Ceiling on Parallel Speedup

Not all code can be parallelized. Amdahl's Law gives the theoretical maximum speedup:

```
Speedup = 1 / (S + (1 - S) / N)

Where:
  S = fraction of the program that is inherently sequential
  N = number of processors/cores

Example:
  If 20% of your program is sequential (cannot be parallelized)
  And you have 8 cores:

  Speedup = 1 / (0.2 + (0.8 / 8))
           = 1 / (0.2 + 0.1)
           = 1 / 0.3
           = 3.33×

  Even with INFINITE cores:
  Speedup = 1 / 0.2 = 5×

  The sequential 20% is the hard ceiling.
```

This is why "just add more cores" doesn't linearly scale. Programs have inherently sequential parts: initialization, final result aggregation, serial dependencies.

### When to Use Parallelism vs. Concurrency

| Situation | Use | Example |
|---|---|---|
| CPU-intensive, independent tasks | Parallelism | Image processing, cryptographic hashing, data compression |
| I/O-intensive, waiting tasks | Concurrency | Web server, database client, file operations |
| Mixed | Both | Web server (concurrent I/O) + background workers (parallel CPU) |
| Ordered data pipeline | Concurrency with back-pressure | Stream processing |

---

## 13. Blocking vs. Non-Blocking

### Definition

**Blocking** I/O: The calling thread suspends (blocks) execution until the I/O operation completes. The thread cannot do anything else while waiting.

**Non-blocking** I/O: The calling thread initiates the I/O operation and immediately gets control back. The thread can do other work while waiting, and is notified when the I/O completes.

### The System Call Level

```
Blocking I/O:

  Thread 1:  |──request──|─────────────WAITING─────────────|──process──|
  Thread 2:                                      |──request──|─────WAIT──|──process──|

  While waiting, the thread is suspended by the OS.
  CPU time is freed for other processes/threads.
  But this thread uses up a thread from your thread pool while blocked.


Non-Blocking I/O (with event notification):

  Thread 1:  |──request──|──do other work───────────────|──callback──|
                         ↕ (kernel handles I/O)
  Kernel:               |─────────────────────────async──|

  epoll/kqueue/IOCP: kernel mechanisms that watch many I/O fds
  and notify the thread when any become ready
```

### The C10K Problem and Why Non-Blocking Matters

In 1999, Dan Kegel wrote "The C10K Problem": how do you handle 10,000 simultaneous connections? The answer of the time — one thread per connection — doesn't scale because:

- Each OS thread uses 1–8 MB of stack memory
- 10,000 threads × 1 MB = 10 GB of memory just for stacks
- Thread context switching overhead becomes prohibitive
- Most threads are just blocking on I/O anyway

Non-blocking I/O with event notification (select → poll → epoll on Linux) allows a **single thread** to manage thousands of connections by:
1. Registering interest in multiple file descriptors
2. Calling `epoll_wait()` — blocks until ANY fd is ready
3. Processing the ready fd(s)
4. Returning to wait

This is exactly what libuv does for Node.js. One thread, thousands of connections.

### Implementation: Blocking vs. Non-Blocking in Node.js

```javascript
// BLOCKING I/O — synchronous filesystem operations
// These block the entire Node.js event loop
// NO other code can run while these execute

const fs = require('fs');

console.log('Before read');
// readFileSync BLOCKS until the file is fully read
const data = fs.readFileSync('/etc/hosts', 'utf8');
console.log('File content:', data.slice(0, 50));
console.log('After read');
// Output order is always: Before → File content → After

// In a server context, this means:
// While reading the file, NO incoming HTTP requests are handled.
// ALL connections wait. This is catastrophically bad for throughput.
```

```javascript
// NON-BLOCKING I/O — asynchronous filesystem operations
// These register a callback and return immediately
// The event loop can process other tasks while I/O waits

const fs = require('fs');

console.log('Before read');

// readFile is non-blocking:
// It registers the operation with libuv's I/O poller
// Returns immediately
// Node.js event loop continues processing other events
fs.readFile('/etc/hosts', 'utf8', (err, data) => {
  // This callback runs when the file is available
  // It's placed in the event loop's I/O callback queue
  console.log('File content:', data.slice(0, 50));
});

console.log('After read'); // This runs BEFORE the file content!
// Output order: Before → After → File content

// The event loop while readFile is in progress:
// 1. Receives HTTP request → handles it immediately
// 2. Receives another HTTP request → handles it
// 3. /etc/hosts read completes → invokes callback
// Thousands of requests can be handled while one file read is in progress
```

---

## 14. Synchronous vs. Asynchronous

### Definition

These are related to but distinct from blocking/non-blocking:

**Synchronous**: Operations occur in a defined order. Each operation completes before the next begins. The caller waits for the result.

**Asynchronous**: The caller does not wait for the result. The result arrives at some future time via a callback, promise, or event.

The terms are often conflated with blocking/non-blocking, but the distinctions matter:

```
Synchronous + Blocking:
  Standard function call in most languages.
  Caller waits, thread is blocked until return.

Synchronous + Non-Blocking:
  Non-blocking syscall that returns immediately with "not ready yet".
  Caller checks repeatedly (polling). Thread is not suspended.

Asynchronous + Non-Blocking:
  The standard Node.js model.
  Caller initiates, continues other work.
  Result arrives via callback/promise.

Asynchronous + Blocking:
  Rare. Thread is blocked but waiting for a future-triggered event
  (e.g., blocking on a channel receive in Go).
```

### How JavaScript Handles Asynchrony

JavaScript is synchronous and single-threaded at the language level. Asynchrony is handled by the **event loop** — a runtime mechanism (implemented by libuv in Node.js) that:

1. Runs JavaScript synchronously to completion
2. When the call stack is empty, checks I/O completion events, timer expirations, etc.
3. Runs the callback for the next completed async operation
4. Repeat

This is covered in complete depth in Pillar 4 (JavaScript Runtime). The key point here: JavaScript does not have threads managing asynchronous work — it has a single thread and an event loop that efficiently interleaves work.

---

## 15. Context Switching

### Definition

A context switch is the process by which the OS saves the state of the currently running process/thread and loads the state of another, allowing multiple processes to share a single CPU over time.

### What Gets Saved and Restored

```
CPU State (must be saved per thread):
  ┌────────────────────────────────────┐
  │ General Purpose Registers          │  rax, rbx, rcx, rdx, rsi, rdi...
  │ Program Counter (RIP)              │  where execution will resume
  │ Stack Pointer (RSP)                │  top of this thread's stack
  │ Base Pointer (RBP)                 │  current frame
  │ Flags Register (RFLAGS)            │  zero, carry, overflow flags
  │ FPU/SIMD Registers                 │  floating point, vector state
  │ TLS Pointer                        │  thread-local storage
  └────────────────────────────────────┘

OS Kernel State (must be saved per process):
  ┌────────────────────────────────────┐
  │ Page Table Base (CR3)              │  virtual→physical mapping
  │ Signal Handlers                    │
  │ File Descriptor Table              │
  │ Scheduling Priority                │
  └────────────────────────────────────┘
```

### Context Switch Cost

A thread context switch costs approximately 1–10 microseconds (on modern hardware):
- Save registers to PCB (Process Control Block)
- Load new thread's registers from its PCB
- Flush Translation Lookaside Buffer (TLB) for process switch
- Cold cache effects: the new thread's working set is not in cache

A process context switch is more expensive than a thread context switch because:
- The virtual memory mapping changes (requires TLB flush — very expensive)
- The cache footprint of the new process is completely cold

```
Thread Switch:  ~1-5 µs (no virtual memory change, partial cache overlap)
Process Switch: ~10-100 µs (virtual memory change, TLB flush, cold cache)
```

This is why Node.js's approach (single-threaded, event-loop) is efficient for I/O-bound workloads: zero context switching overhead. But it's why CPU-bound work blocks the event loop — there's only one thread, and if it's doing CPU work, it can't interleave I/O callbacks.

### When Does Context Switching Happen?

```
Voluntary (cooperative):
  - Thread calls blocking syscall (read, sleep, wait)
  - Thread yields the CPU voluntarily
  - Thread completes and exits

Involuntary (preemptive):
  - Timer interrupt fires (scheduler's time slice expired)
  - Higher-priority thread becomes runnable
  - Hardware interrupt occurs
```

Modern OS schedulers are preemptive: they use a hardware timer to interrupt running processes/threads at regular intervals and give CPU time to others. This is what makes your OS "responsive" even when one process is doing heavy computation — the scheduler preempts it periodically.

---

## 16. Inter-Process Communication

### Definition

IPC (Inter-Process Communication) is the set of mechanisms by which separate processes exchange data and coordinate. Since processes have isolated address spaces, they cannot directly share memory without OS assistance.

### IPC Mechanisms

#### 1. Pipes

```
Process A  ──write──→  [kernel buffer]  ──read──→  Process B
(producer)               (pipe buffer)              (consumer)

Anonymous Pipe: between parent and child process (unidirectional)
Named Pipe (FIFO): between any processes (via filesystem path)
```

```bash
# Shell pipes use anonymous pipe IPC
ls -la | grep ".js" | wc -l
# ls writes to pipe1, grep reads pipe1 and writes to pipe2, wc reads pipe2
```

#### 2. Sockets (Unix Domain Sockets and TCP)

```
Process A                    Process B
+--------+   Unix Socket    +--------+
|        | ←────────────→   |        |
+--------+   or TCP/IP      +--------+

Node.js child_process.fork() uses a socket pair for message passing
Nginx → Node.js app server uses a Unix domain socket or TCP socket
```

#### 3. Shared Memory

```
Process A                Process B
  │                         │
  └──→ [Shared Memory] ←───┘
       (physical RAM page
        mapped into both
        processes' virtual
        address spaces)

Fastest IPC (no copying)
Requires explicit synchronization (mutex/semaphore)
Used for high-performance scenarios: video processing, game engines
```

#### 4. Message Queues

```
Process A     [Message Queue]     Process B
──send──→     [msg1][msg2][msg3]  ←──receive──
              (kernel-managed)

Decoupled: sender and receiver don't need to be running simultaneously
```

#### 5. Signals

```
Process A    kill(pid, SIGTERM)    Process B
──────────────────────────────→    handles signal
                                   or exits

Signals are asynchronous notifications, not data channels
```

### Node.js IPC in Practice

```javascript
// Production-grade IPC between Node.js processes
// Using child_process.fork() with structured message passing

// parent.js
const { fork } = require('child_process');

class WorkerManager {
  constructor() {
    this.workers = new Map();
    this.pendingRequests = new Map();
    this.requestId = 0;
  }

  spawn(workerPath) {
    const worker = fork(workerPath);
    const id = ++this.requestId;
    
    this.workers.set(id, worker);

    worker.on('message', (msg) => {
      // Structured response with correlation ID
      const pending = this.pendingRequests.get(msg.requestId);
      if (pending) {
        pending.resolve(msg.result);
        this.pendingRequests.delete(msg.requestId);
      }
    });

    worker.on('exit', (code) => {
      console.log(`Worker ${id} exited: ${code}`);
      this.workers.delete(id);
    });

    return id;
  }

  request(workerId, data) {
    return new Promise((resolve, reject) => {
      const requestId = ++this.requestId;
      
      this.pendingRequests.set(requestId, { resolve, reject });
      
      const worker = this.workers.get(workerId);
      if (!worker) return reject(new Error('Worker not found'));
      
      // Send via Node's IPC channel (internally a socket)
      worker.send({ requestId, data });
      
      // Timeout for unresponsive workers
      setTimeout(() => {
        if (this.pendingRequests.has(requestId)) {
          reject(new Error('Worker request timed out'));
          this.pendingRequests.delete(requestId);
        }
      }, 5000);
    });
  }
}

const manager = new WorkerManager();
const wId = manager.spawn('./compute-worker.js');

const result = await manager.request(wId, { type: 'fibonacci', n: 40 });
console.log('Fibonacci result:', result);
```

```javascript
// compute-worker.js — worker side
process.on('message', ({ requestId, data }) => {
  let result;
  
  switch (data.type) {
    case 'fibonacci':
      result = fibonacci(data.n);
      break;
    default:
      result = null;
  }
  
  process.send({ requestId, result });
});

function fibonacci(n) {
  if (n <= 1) return n;
  return fibonacci(n - 1) + fibonacci(n - 2);
}
```

### IPC Mechanism Comparison

| Mechanism | Speed | Complexity | Use Case |
|---|---|---|---|
| Pipe | Fast | Low | Simple one-directional data stream |
| Unix Socket | Very fast | Medium | Local RPC, database sockets |
| TCP Socket | Moderate | Medium | Cross-host communication |
| Shared Memory | Fastest | High | High-throughput local IPC |
| Message Queue | Moderate | Medium | Decoupled async communication |
| Signals | Very fast | Low | Process control (SIGTERM, SIGUSR1) |
| File | Slow | Low | Configuration, large persistent data |

---

## Summary: How These Concepts Connect

```
                        Your Source Code
                              │
                    Compiler / Interpreter
                              │
                         Machine Code
                              │
                        ┌─────┴─────┐
                        │    CPU    │
                        │  Fetch    │
                        │  Decode   │
                        │  Execute  │
                        └─────┬─────┘
                              │
               ┌──────────────┼──────────────┐
               │              │              │
         Registers          Cache           RAM
         (fastest)        (fast)         (slower)
                                            │
                                      Virtual Memory
                                     /            \
                                  Stack            Heap
                              (automatic)        (managed)
                                    │                │
                              Local vars         Objects,
                              Call frames        arrays,
                              Return addrs       closures
                                         \      /
                                        Process
                                        (isolated)
                                            │
                                  ┌─────────┴──────────┐
                                  │       Threads       │
                                  │  (share heap/code)  │
                                  └─────────┬──────────┘
                                            │
                                    ┌───────┴───────┐
                              Concurrency       Parallelism
                              (interleaved)    (simultaneous)
                                    │               │
                               Event Loop      Multi-Core
                               (Node.js)       CPU Work
                                    │
                               IPC (when
                               multiple
                               processes
                               needed)
```

Every concept in this pillar connects to the others. A deep understanding of this chain — from machine code to process isolation to IPC — is what separates engineers who "know Node.js" from engineers who understand *why Node.js works the way it does*.

---

## Interview Questions — Pillar 1

### Junior Level

1. What is the difference between a process and a thread?
2. What is a stack overflow and when does it occur?
3. What is the difference between synchronous and asynchronous code?
4. What is garbage collection and why do we need it?
5. What is the difference between compilation and interpretation?

### Mid Level

1. Explain what happens in memory when a function is called and when it returns.
2. Why can't two processes directly share memory without OS help?
3. What is a context switch and what does it cost?
4. Explain the difference between concurrency and parallelism. Give an example of each.
5. What is a race condition? How do you prevent it?
6. Why is Node.js non-blocking I/O efficient for web servers?
7. What is a memory leak in JavaScript? Give a concrete example.

### Senior Level

1. Explain generational garbage collection. Why does it work better than simple mark-and-sweep for most workloads?
2. How does the CPU's branch predictor affect JavaScript performance? Give a concrete example.
3. A Node.js cluster has 8 workers but you're seeing worse performance than 4 workers under load. What would you investigate?
4. Explain copy-on-write in the context of `fork()`. Why does it matter for Node.js's cluster module?
5. Your Node.js server's heap is growing unboundedly. Walk me through your debugging process from first alert to root cause.
6. What is Amdahl's Law and how does it apply when deciding whether to use Worker Threads?
7. Explain the difference between `SharedArrayBuffer` and regular message passing in Worker Threads. When would you use one over the other? What safety mechanisms does `SharedArrayBuffer` require?
8. Why did Spectre and Meltdown require browser mitigations? What was the fundamental vulnerability?

---

*Continue to `02-Networking.md` →*
