import psutil
import os
from tkinter import filedialog
from time_class import Time

class FileAccess:
#Will get the file path and return the string
    @classmethod
    def get_file_path(cls):
        #Prompts user for file path and stores the location
        file_path = filedialog.askopenfilename()
        file = ""
        #Will iterate thru the file path reversely and stop at the first "/" 
        #It will store the name
        #EX: C:/Dennis/Steam.Exe
        #It will store in "Steam.exe"
        for x in file_path[::-1]:
            if x == "/":
                break
            else:
                file += x
        #Split will split the string into 2 parts
        #['steam', '.exe']
        #Will target the first value
        return file[::-1].split('.')[0]

#Kills the process
    @classmethod
    def kill_application(cls, hit_list):
        #Iterates thru all of the processes
        for proc in psutil.process_iter():
            try:
                #Iterates thru all of the hit_list items
                for programs in hit_list:
                    #If the item is a substring of a process
                    #It will kill the process
                    if programs in proc.name():
                        if programs == "":
                            pass
                        else:
                            os.system("taskkill /F /PID " + str(proc.pid))
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

#Will write to file names of programs to txt
    @classmethod
    def write_to_file(cls, file_name):
        #Will write to blacklist what files need to be added
        file = open("black_list.txt", "a")
        file.write(file_name + "\n")
        file.close()

#Will read the file and return a list of programs on the blacklist
    @classmethod
    def read_from_file(cls):
        file = open("black_list.txt", "r")
        files = file.readlines()
        file.close()  

        for i in range(len(files)):
            files[i] = files[i].replace("\n", "")
        return files

    @classmethod
    def delete_from_file(cls, removal):
        file = open("black_list.txt", "r")
        lines = file.readlines()
        file.close()
        del lines[removal]

        file = open("black_list.txt", "w+")
        for items in lines:
            file.write(items)

        file.close()

