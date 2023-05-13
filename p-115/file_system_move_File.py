import os 
import shutil 
source="main.txt"
destination="newfile.txt"
os.rename(source,destination)
print("source path renamed to destination path successfully.")