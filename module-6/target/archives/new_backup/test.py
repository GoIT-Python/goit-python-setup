import shutil

archive_name = shutil.make_archive("backup", "zip")
archive_name = shutil.make_archive("new_backup", "tar")
# shutil.unpack_archive(archive_name, "new_folder_for_data")
