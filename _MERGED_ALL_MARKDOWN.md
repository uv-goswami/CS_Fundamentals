# Merged Documentation

**Root Directory:** `/media/user/New Volume/Study_Materials/CS_Fundamentals`

---


## 📄 File: 00-How-To-Use-This-Course.md
*====================================*

# Interview Mastery Resource
## How to Use This Course

---

## Who This Is For

This resource is built for developers who have already tried to prepare for senior engineering interviews and *still failed* — not because they didn't study, but because they studied the wrong things in the wrong way.

You may recognize yourself:

- You memorized what a closure is. The interviewer asked "what happens to a closure reference when the outer function is garbage collected?" and you blanked.
- You know how `async/await` works in JavaScript. The interviewer asked "how does the event loop interact with the microtask queue during promise resolution?" and you guessed.
- You've built REST APIs. The interviewer asked "how does your server handle 50,000 concurrent connections with a single thread?" and you said "Node is fast."
- You know what an index is. The interviewer asked "why did adding an index make this query *slower*?" and you had no model for that.

This resource fixes the root cause: **you know what things are called, but you don't know how they work**.

---

## The Core Philosophy

> **Memorization is a losing strategy against senior interviewers.**

Senior engineers at Google, Meta, Amazon, and Stripe are not testing whether you can recall definitions. They are testing whether you have built *mental models* of how systems behave — because that's what determines whether you can debug production incidents, reason about tradeoffs, and design things that don't fall apart.

The only reliable interview strategy is **first-principles understanding**: knowing a system well enough that you could reconstruct its behavior from scratch if you had to.

This resource is built around that goal.

---

## How This Course Is Structured

The course is organized into **15 Pillars**. Each pillar covers a domain of engineering knowledge.

```
00-How-To-Use-This-Course.md      ← You are here
01-Computer-Science-Foundations.md
02-Networking.md
03-JavaScript-Fundamentals.md
04-JavaScript-Runtime.md
05-NodeJS-Internals.md
06-Browser-Internals.md
07-React.md
08-Databases.md
09-Backend-Engineering.md
10-Authentication-Security.md
11-System-Design.md
12-Operating-Systems.md
13-Git.md
14-Linux.md
15-Cloud.md
glossary.md
interview-questions/
    pillar-1.md through pillar-15.md
```

Each topic in each pillar follows a **mandatory depth template**:

1. Definition
2. Historical Context
3. Why It Exists / Problem It Solves
4. Internal Architecture
5. Step-by-Step Execution Flow
6. Memory Behavior
7. Performance Characteristics
8. Common Misconceptions
9. Interview Questions (Junior → Mid)
10. Senior-Level Interview Questions
11. Real Production Examples
12. Failure Scenarios
13. Debugging Examples
14. Tradeoffs
15. Best Practices

Every topic includes:
- At minimum two full code implementations (not snippets)
- ASCII architecture diagrams
- A **"How to Think About It"** mental model section
- A **"How Interviewers Attack This Topic"** section with follow-up chains
- Comparison tables where applicable

---

## How to Read This

**Do not skim.**

These files are dense on purpose. The goal is not coverage, it is *depth*.

### Recommended Sequence

**Phase 1 — Foundations (Week 1–2)**
Read Pillars 1, 3, 4, 6 in order. These establish the cognitive bedrock everything else builds on. Do not skip Computer Science Foundations even if you feel you "know this." You don't know it at the depth this document covers it.

**Phase 2 — Backend Stack (Week 3–4)**
Read Pillars 2, 5, 8, 9, 10 in order. This covers the full lifecycle of a backend request — from network packet to database row.

**Phase 3 — Architecture (Week 5–6)**
Read Pillars 11, 12, 7, 15. This covers system design, operating systems, React internals, and cloud infrastructure.

**Phase 4 — Tooling (Week 7)**
Read Pillars 13 and 14. Git and Linux are underestimated in interviews. Many senior-level "gotcha" questions live here.

**Phase 5 — Interview Questions**
Work through the `interview-questions/` folder for each pillar. Attempt to answer each one from scratch *before* reading the pillar explanation again.

---

## How to Use the Interview Questions

The `interview-questions/` directory contains layered question sets for each pillar.

Each question has:
- The question itself
- The **expected junior answer** (what most people say)
- The **mid-level follow-up** (what trips up most candidates)
- The **senior follow-up chain** (what separates senior from staff)
- **What a great answer demonstrates**

Practice like this:

1. Read the question.
2. Answer it out loud, as if in an interview.
3. Record yourself if possible.
4. Compare against the provided chain.
5. Identify where your answer stopped and where the chain continues.
6. Go back to the pillar and read that gap.

The gap between where your answer stops and where the chain continues is *exactly* what you need to study.

---

## How Interviewers Think at Senior Level

Senior engineering interviews operate on **layers**. Every question has at least four:

```
Layer 1: Definition
         "Can you define X?"
         → Most candidates can do this.

Layer 2: Mechanism
         "How does X actually work internally?"
         → Most candidates fail here.

Layer 3: Tradeoffs
         "What are the costs of X? When would you NOT use it?"
         → Very few candidates reach here.

Layer 4: Production Behavior
         "What happens to X under failure? Under load? In edge cases?"
         → Almost no candidates reach here unprompted.
```

Interviewers at FAANG companies almost never stop at Layer 1. Their job is to find the depth boundary of your knowledge. This course is designed to push that boundary as far as possible.

---

## A Note on Code Examples

Every code example in this resource is written to be read, not just run.

Each example is annotated with comments that explain *why* each line exists, not just what it does. If you find yourself reading code and thinking "I understand what this does" — that is not enough. Push yourself to be able to explain *why this was written this way*, *what would happen if this line were removed*, and *what the alternative approaches are and why they were rejected*.

---

## Target Roles

This resource is calibrated to prepare you for:

- **Senior Frontend Engineer** — Pillars 3, 4, 6, 7, 10, 13
- **Senior Fullstack Engineer** — All pillars
- **Senior Backend Engineer** — Pillars 1, 2, 5, 8, 9, 10, 11, 12, 14
- **Staff/Principal Engineer** — All pillars + System Design depth

Target companies: Google, Meta, Amazon, Microsoft, Stripe, Airbnb, Netflix, Uber, DoorDash, and equivalents.

---

## What This Is Not

This is not a cheat sheet. There are no "top 10 answers to memorize." There are no "just say this in an interview" templates.

If you are looking for that kind of resource, this is not it.

This resource is for developers who are willing to do the hard work of actually understanding how computers work. That understanding doesn't expire, doesn't get outdated by a new framework, and cannot be taken from you.

---

## One Final Principle

> **If you can't explain it simply, you don't understand it yet.**

After reading any section in this course, close the file and explain the topic out loud to yourself, as if teaching it to a junior engineer. If you stumble, you found the gap. Go back and read that section again.

The goal is not to finish this course. The goal is to reach the point where you can *reason through anything* because you understand the systems underneath.

---

*Begin with `01-Computer-Science-Foundations.md`.*

---


## 📄 File: 01-Computer-Science-Foundations.md
*==========================================*

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

---


## 📄 File: 02-Networking.md
*========================*

# Pillar 2 — Networking

> *"Every HTTP request is a negotiation between machines that don't trust each other, across a medium that drops packets, in a protocol stack built from four decades of engineering compromise."*

---

## Table of Contents

1. [The Internet](#1-the-internet)
2. [Network Models — OSI and TCP/IP](#2-network-models)
3. [IP Addresses](#3-ip-addresses)
4. [MAC Addresses](#4-mac-addresses)
5. [DNS](#5-dns)
6. [Ports](#6-ports)
7. [TCP](#7-tcp)
8. [UDP](#8-udp)
9. [HTTP](#9-http)
10. [HTTPS and TLS](#10-https-and-tls)
11. [The Full Request Lifecycle](#11-the-full-request-lifecycle)
12. [Cookies](#12-cookies)
13. [HTTP Headers](#13-http-headers)
14. [CORS](#14-cors)
15. [Load Balancers](#15-load-balancers)
16. [Proxies and Reverse Proxies](#16-proxies-and-reverse-proxies)
17. [CDNs](#17-cdns)
18. [WebSockets](#18-websockets)
19. [Server-Sent Events (SSE)](#19-server-sent-events)

---

## 1. The Internet

### Definition

The Internet is a global system of interconnected computer networks that communicate using a standardized protocol suite (TCP/IP). It is not one network — it is a **network of networks**: ISPs, universities, corporations, data centers, and home routers all maintain independent networks, and the Internet is the agreements and infrastructure that lets them route packets between each other.

### Historical Context

The Internet's direct ancestor is **ARPANET** (1969), funded by the US Defense Advanced Research Projects Agency. ARPANET's design goal was a communications network that could survive partial failures — if nodes were destroyed, packets would find alternate routes. This design principle — **decentralized, packet-switched routing** — is the Internet's DNA.

Key milestones:
- 1969: ARPANET first message (UCLA → Stanford — the system crashed after "LO" of "LOGIN")
- 1973: TCP/IP conceptualized by Vint Cerf and Bob Kahn
- 1983: ARPANET migrates to TCP/IP ("flag day")
- 1991: Tim Berners-Lee invents the World Wide Web (HTTP + HTML + URLs) at CERN
- 1993: Mosaic web browser — mass adoption begins
- 1994: Netscape, SSL encryption for the web
- 2000: Internet backbone privatized; dot-com infrastructure largely in place

### Packet Switching vs. Circuit Switching

The telephone network used **circuit switching**: before a call, a dedicated physical circuit is established end-to-end. Resources are reserved for the entire call duration. If one node fails, the call drops.

The Internet uses **packet switching**: data is broken into packets. Each packet carries a destination address. Each router independently decides where to forward each packet. Packets from the same "connection" may take different routes through the network. If one node fails, packets route around it.

```
Circuit Switching (telephone):
  Sender ──[dedicated wire]──────────────────── Receiver
  One reserved path, no sharing, cannot reroute

Packet Switching (Internet):
  Sender → [Router A] → [Router C] → [Router E] → Receiver
              ↓                          ↑
           [Router B] ──────────────────
  
  Packets may take different paths.
  No single path reserved.
  Routers forward based on best available path.
```

### Autonomous Systems and BGP

The Internet is organized into **Autonomous Systems (AS)** — independently managed networks, each identified by an AS Number (ASN). Google's network is AS15169. Cloudflare is AS13335. Comcast is AS7922.

**BGP (Border Gateway Protocol)** is the routing protocol that lets ASes advertise which IP prefixes they can reach to neighboring ASes. It is the Internet's "postal system" directory — routers use BGP tables to decide which direction to forward packets.

BGP route hijacking (accidentally advertising another AS's IP prefixes) has caused major Internet outages. Pakistan Telecom accidentally hijacked YouTube's IP space in 2008, making YouTube unreachable globally for two hours.

---

## 2. Network Models

### The OSI Model (Theoretical Reference)

The OSI (Open Systems Interconnection) model is a conceptual framework for understanding network communication. It defines 7 layers, each with a specific responsibility:

```
+---+--------------------+-------------------------------------------+
| 7 | Application        | HTTP, SMTP, DNS, FTP                      |
|   |                    | What the user/application sends           |
+---+--------------------+-------------------------------------------+
| 6 | Presentation       | Encoding, encryption, compression         |
|   |                    | TLS lives here (conceptually)             |
+---+--------------------+-------------------------------------------+
| 5 | Session            | Session management, reconnection          |
+---+--------------------+-------------------------------------------+
| 4 | Transport          | TCP, UDP                                  |
|   |                    | Port numbers, reliability, flow control   |
+---+--------------------+-------------------------------------------+
| 3 | Network            | IP, ICMP, routing                         |
|   |                    | IP addresses, routers, packet forwarding  |
+---+--------------------+-------------------------------------------+
| 2 | Data Link          | Ethernet, Wi-Fi (802.11)                  |
|   |                    | MAC addresses, frames, switches           |
+---+--------------------+-------------------------------------------+
| 1 | Physical           | Electrical signals, fiber optics, radio   |
|   |                    | Bits on wire                              |
+---+--------------------+-------------------------------------------+
```

### The TCP/IP Model (Practical)

In practice, networks use the TCP/IP model (4 layers):

```
+--------------------+-------------------------------------------+
| Application        | HTTP, HTTPS, DNS, SMTP, SSH, FTP, WebSocket|
+--------------------+-------------------------------------------+
| Transport          | TCP, UDP                                   |
+--------------------+-------------------------------------------+
| Internet           | IP (IPv4, IPv6), ICMP, ARP                |
+--------------------+-------------------------------------------+
| Network Access     | Ethernet, Wi-Fi, fiber optic drivers       |
+--------------------+-------------------------------------------+
```

### How Encapsulation Works

When you send an HTTP request, each layer **wraps** the data in its own header:

```
Application Layer data:
  [HTTP Request: GET /index.html HTTP/1.1...]

Transport Layer wraps it:
  [TCP Header: src_port=52341, dst_port=80, seq=100, ...]
  [HTTP Request]

Network Layer wraps it:
  [IP Header: src=192.168.1.5, dst=93.184.216.34, ...]
  [TCP Header][HTTP Request]

Data Link Layer wraps it:
  [Ethernet Frame: src_mac=AA:BB:CC:DD:EE:FF, dst_mac=...]
  [IP Header][TCP Header][HTTP Request]

Physical Layer:
  01100101 01001000 00110001... (actual bits on wire)
```

At the receiver, each layer **unwraps** its header and passes the payload up. This is the encapsulation/decapsulation process.

### How to Think About It

> Each layer of the network stack is a team with one job. The HTTP layer says "give this document request to whoever is on port 80 at this IP." The TCP layer says "make sure all the pieces arrive in order and intact." The IP layer says "route this packet toward its destination, one hop at a time." The Ethernet layer says "get this frame to the next device on this physical network segment." They do not know or care about each other's jobs. This separation of concerns is why you can run HTTP over Wi-Fi or fiber or satellite without changing the application.

---

## 3. IP Addresses

### Definition

An IP (Internet Protocol) address is a numerical label assigned to each device on a network that uses IP for communication. It serves two functions: **network identification** (which network?) and **host identification** (which device on that network?).

### IPv4

IPv4 addresses are 32-bit integers, written as four decimal octets separated by dots:

```
192.168.1.100
│   │   │ │
│   │   │ └── Host portion (depends on subnet mask)
│   │   └──── Network portion (depends on subnet mask)
└───┴──────── Network portion (depends on subnet mask)

Total IPv4 space: 2^32 = ~4.3 billion addresses
```

**IPv4 Address Classes and CIDR**:

```
192.168.1.0/24  (CIDR notation)
                 ^^ subnet mask bits
                 
/24 means first 24 bits are the NETWORK, last 8 are HOSTS
  Network:  192.168.1.0
  Hosts:    192.168.1.1  through  192.168.1.254
  Broadcast: 192.168.1.255
  Total: 256 - 2 = 254 usable host addresses

/16 gives 65,534 hosts
/8 gives 16,777,214 hosts
```

**Private IP Ranges** (RFC 1918 — not routable on the public Internet):

```
10.0.0.0/8          (10.x.x.x)          — large private networks
172.16.0.0/12       (172.16.x.x to      — medium private networks
                     172.31.x.x)
192.168.0.0/16      (192.168.x.x)       — home/small office networks
127.0.0.0/8         (127.x.x.x)         — loopback (your machine itself)
```

Your home router gets one public IP from your ISP. Every device in your home gets a private IP. The router uses **NAT (Network Address Translation)** to map outgoing connections from private IPs to the single public IP, maintaining a table of which private device made which connection.

### IPv6

IPv4 exhaustion (we ran out of allocatable IPv4 addresses around 2011–2019) drove adoption of IPv6: 128-bit addresses, providing 2^128 = ~340 undecillion addresses.

```
IPv6 format: eight groups of four hex digits
  2001:0db8:85a3:0000:0000:8a2e:0370:7334
  (can compress consecutive zeros):
  2001:db8:85a3::8a2e:370:7334

Loopback: ::1  (equivalent of 127.0.0.1)
```

### Subnetting (Interview Depth)

Subnetting divides a large network into smaller segments. This is a common interview question for senior engineers:

```
Given: 192.168.10.0/24
Requirement: Divide into 4 equal subnets

Solution:
  Need 4 subnets → need 2 bits for subnet identifier (2^2 = 4)
  Borrow 2 bits from host portion: /24 + 2 = /26

  Subnet 1: 192.168.10.0/26   (hosts: .1 - .62)
  Subnet 2: 192.168.10.64/26  (hosts: .65 - .126)
  Subnet 3: 192.168.10.128/26 (hosts: .129 - .190)
  Subnet 4: 192.168.10.192/26 (hosts: .193 - .254)
  
  Each subnet has 2^(32-26) - 2 = 62 usable hosts
```

---

## 4. MAC Addresses

### Definition

A MAC (Media Access Control) address is a 48-bit hardware identifier burned into a network interface card (NIC) by the manufacturer. It is used for communication within a single network segment (Layer 2). Unlike IP addresses, MAC addresses are not routable — routers strip and replace them at each hop.

```
MAC Address format: 6 bytes in hex, separated by colons
  AA:BB:CC:DD:EE:FF
  │││││
  First 3 bytes: OUI (Organizationally Unique Identifier)
    — identifies the manufacturer
    00:1A:2B = Apple
    00:50:56 = VMware (virtual NIC)
  
  Last 3 bytes: NIC-specific identifier assigned by manufacturer
```

### IP vs. MAC — When Each Is Used

```
Scenario: Your laptop (192.168.1.5) requests google.com (142.250.80.46)

Step 1 — Same network segment (your LAN):
  Your laptop needs to send a packet to your router (192.168.1.1)
  It knows the router's IP (default gateway) but needs its MAC
  → ARP (Address Resolution Protocol): broadcast "who has 192.168.1.1?"
  → Router responds: "I do — my MAC is AA:BB:CC:11:22:33"
  → Packet sent with:
      IP:  src=192.168.1.5,      dst=142.250.80.46  (end-to-end, unchanged)
      MAC: src=your-laptop-MAC,  dst=router-MAC      (hop-specific, changes)

Step 2 — At the router:
  Router strips your MAC header
  Looks up routing table: "142.250.80.46 → send to ISP gateway"
  ARP for ISP gateway's MAC
  Sends packet with:
      IP:  src=192.168.1.5,      dst=142.250.80.46  (unchanged)
      MAC: src=router-MAC,       dst=ISP-gateway-MAC (new hop-specific)

Each hop: IP stays the same, MAC changes
```

**Why this matters for interviews**: When debugging network issues, understanding the IP vs MAC distinction explains why `ping 192.168.1.1` works but `ping 8.8.8.8` doesn't (your router is up but your ISP connection is down). It also explains ARP cache poisoning attacks (a security interview topic).

---

## 5. DNS

### Definition

DNS (Domain Name System) is a distributed, hierarchical database that maps human-readable domain names (e.g., `api.github.com`) to IP addresses (e.g., `140.82.114.5`). It is the Internet's phonebook.

### Why It Exists

IP addresses change. Servers scale horizontally, migrate between data centers, update infrastructure. The domain name provides a stable human-readable identifier that DNS translates to the current IP. Without DNS, every browser bookmark would break when a server's IP changed.

### DNS Hierarchy

```
.  (Root — 13 root server clusters worldwide)
│
├── .com  (TLD — Top-Level Domain, managed by Verisign)
│     ├── github.com  (Authoritative NS — managed by GitHub/their DNS provider)
│     │     └── api.github.com  → 140.82.114.5
│     └── google.com
│
├── .org
├── .io
└── .uk  (country code TLD)
```

### DNS Resolution — Step by Step

When your browser resolves `api.github.com`:

```
1. Browser cache check:
   → Did I already resolve this recently? (TTL not expired?)
   → If yes: return cached IP. DONE.

2. OS resolver cache check (/etc/hosts or Windows host file):
   → Is there a local override?
   → systemd-resolved or nscd cache on Linux?
   → If yes: return. DONE.

3. Recursive resolver query (your ISP's or 8.8.8.8):
   → Your OS sends UDP packet to configured DNS resolver
   (e.g., 8.8.8.8 for Google's resolver)

4. Recursive resolver works the hierarchy:

   a. Query root servers: "Who handles .com?"
      → Root server: "Ask 192.5.6.30 (com. nameserver)"

   b. Query .com TLD servers: "Who handles github.com?"
      → TLD server: "Ask 205.251.196.1 (github.com nameserver)"

   c. Query github.com authoritative NS: "What is api.github.com?"
      → Auth NS: "api.github.com → 140.82.114.5, TTL=60"

5. Recursive resolver caches the result for TTL seconds
   Returns 140.82.114.5 to your OS

6. OS returns to browser, browser caches result
   Browser connects to 140.82.114.5:443
```

```
Your Machine        Recursive Resolver     Root NS     .com NS   Github NS
     │                      │                │            │           │
     │──"api.github.com?"──→│                │            │           │
     │                      │──"who has.com"→│            │           │
     │                      │←──"ask X.X.X.X"│            │           │
     │                      │────────────────────"github.com?"──→│           │
     │                      │◄───────────────────"ask Y.Y.Y.Y"──│           │
     │                      │──────────────────────────────────────→│
     │                      │◄─────────────────────────────────────│
     │                      │           "140.82.114.5, TTL=60"      │
     │◄────"140.82.114.5"───│                │            │           │
```

### DNS Record Types

| Type | Purpose | Example |
|---|---|---|
| A | IPv4 address | `github.com → 140.82.114.5` |
| AAAA | IPv6 address | `github.com → 2606:50c0:8000::154` |
| CNAME | Alias to another hostname | `www.github.com → github.com` |
| MX | Mail exchange server | `github.com → aspmx.l.google.com` |
| TXT | Arbitrary text (SPF, DKIM, domain verification) | `v=spf1 include:...` |
| NS | Authoritative nameservers for the domain | `github.com → ns1.p16.dynect.net` |
| SOA | Start of Authority (zone metadata) | Serial, refresh, retry, expire |
| PTR | Reverse DNS (IP → hostname) | `5.114.82.140.in-addr.arpa → github.com` |
| SRV | Service discovery | `_http._tcp.example.com → priority weight port target` |

### DNS TTL and Caching Implications

TTL (Time To Live) is the duration in seconds that resolvers may cache a record. This has production consequences:

```
Low TTL (60 seconds):
  ✓ DNS changes propagate fast (migration, failover)
  ✗ More DNS queries, higher resolver load, more latency per request
  Use for: active migrations, blue-green deployments

High TTL (86400 = 24 hours):
  ✓ Fewer DNS queries, faster resolution from cache
  ✗ Changes take up to 24h to propagate globally
  Use for: stable, long-lived infrastructure

Operational Reality:
  Before a migration: lower TTL to 60s, wait 24h
  Perform migration
  Update DNS record to new IP
  Propagation is fast (60s TTL already in effect)
  After migration stabilizes: raise TTL back to 3600+
```

### DNS Security

**DNS Spoofing / Cache Poisoning**: An attacker injects false DNS records into a resolver's cache, redirecting traffic to a malicious IP. Mitigation: **DNSSEC** (cryptographically signs DNS records).

**DNS over HTTPS (DoH)**: Encrypts DNS queries inside HTTPS, preventing ISPs from seeing your DNS lookups. Used by Firefox and Chrome. Controversial because it centralizes DNS to providers like Cloudflare and Google.

**DNS Hijacking**: ISPs or malicious actors intercept DNS queries to redirect traffic (e.g., showing ads on NXDOMAIN responses, or nation-state surveillance).

### Implementation: DNS Lookup in Node.js

```javascript
// Basic DNS resolution
const dns = require('dns');
const { promisify } = require('util');

const resolve4 = promisify(dns.resolve4);
const resolveMx = promisify(dns.resolveMx);
const resolveTxt = promisify(dns.resolveTxt);

async function inspectDomain(domain) {
  try {
    const [aRecords, mxRecords, txtRecords] = await Promise.all([
      resolve4(domain),
      resolveMx(domain).catch(() => []),
      resolveTxt(domain).catch(() => []),
    ]);

    console.log(`=== DNS Records for ${domain} ===`);
    console.log('A records (IPv4):', aRecords);
    console.log('MX records (mail):', mxRecords);
    console.log('TXT records:', txtRecords.flat());
  } catch (err) {
    if (err.code === 'ENOTFOUND') {
      console.log(`${domain}: domain does not exist`);
    } else if (err.code === 'ETIMEOUT') {
      console.log(`${domain}: DNS resolver timed out`);
    } else {
      throw err;
    }
  }
}

inspectDomain('github.com');
```

```javascript
// Production DNS health check with fallback resolvers
const dns = require('dns');

class ResilientDNS {
  constructor(resolvers = ['8.8.8.8', '1.1.1.1', '9.9.9.9']) {
    this.resolvers = resolvers;
    this.cache = new Map();
  }

  async resolve(hostname) {
    // Check cache first
    const cached = this.cache.get(hostname);
    if (cached && cached.expires > Date.now()) {
      return cached.addresses;
    }

    // Try each resolver in order
    for (const resolver of this.resolvers) {
      try {
        const addresses = await this._queryResolver(hostname, resolver);
        // Cache with 60 second TTL (in production, respect actual DNS TTL)
        this.cache.set(hostname, {
          addresses,
          expires: Date.now() + 60_000
        });
        return addresses;
      } catch (err) {
        console.warn(`Resolver ${resolver} failed for ${hostname}: ${err.message}`);
        // Try next resolver
      }
    }

    throw new Error(`All DNS resolvers failed for ${hostname}`);
  }

  _queryResolver(hostname, resolverIP) {
    return new Promise((resolve, reject) => {
      const dnsInstance = new dns.Resolver();
      dnsInstance.setServers([resolverIP]);
      
      dnsInstance.resolve4(hostname, (err, addresses) => {
        if (err) reject(err);
        else resolve(addresses);
      });
    });
  }
}

const dnsClient = new ResilientDNS();
const ips = await dnsClient.resolve('api.example.com');
```

### How Interviewers Attack DNS

**Question**: "How does DNS resolution work?"

Follow-up chain:
- "What if the recursive resolver's cache has a stale entry?" → It serves the stale entry until TTL expires. No mechanism forces immediate cache invalidation across the Internet.
- "How does low TTL help during a database migration?" → Lower TTL means caches expire sooner, so the new IP propagates faster after you update the record.
- "Can DNS be a single point of failure?" → Yes. Dyn DNS attack (2016) took down Twitter, Spotify, Reddit for hours by DDoSing a major DNS provider. Mitigation: multiple DNS providers, anycast routing.
- "What's the difference between a CNAME and an A record? When can you NOT use a CNAME?" → CNAME is an alias; cannot use CNAME at the zone apex (root of a domain). `example.com` cannot be a CNAME — only subdomains can. (Solution: ALIAS/ANAME records, or DNS providers that flatten CNAME.)

---

## 6. Ports

### Definition

A port is a 16-bit unsigned integer (0–65535) that identifies a specific process or service on a host. IP addresses identify machines; port numbers identify which service on that machine should receive a packet.

### Port Ranges

```
0 – 1023:     Well-known ports (requires root/admin to bind)
              80:   HTTP
              443:  HTTPS
              22:   SSH
              25:   SMTP (email)
              53:   DNS
              3306: MySQL
              5432: PostgreSQL

1024 – 49151: Registered ports (IANA-registered applications)
              3000: Common Node.js dev server
              6379: Redis
              27017: MongoDB
              8080: Alternative HTTP

49152 – 65535: Ephemeral (dynamic) ports
              Assigned by OS for outgoing connections (client side)
              When your browser connects to a server, it picks a random
              port from this range as the source port
```

### The 4-Tuple That Defines a Connection

Every TCP connection is uniquely identified by four values:

```
(source IP, source port, destination IP, destination port)

Your browser connecting to GitHub:
  (192.168.1.5, 54312, 140.82.114.5, 443)

Same machine, another tab connecting to GitHub:
  (192.168.1.5, 54313, 140.82.114.5, 443)

These are DIFFERENT connections even though they go to the same server.
The OS demultiplexes incoming packets to the right socket using all 4 values.
```

This is why a single server can handle tens of thousands of simultaneous connections on one port (443): each connection is distinguished by the client's ephemeral source port. The server doesn't need 50,000 ports — it needs one.

---

## 7. TCP

### Definition

TCP (Transmission Control Protocol) is a connection-oriented, reliable, ordered, error-checked transport protocol. It is the protocol underlying HTTP, HTTPS, SSH, SMTP, and most data-transfer protocols.

"Reliable" means: every byte sent is guaranteed to arrive, in order, or the sender is notified of failure.

### Why TCP Exists

IP is inherently unreliable. IP routers drop packets under congestion. Packets can arrive out of order (different paths). Packets can be corrupted. IP does nothing to fix these problems — it just delivers best-effort.

TCP was designed to layer reliability on top of unreliable IP.

### TCP Three-Way Handshake

Before any data can flow, TCP establishes a connection:

```
Client                          Server
  │                               │
  │──── SYN (seq=1000) ──────────→│  "I want to connect; my seq starts at 1000"
  │                               │
  │←─── SYN-ACK (seq=5000,       │  "OK; my seq starts at 5000;
  │            ack=1001) ─────────│   I received your seq, expecting 1001 next"
  │                               │
  │──── ACK (ack=5001) ──────────→│  "Got it; expecting your seq 5001 next"
  │                               │
  │═══════ DATA TRANSFER ═════════│
  │                               │

Time cost:  1 RTT (Round Trip Time) to establish connection
            before any HTTP data can be sent
```

This 1 RTT cost of TCP handshake is why HTTP/2 and QUIC (HTTP/3) work hard to reduce connection establishment time.

### TCP Four-Way Teardown

```
Client                          Server
  │                               │
  │──── FIN ────────────────────→ │  "I'm done sending"
  │                               │
  │ ←── ACK ──────────────────── │  "Got it"
  │                               │
  │ ←── FIN ──────────────────── │  "I'm also done sending"
  │                               │
  │──── ACK ────────────────────→ │  "Got it"
  │                               │
  Client enters TIME_WAIT state for 2 × MSL (Maximum Segment Lifetime)
  (~2 minutes) before the port is reused
```

**TIME_WAIT** is why high-traffic servers can exhaust ephemeral port ranges: each closed connection holds a port in TIME_WAIT for ~60–120 seconds.

### TCP Reliability Mechanisms

#### Sequence Numbers and Acknowledgments

```
Sender sends:
  Segment 1: bytes 1-1000   (seq=1)
  Segment 2: bytes 1001-2000 (seq=1001)
  Segment 3: bytes 2001-3000 (seq=2001)

If Segment 2 is dropped:
  Receiver ACKs: ack=1001 (got up to byte 1000, expecting 1001)
  Receives Segment 3: still sends ack=1001 (missing bytes 1001-2000!)
  Sender receives 3 duplicate ACKs for 1001 → fast retransmit
  Sender retransmits Segment 2
```

#### Sliding Window / Flow Control

TCP prevents a fast sender from overwhelming a slow receiver:

```
Receiver advertises its receive buffer size: rwnd (receive window)
Sender may not have more than rwnd bytes unacknowledged in flight

If receiver is slow (buffer fills): rwnd shrinks → sender slows down
If receiver processes data: rwnd grows → sender speeds up

This is flow control: matching sender speed to receiver capacity
```

#### Congestion Control

TCP also adapts to network congestion (Slow Start, Congestion Avoidance, Fast Retransmit, Fast Recovery):

```
Slow Start:
  Begin with cwnd (congestion window) = 1 MSS (~1460 bytes)
  Double cwnd each RTT until a packet is dropped
  (Exponential growth: 1 → 2 → 4 → 8 → 16 → ...)

Congestion Avoidance:
  After hitting ssthresh (slow start threshold):
  Increase cwnd by 1 MSS per RTT (linear growth)
  Until packet loss detected

On packet loss:
  ssthresh = cwnd / 2
  Reset cwnd = 1 (Tahoe) or cwnd = ssthresh (Reno/CUBIC)
  Resume Slow Start or Congestion Avoidance

This is why bandwidth-delay product matters:
  BDP = bandwidth × RTT
  A 1 Gbps link with 100ms RTT can have 100 Mbps × 0.1s = 10 MB in flight
  TCP's window must be large enough to fill the "pipe"
```

### TCP vs. UDP Comparison

| Property | TCP | UDP |
|---|---|---|
| Connection | Connection-oriented (handshake) | Connectionless |
| Reliability | Guaranteed delivery + ordering | Best-effort, no guarantee |
| Order | In-order delivery guaranteed | May arrive out of order |
| Error checking | Checksum + retransmit | Checksum only (no retransmit) |
| Flow control | Yes (receiver window) | No |
| Congestion control | Yes (slow start, CUBIC) | No |
| Speed | Slower (overhead) | Faster (minimal overhead) |
| Latency | Higher (ACKs, retransmits) | Lower |
| Use cases | HTTP, SSH, database, email | DNS, video streaming, gaming, VoIP |
| Header size | 20–60 bytes | 8 bytes |

---

## 8. UDP

### Definition

UDP (User Datagram Protocol) is a connectionless, unreliable, unordered transport protocol. It provides minimal service: send a datagram to an IP:port and hope it arrives. No handshake, no acknowledgment, no retransmit.

### Why UDP Exists

For many applications, TCP's reliability mechanisms are a liability, not an asset:

**DNS**: A single question-answer pair. If no response arrives, the client simply retries. No need for a persistent TCP connection.

**Video streaming**: Old frames have no value. If frame 100 is dropped, retransmitting it at frame 110 would cause the video to stutter worse than just skipping it. UDP lets the application decide what to do with loss.

**Online gaming**: Position updates must be low-latency. A TCP retransmit of an old position update could cause more jank than ignoring the loss.

**QUIC (HTTP/3)**: Built on UDP, but implements its own reliability, multiplexing, and encryption. Gets the benefits of TCP while avoiding head-of-line blocking.

### UDP Implementation: DNS Client

```javascript
// A raw UDP DNS query — demonstrates exactly what DNS over UDP looks like
const dgram = require('dgram');

function buildDNSQuery(hostname) {
  // DNS wire format (RFC 1035)
  const buf = Buffer.alloc(512);
  let offset = 0;

  // Header (12 bytes)
  buf.writeUInt16BE(0x1234, offset); offset += 2; // Transaction ID
  buf.writeUInt16BE(0x0100, offset); offset += 2; // Flags: standard query, recursion desired
  buf.writeUInt16BE(1, offset);      offset += 2; // QDCOUNT: 1 question
  buf.writeUInt16BE(0, offset);      offset += 2; // ANCOUNT: 0 answers
  buf.writeUInt16BE(0, offset);      offset += 2; // NSCOUNT: 0 authority
  buf.writeUInt16BE(0, offset);      offset += 2; // ARCOUNT: 0 additional

  // Question section
  // Encode hostname: api.github.com → \x03api\x06github\x03com\x00
  const labels = hostname.split('.');
  for (const label of labels) {
    buf.writeUInt8(label.length, offset++);
    Buffer.from(label, 'ascii').copy(buf, offset);
    offset += label.length;
  }
  buf.writeUInt8(0, offset++); // Null terminator

  buf.writeUInt16BE(1, offset); offset += 2; // QTYPE: A (IPv4)
  buf.writeUInt16BE(1, offset); offset += 2; // QCLASS: IN (Internet)

  return buf.slice(0, offset);
}

function queryDNS(hostname, resolver = '8.8.8.8') {
  return new Promise((resolve, reject) => {
    const socket = dgram.createSocket('udp4');
    const query = buildDNSQuery(hostname);
    
    socket.on('message', (msg) => {
      socket.close();
      // Parse the DNS response (simplified)
      // In production: use a proper DNS parsing library
      const answerCount = msg.readUInt16BE(6);
      if (answerCount === 0) {
        reject(new Error(`No DNS answers for ${hostname}`));
        return;
      }
      // Skip header (12 bytes) + question section to find answer
      // Actual parsing is more complex due to DNS compression
      resolve(`DNS response received (${msg.length} bytes), ${answerCount} answers`);
    });

    socket.on('error', reject);
    
    // UDP: fire and forget — send the query datagram
    socket.send(query, 53, resolver, (err) => {
      if (err) { socket.close(); reject(err); }
    });

    // Timeout: UDP has no connection, so we must implement our own timeout
    setTimeout(() => {
      socket.close();
      reject(new Error(`DNS query for ${hostname} timed out`));
    }, 3000);
  });
}

queryDNS('github.com').then(console.log).catch(console.error);
```

---

## 9. HTTP

### Definition

HTTP (HyperText Transfer Protocol) is an application-layer request-response protocol that defines how clients and servers communicate. It is stateless, text-based (HTTP/1.1), and runs over TCP (HTTP/1.1, HTTP/2) or UDP (HTTP/3 / QUIC).

### HTTP Version History

```
HTTP/0.9 (1991):  Single method (GET), single document type (HTML)
HTTP/1.0 (1996):  Headers, status codes, multiple content types
                  One TCP connection per request → huge overhead
HTTP/1.1 (1997):  Persistent connections (Keep-Alive), Host header,
                  chunked transfer encoding, pipelining (flawed)
HTTP/2 (2015):    Multiplexing, header compression (HPACK),
                  server push, binary framing, single TCP connection
HTTP/3 (2022):    Built on QUIC (UDP), 0-RTT connection, no
                  head-of-line blocking at transport layer
```

### HTTP/1.1 Request and Response Anatomy

```
HTTP Request:
  ┌─────────────────────────────────────────────────────────────┐
  │ GET /api/users/42 HTTP/1.1                                  │ ← Request line
  │ Host: api.example.com                                       │
  │ Authorization: Bearer eyJhbGc...                            │ ← Headers
  │ Accept: application/json                                    │
  │ Accept-Encoding: gzip, deflate, br                         │
  │ Connection: keep-alive                                      │
  │                                                             │ ← Empty line (end of headers)
  │ (no body for GET)                                           │
  └─────────────────────────────────────────────────────────────┘

HTTP Response:
  ┌─────────────────────────────────────────────────────────────┐
  │ HTTP/1.1 200 OK                                             │ ← Status line
  │ Content-Type: application/json; charset=utf-8               │
  │ Content-Length: 127                                         │ ← Headers
  │ Cache-Control: max-age=60                                   │
  │ X-Request-Id: f3a2c8b1-...                                  │
  │                                                             │ ← Empty line
  │ {"id": 42, "name": "Harish", "email": "h@example.com"}     │ ← Body
  └─────────────────────────────────────────────────────────────┘
```

### HTTP Methods — Semantics and Safety Properties

| Method | Safe? | Idempotent? | Has Body? | Usage |
|---|---|---|---|---|
| GET | Yes | Yes | No | Retrieve resource |
| HEAD | Yes | Yes | No | GET without body (check existence, headers) |
| OPTIONS | Yes | Yes | No | Discover allowed methods (used in CORS preflight) |
| POST | No | No | Yes | Create resource, trigger action |
| PUT | No | Yes | Yes | Replace entire resource |
| PATCH | No | No* | Yes | Partial update |
| DELETE | No | Yes | Optional | Delete resource |

**Safe**: Does not modify server state. **Idempotent**: Multiple identical requests produce the same result as one.

Idempotency is critical for retry logic. A network timeout on a POST (create order) and retrying may create a duplicate order. A timeout on a PUT (set quantity to 5) and retrying is safe — the result is the same.

### HTTP Status Codes

```
1xx — Informational
  100 Continue:            Server received request headers; send body
  101 Switching Protocols: Upgrading to WebSocket

2xx — Success
  200 OK:                  Standard success
  201 Created:             Resource created (POST/PUT success)
  204 No Content:          Success but no body (DELETE success)
  206 Partial Content:     Range request response (video streaming)

3xx — Redirection
  301 Moved Permanently:   Permanent redirect (update bookmarks, caches)
  302 Found:               Temporary redirect (don't update caches)
  304 Not Modified:        Client cache is valid; use cached response
  307 Temporary Redirect:  Like 302 but preserves HTTP method
  308 Permanent Redirect:  Like 301 but preserves HTTP method

4xx — Client Errors
  400 Bad Request:         Malformed request syntax
  401 Unauthorized:        Authentication required (despite the name!)
  403 Forbidden:           Authenticated but not authorized
  404 Not Found:           Resource doesn't exist
  405 Method Not Allowed:  Method not supported for this endpoint
  409 Conflict:            State conflict (duplicate creation, edit conflict)
  410 Gone:                Resource existed but was permanently deleted
  422 Unprocessable:       Semantic validation failure
  429 Too Many Requests:   Rate limited

5xx — Server Errors
  500 Internal Server Error: Generic server failure
  502 Bad Gateway:           Upstream server returned invalid response
  503 Service Unavailable:   Server overloaded or in maintenance
  504 Gateway Timeout:       Upstream server didn't respond in time
```

**Interview trap**: "What's the difference between 401 and 403?"
- 401 means: "I don't know who you are. Authenticate first." (unauthenticated)
- 403 means: "I know who you are. You're not allowed." (unauthorized)

The HTTP spec named 401 "Unauthorized" but it functionally means "unauthenticated." This naming is a historical mistake that confuses everyone.

### HTTP/2 — What Changed and Why

HTTP/1.1's fundamental problem: each request-response pair must complete before the next starts on a TCP connection. Even with Keep-Alive (reusing the connection), requests are sequential. Loading a page with 30 assets requires 30 sequential round-trips — or multiple TCP connections (browsers open up to 6 per origin).

```
HTTP/1.1 (sequential on each connection):
  Connection 1: [req1────resp1][req2────resp2]
  Connection 2: [req3────resp3][req4────resp4]
  Connection 3: [req5────resp5][req6────resp6]
  (6 parallel connections max per browser)

HTTP/2 (multiplexed on one connection):
  Stream 1:  [req1──────────────────resp1]
  Stream 2:    [req2──────────────resp2]
  Stream 3:      [req3──────────resp3]
  Stream 4:        [req4──────resp4]
  All on ONE TCP connection, interleaved
```

HTTP/2 innovations:
- **Multiplexing**: Multiple streams on one connection. No head-of-line blocking at HTTP layer.
- **Binary framing**: Instead of text, frames are binary — smaller, faster to parse.
- **Header compression (HPACK)**: Headers are compressed using a shared dynamic table. Repetitive headers (like `Authorization: Bearer ...`) sent once, referenced by index thereafter.
- **Server push**: Server can proactively send resources the client will need (e.g., push CSS when HTML is requested). Largely deprecated in practice due to caching complexity.
- **Stream prioritization**: Clients can signal priority of streams (CSS before images).

**HTTP/2's remaining problem**: Still uses TCP. A single packet loss causes ALL streams to stall (TCP-level head-of-line blocking).

### HTTP/3 / QUIC

HTTP/3 moves from TCP to **QUIC** (Quick UDP Internet Connections), a protocol built on UDP:

```
HTTP/2 over TCP:
  Single TCP connection → packet loss stalls ALL streams
  
HTTP/3 over QUIC:
  QUIC stream is independent — loss in stream 1 doesn't stall stream 2
  0-RTT connection establishment for repeated connections
  Built-in TLS 1.3 (no separate TLS handshake round-trip)
  Connection migration: same QUIC connection survives IP change
    (your phone moving from Wi-Fi to cellular — connection persists!)
```

---

## 10. HTTPS and TLS

### Definition

HTTPS is HTTP over TLS (Transport Layer Security). TLS provides: **confidentiality** (encrypted data), **integrity** (tamper detection), and **authentication** (server identity verified via certificate).

### TLS 1.3 Handshake

TLS 1.3 reduced the handshake to 1 RTT (from TLS 1.2's 2 RTTs):

```
Client                                          Server
  │                                               │
  │──── ClientHello ────────────────────────────→ │
  │     supported_versions=[TLS1.3]               │
  │     cipher_suites=[AES_256_GCM_SHA384, ...]   │
  │     client_random=<32 bytes>                  │
  │     key_share=[x25519 public key]             │
  │                                               │
  │ ←── ServerHello + Certificate + Finished ──── │
  │     server_random=<32 bytes>                  │
  │     key_share=[server's x25519 public key]    │
  │     Certificate=[server cert chain]           │
  │     CertificateVerify=[signature over handshake]
  │     Finished=[HMAC of handshake]              │
  │                                               │
  │ Both sides derive the same session keys       │
  │ using ECDH: client_private × server_public    │
  │ = server_private × client_public              │
  │ (Diffie-Hellman key exchange magic)           │
  │                                               │
  │──── Finished ───────────────────────────────→ │
  │     [HMAC proving client derived same keys]   │
  │                                               │
  │═════════ Encrypted Application Data ══════════│
  │         (HTTP request/response)               │

Total cost: 1 RTT for TLS + 1 RTT for TCP = 2 RTTs before first byte
(Plus DNS resolution time)
```

### Certificate Chain and PKI

When your browser connects to `https://github.com`, how does it trust the server?

```
Trust Chain:

Root CA Certificate (trusted by OS/browser by default)
  └── Intermediate CA Certificate (issued by Root CA)
        └── github.com Certificate (issued by Intermediate CA)

Browser verifies:
  1. github.com cert is signed by Intermediate CA (valid signature?)
  2. Intermediate CA cert is signed by Root CA (valid signature?)
  3. Root CA is in browser's trusted root store (shipped with OS/browser)
  4. github.com cert's CN/SAN matches the hostname we connected to
  5. Cert is not expired
  6. Cert is not in CRL (Certificate Revocation List) or OCSP says valid

If ALL checks pass → connection is trusted
If ANY check fails → browser shows "Not Secure" / warning
```

### TLS Implementation Details

```javascript
// Express HTTPS server with TLS configuration
const https = require('https');
const express = require('express');
const fs = require('fs');
const tls = require('tls');

const app = express();
app.get('/', (req, res) => res.send('Secure!'));

// In production: obtain certificates via Let's Encrypt / certbot
// For local dev: generate with: openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
const options = {
  key: fs.readFileSync('./key.pem'),
  cert: fs.readFileSync('./cert.pem'),
  
  // TLS security hardening
  minVersion: 'TLSv1.2',   // Reject TLS 1.0 and 1.1 (deprecated, vulnerable)
  maxVersion: 'TLSv1.3',
  
  // Only strong cipher suites
  // TLS 1.3 ciphers are configured separately and are all strong
  ciphers: [
    'ECDHE-RSA-AES256-GCM-SHA384',
    'ECDHE-RSA-AES128-GCM-SHA256',
    'ECDHE-RSA-CHACHA20-POLY1305',
  ].join(':'),
  
  // ECDHE key exchange (perfect forward secrecy)
  // Each connection uses ephemeral keys
  // If the server's private key is later compromised,
  // past sessions CANNOT be decrypted
  dhparam: fs.readFileSync('./dhparam.pem'), // For DHE suites
  
  // HSTS: tell browsers to always use HTTPS for this domain
  // (handled via HTTP headers, see below)
};

const server = https.createServer(options, app);

// Security headers
app.use((req, res, next) => {
  // Force HTTPS for 1 year, include subdomains, allow preloading
  res.setHeader('Strict-Transport-Security', 'max-age=31536000; includeSubDomains; preload');
  next();
});

server.listen(443, () => console.log('HTTPS server running on port 443'));

// Also redirect HTTP to HTTPS
const http = require('http');
http.createServer((req, res) => {
  res.writeHead(301, { Location: `https://${req.headers.host}${req.url}` });
  res.end();
}).listen(80);
```

### Perfect Forward Secrecy

A critical TLS concept interviewers probe:

Without PFS: If an attacker records encrypted traffic today and later obtains the server's private key, they can decrypt all historical traffic.

With PFS (ECDHE key exchange): Each connection uses ephemeral (temporary) key pairs. The session key is derived from these ephemeral keys, which are discarded after the session. Even with the server's long-term private key, past sessions cannot be decrypted.

PFS is achieved with **DHE** (Diffie-Hellman Ephemeral) or **ECDHE** (Elliptic Curve DHE) key exchange. All TLS 1.3 cipher suites require ECDHE — PFS is mandatory in TLS 1.3.

---

## 11. The Full Request Lifecycle

Let us trace the complete journey of `fetch('https://api.github.com/users/torvalds')` from a browser:

```
Browser calls fetch('https://api.github.com/users/torvalds')

PHASE 1 — DNS RESOLUTION (~1-100ms, often cached)
  1. Browser checks DNS cache → miss
  2. OS checks /etc/hosts → miss
  3. OS sends UDP query to 8.8.8.8 for api.github.com
  4. Recursive resolver traverses root → .com → github.com nameservers
  5. Returns: 140.82.113.5, TTL=60
  6. Browser caches for 60 seconds

PHASE 2 — TCP HANDSHAKE (~1 RTT = ~10-100ms depending on distance)
  7. OS allocates ephemeral port: 54231
  8. SYN → 140.82.113.5:443
  9. ← SYN-ACK
  10. ACK →
  TCP connection established

PHASE 3 — TLS HANDSHAKE (~1 RTT for TLS 1.3)
  11. ClientHello (with key share)
  12. ← ServerHello + Certificate + Finished
  13. Browser verifies certificate chain:
      github.com cert → DigiCert CA → root trusted by browser
  14. Finished → (confirms key derivation)
  Session keys established

PHASE 4 — HTTP/2 CONNECTION SETUP
  15. SETTINGS frame exchanged (max streams, header table size, etc.)
  16. New stream opened (stream ID = 1)

PHASE 5 — HTTP REQUEST
  17. HEADERS frame (compressed):
      :method: GET
      :path: /users/torvalds
      :authority: api.github.com
      :scheme: https
      authorization: token ghp_...
      accept: application/json

PHASE 6 — SERVER PROCESSING
  18. GitHub's load balancer receives request
  19. Routes to an application server based on headers/path
  20. App server queries internal DB/cache for user "torvalds"
  21. Serializes response to JSON

PHASE 7 — HTTP RESPONSE
  22. HEADERS frame:
      :status: 200
      content-type: application/json; charset=utf-8
      cache-control: public, max-age=60
      x-ratelimit-remaining: 59
  23. DATA frame(s): { "login": "torvalds", "id": 1024025, ... }

PHASE 8 — BROWSER PROCESSING
  24. Decompress body if Content-Encoding: gzip/br
  25. Parse JSON
  26. Resolve fetch() promise with Response object
  27. Your .then() callback runs with the data

PHASE 9 — CONNECTION HANDLING
  28. TCP connection kept alive (HTTP/2 persistent connection)
  29. Next fetch() to api.github.com reuses this connection
  30. Skips DNS + TCP + TLS handshake!
```

This is the answer to "what happens when you make an HTTP request?" at senior level.

---

## 12. Cookies

### Definition

Cookies are small key-value data stores maintained by the browser and sent with every HTTP request to the matching domain. They were invented to add statefulness to stateless HTTP — primarily for session management.

### Cookie Attributes and Their Security Implications

```
Set-Cookie: sessionId=abc123;
            Domain=example.com;
            Path=/;
            Expires=Thu, 01 Jan 2026 00:00:00 GMT;
            HttpOnly;
            Secure;
            SameSite=Strict
```

| Attribute | Effect | Security Relevance |
|---|---|---|
| `Domain` | Which domains receive this cookie | Too broad (`.example.com`) exposes to subdomains |
| `Path` | Which paths receive this cookie | Rarely used for security |
| `Expires`/`Max-Age` | Cookie lifetime | Session cookies (no Expires) deleted on browser close |
| `HttpOnly` | JS cannot access via `document.cookie` | **Prevents XSS cookie theft** |
| `Secure` | Only sent over HTTPS | **Prevents cookie interception on HTTP** |
| `SameSite=Strict` | Never sent in cross-site requests | **Prevents CSRF** |
| `SameSite=Lax` | Sent on top-level navigations, not sub-resources | Default in modern browsers |
| `SameSite=None` | Always sent (requires Secure) | Needed for cross-site OAuth flows |

### Cookies vs. LocalStorage vs. SessionStorage

| Property | Cookie | LocalStorage | SessionStorage |
|---|---|---|---|
| Capacity | ~4 KB | ~5–10 MB | ~5–10 MB |
| Sent with requests | Yes (automatically) | No | No |
| Server access | Yes | No | No |
| Expiration | Configurable | Never (manual clear) | Tab close |
| JS access | Yes (unless HttpOnly) | Yes | Yes |
| Security controls | HttpOnly, Secure, SameSite | None | None |
| Best for | Session tokens | User preferences, cache | Temp form state |

**Critical insight**: Never store JWT access tokens in localStorage. XSS can steal them. Store short-lived tokens in `HttpOnly; Secure; SameSite=Strict` cookies. (Covered in depth in Pillar 10.)

---

## 13. HTTP Headers

### Definition

HTTP headers are metadata key-value pairs in the HTTP request and response. They control caching, security, content negotiation, authentication, connection behavior, and more.

### Essential Headers (Grouped by Function)

#### Request Headers

```
Authorization: Bearer eyJhbGciOiJSUzI1NiJ9...   ← authentication token
Accept: application/json, text/html;q=0.9       ← content type preference
Accept-Encoding: gzip, deflate, br              ← compression preference
Accept-Language: en-US,en;q=0.9                 ← language preference
Content-Type: application/json                  ← body format (for POST/PUT)
Content-Length: 127                             ← body size in bytes
Host: api.example.com                           ← required in HTTP/1.1
User-Agent: Mozilla/5.0...                      ← client identification
Referer: https://example.com/page              ← where request came from
Cookie: sessionId=abc123; theme=dark            ← cookies for this domain
Origin: https://app.example.com                 ← CORS origin
If-None-Match: "abc123etag"                     ← conditional GET (ETag)
If-Modified-Since: Thu, 01 Jan 2025 00:00:00   ← conditional GET (date)
X-Request-Id: f3a2c8b1-7e2d-4f3a-8c9b-...     ← tracing correlation ID
```

#### Response Headers

```
Content-Type: application/json; charset=utf-8   ← what the body is
Content-Length: 127                             ← body size
Content-Encoding: gzip                          ← body is compressed
Transfer-Encoding: chunked                      ← streaming body
Cache-Control: public, max-age=3600, s-maxage=86400
ETag: "abc123etag"                              ← resource version identifier
Last-Modified: Mon, 01 Jan 2024 00:00:00 GMT   ← last modification time
Location: /users/42                             ← redirect target (3xx)
Retry-After: 60                                 ← rate limit reset (429)
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 99
X-RateLimit-Reset: 1735689600
Access-Control-Allow-Origin: https://app.com   ← CORS permission
Set-Cookie: sessionId=abc123; HttpOnly; Secure  ← set cookie
Strict-Transport-Security: max-age=31536000     ← HSTS
X-Frame-Options: DENY                           ← clickjacking prevention
X-Content-Type-Options: nosniff                 ← MIME sniffing prevention
Content-Security-Policy: default-src 'self'    ← XSS mitigation
```

### Cache-Control Directives

This is heavily tested in senior interviews:

```
Cache-Control: public, max-age=3600, s-maxage=86400, stale-while-revalidate=60

public:                  CDNs and proxies may cache this response
private:                 Only the end-user's browser may cache (not CDNs)
no-cache:                MUST revalidate with server before using cache
                         (confusingly named — it doesn't mean "don't cache")
no-store:                Never cache — not even in browser (medical records, banking)
max-age=3600:            Browser cache valid for 3600 seconds (1 hour)
s-maxage=86400:          Shared cache (CDN) valid for 86400 seconds (1 day)
                         Overrides max-age for CDNs
must-revalidate:         After max-age expires, must check server before serving
stale-while-revalidate=60: Serve stale response for 60s while fetching fresh
immutable:               Resource will NEVER change; browsers skip revalidation
                         (used for content-hashed assets like bundle.abc123.js)
```

### ETags and Conditional Requests

```
First request:
  GET /api/users/42 HTTP/1.1

  HTTP/1.1 200 OK
  ETag: "v1-abc123"          ← fingerprint of the response body
  Cache-Control: max-age=60
  {"id": 42, "name": "Harish"}

60 seconds later, browser re-requests:
  GET /api/users/42 HTTP/1.1
  If-None-Match: "v1-abc123"  ← "Do you have a newer version?"

  If resource unchanged:
  HTTP/1.1 304 Not Modified   ← No body! Browser uses cached version
                               → Saves bandwidth, saves server processing

  If resource changed:
  HTTP/1.1 200 OK
  ETag: "v2-def456"           ← New fingerprint
  {"id": 42, "name": "Harish S."}  ← Full response
```

---

## 14. CORS

### Definition

CORS (Cross-Origin Resource Sharing) is a browser security mechanism that restricts JavaScript's ability to make HTTP requests to a different origin than the one that served the current page.

An **origin** is the combination of `scheme + host + port`:
- `https://app.example.com` is an origin
- `https://api.example.com` is a **different** origin (different subdomain)
- `http://app.example.com` is a **different** origin (different scheme)
- `https://app.example.com:8080` is a **different** origin (different port)

### The Same-Origin Policy

Without CORS, browsers enforce the Same-Origin Policy: JavaScript on `https://evil.com` cannot make authenticated requests to `https://your-bank.com` because:
1. The browser automatically sends your bank's cookies
2. The response would contain your private data
3. evil.com's JavaScript would read that data

CORS is the controlled relaxation of this restriction.

### CORS Request Types

**Simple Request** (no preflight): Automatically sent for GET/POST with basic headers:

```
Origin: https://app.example.com
GET /api/data HTTP/1.1
Host: api.differentdomain.com

←── Access-Control-Allow-Origin: https://app.example.com
    (or *)
←── Response body (browser allows JS to read it)
```

**Preflight Request** (OPTIONS first): Required for custom headers, non-simple methods (PUT, DELETE, PATCH):

```
Browser sends preflight:
OPTIONS /api/users/42 HTTP/1.1
Origin: https://app.example.com
Access-Control-Request-Method: DELETE
Access-Control-Request-Headers: Authorization, X-Custom-Header

Server responds to preflight:
HTTP/1.1 204 No Content
Access-Control-Allow-Origin: https://app.example.com
Access-Control-Allow-Methods: GET, POST, PUT, DELETE, PATCH
Access-Control-Allow-Headers: Authorization, X-Custom-Header
Access-Control-Max-Age: 86400      ← Cache preflight for 24 hours
                                     (avoid preflight on every request)

Only if preflight succeeds does browser send actual request:
DELETE /api/users/42 HTTP/1.1
Origin: https://app.example.com
Authorization: Bearer token...
```

### CORS Implementation in Express

```javascript
// Production CORS configuration — NOT the simple "cors()" default
const express = require('express');
const app = express();

// Define allowed origins — do NOT use wildcard (*) with credentials
const ALLOWED_ORIGINS = new Set([
  'https://app.example.com',
  'https://staging.example.com',
  process.env.NODE_ENV === 'development' ? 'http://localhost:3000' : null,
].filter(Boolean));

function corsMiddleware(req, res, next) {
  const origin = req.headers.origin;
  
  // Check if this origin is allowed
  if (origin && ALLOWED_ORIGINS.has(origin)) {
    res.setHeader('Access-Control-Allow-Origin', origin);  // Not *!
    res.setHeader('Vary', 'Origin');  // CRITICAL: tell caches this varies by origin
    res.setHeader('Access-Control-Allow-Credentials', 'true');  // Allow cookies
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, PATCH, DELETE, OPTIONS');
    res.setHeader('Access-Control-Allow-Headers', 
      'Authorization, Content-Type, X-Request-Id, X-CSRF-Token'
    );
    res.setHeader('Access-Control-Expose-Headers',
      'X-Request-Id, X-RateLimit-Remaining'  // Headers JS can read
    );
    res.setHeader('Access-Control-Max-Age', '86400');  // Cache preflight 24h
  }
  
  // Handle preflight
  if (req.method === 'OPTIONS') {
    return res.status(204).end();
  }
  
  next();
}

app.use(corsMiddleware);

// Why NOT Access-Control-Allow-Origin: * with credentials?
// Using * prevents browsers from sending cookies/auth headers.
// You must specify the exact origin to use credentials.
// If you use * with credentials, browser refuses the response.
```

### CORS Common Misconceptions (Interview Traps)

1. **"CORS is a server-side security mechanism."** WRONG. CORS is a BROWSER mechanism. The server receives the request regardless. CORS only controls whether the browser lets JavaScript read the response. Server-side firewalls and auth are separate.

2. **"Disabling CORS fixes the security issue."** WRONG. Disabling CORS (allowing `*`) removes the browser's protection. The security issue was having unauthenticated endpoints.

3. **"curl has a CORS error."** IMPOSSIBLE. curl is not a browser. CORS only exists in browsers.

4. **"Adding `Access-Control-Allow-Origin: *` is always safe."** WRONG. When used with `Access-Control-Allow-Credentials: true`, browsers refuse the response. And `*` prevents reading response cookies.

---

## 15. Load Balancers

### Definition

A load balancer is a device (hardware or software) that distributes incoming network traffic across multiple backend servers. It prevents any single server from becoming a bottleneck and provides fault tolerance.

### Load Balancing Algorithms

```
Round Robin:
  Request 1 → Server A
  Request 2 → Server B
  Request 3 → Server C
  Request 4 → Server A  (back to start)
  Simple, ignores server load

Weighted Round Robin:
  Server A has weight 3, Server B has weight 1
  3 requests to A, 1 to B, 3 to A, 1 to B...
  For servers with different capacities

Least Connections:
  Send to server with fewest active connections
  Better for requests with variable processing time
  
Least Response Time:
  Send to server with lowest latency
  Requires health check probes

IP Hash / Sticky Sessions:
  Hash client IP → always route to same server
  Required for stateful applications (sessions not in shared store)
  Caveat: poor distribution if many users behind one NAT IP

Random:
  Random selection — surprisingly effective at scale
  (AWS Application Load Balancer uses this + least outstanding requests)
```

### Layer 4 vs. Layer 7 Load Balancing

```
Layer 4 (Transport — TCP/UDP):
  Routes based on IP + port only
  Cannot inspect HTTP headers or paths
  Fast (minimal packet inspection)
  Example: AWS NLB (Network Load Balancer)
  Use case: TCP streams, databases, when L7 overhead isn't acceptable

Layer 7 (Application — HTTP):
  Inspects HTTP headers, URLs, cookies
  Can route based on path (/api/ → API servers, /static/ → file servers)
  Can modify headers, compress responses, terminate TLS
  Slower (must parse full HTTP)
  Example: AWS ALB, Nginx, HAProxy, Cloudflare
  Use case: Web applications, microservices routing
```

### Health Checks

```
Load Balancer → Server A: GET /health HTTP/1.1
Server A: 200 OK {"status": "healthy", "db": "connected", "queue": "connected"}

Load Balancer → Server B: GET /health HTTP/1.1
Server B: 500 Internal Server Error (database connection failed)

Load Balancer:
  Server B marked as UNHEALTHY
  No traffic routed to Server B
  Alerts fired
  Continue health checking every 10s
  When Server B returns 200, gradually restore traffic
```

### Implementation: Health Check Endpoint

```javascript
// Production-grade health check endpoint
const express = require('express');
const { Pool } = require('pg');

const app = express();
const db = new Pool({ connectionString: process.env.DATABASE_URL });

// Shallow health check — just confirms process is alive
// Used for load balancer basic liveness checks
app.get('/health/live', (req, res) => {
  res.json({ status: 'ok', timestamp: new Date().toISOString() });
});

// Deep health check — checks all dependencies
// Used for readiness (is the server ready to handle traffic?)
app.get('/health/ready', async (req, res) => {
  const checks = {};
  let healthy = true;
  
  // Database check
  try {
    const result = await db.query('SELECT 1');
    checks.database = { status: 'ok', latencyMs: 0 }; // add real timing
  } catch (err) {
    checks.database = { status: 'error', message: err.message };
    healthy = false;
  }
  
  // Redis check (if applicable)
  // try { await redis.ping(); checks.redis = { status: 'ok' }; }
  // catch (err) { checks.redis = { status: 'error' }; healthy = false; }
  
  // Memory check
  const memUsage = process.memoryUsage();
  const heapUsedMB = Math.round(memUsage.heapUsed / 1024 / 1024);
  const heapLimitMB = 512; // Our configured heap limit
  if (heapUsedMB > heapLimitMB * 0.9) {
    checks.memory = { status: 'warning', heapUsedMB, limit: heapLimitMB };
    // Don't mark unhealthy for memory warnings, but do alert
  } else {
    checks.memory = { status: 'ok', heapUsedMB };
  }
  
  const statusCode = healthy ? 200 : 503;
  res.status(statusCode).json({
    status: healthy ? 'healthy' : 'unhealthy',
    checks,
    version: process.env.APP_VERSION,
    uptime: process.uptime(),
  });
});

app.listen(3000);
```

---

## 16. Proxies and Reverse Proxies

### Forward Proxy

A **forward proxy** sits between clients and the Internet, forwarding requests on behalf of clients. The server sees the proxy's IP, not the client's.

```
Clients → [Forward Proxy] → Internet → Servers
          (clients are hidden)

Use cases:
  - Corporate networks (content filtering, monitoring)
  - VPN-like anonymization
  - Caching outbound requests
  - Access control (which sites can employees visit)
```

### Reverse Proxy

A **reverse proxy** sits between the Internet and servers, forwarding requests on behalf of servers. Clients see the proxy's address, not the servers'.

```
Internet → [Reverse Proxy] → Servers (multiple)
           (servers are hidden)

Use cases:
  - Load balancing
  - TLS termination (decrypt HTTPS at proxy, HTTP internally)
  - Caching (static files, API responses)
  - Request buffering (protect slow servers from slow clients)
  - Security (WAF, rate limiting, DDoS mitigation)
  - Unified entry point for microservices
```

### Nginx as Reverse Proxy

```nginx
# /etc/nginx/nginx.conf — Production reverse proxy configuration

worker_processes auto;  # One worker per CPU core
worker_rlimit_nofile 65535;  # Max open file descriptors per worker

events {
    worker_connections 10000;  # Max simultaneous connections per worker
    use epoll;                  # Linux's high-performance I/O event mechanism
    multi_accept on;            # Accept multiple connections per epoll event
}

http {
    # Upstream group of app servers (load balanced)
    upstream app_servers {
        least_conn;  # Least connections algorithm
        
        server 10.0.1.1:3000 weight=3 max_fails=3 fail_timeout=30s;
        server 10.0.1.2:3000 weight=3 max_fails=3 fail_timeout=30s;
        server 10.0.1.3:3000 weight=1 max_fails=3 fail_timeout=30s;
        
        keepalive 32;  # Keep 32 idle connections to upstream
    }

    server {
        listen 80;
        server_name api.example.com;
        return 301 https://$server_name$request_uri;  # Redirect HTTP → HTTPS
    }

    server {
        listen 443 ssl http2;
        server_name api.example.com;
        
        # TLS configuration
        ssl_certificate     /etc/ssl/certs/api.example.com.crt;
        ssl_certificate_key /etc/ssl/private/api.example.com.key;
        ssl_protocols       TLSv1.2 TLSv1.3;
        ssl_ciphers         ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256;
        ssl_session_cache   shared:SSL:10m;   # Share TLS sessions across workers
        ssl_session_timeout 10m;
        
        # Security headers
        add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
        add_header X-Frame-Options DENY always;
        add_header X-Content-Type-Options nosniff always;
        
        # Rate limiting (define zone above in http block)
        # limit_req zone=api burst=20 nodelay;
        
        location /api/ {
            proxy_pass http://app_servers;  # Forward to upstream
            
            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection 'upgrade';  # WebSocket support
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;  # Pass client IP
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            
            # Timeouts
            proxy_connect_timeout 5s;
            proxy_read_timeout 60s;
            proxy_send_timeout 60s;
            
            # Buffer settings
            proxy_buffering on;          # Buffer responses (protect slow clients)
            proxy_buffer_size 4k;
            proxy_buffers 8 4k;
        }
        
        location /static/ {
            # Serve static files directly from nginx (bypass Node.js)
            alias /var/www/static/;
            expires 1y;
            add_header Cache-Control "public, immutable";
        }
    }
}
```

---

## 17. CDNs

### Definition

A CDN (Content Delivery Network) is a globally distributed network of servers (Points of Presence, PoPs) that serve content from the edge location closest to the user. CDNs reduce latency by minimizing the physical distance between server and client.

### How CDNs Work

```
Without CDN:
  User in Mumbai → Request → Origin Server in Virginia
  Round trip: ~200ms × 14 hops = ~280ms RTT
  
With CDN:
  User in Mumbai → Request → Cloudflare PoP in Mumbai
  Cache HIT: response served locally → ~5ms RTT
  Cache MISS: Cloudflare fetches from origin, caches, serves
              Future requests served from Mumbai PoP
```

### CDN Caching Strategies

```
Cache-Control: public, max-age=31536000, immutable
  → CDN caches forever; browser caches forever; never re-checks
  → Use for content-hashed static assets (bundle.a3f8c1.js)
  → Content hash changes → URL changes → new cache entry

Cache-Control: public, s-maxage=86400, max-age=0, must-revalidate
  → CDN caches for 24 hours; browser always checks CDN
  → Use for frequently updated, globally consistent content
  → CDN serves cached; browser gets fast response even if CDN revalidates

Surrogate-Control: max-age=3600  (Varnish/Fastly CDN header)
  → CDN-specific cache duration, stripped before sending to browser
  → Browser can have different cache behavior from CDN
```

### CDN Cache Invalidation

CDN cache invalidation is the hard problem:

```
Strategy 1: URL-based cache busting (BEST for static assets)
  Old: /static/bundle.js          → cached everywhere
  New: /static/bundle.a3f8c1.js  → new URL, cold cache
  Never need to invalidate! Just change the URL.
  
Strategy 2: Manual purge API
  Cloudflare, Fastly, CloudFront all expose purge APIs
  POST /zones/{zone_id}/purge_cache { "files": ["https://..."] }
  Risk: eventual consistency — purge propagates to ~400 PoPs
  Not instant; during propagation, some users get stale content
  
Strategy 3: Short TTL
  Cache-Control: max-age=60
  Staleness window is bounded to 60 seconds
  High origin load (every 60s, CDN re-fetches)
  Trade-off: freshness vs. performance
```

---

## 18. WebSockets

### Definition

WebSocket is a protocol providing **full-duplex** (bidirectional) communication over a single TCP connection. After an HTTP-based handshake, the connection is "upgraded" to the WebSocket protocol, and both client and server can send messages at any time without request-response overhead.

### HTTP vs WebSocket

```
HTTP (request-response):
  Client: "Give me data" ────────→ Server
  Server: "Here it is"  ←────────
  Client: "Give me data" ────────→ Server
  Client must poll to receive updates

WebSocket (full-duplex):
  Client ←────────────────────────→ Server
         send anytime, receive anytime
         no polling needed
  Server can PUSH data without client asking
```

### WebSocket Handshake

```
HTTP Upgrade Request:
  GET /ws HTTP/1.1
  Host: api.example.com
  Upgrade: websocket
  Connection: Upgrade
  Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==   ← random base64
  Sec-WebSocket-Version: 13

HTTP 101 Switching Protocols:
  HTTP/1.1 101 Switching Protocols
  Upgrade: websocket
  Connection: Upgrade
  Sec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=
  (Accept = SHA1(Key + magic string), base64 encoded)
  
  After this exchange: TCP connection switches to WebSocket frames.
  HTTP is gone. Both sides speak WebSocket protocol.
```

### WebSocket Implementation

```javascript
// Server: WebSocket with ws library (production-ready)
const WebSocket = require('ws');
const http = require('http');
const { v4: uuidv4 } = require('uuid');

const server = http.createServer();
const wss = new WebSocket.Server({ server });

// Track connected clients
const clients = new Map();

wss.on('connection', (ws, req) => {
  const clientId = uuidv4();
  const clientIp = req.socket.remoteAddress;
  
  clients.set(clientId, {
    ws,
    id: clientId,
    ip: clientIp,
    connectedAt: Date.now(),
    isAlive: true,
  });
  
  console.log(`Client connected: ${clientId} from ${clientIp}. Total: ${clients.size}`);

  // Heartbeat: WebSocket doesn't auto-detect dead connections
  // We use ping/pong to detect stale connections
  ws.on('pong', () => {
    const client = clients.get(clientId);
    if (client) client.isAlive = true;
  });

  ws.on('message', (data) => {
    let message;
    try {
      message = JSON.parse(data.toString());
    } catch {
      ws.send(JSON.stringify({ error: 'Invalid JSON' }));
      return;
    }
    
    // Echo back to sender
    ws.send(JSON.stringify({ type: 'echo', data: message }));
    
    // Broadcast to all other clients
    if (message.type === 'broadcast') {
      broadcast(message, clientId);
    }
  });

  ws.on('close', (code, reason) => {
    clients.delete(clientId);
    console.log(`Client ${clientId} disconnected: ${code} ${reason}`);
  });

  ws.on('error', (err) => {
    console.error(`WebSocket error for ${clientId}:`, err.message);
    clients.delete(clientId);
  });

  // Send welcome message
  ws.send(JSON.stringify({ type: 'connected', clientId }));
});

// Heartbeat interval — detect dead connections every 30s
const heartbeatInterval = setInterval(() => {
  clients.forEach((client, clientId) => {
    if (!client.isAlive) {
      // No pong received — connection is dead
      console.log(`Terminating dead connection: ${clientId}`);
      client.ws.terminate(); // Force close
      clients.delete(clientId);
      return;
    }
    client.isAlive = false;   // Reset; expect pong before next check
    client.ws.ping();          // Send ping; client responds with pong
  });
}, 30000);

wss.on('close', () => clearInterval(heartbeatInterval));

function broadcast(message, senderId) {
  const payload = JSON.stringify({ type: 'broadcast', from: senderId, ...message });
  clients.forEach((client, clientId) => {
    if (clientId !== senderId && client.ws.readyState === WebSocket.OPEN) {
      client.ws.send(payload);
    }
  });
}

server.listen(8080, () => console.log('WebSocket server on port 8080'));
```

```javascript
// Client: WebSocket with reconnection logic
class ResilientWebSocket {
  constructor(url, options = {}) {
    this.url = url;
    this.options = {
      maxReconnectAttempts: 10,
      reconnectIntervalMs: 1000,
      maxReconnectIntervalMs: 30000,
      reconnectDecay: 1.5,  // Exponential backoff multiplier
      ...options
    };
    this.reconnectAttempts = 0;
    this.handlers = { message: [], open: [], close: [], error: [] };
    this.connect();
  }

  connect() {
    this.ws = new WebSocket(this.url);
    
    this.ws.onopen = (event) => {
      console.log('WebSocket connected');
      this.reconnectAttempts = 0;  // Reset on successful connection
      this.handlers.open.forEach(h => h(event));
    };

    this.ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      this.handlers.message.forEach(h => h(data));
    };

    this.ws.onclose = (event) => {
      this.handlers.close.forEach(h => h(event));
      
      if (!event.wasClean && this.reconnectAttempts < this.options.maxReconnectAttempts) {
        // Exponential backoff: 1s, 1.5s, 2.25s, 3.375s, ...
        const delay = Math.min(
          this.options.reconnectIntervalMs * Math.pow(this.options.reconnectDecay, this.reconnectAttempts),
          this.options.maxReconnectIntervalMs
        );
        console.log(`Reconnecting in ${delay}ms (attempt ${this.reconnectAttempts + 1})`);
        setTimeout(() => this.connect(), delay);
        this.reconnectAttempts++;
      }
    };

    this.ws.onerror = (event) => {
      this.handlers.error.forEach(h => h(event));
    };
  }

  on(event, handler) {
    this.handlers[event].push(handler);
    return this;
  }

  send(data) {
    if (this.ws.readyState === WebSocket.OPEN) {
      this.ws.send(JSON.stringify(data));
    } else {
      console.warn('WebSocket not open. Message dropped:', data);
    }
  }

  close() {
    this.options.maxReconnectAttempts = 0;  // Prevent reconnect
    this.ws.close(1000, 'Client closed');
  }
}

// Usage
const ws = new ResilientWebSocket('wss://api.example.com/ws');
ws.on('open', () => ws.send({ type: 'subscribe', channel: 'prices' }));
ws.on('message', (data) => console.log('Price update:', data));
```

---

## 19. Server-Sent Events

### Definition

SSE (Server-Sent Events) is a one-directional server-push mechanism over HTTP where the server continuously streams events to a client. Unlike WebSockets (full-duplex), SSE is unidirectional: server → client only. The client communicates back via normal HTTP requests.

### SSE vs. WebSocket

| Property | SSE | WebSocket |
|---|---|---|
| Direction | Server → Client only | Bidirectional |
| Protocol | HTTP/1.1 or HTTP/2 | WebSocket (ws:// or wss://) |
| Reconnection | Automatic (browser handles) | Manual implementation needed |
| Firewall friendly | Yes (HTTP) | Sometimes blocked |
| Multiplexing | Yes (over HTTP/2) | No (one connection per stream) |
| Complexity | Low | Higher |
| Use cases | Live feeds, notifications, logs | Chat, gaming, real-time collaboration |

### SSE Implementation

```javascript
// Server: SSE endpoint with proper headers and event formatting
const express = require('express');
const app = express();

app.get('/events', (req, res) => {
  // SSE headers — these are MANDATORY
  res.setHeader('Content-Type', 'text/event-stream');
  res.setHeader('Cache-Control', 'no-cache');
  res.setHeader('Connection', 'keep-alive');
  res.setHeader('X-Accel-Buffering', 'no');  // Disable Nginx buffering for SSE
  
  // Send initial connection confirmation
  res.write('data: {"type":"connected"}\n\n');

  // SSE event format:
  // event: eventType\n    (optional — 'message' if omitted)
  // id: eventId\n         (optional — enables client reconnection from last ID)
  // data: payload\n       (required — can be multiple lines)
  // retry: milliseconds\n (optional — reconnection delay hint)
  // \n                    (blank line = end of event)

  let eventId = 0;
  
  // Simulate a real-time data stream
  const interval = setInterval(() => {
    const event = {
      type: 'price_update',
      symbol: 'BTC/USD',
      price: 45000 + Math.random() * 1000,
      timestamp: Date.now(),
    };
    
    res.write(`id: ${++eventId}\n`);
    res.write(`event: price_update\n`);
    res.write(`data: ${JSON.stringify(event)}\n`);
    res.write(`\n`);  // Blank line terminates the event
  }, 1000);

  // Heartbeat comment — keeps connection alive through proxies
  // Lines starting with : are comments, ignored by client
  const heartbeat = setInterval(() => {
    res.write(`: heartbeat\n\n`);
  }, 25000);

  // Clean up when client disconnects
  req.on('close', () => {
    clearInterval(interval);
    clearInterval(heartbeat);
    console.log(`SSE client disconnected: ${req.ip}`);
  });
});

app.listen(3000);
```

```javascript
// Client: Browser EventSource API
const eventSource = new EventSource('/events', {
  withCredentials: true,  // Send cookies with SSE request
});

// Default 'message' events
eventSource.onmessage = (event) => {
  const data = JSON.parse(event.data);
  console.log('Default message:', data);
};

// Named event type listener
eventSource.addEventListener('price_update', (event) => {
  const data = JSON.parse(event.data);
  console.log(`${data.symbol}: $${data.price.toFixed(2)}`);
  // Update UI...
});

eventSource.addEventListener('error', (event) => {
  if (eventSource.readyState === EventSource.CLOSED) {
    console.log('Connection closed permanently');
  } else {
    // Browser will automatically reconnect
    // The Last-Event-ID header will be sent, allowing server to resume
    console.log('Connection error — browser will retry');
  }
});

// To close the connection
// eventSource.close();
```

---

## Summary: Networking Stack Layered View

```
User types: https://api.github.com/users/torvalds

Application Layer:
  HTTPS (HTTP + TLS)
  DNS resolution → IP
  HTTP/2 or HTTP/1.1 request framing
  
Transport Layer:
  TCP: reliable, ordered, flow-controlled stream
  3-way handshake before data flows
  TLS handshake within TCP stream
  
Internet Layer:
  IP packets routed hop-by-hop through BGP network
  NAT at home router translates private → public IP
  
Data Link / Physical Layer:
  Wi-Fi frames → router
  Ethernet frames → ISP
  Fiber optic signals across backbone
  
Each layer: knows only its job, wraps previous layer's data.
All these layers run every time you click a link.
```

---

## Interview Questions — Pillar 2

### Junior Level

1. What is DNS and what problem does it solve?
2. What is the difference between TCP and UDP?
3. What is an HTTP status code? What does 404 mean? What does 401 mean?
4. What is HTTPS and how is it different from HTTP?
5. What is CORS and why does it exist?

### Mid Level

1. Walk me through what happens when a browser makes an HTTPS request.
2. What is the TCP three-way handshake? Why is it necessary?
3. What is the difference between 301 and 302? Between 401 and 403?
4. Explain how TLS provides confidentiality, integrity, and authentication.
5. What is a reverse proxy? What does it do that your Node.js app server shouldn't do?
6. What is perfect forward secrecy and why does it matter?
7. How does a CDN work? What determines cache hit vs. miss?

### Senior Level

1. Your API is experiencing "CORS errors" in production only. Users' browsers show `Access-Control-Allow-Origin` issues, but your development environment works fine. What would you investigate?
2. Explain cache-control: `no-cache` vs. `no-store` vs. `max-age=0, must-revalidate`. When would you use each?
3. How would you design a real-time notification system for 100,000 concurrent users? Compare SSE, WebSocket, and long-polling. What are the tradeoffs?
4. A user in Mumbai connecting to a US-based server has high latency. Walk me through every step in the connection lifecycle where you could reduce this latency.
5. What is BGP and why does a DNS attack like the Dyn incident in 2016 take down half the Internet?
6. Your load balancer is forwarding requests to 4 app servers. One server has CPU at 95%, others at 30%. What does this tell you about your load balancing algorithm? What would you change?
7. Explain how HTTP/2 multiplexing works and why HTTP/3 was still needed after HTTP/2 solved head-of-line blocking at the HTTP layer.
8. A client is getting intermittent 504 Gateway Timeout errors. Your Node.js server logs show no errors. Where is the timeout occurring and how would you diagnose it?

---

*Continue to `03-JavaScript-Fundamentals.md` →*

---


## 📄 File: 03-JavaScript-Fundamentals.md
*=====================================*

# Pillar 3 — JavaScript Fundamentals

> *"JavaScript is the only language where understanding it requires understanding how it was designed around a browser security model, a marketing deadline, and a 10-day prototype."*

---

## Table of Contents

1. [Execution Context](#1-execution-context)
2. [The Call Stack](#2-the-call-stack)
3. [Memory Allocation in JavaScript](#3-memory-allocation)
4. [Garbage Collection in V8](#4-garbage-collection)
5. [Scope](#5-scope)
6. [Lexical Environment](#6-lexical-environment)
7. [Closures](#7-closures)
8. [Hoisting](#8-hoisting)
9. [The `this` Keyword](#9-this)
10. [Prototype and Prototype Chain](#10-prototype-and-prototype-chain)
11. [Classes](#11-classes)
12. [Modules](#12-modules)

---

## 1. Execution Context

### Definition

An Execution Context (EC) is the abstract environment in which JavaScript code is evaluated and executed. It contains all the information needed to run a piece of code: variable bindings, the value of `this`, references to the outer scope.

Every time JavaScript code runs, it runs inside an execution context. You cannot run JavaScript outside one.

### Types of Execution Contexts

```
1. Global Execution Context (GEC)
   Created once when the JS engine starts.
   In browsers: `this` === window
   In Node.js: `this` === module.exports (at file level) or global

2. Function Execution Context (FEC)
   Created each time a function is called.
   Each call creates a NEW context — recursive calls create separate contexts.

3. Eval Execution Context
   Created when eval() is called.
   Avoid eval() in production. (security, performance, strict mode issues)
```

### What an Execution Context Contains

An execution context has two components that get created in two phases:

```
Execution Context = {
  
  VariableEnvironment: {
    // Created in CREATION phase (before any code runs)
    // Holds function declarations and var declarations
    // var declarations initialized to undefined
    // function declarations fully available (hoisted)
  },
  
  LexicalEnvironment: {
    // Created in CREATION phase
    // Holds let, const, function expressions, class declarations
    // let/const are in "temporal dead zone" until their line
    // Outer reference: pointer to parent scope's LexicalEnvironment
  },
  
  ThisBinding: <value of 'this' for this context>
}
```

### Two Phases of Execution

**Phase 1 — Creation Phase** (before any code runs in this context):
```
The engine scans the code and:
  1. Sets up memory space for variables declared with var → initialized to undefined
  2. Sets up memory space for function declarations → entire function stored
  3. let/const are NOTED but kept in temporal dead zone (TDZ)
  4. Determines value of 'this'
  5. Sets up Outer Environment reference (scope chain)
```

**Phase 2 — Execution Phase** (code runs line by line):
```
  1. Values are assigned to variables as their assignment lines execute
  2. Functions are called (creating new execution contexts)
  3. let/const become accessible at their declaration line
```

### The Execution Context Stack

```javascript
// What happens when this code runs:

var x = 10;  // Line 1

function outer() {      // Line 3
  var y = 20;           // Line 4
  
  function inner() {    // Line 6
    var z = 30;         // Line 7
    console.log(x + y + z);  // Line 8
  }
  
  inner();  // Line 11
}

outer();  // Line 14
```

```
Execution Stack (grows upward):

LINE 14: outer() called
  +----------------------+
  | inner() EC           |  ← pushed at line 11, popped after line 8
  | z = 30               |
  | this = global        |
  | outer = outer's env  |
  +----------------------+
  | outer() EC           |  ← pushed at line 14
  | y = 20               |
  | this = global        |
  | outer = global env   |
  +----------------------+
  | Global EC            |  ← always at bottom
  | x = 10               |
  | outer = function     |
  | this = window/global |
  +----------------------+

After inner() returns: inner() EC is popped
After outer() returns: outer() EC is popped
Global EC remains until program terminates
```

### Implementation: Observing Execution Context Behavior

```javascript
// Demonstrates the creation and execution phases

console.log(typeof getName);  // "function" — function declaration hoisted fully
console.log(typeof getAge);   // "undefined" — var declaration hoisted, not assignment
console.log(typeof getEmail); // ReferenceError! — let not accessible before declaration

// CREATION PHASE:
// Engine scans this code BEFORE executing any of it
// It finds:
//   - getName: function declaration → stored fully
//   - getAge: var declaration → stored as undefined
//   - getEmail: let declaration → noted, in temporal dead zone

function getName() { return 'Harish'; }  // Available from start (hoisted)
var getAge = function() { return 25; };   // Only the var is hoisted, not the function
let getEmail = () => 'h@example.com';     // NOT accessible before this line

console.log(getName()); // "Harish" — works because function hoisted
console.log(getAge());  // works now — assignment executed at this line
console.log(getEmail()); // works now — let is past its declaration line
```

---

## 2. The Call Stack

### Definition

The call stack is a data structure (a stack — LIFO) that the JavaScript engine uses to track which function is currently executing and where to return control when that function finishes.

Each function call pushes a **stack frame** (an execution context's runtime representation) onto the stack. When the function returns, its frame is popped.

### Why Understanding the Call Stack Matters

The call stack is the mechanism behind:
- How JavaScript "knows" where to return after a function call
- How `this` is determined (partly)
- Why deeply recursive functions cause "Maximum call stack size exceeded"
- What you see in stack traces in error messages
- Why JavaScript is single-threaded (one call stack = one thread of execution)

```javascript
// Reading and understanding stack traces — a critical debugging skill

function parseUserInput(input) {
  if (typeof input !== 'string') {
    throw new TypeError(`Expected string, got ${typeof input}`);
  }
  return JSON.parse(input);
}

function validateRequest(body) {
  const parsed = parseUserInput(body.data);
  return parsed;
}

function handleRequest(req) {
  const result = validateRequest(req.body);
  return result;
}

try {
  handleRequest({ body: { data: 123 } }); // data is a number, not string
} catch (e) {
  console.error(e.stack);
  /*
  TypeError: Expected string, got number
    at parseUserInput (app.js:3:11)    ← innermost function where throw happened
    at validateRequest (app.js:9:19)   ← called parseUserInput
    at handleRequest (app.js:14:18)    ← called validateRequest
    at Object.<anonymous> (app.js:19:3) ← top-level call
  
  Reading bottom-up: handleRequest called validateRequest called parseUserInput which threw
  */
}
```

### Stack Overflow — What Actually Happens in V8

```javascript
// V8 maintains a call stack with a fixed number of frames
// The default in Node.js is approximately 10,000-15,000 frames

function countDown(n) {
  // No base case — infinite recursion
  return countDown(n - 1);
}

try {
  countDown(0);
} catch (e) {
  console.log(e instanceof RangeError); // true
  console.log(e.message); // "Maximum call stack size exceeded"
  
  // What happened:
  // V8 tried to push ~10,000+ frames onto the call stack
  // It detected the stack was exhausted
  // Threw RangeError
  // The catch unwinds all frames at once
}

// How to increase (Node.js):
// node --stack-size=65536 app.js  (64KB per frame × lots of frames)

// Proper tail recursion (avoids stack growth):
// ECMAScript 2015 specifies TCO (Tail Call Optimization)
// V8 removed support due to debuggability concerns
// Workaround: use trampolining

function trampolineFactorial(n, acc = 1n) {
  if (n <= 1n) return acc;
  // Return a function instead of recursing directly
  return () => trampolineFactorial(n - 1n, n * acc);
}

function trampoline(fn) {
  let result = fn;
  // While the result is a function, keep calling it
  while (typeof result === 'function') {
    result = result();
  }
  return result;
}

console.log(trampoline(trampolineFactorial(100000n)));
// Computes factorial of 100,000 without stack overflow
// The call stack never grows beyond 2 frames
```

---

## 3. Memory Allocation

### How JavaScript Allocates Memory

JavaScript manages two primary memory regions for runtime data:

**Stack**: Primitive values and references (pointers) — stored directly in execution context.
**Heap**: Objects, arrays, functions — allocated dynamically.

```javascript
// STACK storage: primitives are stored by VALUE
let a = 5;          // stack: [a: 5]
let b = a;          // stack: [a: 5, b: 5] — b gets a COPY of the value
b = 10;
console.log(a); // 5 — a is unaffected. b changed its own copy.

// HEAP storage: objects are stored by REFERENCE
let obj1 = { x: 1 }; // heap: {x:1} at address 0x1234
                       // stack: [obj1: → 0x1234]
let obj2 = obj1;      // stack: [obj1: → 0x1234, obj2: → 0x1234]
                       // BOTH variables point to SAME heap object

obj2.x = 99;
console.log(obj1.x); // 99 — obj1 and obj2 point to the SAME object
console.log(obj1 === obj2); // true — same heap address
```

### Primitive Types and Value Semantics

Primitive types in JavaScript: `number`, `string`, `boolean`, `null`, `undefined`, `symbol`, `bigint`.

All primitives are **immutable** — their values cannot be changed. When you "modify" a string, you create a new string. The original is unchanged.

```javascript
let str = "hello";
let str2 = str;
str2 = str2.toUpperCase(); // Creates a NEW string "HELLO"
console.log(str);  // "hello" — original unchanged
console.log(str2); // "HELLO" — new string

// Strings are immutable — you cannot modify character in place:
str[0] = 'H'; // Silently does nothing in non-strict mode
console.log(str); // "hello" — unchanged
```

### Memory Implications of Pass-by-Value vs. Pass-by-Reference

JavaScript is always **pass-by-value**. But the value for objects is a reference (pointer). This is often called "pass-by-sharing" to distinguish it:

```javascript
function modifyPrimitive(num) {
  num = 100; // Modifies LOCAL copy of the value
}

function modifyObject(obj) {
  obj.x = 100; // Modifies the heap object the reference points to
}

function replaceObject(obj) {
  obj = { x: 999 }; // Replaces LOCAL reference — caller's reference unchanged
}

let n = 5;
let o = { x: 1 };

modifyPrimitive(n);
console.log(n); // 5 — unchanged

modifyObject(o);
console.log(o.x); // 100 — heap object was mutated through the reference

replaceObject(o);
console.log(o.x); // 100 — caller's reference still points to the SAME object
                   // replaceObject only changed its local copy of the reference
```

---

## 4. Garbage Collection

### V8's Generational GC Architecture

Covered architecturally in Pillar 1 (Heap section). Key JavaScript-specific points:

### What Makes an Object Eligible for GC

An object is **reachable** if it can be accessed from any **root**:
- Global variables
- Local variables in the current call stack
- Closure variables that are still referenced
- Registered event listeners
- Active timers (setTimeout/setInterval callbacks)

An object is **garbage** when it is no longer reachable from any root. V8's GC identifies and reclaims it.

### Memory Leaks in JavaScript — The Production Patterns

```javascript
// LEAK 1: Accidental global variable
function setup() {
  // Missing 'var', 'let', or 'const' — creates a global!
  userData = { id: 1, data: new Array(1000000) };
  // In strict mode: throws ReferenceError
  // In sloppy mode: creates window.userData (never GC'd until window closes)
}

// LEAK 2: Forgotten timers
function startPolling() {
  const cache = { data: new Array(100000) };
  
  setInterval(() => {
    // setInterval callback holds reference to 'cache' via closure
    // If you never clearInterval(), 'cache' is NEVER garbage collected
    console.log('polling...', cache.data.length);
  }, 1000);
  
  // Fix: return the interval ID and clearInterval when done
  // const id = setInterval(...);
  // return () => clearInterval(id);
}

// LEAK 3: Detached DOM nodes
function createLeak() {
  const container = document.getElementById('container');
  const element = document.createElement('div');
  element.addEventListener('click', () => {
    // This listener holds a reference to 'element'
    console.log(element.textContent);
  });
  container.appendChild(element);
  
  // Remove from DOM but keep JS reference
  container.removeChild(element);
  // 'element' is not in DOM anymore but the event listener
  // prevents GC if something else references the listener
  
  // Fix: removeEventListener before removing from DOM
  // OR use once: true option for one-time handlers
  // OR use WeakRef for weak references
}

// LEAK 4: Closures holding large data unnecessarily
function processLargeData(data) {
  const largeBuffer = new ArrayBuffer(50_000_000); // 50 MB
  
  // This inner function closes over largeBuffer
  // If returnedFn lives long, largeBuffer is never collected
  const returnedFn = () => {
    // Actually only uses data, not largeBuffer
    return data.length;
  };
  
  return returnedFn;
}

// Fix: don't create the closure over largeBuffer if not needed
// Or explicitly: largeBuffer = null; before returning

// PRODUCTION DETECTION: Use Node.js heap snapshots
// node --inspect app.js → Chrome DevTools → Memory tab → Take heap snapshot
// Compare snapshots over time to find growing objects
```

### WeakRef and FinalizationRegistry (ES2021)

```javascript
// WeakRef: hold a reference to an object WITHOUT preventing GC
let target = { id: 1, data: new Array(1000000) };
const weakRef = new WeakRef(target);

// The WeakRef does NOT prevent GC of 'target'
target = null; // Remove strong reference

// At some future GC cycle, the original object may be collected
// weakRef.deref() returns undefined if the object was collected
const obj = weakRef.deref();
if (obj !== undefined) {
  console.log('Object still alive:', obj.id);
} else {
  console.log('Object was garbage collected');
}

// FinalizationRegistry: callback when an object is GC'd
// Useful for cleanup of external resources
const registry = new FinalizationRegistry((heldValue) => {
  // Called when registered object is GC'd
  // heldValue is whatever you passed as third argument to register()
  console.log(`Object with id ${heldValue} was garbage collected`);
  // Perform cleanup: close file handle, release native resource, etc.
});

let resource = { id: 42, connection: 'open' };
registry.register(resource, resource.id); // Register with cleanup value

resource = null; // Remove strong reference → will be GC'd eventually
```

---

## 5. Scope

### Definition

Scope defines the region of a program where a particular variable binding is accessible. JavaScript has lexical scoping (also called static scoping): the scope of a variable is determined by its position in the source code, not by where or how the function is called.

### Scope Types

**Global scope**: Accessible everywhere. Variables declared outside any function or block.

**Function scope**: Variables declared with `var` are scoped to the enclosing function.

**Block scope**: Variables declared with `let` or `const` are scoped to the enclosing block `{}`.

**Module scope**: In ES modules, top-level variables are module-scoped, not global.

```javascript
// Demonstrating all scope types

var globalVar = 'I am global';         // Global scope
let globalLet = 'I am also global';   // Global scope (but not on window in browsers)

function functionScope() {
  var funcVar = 'function scope';      // Function scope
  let blockLet = 'also function scope (block = function here)';
  
  if (true) {
    var blockVar = 'SURPRISE! var is function-scoped!'; // Goes to functionScope's scope
    let trueBlockLet = 'true block scope — this if block';
    const trueBlockConst = 'also true block scope';
    
    console.log(funcVar);       // "function scope" ← accessible (outer scope)
    console.log(trueBlockLet); // "true block scope" ← accessible
  }
  
  console.log(blockVar);      // "SURPRISE! var is function-scoped!" ← accessible!
  // console.log(trueBlockLet); // ReferenceError ← block is over
  
  return () => {
    // Arrow function creates a new block (lexical 'this') but same scope chain
    console.log(funcVar);     // still accessible — closure over functionScope
    console.log(globalVar);   // accessible — global scope
  };
}

const fn = functionScope();
fn(); // Can still access funcVar via closure
// console.log(funcVar); // ReferenceError ← funcVar is function-scoped
```

### The Scope Chain

When code in an inner scope references a variable, JavaScript searches:
1. Current scope (function/block)
2. Outer scope
3. Outer outer scope
4. ...until Global scope
5. If not found: `ReferenceError`

```javascript
const x = 'global x';

function outer() {
  const y = 'outer y';
  
  function inner() {
    const z = 'inner z';
    
    // Scope chain lookup:
    // z → found in inner scope ✓
    // y → not in inner → search outer → found ✓
    // x → not in inner → not in outer → search global → found ✓
    // w → not anywhere → ReferenceError
    
    console.log(z); // 'inner z' — own scope
    console.log(y); // 'outer y' — outer scope
    console.log(x); // 'global x' — global scope
  }
  
  inner();
}

outer();
```

The scope chain is created at **parse time** based on where functions are written, not where they are called. This is **lexical scoping**.

---

## 6. Lexical Environment

### Definition

A Lexical Environment is the internal data structure that the JavaScript engine uses to implement scoping. Each execution context has a Lexical Environment consisting of:

1. **Environment Record**: The actual storage of variable → value bindings for this scope
2. **Outer reference**: A pointer to the parent (enclosing) Lexical Environment

The scope chain is the chain of these outer references.

### Anatomy

```
Global Lexical Environment:
  EnvironmentRecord:
    x: 'global x'
    outer: undefined  ← outer function → globally defined
  OuterEnv: null  ← no outer for global

outer() Lexical Environment (when outer() is called):
  EnvironmentRecord:
    y: 'outer y'
    inner: <function>
  OuterEnv: → Global Lexical Environment

inner() Lexical Environment (when inner() is called):
  EnvironmentRecord:
    z: 'inner z'
  OuterEnv: → outer() Lexical Environment
```

When `inner` looks up `y`:
- Check inner's EnvironmentRecord → not found
- Follow OuterEnv → outer's EnvironmentRecord → found `y: 'outer y'`

This chain of EnvironmentRecords is what the "scope chain" physically is.

### Lexical Environment vs. Variable Environment

In modern JavaScript (ES6+), each execution context has **two** environment records:
- `VariableEnvironment`: Holds `var` and function declarations
- `LexicalEnvironment`: Holds `let`, `const`, class declarations

They start identically but diverge in block statements:

```javascript
function example() {
  // VariableEnvironment: { varDecl: undefined }
  // LexicalEnvironment:  { letDecl: <TDZ> }
  
  var varDecl = 1;  // Goes to VariableEnvironment
  let letDecl = 2;  // Goes to LexicalEnvironment
  
  {
    // NEW LexicalEnvironment created for this block:
    // { blockLet: <TDZ> }
    // OuterEnv: → example's LexicalEnvironment
    
    let blockLet = 3; // In this block's LexicalEnvironment
    var blockVar = 4; // Goes to FUNCTION's VariableEnvironment (var ignores blocks)
  }
  
  console.log(blockVar); // 4 — var in function's VarEnv
  // console.log(blockLet); // ReferenceError — block's LexEnv is gone
}
```

---

## 7. Closures

### Definition

A closure is the combination of a function and its **captured lexical environment** — the set of variable bindings that were in scope when the function was created. A closure "closes over" the variables it references from outer scopes.

This is not a JavaScript-specific concept — it exists in any language with first-class functions and lexical scoping (Python, Swift, Kotlin, Go, Rust, etc.).

### The Mechanism

```javascript
function makeCounter() {
  let count = 0; // In makeCounter's LexicalEnvironment
  
  // This inner function is returned to the outside world
  return function increment() {
    // increment's LexicalEnvironment:
    //   {} (no own variables)
    //   OuterEnv: → makeCounter's LexicalEnvironment
    //                which contains: count = 0
    
    count++; // Reads AND WRITES makeCounter's 'count' via the scope chain
    return count;
  };
}

const counter = makeCounter();
// makeCounter's call frame is GONE from the call stack
// BUT its LexicalEnvironment is NOT garbage collected!
// WHY? Because 'counter' (the returned function) holds a reference to it

console.log(counter()); // 1
console.log(counter()); // 2
console.log(counter()); // 3
// Each call reads and updates the SAME count variable
// That variable lives in makeCounter's preserved LexicalEnvironment

const counter2 = makeCounter(); // SEPARATE LexicalEnvironment!
console.log(counter2()); // 1 — independent counter
console.log(counter()); // 4 — original counter unaffected
```

This is the critical insight: **a closure preserves the lexical environment of the outer function even after the outer function has returned**. The GC cannot collect that environment because the inner function still holds a reference to it.

### Closures in Production: The Module Pattern

Before ES modules, closures were used to create private state:

```javascript
// Classic Module Pattern using closures
// This was the standard for 2009–2015 JavaScript

const UserModule = (function() {
  // Private state — inaccessible from outside
  let users = [];
  let nextId = 1;
  
  // Private function — not exposed
  function validateEmail(email) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
  }
  
  // Public API — returned and accessible
  return {
    addUser(name, email) {
      if (!validateEmail(email)) {
        throw new Error(`Invalid email: ${email}`);
      }
      const user = { id: nextId++, name, email };
      users.push(user);
      return user;
    },
    
    getUser(id) {
      return users.find(u => u.id === id);
    },
    
    getAllUsers() {
      // Return a copy — prevent external mutation of internal array
      return [...users];
    },
    
    getUserCount() {
      return users.length;
    }
  };
})(); // IIFE: Immediately Invoked Function Expression

// External code can only access the public API:
const user = UserModule.addUser('Harish', 'h@example.com');
console.log(UserModule.getUserCount()); // 1
// console.log(users); // ReferenceError — 'users' is private to the closure
```

### Closure Gotcha: The Classic Loop Problem

This trips up developers consistently in interviews:

```javascript
// THE BROKEN VERSION — classic interview trap
for (var i = 0; i < 3; i++) {
  setTimeout(() => {
    console.log(i); // Logs: 3, 3, 3 — NOT 0, 1, 2!
  }, 100);
}

// WHY?
// 'var i' is function-scoped (or global here) — there is ONE 'i' variable
// All three arrow functions close over the SAME 'i'
// When the timeouts fire (100ms later), the loop has finished
// i = 3 (loop ended)
// All three functions read the same i = 3
```

```javascript
// FIX 1: Use 'let' (block scoping creates new binding per iteration)
for (let i = 0; i < 3; i++) {
  setTimeout(() => {
    console.log(i); // Logs: 0, 1, 2 ✓
  }, 100);
}
// WHY? 'let' creates a NEW binding per loop iteration
// Each closure closes over a DIFFERENT 'i' binding
// i=0 for first iteration, i=1 for second, i=2 for third
// Each timeout function has its own 'i'
```

```javascript
// FIX 2: Use an IIFE to capture the current value
for (var i = 0; i < 3; i++) {
  (function(capturedI) {
    // capturedI is a NEW parameter binding for each IIFE call
    // The function parameter creates a new scope with a copy of i
    setTimeout(() => {
      console.log(capturedI); // Logs: 0, 1, 2 ✓
    }, 100);
  })(i); // Pass current value of i into IIFE
}
```

```javascript
// FIX 3: Use setTimeout's extra argument (less known)
for (var i = 0; i < 3; i++) {
  setTimeout((capturedI) => {
    console.log(capturedI); // Logs: 0, 1, 2 ✓
  }, 100, i); // setTimeout passes extra args to callback
}
```

### Production Closure: Memoization

```javascript
// Memoization using closures — cache expensive computation results
function memoize(fn) {
  // The cache is private state in the closure
  const cache = new Map();
  
  return function(...args) {
    // Create a cache key from arguments
    const key = JSON.stringify(args);
    
    if (cache.has(key)) {
      console.log('Cache hit!');
      return cache.get(key);
    }
    
    console.log('Computing...');
    const result = fn.apply(this, args);
    cache.set(key, result);
    return result;
  };
}

function expensiveFibonacci(n) {
  if (n <= 1) return n;
  return expensiveFibonacci(n - 1) + expensiveFibonacci(n - 2);
}

const memoFib = memoize(expensiveFibonacci);
console.log(memoFib(40)); // "Computing..." — takes ~1 second
console.log(memoFib(40)); // "Cache hit!" — instant

// Production-grade: bounded cache with LRU eviction
function memoizeWithLRU(fn, maxSize = 100) {
  const cache = new Map(); // Map preserves insertion order
  
  return function(...args) {
    const key = JSON.stringify(args);
    
    if (cache.has(key)) {
      // LRU: move accessed entry to end (most recently used)
      const value = cache.get(key);
      cache.delete(key);
      cache.set(key, value);
      return value;
    }
    
    const result = fn.apply(this, args);
    
    // Evict least recently used (first inserted) if at capacity
    if (cache.size >= maxSize) {
      const firstKey = cache.keys().next().value;
      cache.delete(firstKey);
    }
    
    cache.set(key, result);
    return result;
  };
}
```

### Closures and Memory Leaks

```javascript
// A closure that accidentally prevents GC of a large object

function createClosure() {
  const LARGE_DATA = new Array(1000000).fill('data'); // ~8MB
  
  // This closure only uses 'count', but it closes over the ENTIRE scope
  // of createClosure, which includes LARGE_DATA
  let count = 0;
  
  return function() {
    // Only accesses 'count', NOT 'large_data'
    // But V8 must keep the entire lexical environment alive
    // because the closure references this scope
    return ++count;
  };
  
  // Note: V8 is smart about this in modern versions — it may only
  // retain variables that are actually referenced by the inner function.
  // But this is an implementation detail, not guaranteed behavior.
  // Better practice: explicitly set LARGE_DATA = null before returning.
}
```

### How Interviewers Attack Closures

**Entry question**: "What is a closure?"

Follow-up chain:
1. "Where does the closed-over variable live in memory?" → In the lexical environment of the outer scope, on the heap (not the stack, since the outer function's stack frame is gone)
2. "Can closures cause memory leaks?" → Yes — if the inner function is kept alive (stored globally, in event listeners, etc.), the entire closed-over environment is kept alive
3. "Show me the loop problem and explain why it happens." → The `var`/`let` distinction, scope chain, when closures are evaluated vs. when the callback fires
4. "What is a WeakRef and how does it relate to closures?" → WeakRef lets you hold a reference without preventing GC; useful when you don't want a closure to force retention of a large object
5. "If two closures are returned from the same function, do they share the same environment?" → Yes — they both close over the SAME environment record of the outer function. This means mutation in one is visible in the other.

---

## 8. Hoisting

### Definition

Hoisting is the JavaScript behavior where variable and function declarations are conceptually "moved" to the top of their containing scope before any code executes. In reality, no code is moved — during the **creation phase** of the execution context, the engine pre-processes declarations.

### What Gets Hoisted and How

```
Declaration Type        | Hoisted? | Initialized?
------------------------|----------|--------------
var declaration         | Yes      | undefined
function declaration    | Yes      | Full function value
let declaration         | Yes*     | No (temporal dead zone)
const declaration       | Yes*     | No (temporal dead zone)
function expression     | Var only | undefined (not the function)
class declaration       | Yes*     | No (temporal dead zone)
import (ES modules)     | Yes      | Yes (fully linked)

* "Hoisted" to the top of block, but in TDZ until the declaration line
```

### Temporal Dead Zone (TDZ)

The TDZ is the period between the start of the enclosing block and the `let`/`const` declaration line. During this period, the binding exists (it was noted in the creation phase) but accessing it throws a `ReferenceError`.

```javascript
{
  // TDZ begins for 'x' here
  
  console.log(typeof x); // ReferenceError — NOT "undefined" like with var!
  // Many developers think typeof always returns safely. Not with let in TDZ.
  
  let x = 5; // TDZ ends here; x is initialized to 5
  
  console.log(x); // 5
}

// This is different from an undeclared variable:
console.log(typeof undeclaredVar); // "undefined" — typeof is safe for truly undeclared
```

### Practical Hoisting Examples

```javascript
// EXAMPLE 1: Function declaration vs. expression hoisting

// Function DECLARATION is fully hoisted — call it before its "location"
console.log(declaredFn()); // "I was declared" — works!

function declaredFn() {
  return 'I was declared';
}

// Function EXPRESSION assigned to var — only var is hoisted (as undefined)
// console.log(expressionFn()); // TypeError: expressionFn is not a function
// (expressionFn exists as undefined, calling undefined() throws TypeError)

var expressionFn = function() {
  return 'I was expressed';
};

// EXAMPLE 2: var hoisting across blocks — the confusing behavior

function demonstrateVarHoisting() {
  console.log(x); // undefined (NOT ReferenceError)
  // The engine pre-scanned and saw 'var x' → initialized x to undefined
  // Execution hasn't reached 'var x = 10' yet
  
  if (true) {
    console.log(x); // undefined — var ignores block boundaries
    var x = 10;
    console.log(x); // 10
  }
  
  console.log(x); // 10 — var is function-scoped, accessible here
}

demonstrateVarHoisting();

// EXAMPLE 3: The function declaration quirk inside blocks
// (Different behavior across browsers — generally avoid)

{
  // In strict mode: function is block-scoped
  // In sloppy mode: behavior is implementation-defined (don't rely on it)
  function blockFn() { return 'from block'; }
}
// Avoid function declarations inside blocks — use function expressions
```

---

## 9. The `this` Keyword

### Definition

`this` is a special keyword that refers to the **execution context** in which a function is called — specifically, the object to which the function is bound at the time of the call. The value of `this` is determined dynamically at call time, not at definition time (except for arrow functions and bound functions).

This is fundamentally different from lexical scoping. `this` is **not lexically scoped**. It depends on how the function is called.

### The Four Rules of `this` Binding

**Rule 1 — Default Binding**: A function called without any binding context.

```javascript
function standalone() {
  console.log(this);
}

standalone(); 
// Non-strict mode: this === global object (window in browser, global in Node.js)
// Strict mode: this === undefined

'use strict';
standalone(); // undefined — no implicit global binding in strict mode
```

**Rule 2 — Implicit Binding**: A function called as a method of an object.

```javascript
const user = {
  name: 'Harish',
  greet() {
    console.log(`Hello, I am ${this.name}`);
    // 'this' refers to the object left of the dot: user
  }
};

user.greet(); // "Hello, I am Harish"
// this === user (implicit binding via dot notation)

// THE TRAP: Extracting the method loses the binding!
const greetFn = user.greet; // Just a reference to the function
greetFn(); // "Hello, I am undefined" — or throws in strict mode
// 'this' falls back to default binding (global or undefined)
// The function is the same, but how it's CALLED changes 'this'
```

**Rule 3 — Explicit Binding**: Using `call()`, `apply()`, or `bind()`.

```javascript
function greet(greeting) {
  console.log(`${greeting}, I am ${this.name}`);
}

const user1 = { name: 'Harish' };
const user2 = { name: 'Alice' };

greet.call(user1, 'Hello');   // "Hello, I am Harish"
// call: first arg is 'this', rest are function arguments

greet.apply(user2, ['Hi']);   // "Hi, I am Alice"
// apply: first arg is 'this', second is array of arguments

const greetHarish = greet.bind(user1); // Returns new function with 'this' locked
greetHarish('Hey');                     // "Hey, I am Harish"
greetHarish.call(user2, 'Hey');         // "Hey, I am Harish" — bind wins over call!
// Once bound, 'this' cannot be changed
```

**Rule 4 — `new` Binding**: When a function is called with `new`.

```javascript
function Person(name) {
  // When called with 'new':
  // 1. A new empty object is created
  // 2. 'this' is bound to that new object
  // 3. The object's prototype is set to Person.prototype
  // 4. The new object is returned (unless you explicitly return another object)
  
  this.name = name;    // Setting property on the new object
  this.greet = function() {
    return `Hi, I'm ${this.name}`;
  };
}

const person = new Person('Harish');
// Equivalent to:
// const person = Object.create(Person.prototype);
// Person.call(person, 'Harish');
// return person;

console.log(person.name);    // 'Harish'
console.log(person.greet()); // "Hi, I'm Harish"
```

### Arrow Functions and `this` (Lexical `this`)

Arrow functions do **not** have their own `this`. They inherit `this` from the **enclosing lexical context** (where they were defined). This is different from all the rules above.

```javascript
const obj = {
  name: 'Harish',
  
  regularMethod: function() {
    console.log(this.name); // "Harish" — implicit binding, this = obj
    
    // Common problem: 'this' in nested callback
    setTimeout(function() {
      console.log(this.name); // undefined — regular function, this = global/undefined
    }, 100);
    
    // Fix with arrow function: 'this' is inherited from regularMethod's context
    setTimeout(() => {
      console.log(this.name); // "Harish" — arrow inherits this from regularMethod
    }, 100);
  },
  
  arrowMethod: () => {
    // Arrow function as a method — 'this' is NOT the object
    // It's inherited from where the arrow was DEFINED: the object literal's context
    // Object literals don't create a new 'this' binding
    // So 'this' here is the global object (or undefined in strict mode)
    console.log(this); // {} (module.exports in Node.js) or window in browser
    console.log(this?.name); // undefined
  }
};

obj.regularMethod(); // Works as expected
obj.arrowMethod();   // 'this' is NOT obj — arrow methods are a common bug
```

### `this` Binding Priority

When multiple rules could apply:

```
new binding     (highest priority)
  |
explicit bind (call/apply/bind)
  |
implicit bind (method call: obj.method())
  |
default bind (standalone call)  (lowest priority)
```

### Production Pattern: Class Methods and `this`

```javascript
// The lost 'this' problem in event handlers and callbacks

class EventHandler {
  constructor(name) {
    this.name = name;
    this.count = 0;
    
    // FIX 1: Bind in constructor (creates new function per instance)
    this.handleClick = this.handleClick.bind(this);
  }
  
  handleClick() {
    // Without the bind: 'this' would be the DOM element or undefined
    // With the bind: 'this' is always this EventHandler instance
    this.count++;
    console.log(`${this.name} clicked ${this.count} times`);
  }
  
  // FIX 2: Class field arrow function (modern, no bind needed)
  handleScroll = () => {
    // Arrow class field captures 'this' lexically at instance creation
    this.count++;
    console.log(`${this.name} scrolled`);
  }
  
  setup(element) {
    element.addEventListener('click', this.handleClick);    // Works (bound)
    element.addEventListener('scroll', this.handleScroll);  // Works (arrow)
    
    // WRONG: this loses binding when passed as callback without bind
    // element.addEventListener('click', this.handleClick_unbound);
    // Would log 'undefined clicked N times' or throw
  }
}
```

---

## 10. Prototype and Prototype Chain

### Definition

JavaScript uses **prototype-based inheritance**. Every object has an internal property `[[Prototype]]` (accessible as `__proto__`) that points to another object — its prototype. When you access a property on an object, JavaScript looks it up: first on the object itself, then on its prototype, then on the prototype's prototype, and so on, until it finds the property or reaches `null`.

This chain of prototype references is the **prototype chain**.

### Why Prototypes Exist

Prototypes solve the problem of sharing behavior across many objects without copying it into each one:

```javascript
// Without prototypes: methods copied into each object (wasteful)
function createUser(name) {
  return {
    name,
    // Each user object gets its own copy of greet function
    // 1000 users = 1000 copies of the same function in memory
    greet() { return `Hi, I'm ${this.name}`; }
  };
}

// With prototypes: methods shared on the prototype
function User(name) {
  this.name = name; // Instance data on the object itself
}

// Shared methods on the prototype (ONE copy, shared by all instances)
User.prototype.greet = function() {
  return `Hi, I'm ${this.name}`;
};

const u1 = new User('Harish');
const u2 = new User('Alice');

// u1 and u2 both have 'greet' accessible, but via the SHARED prototype
console.log(u1.greet === u2.greet); // true — same function reference!
// Zero duplication of method code regardless of how many User instances
```

### Prototype Chain Lookup — Step by Step

```javascript
const u = new User('Harish');

// u.__proto__ === User.prototype
// User.prototype.__proto__ === Object.prototype
// Object.prototype.__proto__ === null  ← end of chain

u.greet(); // Lookup:
// 1. Does 'u' have 'greet'? → No (only has 'name')
// 2. Does u.__proto__ (User.prototype) have 'greet'? → YES → call it with this=u

u.toString(); // Lookup:
// 1. Does 'u' have 'toString'? → No
// 2. Does User.prototype have 'toString'? → No
// 3. Does Object.prototype have 'toString'? → YES → found it

u.nonExistent; // Lookup:
// 1. 'u' → No
// 2. User.prototype → No
// 3. Object.prototype → No
// 4. null → stop
// Returns: undefined
```

### Visualizing the Prototype Chain

```
User function:
  User.prototype → { greet: fn, constructor: User }

new User('Harish') creates:
  u1 = { name: 'Harish', [[Prototype]]: User.prototype }

new User('Alice') creates:
  u2 = { name: 'Alice', [[Prototype]]: User.prototype }

Chain:
  u1 → User.prototype → Object.prototype → null
  u2 → User.prototype → Object.prototype → null
       ↑
  Both share the SAME User.prototype object
```

### `Object.create()` — Explicit Prototype Setting

```javascript
// Object.create(proto) creates a new object with proto as its [[Prototype]]
const animalProto = {
  breathe() {
    return `${this.name} is breathing`;
  },
  eat(food) {
    return `${this.name} eats ${food}`;
  }
};

const dog = Object.create(animalProto);
dog.name = 'Rex';
dog.bark = function() { return 'Woof!'; };

// dog's prototype chain:
// dog → animalProto → Object.prototype → null

console.log(dog.breathe()); // "Rex is breathing" — from prototype
console.log(dog.bark());    // "Woof!" — own property
console.log(Object.getPrototypeOf(dog) === animalProto); // true
```

### Property Shadowing

```javascript
function Animal(name) { this.name = name; }
Animal.prototype.speak = function() { return 'generic sound'; };

const dog = new Animal('Rex');
// Currently: dog.speak() → "generic sound" (from prototype)

// Adding own 'speak' property SHADOWS the prototype's:
dog.speak = function() { return 'Woof!'; };
console.log(dog.speak()); // "Woof!" — own property found first
// Prototype's speak is shadowed but NOT modified

const cat = new Animal('Whiskers');
console.log(cat.speak()); // "generic sound" — cat's prototype unchanged

// Deleting the own property reveals the prototype's:
delete dog.speak;
console.log(dog.speak()); // "generic sound" — own shadow gone, prototype visible
```

### `hasOwnProperty` vs. `in` Operator

```javascript
const obj = { name: 'Harish' };
// name is an OWN property
// toString is from Object.prototype

console.log('name' in obj);          // true — checks entire chain
console.log('toString' in obj);      // true — found on Object.prototype

console.log(obj.hasOwnProperty('name'));     // true — own property
console.log(obj.hasOwnProperty('toString')); // false — not own property

// Modern alternative: Object.hasOwn() (ES2022, avoids prototype method shadowing risk)
console.log(Object.hasOwn(obj, 'name'));     // true
console.log(Object.hasOwn(obj, 'toString')); // false
```

### Performance Implications of Long Prototype Chains

Property lookup traverses the chain one link at a time. Each link is a memory access. Deep chains (5+ levels) can have measurable performance impact in hot code paths.

V8 optimizes this with **hidden classes** (also called **shapes** or **maps**): it tracks the "shape" of objects (which properties they have, in what order they were added) and compiles specialized machine code for property access that avoids chain traversal in the common case.

This is why adding properties to objects after creation, or in inconsistent order, can hurt V8 performance — it invalidates the hidden class and triggers deoptimization.

---

## 11. Classes

### Definition

ES6 Classes are **syntactic sugar** over the prototype system. They do not introduce a new inheritance mechanism — they provide a cleaner syntax for defining constructor functions and populating their prototypes.

### Class Syntax vs. Prototype Syntax — Equivalence

```javascript
// ES6 Class syntax
class Animal {
  #sound; // Private class field (ES2022)
  
  constructor(name) {
    this.name = name;
    this.#sound = 'generic sound';
  }
  
  speak() {
    return `${this.name} says ${this.#sound}`;
  }
  
  static create(name) {
    return new Animal(name);
  }
}

class Dog extends Animal {
  constructor(name, breed) {
    super(name); // Must call super() before using 'this' in derived class
    this.breed = breed;
    // Private fields: each class has its own private scope
    // Dog cannot access Animal's #sound
  }
  
  speak() {
    // super.speak() calls Animal.prototype.speak with this=this
    return `${super.speak()} (actually "Woof!")`;
  }
}

// THE EQUIVALENT PROTOTYPE CODE (what class compiles to):
function AnimalProto(name) {
  this.name = name;
  // #sound would be a WeakMap or Symbol keyed private field in ES5 era
}
AnimalProto.prototype.speak = function() {
  return `${this.name} says generic sound`;
};
AnimalProto.create = function(name) { // Static method on constructor function
  return new AnimalProto(name);
};

function DogProto(name, breed) {
  AnimalProto.call(this, name); // super(name)
  this.breed = breed;
}
DogProto.prototype = Object.create(AnimalProto.prototype); // Set up inheritance chain
DogProto.prototype.constructor = DogProto; // Fix constructor reference
DogProto.prototype.speak = function() {
  const base = AnimalProto.prototype.speak.call(this); // super.speak()
  return `${base} (actually "Woof!")`;
};
```

### Class Features Deep Dive

```javascript
class BankAccount {
  // Static class field — shared across all instances, not per-instance
  static interestRate = 0.05;
  static #instanceCount = 0; // Private static
  
  // Instance fields (per-instance, defined in class body, not constructor)
  #balance; // Private — inaccessible from outside the class
  #owner;
  transactionHistory = []; // Public instance field
  
  constructor(owner, initialBalance = 0) {
    this.#owner = owner;
    this.#balance = initialBalance;
    BankAccount.#instanceCount++;
  }
  
  // Getter — accessed as property, not method call
  get balance() {
    return this.#balance;
  }
  
  // Setter — validation before assignment
  set balance(amount) {
    if (amount < 0) throw new RangeError('Balance cannot be negative');
    this.#balance = amount;
  }
  
  deposit(amount) {
    if (amount <= 0) throw new RangeError('Deposit amount must be positive');
    this.#balance += amount;
    this.transactionHistory.push({ type: 'deposit', amount, balance: this.#balance });
    return this;  // Return 'this' for method chaining
  }
  
  withdraw(amount) {
    if (amount > this.#balance) throw new Error('Insufficient funds');
    this.#balance -= amount;
    this.transactionHistory.push({ type: 'withdrawal', amount, balance: this.#balance });
    return this;
  }
  
  // Private method
  #formatBalance() {
    return `$${this.#balance.toFixed(2)}`;
  }
  
  toString() {
    return `Account[${this.#owner}]: ${this.#formatBalance()}`;
  }
  
  static getInstanceCount() {
    return BankAccount.#instanceCount;
  }
}

const account = new BankAccount('Harish', 1000);
account.deposit(500).withdraw(200); // Method chaining
console.log(account.balance);       // 1300 — getter
console.log(account.toString());    // "Account[Harish]: $1300.00"
// account.#balance; // SyntaxError — private field

// What 'class' compiles to (simplified for a transpiler target):
// The private fields are stored in a WeakMap or compiled to special JS engine slots
```

### Mixins — Composition Over Inheritance

```javascript
// JavaScript single inheritance chain is limiting
// Mixins provide a way to compose behavior from multiple sources

const Serializable = (Base) => class extends Base {
  serialize() {
    return JSON.stringify(this);
  }
  
  static deserialize(json) {
    const data = JSON.parse(json);
    return Object.assign(new this(), data);
  }
};

const Validatable = (Base) => class extends Base {
  validate() {
    for (const [field, rule] of Object.entries(this.constructor.validationRules ?? {})) {
      if (!rule(this[field])) {
        throw new Error(`Validation failed for field: ${field}`);
      }
    }
    return true;
  }
};

const Timestamped = (Base) => class extends Base {
  constructor(...args) {
    super(...args);
    this.createdAt = new Date().toISOString();
    this.updatedAt = new Date().toISOString();
  }
  
  touch() {
    this.updatedAt = new Date().toISOString();
    return this;
  }
};

// Compose mixins
class User extends Serializable(Validatable(Timestamped(class {}))) {
  static validationRules = {
    name: (v) => typeof v === 'string' && v.length > 0,
    email: (v) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v),
  };
  
  constructor(name, email) {
    super();
    this.name = name;
    this.email = email;
  }
}

const user = new User('Harish', 'h@example.com');
user.validate();                          // Uses Validatable mixin
const json = user.serialize();            // Uses Serializable mixin
console.log(user.createdAt);             // Uses Timestamped mixin
```

---

## 12. Modules

### Why Modules Exist

Before modules, all JavaScript ran in global scope. Including 10 library scripts meant 10 sets of global variables that could collide. The larger the codebase, the worse the global pollution problem.

### CommonJS (Node.js)

```javascript
// utils.js — CommonJS module
const crypto = require('crypto'); // Synchronous require

const SECRET_KEY = 'my-secret'; // Module-private — not exported

function hashPassword(password) {
  return crypto.createHmac('sha256', SECRET_KEY)
               .update(password)
               .digest('hex');
}

function compareHash(password, hash) {
  return hashPassword(password) === hash;
}

// module.exports is the object that gets returned when this module is require()'d
module.exports = {
  hashPassword,
  compareHash,
};

// Alternative: exports shorthand (same as module.exports for object additions)
// exports.hashPassword = hashPassword;
// WARNING: exports = { ... } BREAKS the reference — use module.exports for replacing
```

```javascript
// app.js — consuming the CommonJS module
const { hashPassword, compareHash } = require('./utils');
// require() is SYNCHRONOUS — entire module file is executed and cached
// Second require('./utils') returns the CACHED module.exports — doesn't re-execute

const hash = hashPassword('myPassword123');
console.log(compareHash('myPassword123', hash)); // true
console.log(compareHash('wrongPassword', hash));  // false
```

### ES Modules (ESM)

```javascript
// utils.mjs (or utils.js with "type": "module" in package.json)

// Named exports
export function hashPassword(password) { ... }
export function compareHash(password, hash) { ... }

// Named export with alias
const INTERNAL_KEY = 'secret';
export { INTERNAL_KEY as encryptionKey };

// Default export (one per module)
export default class CryptoService {
  hash(data) { ... }
  verify(data, hash) { ... }
}
```

```javascript
// app.mjs — consuming ES modules
import { hashPassword, compareHash } from './utils.mjs'; // Named imports
import CryptoService from './utils.mjs';                  // Default import
import * as Utils from './utils.mjs';                     // Namespace import

// Dynamic import — loads module lazily (returns Promise)
const heavyModule = await import('./heavy-computation.mjs');
// Useful for code splitting, conditional loading
```

### CommonJS vs. ES Modules — Critical Differences

| Property | CommonJS (require) | ES Modules (import) |
|---|---|---|
| Loading | Synchronous | Asynchronous (can be parallelized) |
| Evaluation | At require() time | Deferred until module graph resolved |
| Binding type | Copies of values | Live bindings (reflect mutations) |
| Caching | Yes (module.exports cached) | Yes (module cached) |
| Tree-shaking | Cannot (dynamic require) | Yes (static analysis of imports) |
| Top-level await | No | Yes |
| Circular deps | Can work (partial object) | Works differently (live bindings) |
| `this` at top level | module.exports | undefined |
| File extension | .js or .cjs | .mjs or .js with type:module |

### Live Bindings vs. Value Copies

```javascript
// counter.mjs
export let count = 0;
export function increment() { count++; }

// app.mjs
import { count, increment } from './counter.mjs';
console.log(count); // 0
increment();
console.log(count); // 1 — live binding! reflects the mutation

// CommonJS equivalent:
// const { count, increment } = require('./counter.cjs');
// console.log(count); // 0
// increment();
// console.log(count); // 0 — copied value! doesn't reflect mutation
```

### Tree Shaking (Production Impact)

```javascript
// math.mjs
export function add(a, b) { return a + b; }
export function subtract(a, b) { return a - b; }
export function multiply(a, b) { return a * b; }
export function factorial(n) {
  if (n <= 1) return 1;
  return n * factorial(n - 1);
}

// app.mjs
import { add } from './math.mjs';
// Only 'add' is used

// BUNDLER (webpack, Rollup, esbuild) with ES modules:
// Static analysis can determine that subtract, multiply, factorial are NEVER imported
// They are removed from the final bundle (tree-shaking)
// RESULT: smaller bundle, faster page load

// With CommonJS:
// const { add } = require('./math.cjs'); // Dynamic — bundler cannot be sure
// what properties of the module object are used at runtime
// Safe assumption: include everything → larger bundle
```

---

## Summary: How These Fundamentals Connect

```
Source code arrives in V8
         │
         ↓
Parsing creates AST
         │
         ↓  (Creation Phase of GEC)
Global Execution Context created
  - Scans declarations
  - Hoists function declarations, var → undefined, let/const → TDZ
  - Sets up global scope (LexicalEnvironment)
  - this = global object
         │
         ↓  (Execution Phase)
Code runs line by line
  - Function calls → new Execution Contexts pushed to call stack
  - Variable assignments → updates in LexicalEnvironment
  - Closures formed → inner functions capture outer LexicalEnvironments
  - 'this' determined by call-time rules (not where function was written)
         │
         ↓
Objects created → heap allocated
  - Prototype chain set up
  - Properties on instance vs. prototype
  - Classes are syntactic sugar over this
         │
         ↓
GC periodically:
  - Scavenge new space (frequent, fast)
  - Mark-Sweep old space (infrequent, potentially slow)
  - Collect unreachable objects
  - Closures prevent collection of their lexical environments
```

---

## Interview Questions — Pillar 3

### Junior Level

1. What is hoisting? Give an example of `var` hoisting vs. `let` hoisting.
2. What is the difference between `==` and `===`?
3. What is a closure? Give a simple example.
4. Explain `this` in a regular function vs. an arrow function.
5. What is the difference between `null` and `undefined`?

### Mid Level

1. What is the prototype chain? How does JavaScript property lookup work?
2. Explain the classic `for (var i ...)` closure bug and three ways to fix it.
3. What is the temporal dead zone? How does it differ from a `var` being `undefined`?
4. What is the difference between CommonJS `require()` and ES Module `import`? When would you use one vs. the other?
5. Explain the four rules of `this` binding, with examples of each.
6. What happens in memory when you create a closure that references a large array?

### Senior Level

1. Explain what an execution context is and what it contains. What is the creation phase vs. execution phase?
2. What are "live bindings" in ES modules? How do they differ from CommonJS value copies? Write code that demonstrates the difference.
3. Two closures returned from the same function — do they share the same lexical environment? What are the implications for shared mutable state?
4. Why does V8 use a generational garbage collector? What is the "generational hypothesis" and why does it apply to typical JavaScript workloads?
5. What is a hidden class (shape) in V8? How do property addition patterns affect JIT performance?
6. Explain the difference between `VariableEnvironment` and `LexicalEnvironment` in an execution context. When do they diverge?
7. You're reviewing a codebase and find that WeakMap is being used instead of Map for a cache. What does this tell you about the developer's intentions regarding memory management? When is this the right choice?
8. How does tree shaking work? Why does it require ES Modules and not CommonJS? What property of `import` makes static analysis possible?

---

*Continue to `04-JavaScript-Runtime.md` →*

---


## 📄 File: 04-JavaScript-Runtime-and-Event-Loop.md
*===============================================*

# Pillar 4 — JavaScript Runtime & The Event Loop

> Start here. This is the most asked topic in every Node.js interview and the one most developers get wrong — not because it's hard, but because nobody explained it from the ground up.

---

## How to Read This Pillar

**Part A** — Build the mental model. Read this even if you think you know it.
**Part B** — See it in code. Simple examples, no tricks.
**Part C** — The internals. How it actually works under the hood.
**Part D** — Interview questions, from easy to senior.

You should be able to read Part A in one sitting and explain it to someone else. That's the test.

---

# PART A — Build the Mental Model

## Start With One Fact

JavaScript can only do **one thing at a time**.

That's it. That's the foundation of everything. One thing at a time. JavaScript has a single thread of execution — which means it has one call stack, and that call stack can only run one function at a time.

This is not a bug. This was a deliberate design decision. JavaScript was invented for browsers in 1995. The browser has a DOM — a visual webpage. If two pieces of JavaScript could run at the same time and both tried to modify the same button, you'd have chaos. So Brendan Eich made it single-threaded. One thing at a time. Clean and predictable.

But here's the problem that creates:

---

## The Problem: What Happens When You Need to Wait?

Imagine you're writing a web server. A request comes in. You need to:
1. Read a user's data from a database (takes ~10ms)
2. Call an external payment API (takes ~200ms)
3. Send back a response

If JavaScript can only do one thing at a time, and step 2 takes 200ms — does your entire server freeze for 200ms while waiting? Can no other requests be handled during that time?

If the answer were yes, Node.js would be useless. A server that handles one request at a time, freezing while it waits for each one, could never handle real traffic.

The answer is no — and the mechanism that makes it no is the **event loop**.

---

## The Restaurant Analogy

Think about a restaurant with one waiter.

**Scenario A — Synchronous (bad)**:
The waiter takes Order 1 from Table 1. Walks to the kitchen. Stands there watching the chef cook. 20 minutes later, food is ready. Walks it back. Only now takes Order 2 from Table 2.

One waiter, doing one thing at a time, waiting through every step. The restaurant can only serve one table at a time. This is blocking code.

**Scenario B — Asynchronous (how Node.js works)**:
The waiter takes Order 1 from Table 1. Walks to the kitchen, hands the order to the chef, and says "call me when it's ready." Immediately goes to Table 2. Takes their order. Hands it to the kitchen. Goes to Table 3. Takes their order.

When the chef calls "Order 1 ready!" — the waiter picks it up and delivers it.

The waiter is still doing one thing at a time. The waiter never cooks two dishes simultaneously. But the waiter isn't *waiting* while the kitchen works — the waiter is doing other things during that time.

This is JavaScript. The waiter is the JavaScript thread. The kitchen is the operating system handling I/O (file reads, network requests, database queries). The event loop is the system that tells the waiter "hey, your order is ready — go handle it."

---

## What Is Synchronous Code?

Synchronous means: finish this completely before moving to the next line.

```
Line 1 executes → finished
Line 2 executes → finished
Line 3 executes → finished
```

Each line waits for the previous one. Predictable. Simple. And fine for most logic.

---

## What Is Asynchronous Code?

Asynchronous means: start this, but don't wait for it to finish. Tell me when it's done.

```
Line 1 executes → starts a background operation → continues immediately
Line 2 executes → finished
Line 3 executes → finished
... time passes ...
Background operation finishes → its callback runs
```

The code doesn't pause. It moves on. When the background work is done, a callback function is invoked.

---

## What Is Blocking?

Blocking means: this line of code holds up the entire JavaScript thread while it runs.

If you read a file synchronously (blocking), the entire Node.js process freezes until that file is read. No other code can run. No other requests can be handled. The single thread is occupied.

```
Thread: [reading file................................................................][next line]
         ← nothing else can happen here →
```

---

## What Is Non-Blocking?

Non-blocking means: this operation starts, hands the actual work to the OS, and returns immediately. JavaScript continues. When the OS finishes, the result comes back via a callback.

```
Thread: [start file read][next line][other work][other work]...[callback: file is ready]
         ↑ returns immediately        ↑ OS doing the actual reading in background
```

The key insight: **the OS is doing the heavy lifting**. Reading a file, making a network request, querying a database — these involve waiting for hardware (disk, network card). JavaScript doesn't need to wait. It hands the job to the OS and moves on. The OS notifies JavaScript when the work is done.

---

## The Event Loop — Plain English

The event loop is the mechanism that makes all of this work.

Here is the event loop explained as a loop you can run in your head:

```
LOOP:
  1. Is there anything in the call stack (synchronous code running)?
     → Yes: let it finish. Go back to step 1.
     → No: continue to step 2.

  2. Is there anything in the microtask queue? (Promise callbacks, .then())
     → Yes: run ALL of them, one by one. After each one, check again.
     → No: continue to step 3.

  3. Is there anything in the macrotask queue? (setTimeout, setInterval, I/O callbacks)
     → Yes: take ONE item, run it. Go back to step 1.
     → No: wait. When something arrives, go back to step 1.
```

That's it. The event loop is literally checking these queues and running things in order.

---

## A Concrete Walkthrough

Let's trace through this code:

```javascript
console.log('A');

setTimeout(() => {
  console.log('B');
}, 0);

console.log('C');
```

What is the output? Walk through the event loop:

**Step 1**: `console.log('A')` — synchronous. Runs immediately. Prints **A**.

**Step 2**: `setTimeout(callback, 0)` — this is async. JavaScript registers the callback with the timer system and moves on immediately. The callback goes into a queue to run "after 0ms."

**Step 3**: `console.log('C')` — synchronous. Runs immediately. Prints **C**.

**Step 4**: Call stack is now empty. Event loop checks: anything in the macrotask queue? Yes — the setTimeout callback. Runs it. Prints **B**.

**Output: A, C, B**

Most people expect A, B, C. Understanding why it's A, C, B is understanding the event loop.

---

## Why Is This Powerful?

Node.js can handle thousands of simultaneous HTTP requests with a single thread. Not because it's doing them simultaneously — but because while one request is waiting for a database response, the thread is available to start another request. Then another. Then another.

When the database responds to request 1, the event loop picks up that callback and finishes handling it.

The thread is almost never sitting idle waiting. It's always doing something useful. That's the power.

---

# PART B — See It In Code

## Example 1: Sync vs Async File Reading

```javascript
const fs = require('fs');

// SYNCHRONOUS (blocking) — the wrong way for a server
console.log('Start');
const data = fs.readFileSync('./file.txt', 'utf8'); // FREEZES here until done
console.log('File contents:', data);
console.log('End');
// Output order: Start → File contents → End
// Nothing else can happen while the file is being read

// ASYNCHRONOUS (non-blocking) — the right way
console.log('Start');
fs.readFile('./file.txt', 'utf8', (err, data) => {
  // This callback runs LATER, when the OS finishes reading
  if (err) throw err;
  console.log('File contents:', data);
});
console.log('End');
// Output order: Start → End → File contents
// 'End' prints BEFORE the file is read because readFile is non-blocking
```

This surprises people. "End" prints before the file contents. That's the whole point — `readFile` doesn't wait. It starts the work and returns immediately.

---

## Example 2: The Event Loop Queue Order

```javascript
console.log('1 - synchronous');

setTimeout(() => {
  console.log('4 - setTimeout (macrotask)');
}, 0);

Promise.resolve().then(() => {
  console.log('3 - Promise.then (microtask)');
});

console.log('2 - synchronous');

// Output:
// 1 - synchronous
// 2 - synchronous
// 3 - Promise.then (microtask)   ← microtasks run BEFORE macrotasks
// 4 - setTimeout (macrotask)
```

Why does the Promise `.then()` run before `setTimeout` even though both are "async"?

Because microtasks (Promises) have higher priority than macrotasks (setTimeout). After the synchronous code finishes, the event loop drains ALL microtasks first, then picks up ONE macrotask.

---

## Example 3: What "Blocking the Event Loop" Means

```javascript
const http = require('http');

const server = http.createServer((req, res) => {
  if (req.url === '/slow') {
    // This is CPU-heavy synchronous work — it BLOCKS the event loop
    // While this runs, NO other requests can be handled
    let result = 0;
    for (let i = 0; i < 5_000_000_000; i++) {
      result += i;
    }
    res.end(`Result: ${result}`);
  } else {
    res.end('Fast response');
  }
});

server.listen(3000);

// If one request hits /slow, the server freezes for ~5 seconds
// ALL other requests wait during this time
// This is why CPU-heavy work in Node.js is a problem
```

This is the thing interviewers are testing when they ask "how do you avoid blocking the event loop?" — they want to know if you understand that synchronous CPU work stops everything.

---

## Example 4: The Correct Pattern With Callbacks

```javascript
const fs = require('fs');
const http = require('http');

const server = http.createServer((req, res) => {
  // Non-blocking: hand the file read to the OS and continue
  fs.readFile('./data.json', 'utf8', (err, data) => {
    // This callback runs when the OS finishes reading
    // The event loop was FREE to handle other requests during the read
    if (err) {
      res.statusCode = 500;
      res.end('Error reading file');
      return;
    }
    res.setHeader('Content-Type', 'application/json');
    res.end(data);
  });
  // readFile returns immediately — execution continues here
  // (but there's nothing else to do, so the function returns)
});

server.listen(3000);
```

---

## Example 5: Promises and Async/Await

Callbacks work but get messy when you need to chain multiple async operations. Promises and async/await are cleaner syntax for the same thing.

```javascript
const fs = require('fs').promises; // The promise-based version of fs

// With Promises
function readUserData(userId) {
  return fs.readFile(`./users/${userId}.json`, 'utf8')
    .then(data => JSON.parse(data))
    .then(user => {
      console.log('Got user:', user.name);
      return user;
    })
    .catch(err => {
      console.error('Failed to read user:', err.message);
      throw err;
    });
}

// With async/await (same thing, cleaner to read)
async function readUserDataAsync(userId) {
  try {
    const data = await fs.readFile(`./users/${userId}.json`, 'utf8');
    // 'await' pauses THIS function and returns control to the event loop
    // The event loop can handle other things while the file is being read
    // When the file is ready, THIS function resumes here
    const user = JSON.parse(data);
    console.log('Got user:', user.name);
    return user;
  } catch (err) {
    console.error('Failed to read user:', err.message);
    throw err;
  }
}
```

**Critical point about `await`**: When you `await` something, you are NOT blocking the thread. You are telling the current function "pause here and come back when this promise resolves." The event loop is free to run other code during that pause. This is fundamentally different from synchronous waiting.

---

## Example 6: Common Mistake — Accidentally Blocking

```javascript
// WRONG: this blocks despite looking async
async function processUsers(userIds) {
  for (const id of userIds) {
    await processOneUser(id); // Waits for each one SEQUENTIALLY
    // While waiting for user 1, user 2 hasn't started
    // While waiting for user 2, user 3 hasn't started
    // Total time = sum of all individual times
  }
}

// RIGHT: run them concurrently with Promise.all
async function processUsersFast(userIds) {
  await Promise.all(userIds.map(id => processOneUser(id)));
  // All users start processing simultaneously
  // Total time ≈ the slowest single operation
}

// Example timing difference:
// 10 users, each takes 100ms
// Sequential: 10 × 100ms = 1000ms
// Concurrent: ~100ms (all run at the same time, all I/O-bound)
```

---

# PART C — The Internals

## How Node.js Actually Works Under the Hood

When you install Node.js, you're installing three things bundled together:

```
Node.js = V8 + libuv + Node Standard Library

V8:      Google's JavaScript engine. Takes your JS, compiles it to machine code, runs it.
         This is the same engine in Chrome.

libuv:   A C library that handles all async I/O.
         Gives Node.js its non-blocking superpowers.
         Manages the event loop, thread pool, OS async interfaces.

Node STD: The built-in modules: fs, http, path, crypto, etc.
          Written in C++ (for performance) + JS (for the API you use).
```

## The libuv Thread Pool

Here's something that surprises people: **Node.js does use multiple threads internally**.

The JavaScript itself runs on one thread. But libuv has a thread pool of 4 threads (by default) that handles operations the OS can't do asynchronously — like file system operations.

```
Your JS code (1 thread):
  fs.readFile('data.txt', callback)
         |
         | hands off to libuv
         v
  libuv thread pool (4 threads):
    Thread 1: reading data.txt ←─── does the actual file I/O
    Thread 2: idle
    Thread 3: idle
    Thread 4: idle
         |
         | file read complete
         v
  Event loop: puts callback in I/O queue
         |
         v
  Your JS thread: runs callback with the file data
```

Your JavaScript never touches those threads. You can't access them. But they exist and they're doing real work.

**Network I/O is different**: TCP/HTTP uses the OS's native async I/O (epoll on Linux, kqueue on macOS, IOCP on Windows). This doesn't need threads — the OS itself notifies libuv when data arrives. This is how Node.js handles thousands of network connections without thousands of threads.

## The Event Loop — The Actual Phases

The event loop in libuv has specific phases that run in order. This matters when you need to reason about execution order:

```
   ┌─────────────────────────┐
   │         timers          │  ← setTimeout, setInterval callbacks
   └──────────┬──────────────┘
              │
   ┌──────────▼──────────────┐
   │     pending callbacks   │  ← I/O errors from previous tick
   └──────────┬──────────────┘
              │
   ┌──────────▼──────────────┐
   │       idle, prepare     │  ← internal use only
   └──────────┬──────────────┘
              │
   ┌──────────▼──────────────┐
   │          poll           │  ← retrieve new I/O events, run callbacks
   └──────────┬──────────────┘    (this is where most of your time is spent)
              │
   ┌──────────▼──────────────┐
   │          check          │  ← setImmediate() callbacks
   └──────────┬──────────────┘
              │
   ┌──────────▼──────────────┐
   │     close callbacks     │  ← socket.on('close', ...) etc
   └──────────┬──────────────┘
              │
   After EACH phase: drain ALL microtasks (Promise .then, queueMicrotask)
              │
              └──────────────── repeat ──────────────────┐
```

For interviews, the most important thing to know is: **microtasks run after every phase**, before the next phase starts. And within the phases: timers come before I/O callbacks, which come before setImmediate.

## `setTimeout(fn, 0)` vs `setImmediate()` vs `Promise.then()`

```javascript
setImmediate(() => console.log('setImmediate'));
setTimeout(() => console.log('setTimeout 0'), 0);
Promise.resolve().then(() => console.log('Promise.then'));
process.nextTick(() => console.log('nextTick'));

// Output (almost always):
// nextTick          ← runs before microtasks even
// Promise.then      ← microtask
// setTimeout 0      ← macrotask (timers phase)
// setImmediate      ← check phase

// process.nextTick is highest priority — runs before ANY other async
// Use it sparingly — it can starve the event loop if overused
```

## V8 and JavaScript Compilation

Your JavaScript doesn't run as JavaScript. V8 compiles it:

```
Your .js file
     │
     ▼
Parsing (reads code, builds AST — Abstract Syntax Tree)
     │
     ▼
Ignition (V8's interpreter — converts AST to bytecode, runs it)
     │
     ▼  (for "hot" code — functions called many times)
TurboFan (V8's optimizing compiler — compiles bytecode to machine code)
     │
     ▼
Machine code runs directly on CPU — near C++ speed
```

This is why JavaScript performance improved dramatically after 2008. It's not really "interpreted" in the traditional sense — it gets compiled to machine code for code that runs frequently.

## Promises — What They Are Internally

A Promise is an object that represents a value that will be available in the future. Internally it's a state machine:

```
Promise states:
  pending   → the async operation hasn't completed yet
  fulfilled → completed successfully, has a value
  rejected  → failed, has an error reason

State transitions:
  pending → fulfilled (via resolve())
  pending → rejected  (via reject())
  fulfilled or rejected → these are final states (cannot change)
```

When you call `.then(callback)`, you're telling the Promise: "when you transition to fulfilled, put this callback in the microtask queue."

```javascript
// What Promise.resolve().then() actually does:
const p = new Promise((resolve, reject) => {
  // This function runs SYNCHRONOUSLY, right now
  resolve(42); // Transitions promise to fulfilled state
});

p.then(value => {
  // This does NOT run right now
  // It is placed in the MICROTASK QUEUE
  // It runs after the current synchronous code finishes
  console.log(value); // 42
});

console.log('This runs before the .then callback');
```

## Async/Await — What It Compiles To

`async/await` is syntactic sugar. Under the hood, an async function returns a Promise. `await` pauses the function and resumes it via a microtask when the awaited promise settles.

```javascript
// What you write:
async function fetchUser(id) {
  const response = await fetch(`/api/users/${id}`);
  const user = await response.json();
  return user;
}

// What it roughly means (conceptually):
function fetchUser(id) {
  return fetch(`/api/users/${id}`)
    .then(response => response.json())
    .then(user => user);
}

// Both are equivalent. async/await just reads more like synchronous code.
// Both are non-blocking. Both use the event loop and microtask queue.
```

---

# PART D — Interview Questions

## Level 1: Questions You Must Answer Immediately

**Q: What is the event loop?**

The event loop is the mechanism that allows Node.js to perform non-blocking operations despite being single-threaded. It's a loop that checks a series of queues: first it runs any synchronous code, then it drains all microtasks (Promise callbacks), then it picks up one macrotask (like a setTimeout callback or an I/O result), then repeats.

**Q: What is the difference between blocking and non-blocking code?**

Blocking code holds up the entire JavaScript thread until it completes. Nothing else can run. Non-blocking code starts an operation, hands it to the OS or a background thread, and returns immediately. The result comes back later via a callback. In a server, non-blocking I/O lets one thread handle thousands of requests concurrently.

**Q: What is the difference between synchronous and asynchronous?**

Synchronous code runs in order — each line waits for the previous one to finish. Asynchronous code doesn't wait — it starts an operation and continues. The result arrives later via a callback, Promise, or event.

**Q: What is the difference between `setTimeout(fn, 0)` and `Promise.resolve().then(fn)`?**

Both are async. But Promise `.then()` is a microtask and runs before `setTimeout` callbacks, which are macrotasks. Microtasks are processed after every piece of synchronous code completes, before the event loop moves to the next macrotask.

---

## Level 2: Questions That Require Understanding

**Q: Why does `console.log` after `await` sometimes run before you expect?**

Because `await` yields control back to the event loop. Code after `await` is essentially a microtask — it resumes when the awaited promise settles, but other microtasks queued before it may run first.

**Q: What happens if you run a heavy synchronous loop inside a Node.js server?**

It blocks the event loop. No other requests can be handled until the loop completes. The server appears frozen. This is why CPU-intensive work should be offloaded to Worker Threads or a separate process.

**Q: What is `process.nextTick` and how is it different from `Promise.then`?**

Both queue a microtask. But `process.nextTick` callbacks run before Promise callbacks, even if the Promise was resolved first. `process.nextTick` runs at the end of the current operation, before I/O events. Overusing it can starve I/O callbacks — a `process.nextTick` that recursively queues itself will freeze the event loop.

**Q: Can Node.js handle thousands of simultaneous connections if it's single-threaded?**

Yes, because most of that handling is waiting — waiting for a database response, waiting for a file to be read, waiting for a network reply. While one connection waits, the thread is free to begin another. The actual I/O happens in the OS or libuv's thread pool. The thread only needs to run when there's actual JavaScript to execute.

---

## Level 3: Senior Questions (Know These for Context)

**Q: What is the libuv thread pool and when does Node.js use it?**

libuv maintains 4 threads by default (configurable via `UV_THREADPOOL_SIZE`). It uses them for operations the OS can't handle asynchronously at a low level: file system operations, DNS resolution, some crypto operations. Network I/O uses OS-native async mechanisms (epoll/kqueue/IOCP) instead and doesn't consume thread pool threads.

**Q: What would cause Node.js performance to degrade as you increase the number of concurrent file read operations?**

The libuv thread pool has only 4 threads by default. If you fire 100 concurrent `fs.readFile` operations, only 4 run at a time. The other 96 wait in the thread pool queue. For I/O-heavy workloads that saturate the thread pool, you can increase `UV_THREADPOOL_SIZE`. For network I/O (HTTP, database connections over TCP), this isn't an issue because it doesn't use the thread pool.

**Q: How does `async/await` interact with error handling and the event loop?**

An unhandled rejection in a Promise that isn't awaited can crash the Node.js process (in Node 15+, it throws an `UnhandledPromiseRejection`). `try/catch` inside an `async` function catches rejections from `await`ed promises. But a Promise that is created and not awaited — and rejects — won't be caught by the surrounding `try/catch`. Always either `await` promises or attach `.catch()` to them.

---

## The One Mental Model to Take From This Pillar

> **JavaScript is a single waiter in a restaurant who never stands still.** When the waiter needs something from the kitchen (I/O), they place the order and immediately move to the next table. When the kitchen calls out that an order is ready, the waiter picks it up and delivers it. The kitchen is the OS. The callbacks are the delivery. The event loop is the waiter's workflow. The waiter can serve hundreds of tables — not by being in two places at once, but by never standing still.

---

*Read this next: `05-NodeJS-Internals.md` — which builds directly on everything here.*

---
