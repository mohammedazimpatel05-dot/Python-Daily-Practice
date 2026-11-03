import os
import shutil

# Safe approach: Ensure the destination folder exists first
os.makedirs("dest", exist_ok=True)
shutil.move("file.txt", "dest/")
