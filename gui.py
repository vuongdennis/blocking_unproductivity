from tkinter import *
from file_access import *
import time
from threading import Thread
import os
import psutil

root = Tk()
root.title("Productivity Booster")
root.resizable(False, False)

#Will prompt a window pop up that allows you to select the program
#you want to add
def add_program():
    selected_program = FileAccess.get_file_path()
    FileAccess.write_to_file(selected_program)
    list_box.insert(END, selected_program)

#Will remove the highlighted program in the list
def remove_program():
    FileAccess.delete_from_file(list_box.curselection()[0])
    list_box.delete(list_box.curselection()[0])

#Will stop all the thread and processes
def stop():
    current_system_pid = os.getpid()
    psutil.Process(current_system_pid).terminate()

#Will make sure that the designated programs are killed in 15s
def timezone():
    timer = Time(hour_entry.get(), minutes_entry.get())
    while timer.check() != True:
        FileAccess.kill_application(FileAccess.read_from_file())
        time.sleep(15)
    stop()

#Will start the whole process
def start():
    thread = Thread(target = timezone)
    thread.start()

#The creation of the buttons at the top
frame1 = Frame(root)
add_button = Button(frame1, text = "Add Program", command = add_program)
remove_button = Button(frame1, text = "Remove Program", command = remove_program)
start_button = Button(frame1, text = "Start", command = start)
stop_button = Button(frame1, text = "Stop", command = stop)

add_button.grid(row = 0, column = 0, padx = 5, pady = 2.5)
remove_button.grid(row = 0, column = 1, padx = 5, pady = 2.5)
start_button.grid(row = 0, column = 2, padx = 5, pady = 2.5)
stop_button.grid(row = 0, column = 3, padx = 5, pady = 2.5)
frame1.pack()

#Will fill out the list from the text file
list_box = Listbox(root)
file_names = FileAccess.read_from_file()
for i in range(len(file_names)):
    list_box.insert(i, file_names[i])
list_box.pack(fill = BOTH, padx = 5, pady = 2.5)

frame2 = Frame(root)
Label(text = "Enter in the time you want the program to stop.").pack()
hour_label = Label(frame2, text = "Hours:")
hour_entry = Entry(frame2)
minutes_label = Label(frame2, text = "Minutes:")
minutes_entry = Entry(frame2)
hour_label.grid(row=0,column=0, pady = 5)
hour_entry.grid(row=0, column=1, pady = 5)
minutes_label.grid(row = 0, column = 2, pady = 5)
minutes_entry.grid(row = 0, column = 3, pady = 5)
frame2.pack()

#sets the protocal of "x" to go to stop()
root.protocol("WM_DELETE_WINDOW", stop)

mainloop()
