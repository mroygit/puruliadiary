import os
import sys
import subprocess
from pathlib import Path


# ==============================
# CONFIGURATION
# ==============================

PROJECT_NAME = "city_services"
BASE_DIRECTORY = r"C:\Users\MAC\Projects"

# ==============================
# DO NOT MODIFY BELOW
# ==============================

project_path = Path(BASE_DIRECTORY) / PROJECT_NAME
venv_path = project_path / "venv"

print("=" * 60)
print("FLASK PROJECT INSTALLER")
print("=" * 60)

# Create project directory
print("\nCreating project directory...")

project_path.mkdir(parents=True, exist_ok=True)

# Create virtual environment
print("Creating virtual environment...")

subprocess.check_call([
    sys.executable,
    "-m",
    "venv",
    str(venv_path)
])

# Locate python executable inside venv
if os.name == "nt":
    python_exe = venv_path / "Scripts" / "python.exe"
else:
    python_exe = venv_path / "bin" / "python"

# Upgrade pip
print("Upgrading pip...")

subprocess.check_call([
    str(python_exe),
    "-m",
    "pip",
    "install",
    "--upgrade",
    "pip"
])

# Install Flask
print("Installing Flask...")

subprocess.check_call([
    str(python_exe),
    "-m",
    "pip",
    "install",
    "Flask"
])

# Create folders
print("Creating folders...")

folders = [
    "templates",
    "static",
    "static/css",
    "static/js",
    "static/images"
]

for folder in folders:
    (project_path / folder).mkdir(parents=True, exist_ok=True)

# Create app.py
print("Creating app.py...")

app_code = '''from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to City Services</h1>"

if __name__ == "__main__":
    app.run(debug=True)
'''

(project_path / "app.py").write_text(app_code)

# Create requirements.txt
print("Generating requirements.txt...")

req = subprocess.check_output([
    str(python_exe),
    "-m",
    "pip",
    "freeze"
]).decode()

(project_path / "requirements.txt").write_text(req)

# Create README
readme = f"""
Flask Project

Project Location

{project_path}

To activate virtual environment:

Windows:

venv\\Scripts\\activate

Run project:

python app.py
"""

(project_path / "README.txt").write_text(readme)

print("\n" + "=" * 60)
print("INSTALLATION COMPLETED SUCCESSFULLY")
print("=" * 60)

print("\nProject Location:")
print(project_path)

print("\nTo start the application:")

print(rf"""
cd "{project_path}"
venv\Scripts\activate
python app.py
""")

print("\nOpen your browser at:")
print("http://127.0.0.1:5000/")