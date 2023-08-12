"""
THIS PROGRAM CAN PRETTIFY ANY FOLDER AND THE FILE

Things it can do:
    • Can Capitalize the first letter of the file name and renames it.
    • Can also put the exception on the files that we don't want to Capitalize.
    • Can also Capitalize the provided extension file names.

folder_path: This is the folder location where the files will be prettified.

file_path: File names belong to this file will be excluded from capitalizing the first letter of the file name.

file_format: Files with this extension will be renamed with No. 1-n (n= No. of such files)
"""

import os

def soldier(par_folder_path, par_file_path, par_file_format):
    os.chdir(par_folder_path)

    with open(par_file_path) as f:
        text = f.read().split("\n")

    i = 1
    for item in os.listdir():

        if item.endswith(par_file_format):
            os.rename(item, f"{i}_{item}")
            i += 1

        elif item not in text:
            os.rename(item, item.capitalize())


print("\n------WELCOME TO FOLDER PRETTIFIER------")
folder_path = input("\nEnter the Folder Path : ")
file_path = input("Enter the File Path : ")
file_format = input("Enter the File Format : ")

soldier(folder_path, file_path, file_format)
print("\nHey, It's done. Check it!")