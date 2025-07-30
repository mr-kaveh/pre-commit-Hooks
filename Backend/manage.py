import subprocess
import sys

if len(sys.argv) > 1 and sys.argv[1] == "precommit":
    subprocess.run(["pre-commit", "run", "--all-files"], check=True)
    sys.exit(0)
