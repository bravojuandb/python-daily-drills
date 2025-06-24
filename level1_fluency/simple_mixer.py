"""
Given two lowercase strings, a and b
each containing space-separated words
with no punctuations and no capital letters.

Write a funtion that returns a sorted list 
of unique words that appear in either string.

- lowecase words
- list of unique words, dont include set()
- output sorted alfabetically
- no external libraries

"""

def word_mixer (a: str, b:str) -> list:
    words_a = a.split()
    words_b =b.split()
    all_words = words_a + words_b
    unique_words = []
    for word in all_words:
        if word not in unique_words:
            unique_words.append(word)
    return sorted(unique_words)

a = "hello world this is a test"
b = "this test is just a test hello world"

result = word_mixer(a,b)

print(result)

