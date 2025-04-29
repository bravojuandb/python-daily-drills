
import os

# Get the folder where the script itself is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Build the full path to the file
file_path = os.path.join(script_dir, 'carmina_I_11.txt')

# Open it
with open(file_path, "r", encoding='utf-8') as file:
    text = file.read()  # text variable is a string

words = text.split()
word_count = len(words)

print(f"Number of words: {word_count}")
print(script_dir)
print(__file__)
print(type(text))