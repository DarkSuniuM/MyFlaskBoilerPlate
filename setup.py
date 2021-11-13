"""Setup project."""

import subprocess
import shutil
import os

dependencies = ["Flask>=2", "gunicorn>=20", "python-dotenv"]

subprocess.call(["python3", "-m", "virtualenv", ".venv"])
subprocess.call([".venv/bin/pip", "install"] + dependencies)
requirements_txt = subprocess.check_output(
    [".venv/bin/pip", "freeze", "requirements.txt"]
)
with open("./requirements.txt", "wb") as requirements_file:
    requirements_file.write(requirements_txt)

shutil.rmtree(".git")
subprocess.call(["git", "init", "."])
os.unlink("setup.py")
