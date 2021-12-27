import os
import os.path

for root, dirs, files in os.walk("D_Z_20_2"):
    if files:
        for i in files:
            print(f"'{root}/{i}',", end="\t")
    if dirs:
        for i in dirs:
            print(f"'{root}/{i}',", end="\t")

os.mkdir("Work/empty_files")

for root, dirs, files in os.walk("Work"):
    for name in files:
        file_path = os.path.join(root, name)
        file_size = os.path.getsize(file_path)
        if file_size == 0:
            os.rename(file_path, f"Work/empty_files/{name}")
            print(f"файл {name} перемещен по адресу Work/empty_files/{name} ")
        if file_size != 0:
            print(name, file_size, "bytes")


