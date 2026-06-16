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
