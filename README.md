# Python Daily Drills

## What is this?

This is my Python trainer for high-quality coding interviews.
It's built around 4 essential pillars:

- Fluency & Logic:
     
Think and code quickly and correctly using Python’s built-in features (lists, dicts, sets, loops).

- Clean Code & Testing:
     
Write reusable, testable functions, use docstrings, handle edge cases, and write pytest tests.

- Script Engineering:
     
Build full scripts with argparse, logging, file I/O, and modular design (main()).

- Pipeline Thinking:
     
Simulate real-world data workflows: read a file → transform it → write it — and organize code well.

## GitHub Workflow

1. Create 4 milestones (one per Pillar):
   - Pillar 1: Fluency & Logic  
   - Pillar 2: Clean Code & Testing  
   - Pillar 3: Script Engineering  
   - Pillar 4: Pipeline Thinking  

2. Create one issue per drill, linked to the right milestone.  
   Use labels like `pillar:1`, `difficulty:medium`, `subcategory:functions`.

3. Create a branch from the issue using GitHub CLI:
   ```bash
   gh issue develop <issue-number>
   ```

4. Solve the drill, make commits, then open a Pull Request.  
   Use commit messages like:
   ```
   feat: add reverse_unique with set logic
   ```

5. Merge the PR when done.

6. Plan each week as a sprint using GitHub Projects.  
   One project = one week = one sprint.  
   Track progress with columns: `to do, in progress ,done`.



## Methodology

- Chatgpt prompt:

            “Give me a Turing-style Python drill from Pillar X, Level Y.”

            being X the pillar number, and Y the difficulty: easy, medium or hard

