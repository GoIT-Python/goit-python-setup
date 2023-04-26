from pathlib import Path
import os
import shutil

path = Path(".")
# print(path.absolute())
print(os.listdir())

# shutil.move("lab1.txt", "./C")
# os.mkdir(f"{os.getcwd()}/M")

# os.rename("lab_basic.txt", "A/lab_basic.txt")
# os.replace("A/lab_basic.txt", "lab1.txt")


# def walk(path, prev_list_dir):
#     print(os.getcwd())

#     os.chdir(path)

#     list_dir = list(filter(os.path.isdir, os.listdir()))

#     for item in list_dir:
#         list_dir.remove(item)
#         walk(f"{path}/{item}", list_dir)


# walk(r".", [])


# print(os.getcwd())
