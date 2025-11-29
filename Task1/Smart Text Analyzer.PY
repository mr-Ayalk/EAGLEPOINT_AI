import re
from collections import Counter

def smart_text_analyzer(text: str) -> dict:
    """
    Analyzes text to calculate word count, average word length, longest word(s),
    and case-insensitive word frequency.
    
    :param text: The input string to analyze.
    :return: A dictionary containing the analysis results.
    """
    if not text:
        return {
            "word_count": 0,
            "average_word_length": 0.00,
            "longest_words": [],
            "word_frequency": {}
        }
        
    # Step 1: Normalize and Tokenize
    # Convert to lowercase and replace any sequence of non-alphanumeric characters 
    # (except spaces) with a single space to handle punctuation cleanly.
    normalized_text = re.sub(r'[^a-z0-9\s]', ' ', text.lower())
    
    # Split the cleaned text into a list of words, filtering out empty strings 
    # that might result from multiple spaces or leading/trailing punctuation.
    words = [word for word in normalized_text.split() if word]
    
    # Calculate fundamental metrics
    word_count = len(words)
    if word_count == 0:
        # Handles case where text only contains punctuation/spaces
        return {
            "word_count": 0,
            "average_word_length": 0.00,
            "longest_words": [],
            "word_frequency": {}
        }

    # Step 2: Calculate Average Word Length
    total_length = sum(len(word) for word in words)
    # Average word length rounded to 2 decimal places
    average_word_length = round(total_length / word_count, 2)
    
    # Step 3: Find Longest Word(s)
    # Find the maximum length first
    max_length = 0
    if words:
        max_length = len(max(words, key=len))
    
    # Filter for all words matching the maximum length (handling ties)
    # Using a set to ensure uniqueness, then converting back to a list
    longest_words = sorted(list(set(word for word in words if len(word) == max_length)))
    
    # Step 4: Calculate Word Frequency (case-insensitive)
    # Use collections.Counter for efficient frequency counting
    word_frequency_counter = Counter(words)
    # Convert Counter object to a regular dictionary for the final output format
    word_frequency = dict(word_frequency_counter)
    
    # Final Result Construction
    return {
        "word_count": word_count,
        "average_word_length": average_word_length,
        "longest_words": longest_words,
        "word_frequency": word_frequency
    }

# --- Working Examples ---
input_text = "The quick brown fox jumps over the lazy dog the fox"
result = smart_text_analyzer(input_text)
print(f"Input: '{input_text}'\nOutput: {result}\n")

