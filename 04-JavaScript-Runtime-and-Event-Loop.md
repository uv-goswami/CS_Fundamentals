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
