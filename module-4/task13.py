def parse_folder(path):
    files = []
    folders = []

    # path = Path(path)

    for x in path.iterdir():
        if x.is_dir():
            folders.append(x.name)
        elif x.is_file():
            files.append(x.name)

    return files, folders


print(parse_folder("/Users/vk/Documents/GitHub/goit-python-setup"))
