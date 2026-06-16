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
