"""
Tool for analyzing an excerp of Alice in Wonderland

Goals:

- Create a pandas df with two colums: word and frequency

"""

from pathlib import Path
import re

def read_text_file(file_path: Path, preview: bool = False) -> str:
    """Reads the content of a .txt file and returns it as a string if preview is True"""
    if not file_path.exists():
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    text = file_path.read_text(encoding='utf-8')
    if preview:
        print("Preview of raw file content:")
        print(text[:500])  # Show the first 500 characters
    return text

def clean_text_file(text: str, preview: bool = False ) :
    """
    Cleans a text string by:
    - Lowercasing all characters
    - Removing punctuation marks
    - Normalizing whitespace
    """
    text = text.lower()
    text = re.sub(r"[.,!?;:¿¡()\"'-]", "", text)  # Remove punctuation
    text = re.sub(r"\s+", " ", text).strip()  # Remove extra spaces

    if preview:
        print("Preview of raw file content:")
        print(text[:500])  # Show the first 500 characters

    return text


if __name__ == "__main__":
    # Example usage
    file_path = Path(__file__).parent / "alice.txt"  # Replace with your actual file path
    try:
        text = read_text_file(file_path)
        text = clean_text_file(text, True)
    except Exception as e:
        print(f"Error: {e}")