"""
Unique Visitors Counter challenge

Given a web server log file `access.log`, each line containing an IP address
(e.g. "192.168.0.5"), implement a function that returns the number of **unique**
visitors.

Rules:
- Read the log line by line from the file path provided.
- Ignore blank lines.
- Treat the same IP appearing multiple times as one visitor.
- You may assume one IP per line.
- Use a set for O(1) membership testing.

Signature:
    def count_unique_visitors(filepath: str) -> int:

Example:
    # access.log
    # 192.168.0.5
    # 192.168.0.6
    # 192.168.0.5
    # Expected: 2

Think fast, code cleanly — this logic is the foundation for
log deduplication and unique-user analytics in pipelines.
"""

def count_unique_visitors(filepath: str) -> int:
    """
    Return the number of unique visitors from a web server log file.

    Args:
        filepath (str): Path to the log file containing one IP address per line.

    Returns:
        int: The number of unique IP addresses found in the file.
    """

    with open(filepath, "r", encoding="utf-8") as f:

        ips = {line.strip() for line in f if line.strip()}  
    return len(ips)

print(count_unique_visitors("resources/access.log"))