# Pillar 7 — React

> React is the most common frontend library you'll be asked about. This pillar builds on Pillar 6 (Browser Internals). If you haven't read that yet, read it first — specifically the DOM and Virtual DOM sections.

---

# PART A — Build the Mental Model

## What Is React?

React is a JavaScript library for building user interfaces. That's it. It does one thing: help you build UIs that update correctly and efficiently when your data changes.

React was built by Facebook (now Meta) in 2013 to solve a specific problem they had: a page with many components that needed to stay in sync with rapidly changing data (like a newsfeed). Manual DOM manipulation was getting out of control.

React's core idea is simple enough to state in one sentence:

> **Describe what your UI should look like for any given data. React takes care of making the actual DOM match.**

You don't say "add this element, remove that one, change this text." You say "given this data, this is what should be displayed." React figures out the DOM operations.

---

## The Component Mental Model

React breaks your UI into **components** — self-contained, reusable pieces of UI.

Think of a webpage as LEGO bricks:

```
Webpage:
  ┌─────────────────────────────────────────┐
  │  Header Component                        │
  │  ┌─────────────┐  ┌───────────────────┐ │
  │  │ Logo Comp   │  │  NavBar Comp      │ │
  │  └─────────────┘  └───────────────────┘ │
  ├─────────────────────────────────────────┤
  │  Feed Component                          │
  │  ┌─────────────────────────────────────┐│
  │  │ Post Component                      ││
  │  │  ┌──────────┐  ┌─────────────────┐ ││
  │  │  │ Avatar   │  │ PostContent     │ ││
  │  │  │ Comp     │  │ Comp            │ ││
  │  │  └──────────┘  └─────────────────┘ ││
  │  └─────────────────────────────────────┘│
  │  ┌─────────────────────────────────────┐│
  │  │ Post Component (another post)       ││
  │  └─────────────────────────────────────┘│
  └─────────────────────────────────────────┘
```

Each component:
- Is a JavaScript function (modern React) that returns JSX
- Manages its own state (or receives data as props)
- Renders independently when its data changes
- Can contain other components

---

## Props — Passing Data Down

Props (properties) are how you pass data from a parent component to a child component. Like function arguments.

```
Parent has data: { name: "Harish", role: "developer" }
                         │
                   passes as props
                         │
                         ▼
                Child receives props
                renders: "Hello, Harish — developer"
```

Props flow **one direction**: parent → child. A child cannot directly modify its parent's data. This one-way data flow makes React apps predictable and easier to debug — if something is wrong, you always know data came from above.

---

## State — Data That Changes

State is data that belongs to a component and can change over time. When state changes, the component re-renders (React calls your function again with the new state, producing new JSX, which React uses to update the DOM).

```
User clicks "Like" button
         │
    onClick handler runs
         │
    setState({ liked: true })
         │
    React re-renders the component
         │
    New JSX produced (heart icon is now filled)
         │
    React diffs new Virtual DOM with previous
         │
    Only the heart icon DOM node is updated
         │
    Browser repaints the heart icon
```

The whole page doesn't re-render. Just the component that had state change, and its children. And within that, React minimizes which actual DOM nodes change.

---

## The Rendering Lifecycle — Simplified

```
1. Initial Render:
   React calls your component function
   You return JSX
   React creates Virtual DOM from the JSX
   React creates real DOM nodes to match
   Browser displays them

2. State/Props Change:
   React calls your component function again
   You return new JSX (based on new data)
   React creates new Virtual DOM
   React diffs: new VD vs previous VD
   React updates only the changed real DOM nodes
   Browser repaints changed areas

3. Unmount:
   Component removed from the page
   React removes its DOM nodes
   Cleanup functions run (useEffect cleanup)
```

---

## Hooks — The Modern Way

Before 2019, React had two types of components: class components (complex, verbose) and functional components (simple, but couldn't have state). Hooks (introduced in React 16.8) let functional components have state, side effects, and everything else. Class components still work but are considered legacy.

The two hooks you need to know deeply:

**`useState`** — adds state to a functional component
**`useEffect`** — runs side effects (data fetching, subscriptions, DOM manipulation) after rendering

---

# PART B — See It In Code

## Example 1: Your First Component — Props and Rendering

```jsx
// A simple component that receives props and renders them
// This is a functional component — just a function that returns JSX

function UserCard({ name, role, email }) {
  // Props are destructured from the first argument object
  // This function runs every time React renders this component

  return (
    <div className="user-card">
      {/* JSX — looks like HTML but it's JavaScript */}
      {/* className instead of class (class is a reserved JS word) */}
      {/* Curly braces {} to embed JavaScript expressions */}
      <h2>{name}</h2>
      <p>{role}</p>
      <a href={`mailto:${email}`}>{email}</a>
    </div>
  );
}

// Using the component — pass data as props (like HTML attributes)
function App() {
  return (
    <div>
      <UserCard
        name="Harish"
        role="Backend Developer"
        email="harish@example.com"
      />
      {/* Reuse the same component with different data */}
      <UserCard
        name="Alice"
        role="Product Manager"
        email="alice@example.com"
      />
    </div>
  );
}
```

---

## Example 2: useState — Adding State

```jsx
import { useState } from 'react';

function Counter() {
  // useState returns [currentValue, setterFunction]
  // The argument to useState is the INITIAL value
  const [count, setCount] = useState(0);
  const [step, setStep] = useState(1);

  // count = current value (0 initially)
  // setCount = function to update count (causes re-render)

  function increment() {
    // NEVER do: count++ or count = count + 1
    // State is immutable — you must use the setter
    // The setter schedules a re-render with the new value
    setCount(count + step);

    // Or use the functional form (safer when new value depends on old value):
    setCount(prevCount => prevCount + step);
    // This guarantees you're working with the latest value
    // Important when multiple state updates happen in sequence
  }

  function reset() {
    setCount(0);
  }

  return (
    <div>
      <p>Count: {count}</p>
      <label>
        Step:
        <input
          type="number"
          value={step}
          onChange={(e) => setStep(parseInt(e.target.value))}
        />
      </label>
      <button onClick={increment}>+</button>
      <button onClick={reset}>Reset</button>
    </div>
  );
}
```

---

## Example 3: useEffect — Side Effects

```jsx
import { useState, useEffect } from 'react';

function UserProfile({ userId }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // useEffect runs AFTER the component renders
  // The second argument is the "dependency array"
  useEffect(() => {
    // This runs after render when userId changes
    setLoading(true);
    setError(null);

    fetch(`/api/users/${userId}`)
      .then(res => {
        if (!res.ok) throw new Error('User not found');
        return res.json();
      })
      .then(data => {
        setUser(data);
        setLoading(false);
      })
      .catch(err => {
        setError(err.message);
        setLoading(false);
      });

    // Cleanup function: runs when userId changes (before next effect)
    // OR when component unmounts
    // Use this to cancel subscriptions, abort fetch, clear timers
    return () => {
      // If userId changes while fetch is in flight, abort the old request
      // (For proper abort: use AbortController — shown in production example below)
    };

  }, [userId]); // Dependency array: re-run this effect when userId changes

  // If dependency array is []:    runs once after first render only
  // If dependency array is [x,y]: runs after first render AND when x or y changes
  // If no dependency array:       runs after EVERY render (usually wrong)

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;
  if (!user) return null;

  return (
    <div>
      <h2>{user.name}</h2>
      <p>{user.email}</p>
    </div>
  );
}
```

---

## Example 4: Rendering Lists

```jsx
function ItemList({ items }) {
  // When rendering lists, React needs a unique 'key' prop on each item
  // The key helps React's diffing algorithm identify which items changed
  // Use a stable, unique ID — not the array index (unless list never reorders)

  return (
    <ul>
      {items.map(item => (
        <li key={item.id}> {/* key prop — required! */}
          {item.name} — ${item.price}
        </li>
      ))}
    </ul>
  );
}

// Why keys matter:
// Without keys: if you prepend an item to a list,
// React assumes ALL items changed and re-renders everything
// With keys: React matches items by key, knows only a new one was added
// → Much more efficient DOM updates

// BAD: using array index as key (breaks when list reorders/filters)
items.map((item, index) => <li key={index}>{item.name}</li>)

// GOOD: using stable, unique ID
items.map(item => <li key={item.id}>{item.name}</li>)
```

---

## Example 5: A Real Component — User List With Search

```jsx
import { useState, useEffect } from 'react';

// This is close to what you'd build in a real project
function UserList() {
  const [users, setUsers] = useState([]);
  const [search, setSearch] = useState('');
  const [loading, setLoading] = useState(false);

  // Fetch users when component mounts
  useEffect(() => {
    const controller = new AbortController(); // For cancelling fetch

    setLoading(true);
    fetch('/api/users', { signal: controller.signal })
      .then(res => res.json())
      .then(data => {
        setUsers(data);
        setLoading(false);
      })
      .catch(err => {
        if (err.name !== 'AbortError') { // Ignore abort errors
          console.error('Failed to fetch users:', err);
          setLoading(false);
        }
      });

    return () => controller.abort(); // Cleanup: cancel fetch if component unmounts

  }, []); // Empty array: run once on mount

  // Filter users based on search term
  // This is computed from state — NOT stored in state itself
  // (Derived state — don't use useState for things you can compute)
  const filteredUsers = users.filter(user =>
    user.name.toLowerCase().includes(search.toLowerCase()) ||
    user.email.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div className="user-list">
      <input
        type="text"
        placeholder="Search users..."
        value={search}
        onChange={(e) => setSearch(e.target.value)}
      />

      {loading && <p>Loading users...</p>}

      {!loading && filteredUsers.length === 0 && (
        <p>No users found for "{search}"</p>
      )}

      <ul>
        {filteredUsers.map(user => (
          <li key={user.id}>
            <strong>{user.name}</strong> — {user.email}
          </li>
        ))}
      </ul>

      <p>{filteredUsers.length} of {users.length} users shown</p>
    </div>
  );
}
```

---

## Example 6: Context — Sharing State Without Prop Drilling

```jsx
import { createContext, useContext, useState } from 'react';

// Problem: passing a prop through many nested components just to reach a deep child
// "Prop drilling" — messy and fragile

// Solution: Context — a way to share data with any component in a tree
// without explicitly passing it as props

// Step 1: Create the context
const AuthContext = createContext(null);

// Step 2: Create a provider component that holds the state
function AuthProvider({ children }) {
  const [user, setUser] = useState(null);

  function login(userData) {
    setUser(userData);
  }

  function logout() {
    setUser(null);
  }

  // Provide the value to all components inside this provider
  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}

// Step 3: Any component inside the provider can access context
function NavBar() {
  const { user, logout } = useContext(AuthContext);

  return (
    <nav>
      {user ? (
        <>
          <span>Welcome, {user.name}</span>
          <button onClick={logout}>Logout</button>
        </>
      ) : (
        <span>Not logged in</span>
      )}
    </nav>
  );
}

function App() {
  return (
    <AuthProvider>    {/* All children can access auth state */}
      <NavBar />
      <MainContent />
    </AuthProvider>
  );
}
```

---

# PART C — The Internals

## React Fiber — The Reconciliation Engine

React 16 (2017) rewrote React's core with a new reconciliation engine called **Fiber**. Understanding why it was rewritten explains a lot about React's design.

**The Old Problem (React ≤ 15):**
The reconciliation algorithm was recursive and synchronous. When a large component tree updated, React would walk the entire tree, diff everything, and update the DOM — in one uninterruptible operation. If this took 50ms, the browser couldn't process any user input during that time. The UI felt unresponsive.

**Fiber's Solution:**
Fiber breaks reconciliation into small units of work that can be paused, resumed, and prioritized. The browser can interrupt React's work to handle high-priority events (user clicks, animations) and then resume React's work.

```
Old React (pre-Fiber):
  Large update: [50ms uninterruptible work]
  User input arrives mid-update: has to WAIT
  UI feels frozen

React Fiber:
  Large update: [work][yield][work][yield][work][yield]...
  User input arrives between yields: handled immediately
  UI stays responsive
```

Fiber enables features like:
- **Concurrent Mode**: React can prepare multiple versions of the UI simultaneously
- **Suspense**: declaratively handle loading states
- **Automatic batching**: multiple state updates grouped into one render

## Reconciliation and the Diffing Algorithm

When React re-renders a component, it creates a new Virtual DOM tree and compares it to the previous one. This comparison is called **diffing**.

React's diff algorithm has one key heuristic: if the element **type** changes, tear it down and build from scratch.

```jsx
// React renders this:
<div>
  <Counter />
</div>

// Then data changes, React renders this:
<span>       {/* type changed from div to span */}
  <Counter />
</span>

// React sees: div → span (different type)
// React's rule: destroy the entire tree and rebuild
// Counter unmounts, remounts — its state is LOST
```

This is why wrapping a component in a different container can reset its state unexpectedly.

Same type, different props → React updates props, keeps the instance, preserves state:

```jsx
// Before: <UserCard name="Harish" />
// After:  <UserCard name="Alice" />
// Same type (UserCard), different prop — React updates, doesn't remount
// Component state (if any) is PRESERVED
```

## The Key Prop — Why It Matters Internally

The `key` prop helps React's diffing algorithm identify elements in lists:

```jsx
// Before update:
<ul>
  <li key="1">Alice</li>
  <li key="2">Bob</li>
  <li key="3">Charlie</li>
</ul>

// After update (new user added at the TOP):
<ul>
  <li key="4">Dave</li>    // new
  <li key="1">Alice</li>
  <li key="2">Bob</li>
  <li key="3">Charlie</li>
</ul>

// With keys: React matches by key
// key="1" → Alice: same, no DOM update needed
// key="2" → Bob: same, no DOM update needed
// key="3" → Charlie: same, no DOM update needed
// key="4" → Dave: new! Insert one DOM node at top

// WITHOUT keys: React compares by position
// Position 1: "Alice" → "Dave"? Different! Update DOM.
// Position 2: "Bob" → "Alice"? Different! Update DOM.
// Position 3: "Charlie" → "Bob"? Different! Update DOM.
// Position 4: nothing → "Charlie"? New! Create DOM node.
// 4 DOM operations instead of 1 — much worse
```

## useState Batching — Avoiding Unnecessary Renders

```jsx
function Component() {
  const [a, setA] = useState(0);
  const [b, setB] = useState(0);

  function handleClick() {
    setA(1); // Does NOT immediately re-render
    setB(2); // Does NOT immediately re-render
    // React BATCHES these two updates into ONE re-render
    // Result: one render with a=1 and b=2
  }

  // React 18 introduced automatic batching even in async callbacks:
  async function handleAsync() {
    const data = await fetchSomething();
    setA(data.a); // Batched together (React 18)
    setB(data.b); // Batched together (React 18)
    // ONE re-render (React 18 behavior)
    // In React 17: TWO separate re-renders
  }
}
```

## Memoization — Preventing Unnecessary Renders

```jsx
import { useState, useCallback, useMemo, memo } from 'react';

// React.memo: wraps a component, prevents re-render if props didn't change
const ExpensiveChild = memo(function ExpensiveChild({ data, onUpdate }) {
  console.log('ExpensiveChild rendered'); // You want this to appear rarely
  return <div>{/* expensive rendering */}</div>;
});

function Parent() {
  const [count, setCount] = useState(0);
  const [items, setItems] = useState([1, 2, 3, 4, 5]);

  // WITHOUT useCallback: new function reference created every render
  // ExpensiveChild receives a "new" onUpdate prop every time Parent re-renders
  // Even though the function does the same thing — memo() fails because prop "changed"
  const handleUpdate = useCallback((newItem) => {
    setItems(prev => [...prev, newItem]);
  }, []); // Empty deps: function never changes — stable reference

  // WITHOUT useMemo: this calculation runs every render
  const expensiveCalculation = useMemo(() => {
    return items.reduce((sum, x) => sum + x * x, 0);
  }, [items]); // Only recalculate when items changes

  return (
    <div>
      <button onClick={() => setCount(c => c + 1)}>
        Count: {count}  {/* This state change re-renders Parent */}
      </button>
      <p>Sum of squares: {expensiveCalculation}</p>
      {/* ExpensiveChild does NOT re-render when count changes,
          because its props (data and onUpdate) haven't changed */}
      <ExpensiveChild data={items} onUpdate={handleUpdate} />
    </div>
  );
}
```

---

# PART D — Interview Questions

## Level 1: Must Answer

**Q: What is React?**

React is a JavaScript library for building user interfaces. Instead of manually manipulating the DOM, you describe what the UI should look like for a given state using components and JSX. React takes care of updating the actual DOM efficiently when state changes.

**Q: What is JSX?**

JSX is a syntax extension for JavaScript that looks like HTML. It's not valid JavaScript — a tool called Babel transforms JSX into `React.createElement()` calls. Those calls return plain JavaScript objects (Virtual DOM nodes). JSX is developer convenience; the browser never sees JSX.

**Q: What is the Virtual DOM?**

A lightweight JavaScript object representation of the real DOM that React maintains in memory. When state changes, React creates a new Virtual DOM, diffs it against the previous one, and applies only the changed operations to the real DOM. This is more efficient than re-rendering the entire page.

**Q: What is the difference between state and props?**

Props are data passed from a parent component to a child — like function arguments. They're read-only from the child's perspective. State is data owned by a component that can change over time. When state changes, the component re-renders. Props flow down; state is local to a component (unless shared via Context or a state manager).

**Q: What is `useState`?**

A Hook that adds state to a functional component. It returns `[currentValue, setterFunction]`. Calling the setter schedules a re-render with the new value. You must use the setter — never mutate state directly.

**Q: What is `useEffect`?**

A Hook that runs side effects after a component renders. Side effects include: fetching data, setting up subscriptions, manually changing the DOM. It accepts a callback and an optional dependency array that controls when it re-runs. The callback can return a cleanup function that runs before the next effect or on unmount.

---

## Level 2: Require Understanding

**Q: Why shouldn't you use array index as a key in lists?**

React uses keys to match items between renders. If you use array index as key and reorder or filter the list, the indices shift. React matches items by key, so it sees "different" items at each position and does unnecessary DOM updates — or worse, confuses stateful components by keeping the wrong component instance alive with stale state. Use stable, unique IDs.

**Q: What is the dependency array in `useEffect`?**

The second argument to `useEffect`. It tells React when to re-run the effect: empty array `[]` means run once (on mount); an array of values `[x, y]` means re-run when `x` or `y` changes; no array means re-run after every render. A common mistake is missing dependencies — an effect that reads a variable but doesn't list it will have a stale closure (reads the initial value forever).

**Q: What is prop drilling and how does Context solve it?**

Prop drilling is passing a prop through many intermediate components that don't need it, just to reach a deep descendant. Context provides a way to share values across the component tree without explicit prop passing. A Provider component wraps the tree and holds the shared value; any descendant can access it via `useContext`.

**Q: What is React reconciliation?**

The process React uses to update the DOM efficiently. When state changes, React re-renders the component and gets new JSX. It creates a new Virtual DOM and compares it to the previous one (diffing). React identifies the minimum number of real DOM operations needed and applies them. The algorithm uses element type and key prop to make intelligent decisions about what changed.

---

## Level 3: Senior Questions

**Q: What is React Fiber and why was it introduced?**

Fiber is React's reconciliation engine (introduced in React 16). The old engine was synchronous and recursive — once started, it couldn't be interrupted. On complex trees, this could freeze the UI for tens of milliseconds. Fiber breaks work into small units that can be paused, prioritized, and resumed. This enables concurrent features: React can yield to the browser between units of work, keeping the UI responsive during large updates.

**Q: What is the difference between `useMemo` and `useCallback`?**

`useMemo` memoizes a computed value — it only recalculates when dependencies change. Use it when a calculation is expensive. `useCallback` memoizes a function reference — it returns the same function object between renders unless dependencies change. Use it when passing callbacks to memoized child components (`React.memo`) — without `useCallback`, the child receives a new function reference every render and re-renders unnecessarily.

**Q: When would you NOT use React Context for state management?**

Context is good for infrequently changing global data (auth state, theme, locale). For frequently changing data (a counter that updates every second, a real-time data feed), Context has a problem: every consumer re-renders when the Context value changes, even if they only care about a subset of the data. For that kind of state, a proper state manager (Zustand, Redux Toolkit) with selective subscriptions is more appropriate.

---

## The Mental Model to Take From This Pillar

> **React is a function: data goes in, UI comes out.** Your components are functions that take data (props + state) and return a description of what the UI should look like. React's engine takes that description, compares it with the previous description, and makes the real browser DOM match using the minimum work possible. You never touch the DOM directly. You never calculate what changed. You just describe the desired outcome and React does the rest. That's the whole idea.

---

*Read this next: `03-JavaScript-Fundamentals.md` from the v1 files — closures and the prototype chain underpin how React hooks work internally.*
