"""
Write a Pure Function → def  🎓 (Latin Golden Age edition)

Task:
Write a PURE function `normalize_classical(text: str) -> str` that prepares Latin
text in a classical, inscription-style form—deterministic, no side effects.

Rules (apply in this order):
1) Map J→I and j→i; V→U and v→u (classical orthography).
2) Remove diacritics/macrons (āēīōūȳ → aeiouy, also any accents).
3) Remove all characters that are not letters or spaces (punctuation/numbers gone).
4) Collapse multiple spaces to a single space.
5) Strip leading/trailing spaces.
6) Return UPPERCASE.

Notes:
- Do not mutate inputs, do not read/write files, no globals—pure function only.
- Consider using Unicode normalization to strip diacritics.

Examples:
- Input:  "Arma virumque canō, Trōiae quī prīmus ab ōrīs."
  Output: "ARMA VIRUMQUE CANO TROIAE QUI PRIMUS AB ORIS"

- Input:  "Iamque dies Veneris—Ovidius!"
  Output: "IAMQUE DIES UENERIS OVIDIUS"

Stretch (optional, still pure):
Write `count_diphthongs(text: str) -> dict` that returns case-insensitive counts
for classical diphthongs {"AE","AU","OE","EI","EU","UI"} *after* normalization,
counting non-overlapping occurrences.

Be quick—aim for under 5 minutes!
"""
import unicodedata

def normalize_latin(text: str) -> str:
    text = unicodedata.normalize("NFD", text)
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    text = "".join(ch for ch in text if ch.isalpha() or ch.isspace())
    text = " ".join(text.split())
    mapped_text = text.upper().replace("V", "U").replace("J", "I")

    return mapped_text


input =  "Arma virumque   canō, Trōiae quī prīmus ab ōrīs."

print(normalize_latin(input))