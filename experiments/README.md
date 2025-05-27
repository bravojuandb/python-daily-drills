
# 🛠️ Python Drill: Reading Files with `os.path` and `__file__`

**Goal**: Practice reading a file from the same directory or subdirectories using dynamic paths.  
Repeat each version manually to build fluency and confidence.  

---

## 🔁 Repetition 1 – Basic Read from Same Folder

```python
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'my_notes.txt')

with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

print(text)
```

---

## 🔁 Repetition 2 – Change File Name

```python
file_path = os.path.join(script_dir, 'poem.txt')
```

✅ Just update the filename and confirm your script still works.

---

## 🔁 Repetition 3 – Read from a Subfolder

```python
file_path = os.path.join(script_dir, 'texts', 'poem.txt')
```

✅ Create a `texts/` folder next to your script and move `poem.txt` there.

---

## 🔁 Repetition 4 – Add Error Handling

```python
if not os.path.exists(file_path):
    print("File not found:", file_path)
else:
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    print(text)
```

✅ Now your script won’t crash if the file is missing.

---

## 🔁 Repetition 5 – Add Logging

```python
import logging
logging.basicConfig(level=logging.INFO)

logging.info(f"Script folder: {script_dir}")
logging.info(f"Full file path: {file_path}")

if not os.path.exists(file_path):
    logging.error("File not found.")
else:
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    logging.info("File read successfully.")
```

✅ You now have clean, informative output and a professional script pattern.
