"""
Tool for analyzing an excerp of Alice in Wonderland

Goals:

- Create a pandas df with two colums: word and frequency

"""

from pathlib import Path

def read_text_file(file_path: Path) -> str:
    """Reads the content of a .txt file and returns it as a string."""
    if not file_path.exists():
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    return file_path.read_text(encoding='utf-8')


if __name__ == "__main__":
    # Example usage
    file_path = Path(__file__).parent / "alice.txt"  # Replace with your actual file path
    try:
        text = read_text_file(file_path)
        print(text[:500])  # Print the first 500 characters for preview
    except Exception as e:
        print(f"Error: {e}")