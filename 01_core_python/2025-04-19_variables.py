
"""
Daily Drill #6 – Parsing a `.env` Config File

**Topic:** Variables & Data Types  
**Focus:** File parsing, type conversion, and dictionary construction — 
key for real-world config loading in data pipelines.

Real-World Scenario

In many data engineering workflows, configs are stored in `.env` or `.ini` files. 
Instead of hardcoding values (like file paths, thresholds, or boolean flags), 
we extract them from config files. This drill simulates such a case and builds fluency with:

- File I/O
- String parsing
- Type conversion (str → bool, int, float)
- Dictionary usage

Task

Create a script `2025-04-19_variables.py` that:

1. Reads a `.env`-like config file.
2. Parses each line in the format `KEY=VALUE`.
3. Converts the value into the correct Python type:
   - `"True"`/`"False"` → `bool`
   - `"123"` → `int`
   - `"0.75"` → `float`
   - `"something.csv"` → `str`
4. Stores all pairs in a dictionary and prints the result.

---

## Example `.env` file (`sample.env`)

```env
DEBUG=True
MAX_ROWS=1000
THRESHOLD=0.75
FILE_NAME=data.csv

"""

def parse_value(value: str):
    """Convert string to bool, int, float, or str."""

    # Normalize boolean values (case-insensitive)
    if value.lower() == "true":
        return True
    if value.lower() == "false":
        return False
    
    # Check for simple integer strings (e.g., "100")
    if value.isdigit():
        return int(value)
    
    # Try converting to float (e.g., "0.75", "3.14")
    try:
        return float(value)
    except ValueError:
        # If conversion fails, treat it as a regular string
        return value

# Function: parse_env_from_string
# Purpose: Simulates reading a .env file from a string,
#          parses key-value pairs, and returns them as a dictionary   
def parse_env_from_string(env_string: str) -> dict:
    config = {} # Dictionary to store parsed key-value pairs

    # Split the string into lines and process each one
    for line in env_string.strip().splitlines():
            
            # Skip empty lines or comment lines that start with '#'
            if not line.strip() or line.startswith('#'):
                continue      
            
            # Split each line into key and value using '='
            key, value = line.strip().split('=', 1)

            # Use the parser function to convert the string value to the correct type
            config[key] = parse_value(value)
    # Return the complete configuration dictionary
    return config

# --- Simulated config content ---
# Here we simulate a .env file directly in the script.
# This could also be read from an actual file in a production setting.
env_content = """
DEBUG=True
MAX_ROWS=1000
THRESHOLD=0.75
FILE_NAME=data.csv
"""

# --- Script Entry Point ---
# This block runs only if the script is executed directly (not imported)
if __name__ == "__main__":
    # Parse the simulated config string
    config_dict = parse_env_from_string(env_content)
    print(config_dict)