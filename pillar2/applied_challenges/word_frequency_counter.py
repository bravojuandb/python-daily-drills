"""
Word Frequency Counter  challenge

Given a text file `article.txt`, implement a function that reads it and
returns a dictionary mapping each *word* to the number of times it appears.

Rules:
- Treat words case-insensitively ("Data" == "data").
- Ignore punctuation marks like .,!?;:
- Preserve order of first appearance (Python 3.7+ dicts do this by default).
- Strip newline characters properly.
- You may assume UTF-8 encoding.
- Remove stopwords

Signature:
    def count_words(filepath: str) -> dict[str, int]:

Example:
    # if article.txt contains:
    # "Data is power. Data drives insight."
    # Expected output:
    # {'data': 2, 'is': 1, 'power': 1, 'drives': 1, 'insight': 1}

Think fast, code cleanly — you’ll need this logic for ETL parsing
and log analytics.
"""
import string

def count_words(filepath: str) -> dict[str, int]:
    """
    Count word frequency in a text file using a manual counter.

    This function reads the file at the given path and process the text:
    - Normalizing to lowercase
    - Removing punctuation
    - Removing english stopwords

    Args:
        filepath (str): Path to the UTF-8 encoded text file.

    Returns:
        dict[str, int]: A dictionary where keys are words and values are their counts.
    """

    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    stopwords = [
    "a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are",
    "aren't", "as", "at", "be", "because", "been", "before", "being", "below", "between", "both",
    "but", "by", "can't", "cannot", "could", "couldn't", "did", "didn't", "do", "does", "doesn't",
    "doing", "don't", "down", "during", "each", "few", "for", "from", "further", "had", "hadn't",
    "has", "hasn't", "have", "haven't", "having", "he", "he'd", "he'll", "he's", "her", "here",
    "here's", "hers", "herself", "him", "himself", "his", "how", "how's", "i", "i'd", "i'll",
    "i'm", "i've", "if", "in", "into", "is", "isn't", "it", "it's", "its", "itself", "let's",
    "me", "more", "most", "mustn't", "my", "myself", "no", "nor", "not", "of", "off", "on",
    "once", "only", "or", "other", "ought", "our", "ours", "ourselves", "out", "over", "own",
    "same", "shan't", "she", "she'd", "she'll", "she's", "should", "shouldn't", "so", "some",
    "such", "than", "that", "that's", "the", "their", "theirs", "them", "themselves", "then",
    "there", "there's", "these", "they", "they'd", "they'll", "they're", "they've", "this",
    "those", "through", "to", "too", "under", "until", "up", "very", "was", "wasn't", "we",
    "we'd", "we'll", "we're", "we've", "were", "weren't", "what", "what's", "when", "when's",
    "where", "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with",
    "won't", "would", "wouldn't", "you", "you'd", "you'll", "you're", "you've", "your",
    "yours", "yourself", "yourselves"
    ]
    text = text.lower().translate(str.maketrans("", "", string.punctuation))
    count = {}
    for word in text.lower().split():
        if word.isalpha() and word not in stopwords:
            count[word] = count.get(word, 0) + 1
    return count



# Print a dataframe with the 50 most common words in descending frequency

path = "resources/ad_catilinam1.txt" # Process the first discourse against Catilina

import pandas as pd

df = pd.DataFrame(count_words(path).items(), columns=["Word", "Count"])
df = df.sort_values(by="Count", ascending=False)
print(df.head(50))