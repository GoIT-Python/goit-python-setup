from pathlib import Path
import sys

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
    "others": [],
}

path = sys.argv[1]
p = Path(path)


# def parse_ext(ext):
#     for key, value in ext.items():
#         print(key, value)


# parse_ext(ext)


def parse_folder(path):
    for item in path.iterdir():
        if item.is_dir():
            parse_folder(item)
        else:
            # print(f"This is file: {item}")
            # print(item.suffix)
            file = item
            sfx = "".join(item.suffix[1:])
            # print(sfx)
            for key, value in ext.items():
                # print(key, value)
                for item in value:
                    if sfx.casefold() == item.casefold():
                        print(file, item)


parse_folder(p)

# def sort(path):
#     list = []
#     list.append(parse_folder(path))
#     print(list)
# sort(p)
