You got it. Here is the concise, GitHub README-formatted guide for your ideal answer key, featuring the best and most expected references for each task.

---

# 🦅 Eagle Point AI - Technical Assessment Solution Guide

This document serves as the solution guide for the Full-stack Developer Technical Assessment, demonstrating optimal approaches for each task and providing the required documentation structure and references.

---

## 💻 Task 1: Smart Text Analyzer (Python)

### **Key Approach: Efficient Tokenization & `collections.Counter`**

| Aspect | Optimal Technique | Expected Reference |
| :--- | :--- | :--- |
| **Punctuation Handling** | Utilize the **`re` module** to replace non-alphanumeric characters (except spaces) with a space, ensuring clean tokenization. | **Python Docs: `re` module** (`re.sub` for cleaning). |
| **Word Frequency** | Use **`collections.Counter`** for highly efficient ($O(N)$) case-insensitive frequency counting. | **Python Docs: `collections.Counter`** |
| **Longest Word(s)** | Find the `max(words, key=len)` then use a **list comprehension with a `set`** to handle ties and ensure uniqueness. | **Python Docs: Built-in Functions** (`max`, `len`). |

---

## 🌐 Task 2: Async Data Fetcher with Retry (JavaScript)

### **Key Approach: `async/await` with Loop-Based Retry**

| Aspect | Optimal Technique | Expected Reference |
| :--- | :--- | :--- |
| **Asynchronous Control** | Use **`async/await`** with a `for` loop to enforce sequential attempts, ensuring clean, readable control flow. | **MDN Web Docs: `async` function and `await`** |
| **Delay Between Retries** | Implement a specific `delay` function using a **`Promise` wrapped around `setTimeout(..., 1000)`** and use `await delay(1000)`. | **MDN Web Docs: `Promise` and `setTimeout`** |
| **Error Management** | Place the `try...catch` block **inside the loop** to handle intermediate failures gracefully without exiting the function prematurely. | **Technical Article: Async/Await Retry Pattern** (Focus on `try...catch` in loop). |

---

## 🔐 Task 3: Rate Limiter (Python)

### **Key Approach: Sliding Window Log**

| Aspect | Optimal Technique | Expected Reference |
| :--- | :--- | :--- |
| **Algorithm** | **Sliding Window Log** approach. This is the most accurate method, avoiding the "burst" problems of the Fixed Window counter. | **Technical Article: Rate Limiting Algorithms** (Detailing the Sliding Window Log).  |
| **Time Tracking** | Use **`time.time()`** for high-resolution, universal timestamps to ensure the 60-second window is measured precisely. | **Python Docs: `time` module** (`time.time`). |
| **User Data Structure**| A **`defaultdict(list)`** mapping `user_id` to a list of request timestamps. **List comprehension** handles the auto-reset by filtering out expired timestamps. | **Python Docs: `collections.defaultdict`** |

---

## ✅ Documentation Quality Guide

Candidates should be evaluated not just on the code, but on how well they structure their thought process. Look for the following in their submission:

1.  **Thought Process:** A clear comparison of alternatives (e.g., Fixed vs. Sliding Window) and a justification for the final choice.
2.  **Step-by-Step:** Explanation of problems encountered (e.g., initial difficulty handling ties in Task 1) and how they were solved.
3.  **Rationale:** Explicit discussion of time complexity ($O(N)$ or $O(1)$) and why the chosen approach is optimal for production use (e.g., accuracy, maintainability).









# 🧠 Task 1 — Thought Process & Solution Steps

## 🔧 **Language Choice**

**Python** was selected due to its:

* Rich standard library for **string manipulation** (`re` module)
* Efficient data structures like `dict` and `collections.Counter`
* Clean, readable syntax
* Linear-time performance for text processing tasks

**Alternatives Considered:**
A manual loop for counting word frequencies was considered, but `collections.Counter` was chosen instead for cleaner syntax and optimal $O(N)$ performance.

---

## 📝 **Step-by-Step Solution Outline**

### 1️⃣ **Text Normalization**

* Convert input to **lowercase**
* Ensures case-insensitive comparison

```python
text.lower()
```

### 2️⃣ **Punctuation Handling**

* Use regex to clean the text
* Replace all non-alphanumeric characters with spaces

```python
re.sub(r'[^a-z0-9\s]', ' ', text.lower())
```

* Handles various punctuation patterns uniformly (e.g., `"word," → "word"`)

### 3️⃣ **Tokenization**

* Split on whitespace to extract words

```python
normalized_text.split()
```

* Filter empty tokens created by multiple spaces

### 4️⃣ **Longest Word Detection**

* Compute the maximum word length
* Select all words matching that length
* Use a `set` to ensure **unique** results

```python
max_length = max(len(w) for w in words)
longest_words = list({w for w in words if len(w) == max_length})
```

### 5️⃣ **Average Word Length**

* Efficiently compute using a generator expression

```python
avg_len = sum(len(w) for w in words) / len(words)
```

* Rounded for readability

---

## ✅ **Why This Solution Works Best**

### ✔️ **Correct & Robust**

* Regex ensures punctuation is handled cleanly
* Normalization avoids inconsistent word matching
* Prevents runtime errors (e.g., checks for empty input)

### ⚡ **Efficient ($O(N)$ Time Complexity)**

The algorithm performs:

* 1 pass for regex substitution
* 1 pass for splitting
* 1 pass for counting and length checks

All operations are **linear** with respect to the input size.

### 🧼 **Clean Code & Best Practices**

* Uses optimized built-ins (`Counter`, `split`, `sum`, `len`)
* Clear variable names
* Easy to maintain and extend



# ⚙️ Task 2 — Retry Logic Implementation (JavaScript)

## 🧠 Thought Process & Solution Steps

### 🔧 **Language Choice**

**JavaScript (ES2017+)** was used as required, leveraging modern features such as `async/await` for cleaner asynchronous flow.

### 🚀 **Core Approach**

The solution uses **async/await** instead of `.then()`/`.catch()` chaining, making the asynchronous retry logic appear **sequential, readable, and maintainable**.

---

## 📝 Step-by-Step Workflow

### 1️⃣ **Loop Control**

A standard `for` loop is used to control the number of attempts:

* Ensures retries stop after `(maxRetries + 1)` attempts
* Cleaner and safer than recursion or `while(true)` loops that need manual break conditions

### 2️⃣ **Error Handling**

A `try...catch` block inside the loop:

* Attempts the operation
* Catches any failure immediately
* Stores the error to be thrown later if retries are exhausted

### 3️⃣ **Delay Mechanism**

A dedicated delay helper ensures proper wait time between retries:

```javascript
const delay = (ms) => new Promise(resolve => setTimeout(resolve, ms));
```

Using `await delay(1000)` guarantees a **1-second wait** before the next retry—exactly matching the requirement.

### 4️⃣ **Final Failure Handling**

If the last retry attempt still fails:

* The stored `lastError` is thrown
* Meets the rule: **"throw error after all retries fail"**

---

## ✅ Why This Solution Is Best

### ✔️ **Clear & Maintainable Control Flow**

`async/await` makes the logic almost read like synchronous code:

1. Try the operation
2. If it fails, catch the error
3. Wait
4. Retry

No callback nesting. No messy promise chains. Extremely clear.

### ⏱️ **Accurate Retry Timing**

The delay occurs **after each failure** and **before the next attempt**, ensuring:

* Consistent retry intervals
* No accidental overlapping or premature execution

### 🛡️ **Robust Error Reporting**

Tracking `lastError` means the final thrown error:

* Contains real failure details
* Reflects all attempts already made
* Provides meaningful debugging context



# ⏱️ Task 3 — Sliding Window Rate Limiter (Python)

## 🧠 Thought Process & Solution Steps

### 🎯 **Pattern Choice**

The **Sliding Window Log Algorithm** was selected for its precision in enforcing API rate limits.

### 🗂️ **Alternatives Considered (and Rejected)**

#### ❌ **Fixed Window Counter**

* Very simple, but suffers from the *burst problem*.
* A user could make 5 requests just before the window resets and 5 right after → **10 requests in seconds**.

#### ❌ **Leaky Bucket**

* More complex to implement correctly.
* Typically requires an underlying queuing system (e.g., Redis).
* Overkill for this task.

➡️ **Winner: Sliding Window Log** — *accurate, simple, and lightweight.*

---

## 📝 Step-by-Step Workflow

### 1️⃣ **Data Structure**

A `defaultdict(list)` maps:

```
user_id → [timestamps_of_requests]
```

Perfect for grouping requests by user and tracking their history.

### 2️⃣ **Current Time Tracking**

`time.time()` provides high-precision timestamps for reliable time-window comparisons.

### 3️⃣ **Sliding Window Logic (Auto-Reset)**

Expired timestamps are removed dynamically using:

```python
timestamp >= current_time - TIME_WINDOW_SECONDS
```

This gives a true **rolling window**, not a fixed reset at minute boundaries.

### 4️⃣ **Limit Enforcement**

* After filtering, the list length represents the number of valid requests within the window.
* If the count is below the limit, the request is allowed and timestamp appended.
* Otherwise, the request is blocked.

---

# ✅ Why This Solution Is Best

### 🎯 **1. Maximum Accuracy**

The Sliding Window Log enforces limits *exactly* as intended:

> **5 requests per 60 seconds per user — no bursts, no loopholes.**

Example:
If a user sends requests at T = 5, 10, 15, 20, 25 →
A 6th request will be blocked until **T = 65**.

### 🧼 **2. Simple & Maintainable**

Uses:

* A list
* A list comprehension
* A small dictionary

No external dependencies. No scheduling jobs. Easy to understand and debug.

### ⚡ **3. Efficient**

Complexity is:

```
O(K)  where K ≤ limit (5)
```

Meaning → **effectively O(1)**.

Extremely fast and scalable.






# ▶️ Running the Scripts

## 📝 **Run Smart Text Analyzer**

Use the following command in your terminal:

```bash
python "/path/to/your/project/Smart Text Analyzer.py"
```

> 💡 **Tip:**
> Replace `/path/to/your/project/` with the actual folder where you saved the file.

---

## 📝 **Run Rate Limiter**

Execute the script using:

```bash
python "/path/to/your/project/Rate Limiter.py"
```

> 📌 This works for **any directory structure**, whether you're on Windows, macOS, or Linux.

---

## 🧭 Example (Windows Git Bash / PowerShell)

```bash
python "C:/Users/YourName/Desktop/YourProjectFolder/Smart Text Analyzer.py"
python "C:/Users/YourName/Desktop/YourProjectFolder/Rate Limiter.py"
```


