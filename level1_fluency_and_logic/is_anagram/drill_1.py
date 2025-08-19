"""

 Goal:
  Implement `is_anagram(a, b) -> bool` using a SORTING-based approach.
   Do NOT use collections.Counter or manual dict counting.

 Rules & Hints:
   1) Case-insensitive: "Listen" vs "Silent" -> True
   2) Ignore spaces and punctuation.
   3) Accents/diacritics should be treated as their base letters:
      "Árbol" vs "labor" -> True
   4) Primary tools: `sorted()`, `''.join(...)`, `lambda`, `filter`/`map`.
   5) Consider Unicode normalization (NFKD) with `unicodedata`.
   6) Target complexity: O(n log n) due to sorting.

 Edge cases to consider:
   - Empty strings -> True
   - Only punctuation -> True (both normalize to empty)
   - Mixed scripts (e.g., Greek/Latin) — keep only alphabetic chars
   - Very long inputs (performance)

 Stretch tasks (optional):
   A) Write a one-liner `canonical = lambda s: ...` that returns the
      normalized, sorted canonical form; then compare forms.
   B) Add `are_anagrams_list(words: list[str]) -> list[tuple[str,str]]`
      that returns all pairs of anagrams using the same canonical form.
"""


import unicodedata
import string

canonical = lambda s: ''.join(sorted(
    char.lower() 
    for char in unicodedata.normalize("NFKD", s) 
    if char.isalpha() and not unicodedata.combining(char)
    ))

def is_anagram(a: str, b: str) -> bool:
    """
    Return True if `a` and `b` are anagrams under these rules:
      - case-insensitive
      - ignore spaces and punctuation
      - treat accented letters as their base letters (NFKD)
      - must be implemented with sorting (no Counter/dict counting)
    """
    return canonical(a) == canonical(b)

# ------------------------
# Minimal self-checks
# ------------------------
if __name__ == "__main__":
    tests = [
        ("listen", "silent", True),
        ("Dormitory", "dirty room!!", True),
        ("Árbol", "labor", True),
        ("The eyes", "They see", True),
        ("àéîõü", "ueoia", True),       # all vowels after stripping accents
        ("anagram", "nagaramm", False),
        ("abc", "abç", False),          # ç -> c + cedilla; keep only alpha, strip mark -> 'c'
        ("", "", True),
        ("!!!", "   ", True),           # both normalize to empty
    ]

    for i, (a, b, expected) in enumerate(tests, 1):
        try:
            got = is_anagram(a, b)
        except NotImplementedError:
            print("Implement `is_anagram` to run checks.")
            break
        ok = "OK" if got == expected else f"FAIL (got {got}, expected {expected})"
        print(f"Test {i}: {ok}")