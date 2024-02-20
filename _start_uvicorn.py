# OOP_Project
import subprocess

uvicorn_path = "myenv\\Scripts\\uvicorn.exe"
subprocess.run([uvicorn_path, "main:app", "--reload"])
