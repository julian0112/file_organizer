from os import listdir, path, mkdir, system
from shutil import move
from mimetypes import guess_type
from tkinter import *
from tkinter import filedialog

#This function detects the type of file using the mimetypes library
def detect_file_type(file_path):
    mime_type, encoding = guess_type(file_path)
    return mime_type

#This function checks if there is already a folder in the source directory for the diferent types of files
#If there is not a folder, it creates one
def create_directory(source_dir, type):
    directory_type = path.join(source_dir, type)
    if not path.exists(directory_type):
        mkdir(directory_type)
        
    return directory_type

#This function organizes the files, it uses the file type to use in the create_directory function and determined the folder that needed to be selected or created
#then moves the file in the selected folder
def new_directory_name(source_dir, file_type):
    
    sections = file_type.split('/')
    dir = ""
    
    if sections[0] == "image" and checkVar_img.get() > 1:
        dir = create_directory(source_dir, 'Images')
    
    # elif (sections == "application" or sections == "text") and checkVar_doc.get() > 1:
    #     dir = create_directory(source_dir, 'Documents')
        
    # elif sections == "audio" and checkVar_aud.get() > 1:
    #     dir = create_directory(source_dir, 'Documents')
        
    # elif sections == "video" and checkVar_vid.get() > 1:
    #     dir = create_directory(source_dir, 'Video')
    
    return dir
    # match sections[0]:
    #     case 'image':
    #         dir = create_directory(source_dir, 'Images')
    #     case 'application' | 'text':
    #         dir = create_directory(source_dir, 'Documents')
    #     case 'audio':
    #         dir = create_directory(source_dir, 'Music')
    #     case 'video':
    #         dir = create_directory(source_dir, 'Video')
    
    

#This function checks the files in the source directory and saves the location in the variable file_dir, then it uses this variable to check the type of file
#if the file is NoneType it skips it, else it goes through the new directory_name function.
def organize_files(source_dir):
    
    files_to_organize = listdir(source_dir)
    
    # try:
    for file in files_to_organize:

        file_dir = path.join(source_dir, file)
        file_type = detect_file_type(file_dir)
        
        if file_type is None:
                continue
            
        dir = new_directory_name(source_dir, file_type)
        
        move(path.join(source_dir, file), path.join(dir, file))
            
            #lbl_finish['text'] = ("Files Organized")
            
    # except:
    #     print("Error")
        

def select_source_directory():
    global source_dir
    source_dir = filedialog.askdirectory(title="Seleccionar carpeta")
    entry_dir_location.configure(state=NORMAL)
    entry_dir_location.delete("1.0", END)
    entry_dir_location.insert(END, source_dir)
    entry_dir_location.configure(state=DISABLED)


def check_directory(source_dir):
    system("start "+source_dir)

root = Tk()
#Variable for the ckeckbox
checkVar_doc = IntVar()
checkVar_img = IntVar()
checkVar_aud = IntVar()
checkVar_vid = IntVar()

#Creates label in all the grid
for r in range(0, 7):
    for c in range(0, 9):
        cell = Label(root, width=10, height= 2, text="")
        cell.grid(row=r, column=c)
        
#Folder icon and resize
folder_icon_img = PhotoImage(file='folder_icon.png')
folder_icon_img = folder_icon_img.subsample(10, 10)

#The title
lbl_title = Label(root, text="File Organizer", font=("Microsoft YaHei UI", 15))

#The brose button, the text of the directory and the check folder button
btn_browse_folder = Button(root, text='Browse Folder', font=("Microsoft YaHei UI", 9), command= select_source_directory, width=15)
entry_dir_location = Text(root, width=60, height=1, state=DISABLED, font=("Microsoft YaHei UI", 10))
btn_check_folder = Button(root, text="J", command= lambda: check_directory(source_dir), image=folder_icon_img, font=("Microsoft YaHei UI", 10))

#All the checkboxes for the diferent types of files
cb_documents = Checkbutton(root, text="Documents", anchor="w", font=("Microsoft YaHei UI", 10), variable=checkVar_doc, 
                           onvalue=1, offvalue=0)
cb_images = Checkbutton(root, text="Images", anchor="w", font=("Microsoft YaHei UI", 10), variable=checkVar_img, 
                           onvalue=1, offvalue=0)
cb_audio = Checkbutton(root, text="Audios", anchor="w", font=("Microsoft YaHei UI", 10), variable=checkVar_aud, 
                           onvalue=1, offvalue=0)
cb_videos = Checkbutton(root, text="Videos", anchor="w", font=("Microsoft YaHei UI", 10), variable=checkVar_vid, 
                           onvalue=1, offvalue=0)

btn_accept = Button(root, text='Start Porcessing', font=("Microsoft YaHei UI", 10), command= lambda: organize_files(source_dir), width=80)

#Adding the widgets to the grid, title to check folder button
lbl_title.grid(row=0, column=0, columnspan=9, pady=10)
btn_browse_folder.grid(row=1, column=0, columnspan=2, pady=5)
entry_dir_location.grid(row=1, column=1, columnspan=9)
btn_check_folder.grid(row=1, column=8, pady=8)

#Adding the checkboxes to the grid
cb_documents.grid(row=2, column=3, columnspan=4, sticky="w", pady=10)
cb_images.grid(row=3, column=3, columnspan=4, sticky="w", pady=10)
cb_audio.grid(row=2, column=5, columnspan=4, sticky="w", pady=10)
cb_videos.grid(row=3, column=5, columnspan=4, sticky="w", pady=10)

#Adding accept button to the grid
btn_accept.grid(row=4, column=0, columnspan=9)

root.title('File Organizer')

height = 255
width = 685
x = (root.winfo_screenwidth()//2) - (width//2)
y = (root.winfo_screenheight()//2) - (height//2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
root.resizable(width=False, height=False)
root.mainloop()