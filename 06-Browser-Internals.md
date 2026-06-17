# Pillar 6 — Browser Internals

> This pillar answers "What is the DOM?" and sets up everything you need for React (Pillar 7). The DOM, Virtual DOM, reflow, repaint — these all connect. Start here before reading the React pillar.

---

# PART A — Build the Mental Model

## What Is the Browser, Really?

A browser is a program that does one job: take an HTML file (plus CSS and JavaScript), and display it as a visual, interactive webpage.

That sounds simple. Under the hood it's one of the most complex pieces of software humans have built. Chrome alone is ~30 million lines of code.

When you type a URL and hit Enter, the browser does this:

```
1. Network: fetch the HTML from the server (HTTP request)
2. Parse: read the HTML and build a tree structure (DOM)
3. Parse: read the CSS and build a tree structure (CSSOM)
4. Combine: merge DOM + CSSOM into a Render Tree
5. Layout: calculate where every element goes on the screen
6. Paint: draw pixels
7. Composite: layer everything and display it
8. JavaScript: run any scripts, which may modify the DOM and restart steps 3-7
```

This is the browser's rendering pipeline. Understanding it explains why some JavaScript is slow, why animations can stutter, and how React's Virtual DOM makes things faster.

---

## What Is the DOM?

**DOM** stands for **Document Object Model**.

When the browser reads your HTML, it doesn't display the raw text. It parses it and converts it into a **tree of objects** in memory. That tree is the DOM.

Your HTML:
```html
<html>
  <body>
    <h1>Hello</h1>
    <p>World</p>
  </body>
</html>
```

Becomes this tree in memory:

```
Document
  └── html (element node)
        └── body (element node)
              ├── h1 (element node)
              │     └── "Hello" (text node)
              └── p (element node)
                    └── "World" (text node)
```

Each box in that tree is a **DOM node** — a JavaScript object with properties and methods. The `<h1>` element becomes an object with properties like `textContent`, `className`, `style`, and methods like `addEventListener`, `appendChild`, `remove`.

**The DOM is the browser's live, in-memory representation of your webpage.** It is not the HTML file. The HTML file is the source code. The DOM is what the browser builds from that source code.

---

## Why Does the DOM Matter for JavaScript?

JavaScript in the browser exists primarily to manipulate the DOM — to change the page dynamically in response to user actions or data.

```javascript
// These are all DOM manipulations
document.getElementById('title').textContent = 'New Title';
document.querySelector('.btn').addEventListener('click', handler);
document.createElement('div');
document.body.appendChild(newElement);
```

Every one of these operations reaches into the in-memory tree, finds a node, and modifies it. The browser then re-renders the affected parts of the page.

Here's the key thing that React's Virtual DOM is solving: **DOM operations are slow**.

Not "slow" as in imperceptible. Slow as in: you can feel them. A page that updates 100 DOM nodes on every user interaction will feel sluggish. A page that re-renders an entire list every second will cause visible lag.

Why are DOM operations slow? We'll get to that in Part C. But first, let's understand what happens when you change the DOM.

---

## Reflow vs. Repaint — The Two Most Important Words

When you change something in the DOM, the browser has to update what's displayed. There are two types of updates:

**Repaint** — something changed visually but the layout didn't change.
Examples: `color`, `background-color`, `visibility`, `border-color`.
The browser redraws the pixel colors. Expensive, but not as expensive as reflow.

**Reflow (Layout)** — something changed that affects the size or position of elements.
Examples: adding/removing elements, changing `width`, `height`, `padding`, `margin`, `font-size`, changing text content.
The browser recalculates the position of every affected element and their neighbors. Very expensive.

```
Reflow triggers:
  element.style.width = '200px'     ← forces reflow
  element.innerHTML = 'New content' ← forces reflow
  document.body.appendChild(el)     ← forces reflow
  element.style.display = 'none'    ← forces reflow
  reading: element.offsetHeight     ← forces reflow to get accurate value!

Repaint only (no reflow):
  element.style.color = 'red'
  element.style.backgroundColor = 'blue'
  element.style.opacity = '0.5'
```

**The critical insight**: Reading certain layout properties forces the browser to immediately recalculate layout, even if you were about to change things. This is called **forced synchronous layout** and it's one of the most common performance killers.

---

## Why React Exists — The Problem It Solves

Imagine building a Twitter-like feed without React. A new tweet comes in. You need to add it to the top of the list.

Without a framework, you'd manually:
1. Create a DOM element for the tweet
2. Set its content
3. Insert it at the top of the list
4. Update the count badge
5. Update the timestamp on existing tweets
6. Maybe show/hide a "load more" button

As your app grows, you're manually tracking which DOM nodes need updating based on which data changed. This becomes unmanageable at scale. You end up with spaghetti code where data changes are scattered and DOM updates are inconsistent.

React's solution: **you describe what the UI should look like for any given state. React figures out what DOM operations are needed to get there.**

Instead of: "add this element, remove that element, change this text"
You say: "given this data, the UI should look like THIS"

React takes care of the difference.

That's what the Virtual DOM makes possible.

---

## What Is the Virtual DOM?

The Virtual DOM is a **lightweight JavaScript object representation of the real DOM**, kept in memory by React.

Instead of directly modifying the real DOM (slow), React:

1. Maintains a virtual copy of the DOM as plain JavaScript objects
2. When data changes, creates a new virtual DOM
3. Compares new virtual DOM with old virtual DOM (**diffing**)
4. Calculates the minimum set of real DOM operations needed
5. Applies only those operations (**reconciliation**)

```
Your component re-renders → new Virtual DOM tree
                                    │
                         diff against previous Virtual DOM
                                    │
                         find minimum changes needed
                                    │
                         apply ONLY those changes to real DOM
```

The virtual DOM itself is just JavaScript objects — fast to create, fast to compare. The real DOM operations (which are slow) are minimized to only what changed.

---

## The Real DOM vs. Virtual DOM

```
Real DOM Node (what the browser uses):
  An actual C++ object in the browser's rendering engine
  Has ~200+ properties and methods
  Changing it can trigger layout, paint, composite
  Direct manipulation is slow

Virtual DOM Node (what React uses):
  A plain JavaScript object
  Something like: { type: 'div', props: { className: 'card' }, children: [...] }
  Creating and comparing these is just in-memory JS — fast
  No browser rendering involved
```

A common misconception: "Virtual DOM is always faster than real DOM." This isn't true. The Virtual DOM has overhead. For simple, infrequent updates, direct DOM manipulation is faster. The Virtual DOM wins when you have complex UIs with frequent updates — because the diffing saves you from unnecessary real DOM operations.

---

## What Is JSX?

JSX is a syntax extension for JavaScript that looks like HTML but isn't.

```jsx
// This is JSX — looks like HTML inside JavaScript
const element = <h1 className="title">Hello, {name}</h1>;
```

JSX is not valid JavaScript. The browser cannot run JSX directly. A tool called **Babel** transforms JSX into regular JavaScript function calls before the browser sees it.

After Babel transforms it:
```javascript
// This is what Babel turns JSX into — plain JavaScript
const element = React.createElement(
  'h1',                          // element type
  { className: 'title' },        // props (attributes)
  'Hello, ',                     // children...
  name                           // ...
);
```

`React.createElement` returns a plain JavaScript object — a Virtual DOM node:
```javascript
{
  type: 'h1',
  props: {
    className: 'title',
    children: ['Hello, ', 'Harish']
  }
}
```

That's all JSX is. Syntactic sugar that makes writing `React.createElement` calls look like HTML. It's more readable and less error-prone than writing `React.createElement` manually for every element.

**The flow:**
```
Your JSX code
     │
     │ Babel transforms
     ▼
React.createElement() calls
     │
     │ React executes these
     ▼
Virtual DOM (plain JS objects)
     │
     │ React's reconciler compares with previous Virtual DOM
     ▼
Minimum real DOM operations
     │
     │ Browser performs
     ▼
Updated webpage
```

---

# PART B — See It In Code

## Example 1: The DOM — Raw JavaScript

```javascript
// This is what you'd do WITHOUT React
// Manually creating and manipulating DOM nodes

// SELECT existing nodes
const title = document.getElementById('title');
const list = document.querySelector('.items-list');
const allButtons = document.querySelectorAll('.btn');

// READ from the DOM
console.log(title.textContent);   // "Hello"
console.log(title.innerHTML);     // "<span>Hello</span>" (includes child HTML)
console.log(title.className);     // "header-title"

// WRITE to the DOM (triggers repaint/reflow)
title.textContent = 'New Title';  // Just text — safer than innerHTML
title.innerHTML = '<span>New</span>'; // Parses HTML — XSS risk if user-provided!
title.style.color = 'red';        // Inline style change

// CREATE and INSERT new nodes
const newItem = document.createElement('li');
newItem.textContent = 'New item';
newItem.classList.add('item', 'item--new');
list.appendChild(newItem);        // Add to end
list.prepend(newItem);            // Add to beginning
list.insertBefore(newItem, list.firstChild); // Insert before specific node

// REMOVE nodes
const oldItem = document.querySelector('.item--old');
oldItem.remove();                 // Modern way
list.removeChild(oldItem);        // Older way

// EVENTS
title.addEventListener('click', (event) => {
  console.log('Clicked!', event.target); // event.target = the clicked element
  event.preventDefault();         // Stop default browser behavior (e.g., link navigation)
  event.stopPropagation();        // Stop event from bubbling up to parent elements
});
```

---

## Example 2: Performance Problem — The Forced Reflow Trap

```javascript
// BAD: Reading layout property inside a write loop
// This causes a forced synchronous reflow on EVERY iteration
const items = document.querySelectorAll('.item');

for (let i = 0; i < items.length; i++) {
  items[i].style.width = '100px';         // WRITE: schedules a reflow
  console.log(items[i].offsetHeight);     // READ: forces reflow to happen NOW
  // Every iteration: write → force read → reflow → write → force read → reflow
  // If you have 100 items: 100 reflows. This is called "layout thrashing"
}

// GOOD: Separate reads from writes (batch them)
const items2 = document.querySelectorAll('.item');

// First: do all READS (browser can batch them)
const heights = Array.from(items2).map(item => item.offsetHeight);

// Then: do all WRITES (browser schedules ONE reflow)
items2.forEach(item => {
  item.style.width = '100px';
});

// Even better: use CSS classes instead of inline styles
// Adding/removing a class is one operation; the browser handles the rest
items2.forEach(item => item.classList.add('item--wide'));
```

---

## Example 3: Event Delegation — Efficient Event Handling

```javascript
// BAD: Attaching event listener to EACH item
// If you have 1000 list items, you have 1000 event listeners
const items = document.querySelectorAll('.item');
items.forEach(item => {
  item.addEventListener('click', (e) => {
    console.log('Clicked item:', e.target.textContent);
  });
});
// Problem: 1000 listeners, memory overhead
// Problem: new items added dynamically don't have listeners

// GOOD: Event delegation — one listener on the parent
// Events "bubble up" from child to parent
const list = document.querySelector('.list');
list.addEventListener('click', (e) => {
  // Check if the clicked element (or its ancestor) is an item
  const item = e.target.closest('.item');
  if (!item) return; // Clicked somewhere else in the list

  console.log('Clicked item:', item.textContent);
});
// ONE listener handles ALL items, including future ones added dynamically
// This is how React handles events internally (attaches one listener to the root)
```

---

## Example 4: requestAnimationFrame for Smooth Animations

```javascript
// BAD: Using setTimeout for animations
function badAnimate() {
  let x = 0;
  setInterval(() => {
    element.style.left = x + 'px';
    x++;
  }, 16); // ~60fps, but NOT synchronized with browser refresh
  // Result: janky animations, possible tearing
}

// GOOD: requestAnimationFrame — syncs with browser refresh rate
function goodAnimate() {
  let x = 0;

  function step() {
    element.style.left = x + 'px';
    x++;

    if (x < 300) {
      // Ask browser to call step() before the NEXT repaint
      requestAnimationFrame(step);
    }
  }

  requestAnimationFrame(step);
}
// requestAnimationFrame runs at the browser's refresh rate (usually 60fps)
// Automatically pauses when tab is in background (saves battery/CPU)
// Results in smooth, jank-free animations
```

---

## Example 5: Web Storage APIs

```javascript
// localStorage — persists forever (until manually cleared)
localStorage.setItem('theme', 'dark');
localStorage.setItem('user', JSON.stringify({ id: 1, name: 'Harish' }));

const theme = localStorage.getItem('theme');           // 'dark'
const user = JSON.parse(localStorage.getItem('user')); // { id: 1, name: 'Harish' }
localStorage.removeItem('theme');
localStorage.clear(); // Remove everything

// sessionStorage — persists only for the current browser tab
// Cleared when tab is closed
sessionStorage.setItem('formDraft', JSON.stringify(formData));

// Key differences vs. cookies:
// - localStorage/sessionStorage: JS-only, NOT sent with requests, larger (5-10MB)
// - Cookies: sent with every request, server-readable, smaller (4KB), can be HttpOnly
// - Never store auth tokens (JWTs) in localStorage — XSS can steal them
// - Store JWTs in HttpOnly cookies instead

// IndexedDB — for larger structured data (beyond localStorage's 5-10MB limit)
// Use for offline-capable apps, caching large datasets
// API is complex — most people use libraries (Dexie.js, idb)
```

---

# PART C — The Internals

## The Complete Browser Rendering Pipeline

```
HTML text arrives from network
         │
         ▼
┌─────────────────────┐
│   HTML Parser       │  Converts HTML text into DOM tree
│                     │  Stops when it hits a <script> tag (blocks!)
│                     │  Unless script has async or defer attribute
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   CSS Parser        │  Converts CSS into CSSOM (CSS Object Model)
│                     │  Like DOM, but for styles
│                     │  Must be complete before rendering can start
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   Render Tree       │  Combines DOM + CSSOM
│                     │  Only visible elements (display:none excluded)
│                     │  Each node has its computed styles
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   Layout            │  Calculate exact position and size of every element
│   (Reflow)          │  Box model: margin, border, padding, content
│                     │  Result: every element has (x, y, width, height)
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   Paint             │  Fill in pixels for each element
│                     │  Background, text, borders, shadows
│                     │  Happens in layers (CSS creates new layers)
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   Composite         │  Combine layers in correct order
│                     │  Send to GPU for display
│                     │  GPU-accelerated: transform, opacity
└─────────────────────┘
```

## Why JavaScript Blocking the Parser Is Dangerous

When the HTML parser encounters a `<script>` tag without `async` or `defer`:

```
HTML parsing... → hit <script> → STOP PARSING
                                       │
                                 Download script
                                       │
                                 Execute script
                                       │
                                 RESUME parsing

During this pause: the page is blank or partially rendered.
User sees a "flash" or blank screen.
```

This is why you see recommendations to put `<script>` at the bottom of `<body>`, or use `async`/`defer`:

```html
<!-- Blocks parser — BAD for render performance -->
<script src="app.js"></script>

<!-- Downloads in parallel with HTML parsing, executes when done -->
<!-- Execution order NOT guaranteed -->
<script async src="analytics.js"></script>

<!-- Downloads in parallel, executes AFTER HTML fully parsed -->
<!-- Execution order IS guaranteed (scripts run in order) -->
<!-- This is what you want for most application scripts -->
<script defer src="app.js"></script>
```

## Critical Rendering Path Optimization

```
First meaningful paint time = DNS + TCP + TLS + server response + render pipeline

Things that block render:
  - Render-blocking CSS (any <link rel="stylesheet"> in <head>)
  - Render-blocking JS (any <script> without async/defer)

Optimizations:
  1. Inline critical CSS (CSS needed for above-the-fold content)
  2. Defer non-critical CSS
  3. Use defer or async for all scripts
  4. Minimize HTML/CSS/JS (smaller files = faster download)
  5. Use HTTP/2 or HTTP/3 (parallel downloads)
  6. Use a CDN (closer server = less network time)
  7. Preload critical resources: <link rel="preload" href="hero-image.jpg" as="image">
```

## Browser Architecture (Multi-Process Model)

Modern browsers (Chrome, Edge) use multiple OS processes for security and stability:

```
Chrome Process Architecture:

Browser Process (1):
  UI, navigation, file access, network requests
  Runs with user's OS permissions

Renderer Processes (one per tab, isolated):
  Runs your website's HTML, CSS, JavaScript
  Runs in a sandbox — cannot access disk, network directly
  If it crashes: only that tab dies, not the browser
  If malicious: cannot escape the sandbox

GPU Process (1):
  Handles rendering and compositing for all tabs
  Accelerates graphics using GPU

Network Process (1):
  Handles all network requests
  Separated for security — websites can't intercept others' requests

Plugin Processes (one per plugin, legacy):
  Flash, etc. (mostly gone now)
```

This is why a tab crashing doesn't crash Chrome. And why Chrome uses a lot of RAM — separate processes, each with their own memory space.

## The Compositor Thread and Why It Matters for Performance

Inside the renderer process, there are multiple threads:

```
Main Thread:
  Runs JavaScript
  Handles DOM operations
  Handles CSS
  Manages layout, paint

Compositor Thread:
  Handles scrolling and CSS animations that are "composited"
  Runs independently from the main thread
  Uses GPU

Raster Thread(s):
  Converts paint operations into actual pixels
```

When people say "avoid jank" and "use CSS transforms for animations instead of left/top" — this is why:

- `left: 100px` → triggers layout → main thread → can block on JS → jank
- `transform: translateX(100px)` → handled by compositor thread → never blocks on JS → smooth

```css
/* SLOW animation — triggers reflow, runs on main thread */
.bad-animation {
  transition: left 0.3s ease;  /* Don't do this */
}

/* FAST animation — runs on compositor thread, never blocks */
.good-animation {
  transition: transform 0.3s ease;  /* Do this */
  will-change: transform;           /* Hint to browser to create a layer */
}
```

---

# PART D — Interview Questions

## Level 1: Must Answer

**Q: What is the DOM?**

The DOM (Document Object Model) is the browser's in-memory, tree-structured representation of an HTML document. When the browser parses HTML, it builds a tree of objects where each element becomes a node. JavaScript can read and modify this tree, which causes the browser to update the displayed page. The DOM is not the HTML source — it's a live data structure that JavaScript interacts with.

**Q: What is the difference between the DOM and HTML?**

HTML is the source code — a text file with markup. The DOM is the live data structure the browser builds from that HTML. They start the same but diverge: JavaScript can modify the DOM without changing the original HTML. The browser's developer tools show the DOM (which reflects JS changes), not necessarily the original HTML.

**Q: What is the Virtual DOM and why does React use it?**

The Virtual DOM is a lightweight JavaScript object representation of the real DOM that React maintains in memory. When your component's data changes, React creates a new Virtual DOM, compares it with the previous one (diffing), and calculates the minimum number of real DOM operations needed to reflect the change. This is more efficient than directly manipulating the real DOM, because DOM operations are expensive (they can trigger layout and paint), while comparing JavaScript objects is fast.

**Q: What is JSX?**

JSX is a syntax extension for JavaScript that looks like HTML. It's not valid JavaScript — a tool called Babel transforms it into `React.createElement()` calls before the browser runs it. Those calls return plain JavaScript objects (Virtual DOM nodes). JSX is purely a developer convenience; it has nothing to do with how the browser works.

---

## Level 2: Require Understanding

**Q: What is the difference between repaint and reflow?**

Reflow (layout) recalculates the position and size of elements on the page. It's triggered by changes that affect layout: adding/removing elements, changing width/height/padding/margin, changing text content. Repaint redraws pixels without recalculating layout — triggered by visual-only changes like color or background. Reflow is more expensive because it cascades: changing one element's size may shift everything around it. After reflow, repaint always follows.

**Q: What causes layout thrashing and how do you fix it?**

Layout thrashing is when you read a layout property (like `offsetHeight`) immediately after writing a style change, forcing the browser to synchronously recalculate layout before it was planning to. Doing this repeatedly in a loop causes dozens of reflows instead of one. Fix: batch all DOM reads together, then batch all writes — never alternate read/write in a loop.

**Q: Why should `<script>` tags be placed at the bottom of `<body>` (or use `defer`)?**

Without `defer` or `async`, a `<script>` tag blocks HTML parsing — the browser stops building the DOM until the script is downloaded and executed. If the script is in `<head>`, the user sees a blank page during that time. Placing scripts at the bottom of `<body>` means HTML is parsed first (page renders), then scripts execute. `defer` achieves the same thing more cleanly and is the modern preferred approach.

---

## Level 3: Senior Questions

**Q: How does the browser decide what CSS to apply to a DOM element?**

The browser builds the CSSOM (CSS Object Model) by parsing all CSS. For each DOM element, it calculates the "computed style" by: (1) finding all CSS rules that match the element via selector specificity, (2) applying cascade rules (specificity wins, then source order), (3) inheriting properties from parent elements, (4) applying browser defaults. The result is a map of every CSS property → its computed value for that element.

**Q: Why is `transform: translateX()` better for animations than changing `left`?**

Changing `left` triggers reflow (layout recalculation), which runs on the main thread and can be blocked by JavaScript. `transform` and `opacity` changes are handled by the compositor thread, independent of the main thread. Even if JavaScript is running heavily, compositor-thread animations stay smooth. The `will-change: transform` CSS property hints to the browser to promote the element to its own GPU layer in advance.

**Q: What is the critical rendering path and how would you optimize it?**

The critical rendering path is the sequence of steps needed for the first pixel to appear: HTML parsing → DOM construction → CSSOM construction → Render tree → Layout → Paint → Composite. It's "critical" because nothing is visible until this completes. Optimization: minimize render-blocking CSS and JS, inline critical CSS, defer non-critical scripts, compress resources, use a CDN to reduce network time, preload critical assets.

---

## The Mental Model to Take From This Pillar

> **The browser is a rendering machine that takes text files (HTML, CSS) and turns them into a visual, interactive UI — and the DOM is the live data structure that represents that UI in memory. JavaScript's job in the browser is almost entirely "manipulate the DOM." Every framework — React, Vue, Angular — exists to make that manipulation manageable at scale. The Virtual DOM is React's strategy: instead of you deciding which DOM nodes to update, you describe the desired state and React figures out the minimum updates needed.**

---

*Read this next: `07-React.md` — which builds directly on the DOM and Virtual DOM concepts from this pillar.*
