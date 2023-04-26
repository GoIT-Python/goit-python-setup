def parse_folder(path):
    list = []
    for item in path.iterdir():
        if item.is_dir():
            parse_folder(item)
        else:
            list.append(item)
    return list
