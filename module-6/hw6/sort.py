import os
import shutil
import sys
from pathlib import Path

# os.rename("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
# os.replace("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
# shutil.move("path/to/current/file.foo", "path/to/new/destination/for/file.foo")

from parse import parse_folder
from normalize import normalize

# p = Path() / "module-04" / "path_lib.py"
# p = Path() / "module-04"
# print(p)
# for i in p.iterdir():
#     pass
# print(i)
# print(p.cwd())

# print(p.home())
# print(p.parent)
# print(p.name)
# print(p.suffix)
# print(p.exists())
# print(p.is_dir())
# print(p.is_file())
# print(p.absolute())

ext = {
    "images": ["JPEG", "PNG", "JPG", "SVG"],
    "video": ["AVI", "MP4", "MOV", "MKV"],
    "documents": ["DOC", "DOCX", "TXT", "PDF", "XLSX", "PPTX"],
    "audio": ["MP3", "OGG", "WAV", "AMR"],
    "archives": ["ZIP", "GZ", "TAR"],
    "other": [],
}

output = "./folder"


def rename(path):
    list = parse_folder(path)
    for file in list:
        old_name = file.absolute()
        new_name = Path(os.path.join(path, f"{normalize(file.stem)}{file.suffix}"))
        os.rename(old_name, new_name)


def sort(path):
    rename(path)
    # allfiles = os.listdir(path)
    # print(allfiles)
    list = parse_folder(path)

    for file in list:
        sfx = "".join(file.suffix[1:])
        for key, value in ext.items():
            directory = key
            parent_dir = path.parent
            dest = os.path.join(parent_dir, output, directory)
            other = os.path.join(parent_dir, output, "other")
            print(value)
            # for item in value:
            # if sfx.casefold() == item.casefold():
            #     if not os.path.exists(dest):
            #         os.makedirs(dest)
            #     # if os.path.exists(file):
            #     shutil.move(file, os.path.join(dest, file.name))
            # else:
            #     if not os.path.exists(other):
            #         os.makedirs(other)
            #     if os.path.exists(file):
            #         shutil.move(file, os.path.join(other, file.name))
            #     # os.rename(file, os.path.join(other, file.name))

    if not parse_folder(path):
        pass
        # os.rmdir(path)


if __name__ == "__main__":
    path = Path(sys.argv[1])
    sort(path)
