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


