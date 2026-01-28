
"""
Orchestration with Python

Goal
Use Python as a controller, not a worker.

Tasks
- Write a Python script that runs:
  - one Bash script
  - then another
- Stop execution if the first fails

Outcome
- You understand `subprocess.run`
- You understand orchestration vs logic

"""

import argparse
import subprocess
import sys

def run_script(cmd: list[str]) -> None:
    """
    Run scripts and fail early if any fail. 
    """
    print(f"run: {' '.join(cmd)}")
    result = subprocess.run(cmd)
    if result.returncode != 0:
        raise SystemExit(result.returncode)


def main():

    p = argparse.ArgumentParser()
    p.add_argument("--from", dest="from_month", required=True, help="YYYY-MM")
    p.add_argument("--to", dest="to_month", required=True, help="YYYY-MM")
    args = p.parse_args()

    print(f"start from={args.from_month} to={args.to_month}")

    # Run first bash script
    run_script(["bash", "drill03-1_loop.sh", args.from_month, args.to_month])

    # Run second bash script
    run_script(["bash", "drill03-1_loop.sh"])

    print("end")


# KeyboardInterrupt handling at the bottom
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\ninterrupted", file=sys.stderr)
        raise SystemExit(130)
