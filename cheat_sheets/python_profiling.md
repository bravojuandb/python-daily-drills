# Python Profiling

This note demonstrates how to profile Python code for **runtime** and **memory**:  
- Quick snapshots  
- Line-by-line analysis  

In Jupyter/IPython, use the magic commands:  
- `%timeit` → quick runtime benchmarks  
- `%lprun` → line-by-line runtime profiling  
- `%memit` → memory usage snapshot  
- `%mprun` → line-by-line memory profiling (requires code in a `.py` file)

⚠️ For plain Python scripts (outside Jupyter/IPython), the profiling syntax and tools differ (e.g. `cProfile`, `timeit` module, or memory profilers). And they're not a subject of this note.

## 1. Setup

Create and activate a virtual environment:

python3 -m venv prof_env
source prof_env/bin/activate
python -m pip install --upgrade pip jupyter ipykernel ipython line_profiler memory-profiler psutil

Add the venv as a Jupyter kernel:

python -m ipykernel install --user --name prof_env --display-name "Python (prof_env)"

---

## 2. Runtime Profiling

### Whole function timing
%timeit build_list(1_000_000)

### Line-by-line runtime
%load_ext line_profiler

def build_list(n):
    out = []
    for i in range(n):
        out.append(i)
    return out

%lprun -f build_list build_list(1_000_000)

**Output explained:**
- *Hits*: how many times each line ran  
- *Time*: total time spent on that line  
- *Per Hit*: average time per execution  
- *% Time*: share of total runtime  

---

## 3. Memory Profiling

### Whole function memory usage
%load_ext memory_profiler
%memit build_list(1_000_000)

### Line-by-line memory usage
Save function into `mymods.py`:
def build_list(n):
    out = []
    for i in range(n):
        out.append(i)
    return out

Then in the notebook:
%run mymods.py
%mprun -f build_list build_list(1_000_000)

**Output explained:**
- *Mem usage*: current memory at that line  
- *Increment*: memory gained since previous line  
- *Occurrences*: how many times the line ran  

---

## 4. Comparison: Loop vs Builtin

def build_list_loop(n):
    out = []
    for i in range(n):
        out.append(i)
    return out

def build_list_builtin(n):
    return list(range(n))

print("Loop:")

%timeit build_list_loop(1_000_000)
%memit build_list_loop(1_000_000)

print("Builtin:")

%timeit build_list_builtin(1_000_000)
%memit build_list_builtin(1_000_000)

---

## 5. Key Takeaways

- **Use `%timeit`** for quick performance benchmarks.  
- **Use `%lprun`** for per-line runtime analysis.  
- **Use `%memit`** for total memory snapshots.  
- **Use `%mprun`** (with a `.py` file) for per-line memory deltas.  

- Builtins (`list(range(n))`) are almost always faster and more memory-friendly than manual loops.  