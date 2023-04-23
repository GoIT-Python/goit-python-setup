import shutil

path = "folder"
file_name = "task13.txt"
employee_residence = {"Michael": "Canada", "John": "USA", "Liza": "Australia"}


def create_backup(path, file_name, employee_residence):
    list = []

    for key, value in employee_residence.items():
        line = "".join("{} {}\n").format(key, value)
        list.append(line)

    with open(f"{path}/{file_name}", "wb") as file:
        for item in list:
            file.write(item.encode())

    archive_name = shutil.make_archive("backup_folder", "zip", path)
    print(archive_name)
    return archive_name


create_backup(path, file_name, employee_residence)
