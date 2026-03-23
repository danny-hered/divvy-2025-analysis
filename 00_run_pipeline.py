# run all scripts in order to ready data for analysis
import subprocess
import sys

from pathlib import Path
assert (Path("data").exists()), "Run from project root so relative paths work."


python_exe = sys.executable
subprocess.run([python_exe, "01_concat.py"], check=True, cwd='.', text=True)
subprocess.run([python_exe, "02_prepare.py"], check=True, cwd='.', text=True)
subprocess.run([python_exe, "03_clean.py"], check=True, cwd='.', text=True)