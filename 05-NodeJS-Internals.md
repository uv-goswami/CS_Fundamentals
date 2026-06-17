# Pillar 5 — Node.js Internals

> This pillar answers the question you failed in your interview: "How is Node.js different from JavaScript in the browser?" By the end of Part A, you'll have a clear, confident answer. By the end of Part C, you'll understand it deeply enough to answer any follow-up.

---

## How to Read This Pillar

**Part A** — The mental model. What Node.js actually is. Read this first, no skipping.
**Part B** — Code. Working examples of Node.js-specific features.
**Part C** — The internals. How Node.js works under the hood.
**Part D** — Interview questions, easy to senior.

---

# PART A — Build the Mental Model

## What Is Node.js, Actually?

Here's the one-sentence answer you should be able to say in an interview:

> **Node.js is a runtime environment that lets you run JavaScript outside the browser, built on V8 (Chrome's JavaScript engine) and libuv (a library that handles async I/O).**

Let's unpack that word by word.

**Runtime environment** — a runtime is what your code runs *inside*. Like how a fish needs water to survive, JavaScript needs a runtime to execute. The browser is one runtime. Node.js is another.

**Outside the browser** — before Node.js (released 2009), JavaScript could only run inside a browser. You could not use JavaScript to write a server, read files, or access the operating system. Node.js changed that.

**V8** — the JavaScript engine. It takes your `.js` code and compiles it to machine code. It's the same engine inside Chrome. V8 doesn't know anything about browsers or servers — it just knows JavaScript.

**libuv** — a C library that gives Node.js its non-blocking superpowers. It handles file I/O, network I/O, timers, and the event loop. Without libuv, Node.js would be just another slow server framework.

---

## Browser JavaScript vs. Node.js — The Real Difference

This is the question you failed. Here's the clean answer:

Both the browser and Node.js use JavaScript (and often V8 as the engine). The **language is the same**. What's different is everything around it — the environment, the APIs, the purpose.

Think of it this way: a hammer is a hammer. But using a hammer to build a house is different from using a hammer in a school workshop. Same tool. Different environment. Different things available to you.

```
BROWSER ENVIRONMENT              NODE.JS ENVIRONMENT
─────────────────────────────    ──────────────────────────────
Purpose: run code on webpages    Purpose: run code on servers/machines

What's available to your JS:     What's available to your JS:
  window object                    process object
  document (the DOM)               require() / import
  fetch API                        fs (file system)
  localStorage                     http (create servers)
  alert(), confirm()               os (operating system info)
  navigator (browser info)         path (file paths)
  history, location                child_process (run system commands)
  Web APIs (Canvas, WebGL, etc)    Buffer (binary data)

Security model:                  Security model:
  Sandboxed — JS cannot            No sandbox — JS CAN
  access your file system          access your file system,
  or run system commands           run processes, make network
  (intentionally)                  connections to anything

Entry point:                     Entry point:
  <script> tag in HTML             node app.js (command line)

Event loop manages:              Event loop manages:
  User events (click, scroll)      I/O callbacks (file, network)
  fetch responses                  Timers
  requestAnimationFrame            Process events
```

The JavaScript syntax — variables, functions, classes, Promises, async/await — is identical. What differs is what's *available* to your code.

---

## Why Does Node.js Exist?

Before 2009, if you wanted to build a web server, you used PHP, Ruby, Java, Python. JavaScript was only for the browser.

Ryan Dahl (Node.js creator) had a specific insight: most web server work is I/O-bound — waiting for databases, waiting for files, waiting for other services. Traditional servers (Apache, early Rails) handled this with threads — one thread per request. Threads are expensive (memory, context switching). When 10,000 users connect simultaneously, 10,000 threads is a problem.

His insight: use JavaScript's event loop model — already built for handling I/O without threads — and put it on a server. One thread, non-blocking I/O, event loop. One server process could handle thousands of simultaneous connections.

This solved the **C10K problem** — handling 10,000 concurrent connections. Node.js made it easy.

---

## The Three Building Blocks of Node.js

```
┌─────────────────────────────────────────────────────────┐
│                     Your JavaScript                      │
│              (app.js, routes, controllers, etc.)         │
└─────────────────────────┬───────────────────────────────┘
                          │ calls
┌─────────────────────────▼───────────────────────────────┐
│              Node.js Standard Library                    │
│         (fs, http, path, crypto, events, etc.)           │
│    Written in JS + C++ bindings to the layer below       │
└──────────────┬──────────────────────┬───────────────────┘
               │                      │
┌──────────────▼──────┐  ┌────────────▼──────────────────┐
│         V8          │  │            libuv               │
│  JavaScript engine  │  │  Async I/O + Event Loop        │
│  Compiles JS to     │  │  Thread pool, OS async         │
│  machine code       │  │  interfaces (epoll, etc.)      │
└─────────────────────┘  └────────────────────────────────┘
```

**V8** handles the JavaScript execution — compiling and running your code.

**libuv** handles everything async — the event loop, the thread pool, talking to the OS for file and network I/O.

**The Node Standard Library** is the bridge — it gives your JavaScript convenient functions (`fs.readFile`, `http.createServer`) that internally call into V8 and libuv.

---

## Streams — The Core Idea

One concept unique to Node.js that you need to know: **Streams**.

Imagine downloading a 1GB video file. You have two options:

**Option 1 (no streams)**: Download the entire 1GB into memory. Then play it. You wait 10 minutes. Your server uses 1GB of RAM per user doing this. 100 users = 100GB of RAM.

**Option 2 (streams)**: Download a chunk, immediately pass it forward for processing, download the next chunk. Like how YouTube buffers video — you start watching while the rest downloads. Your server uses a small fixed amount of RAM regardless of file size.

Streams are how Node.js processes large amounts of data efficiently — by processing it in pieces instead of loading it all into memory.

```
No Streams (dangerous for large data):
  [Read entire file into RAM] → [Send entire file] → [Done]
  RAM usage = file size

With Streams:
  [Read chunk 1] → [Send chunk 1]
                → [Read chunk 2] → [Send chunk 2]
                                → [Read chunk 3] → [Send chunk 3]
  RAM usage = chunk size (constant, regardless of file size)
```

Every HTTP request in Node.js is a stream. Every HTTP response is a stream. Files read as streams. This is fundamental to why Node.js is memory-efficient.

---

## The Process Object

In the browser you have `window`. In Node.js you have `process`.

`process` is a global object that gives you information about and control over the current Node.js process:

```javascript
process.env.NODE_ENV        // 'development', 'production', 'test'
process.argv                // command line arguments: ['node', 'app.js', '--port=3000']
process.pid                 // process ID (integer)
process.exit(0)             // terminate process with exit code 0 (success)
process.exit(1)             // terminate with error code
process.cwd()               // current working directory
process.memoryUsage()       // { heapUsed, heapTotal, rss, external }
process.uptime()            // seconds since process started
process.on('uncaughtException', handler)  // catch unhandled errors
process.on('SIGTERM', handler)           // handle termination signal (from OS/Docker)
```

In your VIPASA project, you use `process.env` every time you access environment variables. This is the `process` object.

---

# PART B — See It In Code

## Example 1: Creating a Basic HTTP Server

```javascript
// This is the foundation everything else builds on
const http = require('http');

const server = http.createServer((req, res) => {
  // req = incoming request (what the client sent)
  // res = outgoing response (what we send back)

  console.log(`${req.method} ${req.url}`); // e.g., "GET /users"

  // Route based on URL
  if (req.method === 'GET' && req.url === '/') {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hello from Node.js!');
    return;
  }

  if (req.method === 'GET' && req.url === '/health') {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'application/json');
    res.end(JSON.stringify({ status: 'ok', uptime: process.uptime() }));
    return;
  }

  // 404 for everything else
  res.statusCode = 404;
  res.end('Not Found');
});

// Start listening for connections
server.listen(3000, () => {
  console.log('Server running at http://localhost:3000');
  console.log('Process ID:', process.pid);
});
```

Express (which you use in VIPASA) is built on top of exactly this `http` module. When you write `app.get('/users', handler)` in Express, Express is internally routing the request through this same `http.createServer` pattern.

---

## Example 2: Reading Files — Streams vs. Buffering

```javascript
const fs = require('fs');
const http = require('http');
const path = require('path');

const server = http.createServer((req, res) => {

  // BAD for large files: loads ENTIRE file into memory
  if (req.url === '/bad') {
    fs.readFile(path.join(__dirname, 'large-file.zip'), (err, data) => {
      if (err) { res.statusCode = 500; res.end('Error'); return; }
      // 'data' is the ENTIRE file in memory (could be 500MB!)
      res.setHeader('Content-Type', 'application/zip');
      res.end(data);
    });
  }

  // GOOD for large files: streams data chunk by chunk
  if (req.url === '/good') {
    const filePath = path.join(__dirname, 'large-file.zip');
    const fileStream = fs.createReadStream(filePath);

    res.setHeader('Content-Type', 'application/zip');

    // Pipe: connect the readable stream (file) to the writable stream (response)
    // Data flows from file → response in chunks
    // Memory usage stays constant no matter how big the file is
    fileStream.pipe(res);

    // Handle errors on the stream
    fileStream.on('error', (err) => {
      res.statusCode = 500;
      res.end('Error reading file');
    });
  }
});

server.listen(3000);
```

---

## Example 3: Environment Variables and Configuration

```javascript
// config.js — how production Node.js apps handle configuration

// process.env contains all environment variables set before running the script
// In development: you set them in a .env file (loaded by dotenv)
// In production: set by your hosting platform (Railway, AWS, etc.)

require('dotenv').config(); // loads .env file into process.env

const config = {
  port: parseInt(process.env.PORT || '3000', 10),
  nodeEnv: process.env.NODE_ENV || 'development',
  database: {
    url: process.env.DATABASE_URL,
    poolSize: parseInt(process.env.DB_POOL_SIZE || '10', 10),
  },
  jwt: {
    secret: process.env.JWT_SECRET,
    expiresIn: process.env.JWT_EXPIRES_IN || '7d',
  },
};

// Validate required env vars at startup (fail fast — better than failing later)
const required = ['DATABASE_URL', 'JWT_SECRET'];
const missing = required.filter(key => !process.env[key]);
if (missing.length > 0) {
  console.error('Missing required environment variables:', missing.join(', '));
  process.exit(1); // Exit immediately with error code
}

module.exports = config;
```

---

## Example 4: The EventEmitter — Node's Core Pattern

Almost everything in Node.js is built on `EventEmitter`. HTTP servers emit events. Streams emit events. Database connections emit events. Understanding EventEmitter explains how all of Node.js is wired together.

```javascript
const EventEmitter = require('events');

// EventEmitter is a class you can extend or use directly
class OrderSystem extends EventEmitter {
  constructor() {
    super();
    this.orders = [];
  }

  placeOrder(item, quantity) {
    const order = { id: Date.now(), item, quantity, status: 'pending' };
    this.orders.push(order);

    // emit() triggers all listeners registered for this event
    this.emit('order:placed', order);

    // Simulate async processing (database save, payment, etc.)
    setTimeout(() => {
      order.status = 'confirmed';
      this.emit('order:confirmed', order);
    }, 1000);

    return order;
  }
}

const orderSystem = new OrderSystem();

// Register event listeners
// These are like callbacks, but decoupled from where the event originates
orderSystem.on('order:placed', (order) => {
  console.log(`[EMAIL] Order placed: ${order.item} x${order.quantity}`);
});

orderSystem.on('order:placed', (order) => {
  console.log(`[INVENTORY] Reserving stock for order ${order.id}`);
});

orderSystem.on('order:confirmed', (order) => {
  console.log(`[SMS] Your order ${order.id} is confirmed!`);
});

// Place an order — all listeners fire
orderSystem.placeOrder('Laptop', 1);

// This is EXACTLY how http.createServer works internally:
// const server = http.createServer();
// server.on('request', (req, res) => { ... });
// server.emit('request', req, res) is called each time a request arrives
```

---

## Example 5: Buffers — Working With Binary Data

```javascript
// Buffer is for binary data — images, files, network packets, encrypted data
// Strings are for text. Buffers are for everything else.

// Create a buffer from a string
const buf1 = Buffer.from('Hello, Node.js!', 'utf8');
console.log(buf1);           // <Buffer 48 65 6c 6c 6f 2c 20 4e 6f 64 65 2e 6a 73 21>
console.log(buf1.length);    // 15 (bytes)
console.log(buf1.toString()); // 'Hello, Node.js!'

// Convert between encodings — common in auth systems
const token = Buffer.from('user:password').toString('base64');
console.log(token); // 'dXNlcjpwYXNzd29yZA=='

const decoded = Buffer.from(token, 'base64').toString('utf8');
console.log(decoded); // 'user:password'

// In your VIPASA project: when you hash passwords with bcrypt or
// generate JWT tokens, you're working with binary data under the hood.
// Buffer is what Node.js uses to represent that binary data.

// Practical: reading an image file
const fs = require('fs');
const imageBuffer = fs.readFileSync('./photo.jpg'); // returns a Buffer
console.log(imageBuffer.length); // file size in bytes
// You can then: upload to S3, convert to base64 for API response, etc.
```

---

## Example 6: Child Processes — Running System Commands

```javascript
const { exec, execSync, spawn } = require('child_process');

// exec — run a shell command, get output as string
// Avoid for user input (shell injection risk)
exec('ls -la', (error, stdout, stderr) => {
  if (error) {
    console.error('Error:', error.message);
    return;
  }
  console.log('Directory listing:', stdout);
});

// spawn — better for long-running commands or large output (streaming)
const ls = spawn('ls', ['-la', '/tmp']);

ls.stdout.on('data', (data) => {
  // data arrives in chunks — streaming output
  process.stdout.write(data);
});

ls.on('close', (code) => {
  console.log(`Process exited with code ${code}`);
});

// Real use case: running database migrations in deployment scripts
const migrate = spawn('npx', ['prisma', 'migrate', 'deploy'], {
  env: { ...process.env }, // Pass environment variables
  stdio: 'inherit',        // Show output in current terminal
});

migrate.on('close', (code) => {
  if (code !== 0) {
    console.error('Migration failed!');
    process.exit(1);
  }
  console.log('Migrations complete');
});
```

---

## Example 7: Cluster Module — Using All CPU Cores

```javascript
// By default Node.js uses ONE core. This is wasteful on a 4-core server.
// cluster lets you spawn one worker process per core.
// Each worker runs your full app independently.

const cluster = require('cluster');
const os = require('os');
const http = require('http');

if (cluster.isPrimary) {
  // This block runs once in the main process
  const numCPUs = os.cpus().length;
  console.log(`Primary ${process.pid} is running`);
  console.log(`Forking ${numCPUs} workers...`);

  // Spawn a worker for each CPU core
  for (let i = 0; i < numCPUs; i++) {
    cluster.fork();
  }

  // If a worker crashes, restart it
  cluster.on('exit', (worker, code) => {
    console.log(`Worker ${worker.process.pid} died. Restarting...`);
    cluster.fork();
  });

} else {
  // This block runs in EACH worker process
  // All workers share the same port — OS distributes incoming connections
  http.createServer((req, res) => {
    res.end(`Handled by worker ${process.pid}`);
  }).listen(3000);

  console.log(`Worker ${process.pid} started`);
}

// On a 4-core machine: 4 workers, each on port 3000
// OS distributes incoming requests across workers
// One worker crash doesn't affect others
// Effectively uses all CPU cores
```

---

# PART C — The Internals

## How Node.js Handles a Request — Full Internal Trace

When a browser requests `http://localhost:3000/users`, here is exactly what happens inside Node.js:

```
1. OS LEVEL
   Network card receives TCP packet from browser
   OS buffers it, notifies libuv via epoll (Linux)

2. LIBUV LEVEL
   libuv's I/O poll phase fires: "new data on socket fd #7"
   libuv calls the registered callback in the event loop

3. NODE LEVEL
   Node's HTTP parser processes the TCP stream
   Reconstructs the HTTP request from packets
   Creates req and res objects

4. YOUR CODE
   http.createServer callback fires with (req, res)
   Your route handler runs
   You call res.end('...')

5. BACK DOWN
   res.end() writes to the TCP socket
   OS sends the data back over the network
   Browser receives the response
```

No threads for handling your code. No thread pool involved here. One event loop iteration per request.

## Why Node.js Is Fast for I/O (and Slow for CPU)

```
I/O-bound request (DB query, file read, API call):
  Your code starts DB query          → 0.1ms
  Waiting for DB to respond          → 10ms  (your thread is FREE here)
  DB responds, your callback runs    → 0.1ms
  Total thread time used: 0.2ms out of 10.2ms
  Thread utilization: ~2% per request
  → One thread can handle hundreds of concurrent requests

CPU-bound request (encryption, image processing, complex math):
  Your code starts computation        → 500ms  (thread is BUSY the whole time)
  Total thread time used: 500ms
  Thread utilization: 100% per request
  → One thread can handle 2 requests/second
  → All other requests wait
```

This is the fundamental Node.js tradeoff: brilliant for I/O, poor for CPU. Solutions for CPU work:

1. **Worker Threads** (Node 12+) — run CPU work in a separate thread
2. **Child processes** — offload to a separate Node.js process
3. **Native addons (C++)** — write the hot path in C++
4. **Separate microservice** — spin up a Python/Go service for the CPU work

## The Module System — How `require()` Works

```javascript
// When you write: const express = require('express')
// Node.js does this:

// STEP 1: Resolve the path
// Is 'express' a built-in module? (fs, path, http) → no
// Is it a relative path? (./ or ../) → no
// Then look in node_modules/express/

// STEP 2: Load the file
// Find node_modules/express/package.json → read "main" field → "index.js"
// Load node_modules/express/index.js

// STEP 3: Wrap it
// Node wraps every module in a function wrapper:
(function(exports, require, module, __filename, __dirname) {
  // Your module code runs here
  // This is why you have access to these variables in every file
  // They're parameters, not globals
});

// STEP 4: Execute it
// Run the wrapper function. module.exports is populated.

// STEP 5: Cache it
// Store the result in require.cache keyed by the resolved file path
// Every subsequent require() for the same file returns the CACHED exports
// The module code does NOT run again
// This is why singletons work in Node.js:
//   if you export a database connection from db.js,
//   every file that requires db.js gets the SAME connection object
```

This caching behavior is important for VIPASA: your Prisma client, your Express app, your configuration — when you `require()` them in multiple files, you get the same instance each time.

## Memory Model in Node.js

```
Node.js process memory:

  ┌─────────────────────────────────────┐
  │  V8 Heap                            │
  │  ┌─────────────┐ ┌──────────────┐  │
  │  │  New Space  │ │  Old Space   │  │  JavaScript objects live here
  │  │  (young GC) │ │  (major GC)  │  │
  │  └─────────────┘ └──────────────┘  │
  ├─────────────────────────────────────┤
  │  Stack                              │  Function call frames
  ├─────────────────────────────────────┤
  │  Code (V8 compiled JS)              │  JIT-compiled machine code
  ├─────────────────────────────────────┤
  │  C++ (libuv, Node bindings)         │  Native code
  ├─────────────────────────────────────┤
  │  Buffers (off-heap)                 │  Binary data — NOT in V8 heap
  └─────────────────────────────────────┘

Key: Buffers are allocated OUTSIDE the V8 heap.
This means garbage collecting Buffers doesn't trigger V8 GC.
Large file streams use Buffers — that's why they don't blow up your heap.
```

## Common Node.js Production Issues

**1. Memory leak from uncleared event listeners**

```javascript
// BUG: every request adds a new listener but never removes it
server.on('request', (req, res) => {
  someEmitter.on('data', (data) => {
    // This listener is added on every request and NEVER removed
    // After 10,000 requests: 10,000 listeners on someEmitter
    // Memory grows unboundedly
  });
});

// FIX: use once() for one-time listeners, or removeListener()
server.on('request', (req, res) => {
  const handler = (data) => { /* ... */ };
  someEmitter.once('data', handler); // Automatically removed after first call

  req.on('close', () => {
    someEmitter.removeListener('data', handler); // Manual cleanup
  });
});
```

**2. Unhandled Promise rejections crashing the process**

```javascript
// Node.js 15+: unhandled rejections throw an uncaughtException and crash
async function riskyOperation() {
  throw new Error('Something went wrong');
}

// BUG: promise is created but not awaited — rejection is unhandled
riskyOperation(); // This crashes your server in Node 15+!

// FIX: always handle your promises
riskyOperation().catch(err => console.error('Handled:', err.message));

// OR: global handler as a safety net (not a replacement for proper handling)
process.on('unhandledRejection', (reason, promise) => {
  console.error('Unhandled Rejection at:', promise, 'reason:', reason);
  // Log it, alert, but DON'T process.exit() silently in production
  // You want to know about these
});
```

**3. Blocking the event loop with JSON.parse on large payloads**

```javascript
// BUG: parsing a huge JSON payload blocks the event loop
app.post('/import', express.json({ limit: '50mb' }), (req, res) => {
  // If body is 50MB of JSON, this parses it synchronously
  // The entire event loop freezes during parsing
  // All other requests wait
  const data = req.body; // Already parsed by express.json() middleware — blocks on parse
  processData(data);
  res.json({ ok: true });
});

// FIX: reject large payloads at the middleware level
// Or use streaming JSON parsers for genuinely large data
app.use(express.json({ limit: '1mb' })); // Reject anything larger
```

---

# PART D — Interview Questions

## Level 1: You Must Answer These

**Q: What is Node.js?**

Node.js is a runtime environment for running JavaScript outside the browser. It's built on V8 (Chrome's JS engine) and libuv (handles async I/O). It uses a single-threaded event loop to handle many concurrent connections efficiently, making it well-suited for I/O-heavy applications like web servers and APIs.

**Q: How is Node.js different from JavaScript in the browser?**

Same language, different environment. The browser gives you the DOM, window, and browser APIs. Node.js gives you the file system, OS access, the ability to create HTTP servers, and no DOM. The core difference: browser JS runs in a sandboxed environment for security. Node.js runs with full access to the machine it's on.

**Q: What is non-blocking I/O in Node.js?**

When Node.js performs I/O (reading a file, making a database query), it doesn't pause and wait. It hands the operation to the OS (via libuv), registers a callback, and immediately continues running other code. When the OS finishes the I/O, it puts the callback in the event loop's queue, and Node.js runs it when the call stack is free. This lets one Node.js thread handle thousands of concurrent I/O operations.

**Q: What is a Stream in Node.js?**

A stream is a way to process data in chunks rather than loading it all into memory at once. Reading a large file as a stream means you process it piece by piece — low memory usage regardless of file size. HTTP requests and responses are streams. Piping connects a readable stream to a writable stream.

---

## Level 2: Require Understanding

**Q: Why would you use the Cluster module?**

By default, Node.js runs on a single CPU core. On a 4-core machine, 75% of your CPU is unused. The cluster module lets you fork one worker process per core. Each worker independently handles requests. The OS distributes incoming connections across workers. Result: ~4x throughput. Commonly replaced in production by running multiple Docker containers behind a load balancer.

**Q: What is the difference between `require()` and ES module `import`?**

`require()` is CommonJS — synchronous, loads and executes the module immediately, returns a cached copy after first load. `import` is ES Modules — static (can be analyzed before running), asynchronous-capable, supports tree-shaking (bundlers can remove unused exports). Node.js supports both, but they can't be mixed freely. Most modern Node.js projects are moving toward ESM.

**Q: What does it mean that `require()` caches modules?**

After a module is loaded for the first time, its exports are stored in a cache. Every subsequent `require()` of the same file returns the cached exports — the module code does NOT run again. This is why exporting a database connection (like Prisma's PrismaClient) and requiring it in multiple files gives you the same connection instance everywhere. It's how Node.js implements singletons.

**Q: What is `process.env` and why does it matter?**

`process.env` is an object containing all environment variables available to the Node.js process. It's how you configure applications for different environments without hardcoding values. Database URLs, API keys, port numbers, and flags like `NODE_ENV` all live here. Never hardcode secrets in code — always use environment variables.

---

## Level 3: Senior Questions

**Q: What is libuv's thread pool used for, and what is NOT in the thread pool?**

The thread pool (4 threads by default) handles operations that don't have OS-level async support: file system operations (`fs.readFile`), DNS resolution (`dns.lookup`), some crypto operations. Network I/O (TCP/HTTP/database connections over sockets) does NOT use the thread pool — it uses the OS's native async mechanisms (epoll on Linux). So HTTP requests to your database don't consume thread pool threads, but `fs.readFile` does.

**Q: What happens when you exceed the libuv thread pool size?**

Operations queue up. If you have 4 thread pool threads and fire 100 concurrent `fs.readFile` calls, 4 start immediately and 96 wait. This can cause unexpected latency in high-concurrency file I/O scenarios. The fix: increase `UV_THREADPOOL_SIZE` environment variable (up to 128) or redesign to avoid parallel file I/O.

**Q: How would you handle CPU-intensive work in Node.js without blocking the event loop?**

Three approaches: (1) **Worker Threads** — run CPU work in a separate V8 isolate within the same process, communicate via message passing. (2) **Child processes** — fork a separate Node.js process for the computation, get result via IPC. (3) **Queue and worker pattern** — put CPU jobs in a queue (Redis/Bull), have separate worker processes consume and execute them. The choice depends on how isolated the work needs to be and how often it runs.

---

## The Mental Model to Take From This Pillar

> **Node.js gave JavaScript a new home.** JavaScript was built for browsers — it could only live there. Node.js took the same language, added a different set of APIs (file system, network servers, OS access), and let it live on servers. The event loop, the non-blocking I/O, the single thread — these were already JavaScript's design. Node.js just pointed them at a different problem: building servers instead of handling clicks.

---

*Read this next: `06-Browser-Internals.md`*
