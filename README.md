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



