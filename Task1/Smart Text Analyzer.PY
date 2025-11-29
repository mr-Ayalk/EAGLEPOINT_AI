import re
from collections import Counter

def smart_text_analyzer(text: str) -> dict:
    """
    Basic text analyzer:
    - count words
    - compute average word length
    - find longest word(s)
    - compute frequency of each word
    """
    if not text:
        return {
            "word_count": 0,
            "average_word_length": 0.0,
            "longest_words": [],
            "word_frequency": {}
        }

    # Clean and normalize text (lowercase + replace punctuation)
    cleaned = re.sub(r"[^a-z0-9\s]", " ", text.lower())
    words = [w for w in cleaned.split() if w]

    if not words:
        # Text contained no actual words
        return {
            "word_count": 0,
            "average_word_length": 0.0,
            "longest_words": [],
            "word_frequency": {}
        }

    # Word count
    count = len(words)

    # Average word length
    avg_len = round(sum(len(w) for w in words) / count, 2)

    # Longest words
    longest_len = max(len(w) for w in words)
    longest_words = sorted({w for w in words if len(w) == longest_len})

    # Frequency
    freq = dict(Counter(words))

    return {
        "word_count": count,
        "average_word_length": avg_len,
        "longest_words": longest_words,
        "word_frequency": freq
    }


# ------------------------------------------------------------------

# Example usage
sample = "The quick brown fox jumps over the lazy dog the fox"
output = smart_text_analyzer(sample)
print(f"Input: {sample}\nResult: {output}")
