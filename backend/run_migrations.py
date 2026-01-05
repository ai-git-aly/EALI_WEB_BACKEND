import subprocess
import sys

def run_makemigrations():
    # We'll send 'y' for every prompt. 
    # There are about 10-15 fields that were renamed.
    inputs = "y\n" * 20
    process = subprocess.Popen(
        [sys.executable, "manage.py", "makemigrations", "api"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, stderr = process.communicate(input=inputs)
    print("STDOUT:", stdout)
    print("STDERR:", stderr)

if __name__ == "__main__":
    run_makemigrations()
