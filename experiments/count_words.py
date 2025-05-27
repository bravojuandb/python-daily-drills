
"""
Count the words of a .txt file
Upgrade using Pathlib, wrapping the logic inside a function.

"""

from pathlib import Path

class TextAnalyzer:

    def __init__(self, filepath):
        self.filepath = Path(filepath).resolve()
        self.text = ''
        self.words = []
        self.word_count = 0

    def read_file(self):
        if not self.filepath.exists():
            raise FileNotFoundError(f"File not found: {self.filepath}")
        self.text = self.filepath.read_text(encoding='utf-8')

    def process(self):
        self.words = self.text.split()
        self.word_count = len(self.words)

    def summary(self):
        print(f"File: {self.filepath.name}")
        print(f"Folder: {self.filepath.parent}")
        print(f"Total words: {self.word_count}")
        print(f"Preview: {self.words[:10]}")

analyzer = TextAnalyzer("carmina_I_11.txt")  # relative or absolute path
analyzer.read_file()
analyzer.process()
analyzer.summary()
