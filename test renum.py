import os
import shutil
from tkinter import filedialog

content = []
file_count = 0
mod_count = 0
repeat_every_xth_frame = int(input("enter repeet frame count"))
perl_filename_base = filedialog.askdirectory()#os.path.splitext(os.path.basename(__file__))[0]
log_file = f"{perl_filename_base}.log"


with open(log_file, 'w') as fh:
    fh.write("fileCount, filePath, fileName\n")

    def file_wanted(file):
        global file_count, mod_count
        if file.lower().endswith('.jpg'):
            content.append(file)
            return

    def copy_file(file_path, file_name):
        global file_count, mod_count
        file_count += 1
        mod_count += 1
        file_dir, file_ext = os.path.splitext(file_path)
        file_dir = file_dir.replace('/', '\\')

        # using shutil to copy the file
        num_format = f"{file_count:09d}"
        copy_name = f"zimg{num_format}.jpg"
        shutil.copy(file_name, copy_name)

        fh.write(f"{file_count}, {file_dir}, {copy_name}\n")
        print(f"{file_count}, {file_dir}, {copy_name}")

        if mod_count == repeat_every_xth_frame:
            # reset "modulo" count
            mod_count = 0
            file_count += 1
            num_format = f"{file_count:09d}"
            copy_name = f"zimg{num_format}.jpg"
            shutil.copy(file_name, copy_name)

            fh.write(f"{file_count}, {file_dir}, {copy_name} - repeated/copied\n")
            print(f"{file_count}, {file_dir}, {copy_name} - repeated/copied")

    # find all files from current and subdirectories
    for root, dirs, files in os.walk('.'):
        for file_found in files:
            file_path = os.path.join(root, file_found)
            file_wanted(file_path)

    for file_found in content:
        copy_file(file_found, file_found)
