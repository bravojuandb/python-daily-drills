"""
Longest Word in a Sentence

Description:

Write a function that takes a sentence as input and returns the longest word in it.
If multiple words have the same length, return the first one.

"""
import string

def longest_word(sentence: str) -> str:

    words = sentence.split()
    clean_words = []
    for word in words:
        cl_word = word.strip(string.punctuation)
        clean_words.append(cl_word)

    return max(clean_words, key=len)

sentence = ("""La libertad, Sancho, es uno de los más preciosos dones 
            que a los hombres dieron los cielos; con ella no pueden igualarse 
            los tesoros que encierran la tierra ni el mar encubre; 
            por la libertad, así como por la honra, 
            se puede y debe aventurar la vida.""")

print(longest_word(sentence))