import os
from pathlib import Path

path = Path(".")


for item in path.iterdir():
    print(os.path.splitext(item)[0])
