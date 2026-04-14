"""
Word Split & Join Drill

Problem:  
Write a function `normalize_sentence(text: str) -> str` that:  
1. Splits the sentence into words with `.split()`.  
2. Lowercases all words.  
3. Joins them back together with `"-"` as a separator.  

Example:
>>> normalize_sentence("Python IS Fun To Learn")
"python-is-fun-to-learn"

⏱️ Challenge: solve it in 1 minute using just `.split()`, list comprehension (or map()), and `.join()`.
"""

def normalize_sentence(s: str) -> str:
    return "-".join(s.lower().split())


print(normalize_sentence("PyThon iS fUn tO LeArn"))