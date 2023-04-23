import shutil

archive_name = ""

archive_name = shutil.make_archive("backup", "zip")

print(archive_name)

# shutil.unpack_archive(archive_name, "new_folder_for_data")
