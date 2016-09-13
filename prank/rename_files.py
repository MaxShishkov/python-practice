import os
import string

def rename_files():
    #1) get file names from the folder

    file_list = os.listdir(r"E:\MyCode\python\prank")
    
    #2) for each file, rename file
    remove_num_map = dict((ord(char), None) for char in string.digits)
    for file_name in file_list:
        os.rename(file_name,file_name.translate(remove_num_map))

    


rename_files()
