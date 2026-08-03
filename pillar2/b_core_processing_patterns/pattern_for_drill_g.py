"""
Position-Tracking Pattern

Write keep_last_color(colors) -> list[str].

Identify each color by its first letter. The last color with that letter wins,
but it stays at the position where the letter first appeared.

Example:
    ["red", "blue", "rose", "green", "brown"]
    -> ["rose", "brown", "green"]

Process the input once. Use a result list and a dictionary mapping each letter
to its position in the result.

Hint: append a new letter; replace at its saved position when seen again.
"""

def keep_last_color(colors: list[str]) -> list[str]:
    result = []
    letter_to_position = {}
    
    for color in colors:
        letter = color[0]
        if letter in letter_to_position:
            position = letter_to_position[letter]
            result[position] = color
        else:
            letter_to_position[letter] = len(result)
            result.append(color)

    return result
