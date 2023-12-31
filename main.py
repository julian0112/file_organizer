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

#This function checks the files in the source directory and saves the location in the variable file_dir, then it uses this variable to check the type of file
#if the file is NoneType it skips it, else it goes through the new directory_name function.
def organize_files(source_dir):
    
    files_to_organize = listdir(source_dir)
    
    try:
        for file in files_to_organize:

            file_dir = path.join(source_dir, file)
            file_type = detect_file_type(file_dir)
            
            if file_type is None:
                    continue
            
            sections = file_type.split('/')
            
            if sections[0] == "image" and checkVar_img.get() > 0:
                dir = create_directory(source_dir, 'Images')
                
            elif sections[0] == "video" and checkVar_vid.get() > 0:
                dir = create_directory(source_dir, 'Video')
                
            elif (sections[0] == "application" or sections[0] == "text") and checkVar_doc.get() > 0:
                dir = create_directory(source_dir, 'Documents')
            
            elif sections[0] == "audio" and checkVar_aud.get() > 0:
                dir = create_directory(source_dir, 'Audio') 
            else:
                continue
            
            
            move(path.join(source_dir, file), path.join(dir, file))
                
                #lbl_finish['text'] = ("Files Organized")
            
    except Exception as error:
        print("Error: ", type(error).__name__)
        
#This function allows to browse for a folder to organize and puts the directory in the text entry
def select_source_directory():
    global source_dir
    source_dir = filedialog.askdirectory(title="Seleccionar carpeta")
    entry_dir_location.configure(state=NORMAL)
    entry_dir_location.delete("1.0", END)
    entry_dir_location.insert(END, source_dir)
    entry_dir_location.configure(state=DISABLED)

#This function opens the windows explorer app
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
        cell = Label(root, width=10, height= 2, text="", bg='#1a0115')
        cell.grid(row=r, column=c)
        
#Folder icon and resize
folder_icon_img = PhotoImage(file='folder_icon2.png')
folder_icon_img = folder_icon_img.subsample(10, 10)

#The title
lbl_title = Label(root, text="File Organizer", font=("Microsoft YaHei UI", 15), bg='#1a0115', fg='white')

#The browse button,the text of the directory, the check folder button and their respective frames for the border color
btn_browse_border = Frame(root, highlightbackground='#4a012d', highlightthickness=2, bd=0)
btn_browse_folder = Button(btn_browse_border, text='Browse Folder', font=("Microsoft YaHei UI", 9), command= select_source_directory, width=15, bg='#1a0115', fg='white', 
                           activebackground='#2b0123', activeforeground='white', bd=0)

entry_dir_border = Frame(root, highlightbackground='#4a012d', highlightthickness=2, bd=0)
entry_dir_location = Text(entry_dir_border, width=60, height=1, state=DISABLED, font=("Microsoft YaHei UI", 10), bd=0, bg='#1a0115', fg='#b5a8b3')

btn_check_border = Frame(root, highlightbackground='#4a012d', highlightthickness=2, bd=0)
btn_check_folder = Button(btn_check_border, text="", command= lambda: check_directory(source_dir), image=folder_icon_img, bg='#1a0115', 
                          activebackground='#2b0123', activeforeground='white', bd=0)

#All the checkboxes for the diferent types of files
cb_documents = Checkbutton(root, text="Documents", anchor="w", font=("Microsoft YaHei UI", 10), variable=checkVar_doc, 
                           onvalue=1, offvalue=0, selectcolor='#1a0115', bg='#1a0115', fg='white', activebackground='#2b0123', activeforeground='white', bd=0)
cb_images = Checkbutton(root, text="Images", anchor="w", font=("Microsoft YaHei UI", 10), variable=checkVar_img, 
                           onvalue=1, offvalue=0, selectcolor='#1a0115', bg='#1a0115', fg='white', activebackground='#2b0123', activeforeground='white', bd=0)
cb_audio = Checkbutton(root, text="Audios", anchor="w", font=("Microsoft YaHei UI", 10), variable=checkVar_aud, 
                           onvalue=1, offvalue=0, selectcolor='#1a0115', bg='#1a0115', fg='white', activebackground='#2b0123', activeforeground='white', bd=0)
cb_videos = Checkbutton(root, text="Videos", anchor="w", font=("Microsoft YaHei UI", 10), variable=checkVar_vid, 
                           onvalue=1, offvalue=0, selectcolor='#1a0115', bg='#1a0115', fg='white', activebackground='#2b0123', activeforeground='white', bd=0)

#The acccept button and its frame for the border color
btn_accept_border = Frame(root, highlightbackground='#4a012d', highlightthickness=2, bd=0)
btn_accept = Button(btn_accept_border, text='Start Porcessing', font=("Microsoft YaHei UI", 10),command= lambda: organize_files(source_dir), width=80, bg='#1a0115', 
                          activebackground='#2b0123', activeforeground='white', bd=0, fg='white')

#Adding the widgets to the grid, title to check folder button
lbl_title.grid(row=0, column=0, columnspan=9, pady=10)

btn_browse_folder.grid(row=0, column=0, columnspan=2)
btn_browse_border.grid(row=1, column=0, columnspan=2, pady=5)

entry_dir_border.grid(row=1, column=1, columnspan=9)
entry_dir_location.grid(row=1, column=1, columnspan=9)

btn_check_folder.grid(row=1, column=8)
btn_check_border.grid(row=1, column=8)

#Adding the checkboxes to the grid
cb_documents.grid(row=2, column=3, columnspan=4, sticky="w", pady=10)
cb_images.grid(row=3, column=3, columnspan=4, sticky="w", pady=10)
cb_audio.grid(row=2, column=5, columnspan=4, sticky="w", pady=10)
cb_videos.grid(row=3, column=5, columnspan=4, sticky="w", pady=10)

#Adding accept button to the grid
btn_accept_border.grid(row=4, column=0, columnspan=9)
btn_accept.grid(row=4, column=0, columnspan=9)

root.title('File Organizer')

height = 255
width = 685
x = (root.winfo_screenwidth()//2) - (width//2)
y = (root.winfo_screenheight()//2) - (height//2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
root.resizable(width=False, height=False)
root.configure(bg='#1a0115')

root.mainloop()