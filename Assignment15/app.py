import platform
from datetime import datetime

print("=" * 50)
print("Dockerized Python Application")
print("=" * 50)

print(f"Python Version : {platform.python_version()}")
print(f"Current Date   : {datetime.now().strftime('%Y-%m-%d')}")
print(f"Current Time   : {datetime.now().strftime('%H:%M:%S')}")

print("=" * 50)