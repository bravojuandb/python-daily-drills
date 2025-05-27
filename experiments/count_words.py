
"""
Count the words of a .txt file
Upgrade using Pathlib, wrapping the logic inside a function.

"""

from pathlib import Path

def analyze_text_file(filename):

    # Get path of the current script
    script_path = Path(__file__).resolve()

    # Get the folder where the script lives
    script_dir = script_path.parent

    # Build the full path to the text file
    file_path = script_dir / filename

    # Read the file
    text = file_path.read_text(encoding='utf-8')

    # Process the text
    words = text.split()
    word_count = len(words)

    print(f"\n The text converted to list: {words}")
    print(f"\n Number of words: {word_count}")
    print(f"\n This is the folder where the script lives: {script_dir}")
    print(f"\n This is the path to the python script: {__file__}")
    print(type(words))

    return words, word_count

words, count = analyze_text_file("carmina_I_11.txt")
