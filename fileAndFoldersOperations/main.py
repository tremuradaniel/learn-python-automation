import os

from pathlib import Path


# p1 = os.path.dirname(__file__) + "\\files\\abc.txt"

p1 = Path("fileAndFoldersOperations\\files\\abc.txt")

if p1.exists():
    with open(p1, 'r') as file:
        print(file.read())

p2 = Path("fileAndFoldersOperations\\files\\zzz.txt")

if not p2.exists():
    with open(p2, 'w') as file:
        file.write("Content 3")

#  print(dir(Path))

print(p2.name)

files = Path("fileAndFoldersOperations\\files")
print(files.iterdir())

for file in files.iterdir():
    print(file.name)
