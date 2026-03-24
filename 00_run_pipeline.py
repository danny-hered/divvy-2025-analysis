# run all scripts in order to ready data for analysis
import subprocess
import sys
from pathlib import Path

assert Path("data").exists(), "Run from project root so relative paths work."

python_exe = sys.executable

scripts = [
    "01_concat.py",
    "02_prepare.py",
    "03_clean.py",
]

print('\nPipeline start\n\n')

for script in scripts:
    print(f"Running {script}...")
    try:
        subprocess.run([python_exe, script], check=True, cwd='.', text=True)
        print('\n')
    except subprocess.CalledProcessError as e:
        print(f"\n{script} failed. Exit code {e.returncode}.")
        sys.exit(1)

print('\nPipeline complete\n')