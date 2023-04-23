import shutil

archive_name = ""

# archive_name = shutil.make_archive("backup", "zip")

print(archive_name)

shutil.unpack_archive("backup.zip", "new_folder_for_data")
