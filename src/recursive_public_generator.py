import os
import shutil

def remove_recursive_directory(main_directory):
    for directory in os.listdir(main_directory):
        # print("the current file to be deleted is " + directory)
        if os.path.isfile(f"{main_directory}/{directory}"):
            os.remove(f"{main_directory}/{directory}")            
        
    for directory in os.listdir(main_directory):
        remove_recursive_directory(f"{main_directory}/{directory}")
    os.rmdir(main_directory)

# copies all files and directories from the source folder to the destination folder
# ![IMPORTANT]: assumes destination folder is empty
def copy_files_recursively(source, destination): # fail for now
    for directory in os.listdir(source):
        if os.path.isfile(os.path.join(source, directory)):
            shutil.copy(os.path.join(source, directory), destination)        
        else:
            os.mkdir(os.path.join(destination, directory))
            copy_files_recursively(os.path.join(source, directory), os.path.join(destination, directory))

def recursive_public_generator(main_dir):
    # print(os.getcwd())
    # print("cuurent path is " + main_dir)
    if os.path.isdir(main_dir + "/public"):
        # os.removedirs(main_dir + "/public")
        # for dirpath, dirnames, filenames in os.walk(main_dir + "/public"):
        #     for file in filenames:
        #         os.remove(dirpath + file)
        remove_recursive_directory(main_dir + "/public") # could have probably used rmtree
    os.mkdir(main_dir + "/public")
    copy_files_recursively(os.path.join(main_dir, "static"), os.path.join(main_dir, "public"))


if __name__ == "__main__":
    recursive_public_generator(os.getcwd())