from os import listdir, path, mkdir
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
    match sections[0]:
        case 'image':
            dir = create_directory(source_dir, 'Images')
        case 'application' | 'text':
            dir = create_directory(source_dir, 'Documents')
        case 'audio':
            dir = create_directory(source_dir, 'Music')
        case 'video':
            dir = create_directory(source_dir, 'Video')
    
    return dir

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
                
            dir = new_directory_name(source_dir, file_type)
            
            move(path.join(source_dir, file), path.join(dir, file))
            
    except:
        print("Error")
        

def select_source_directory():
    global source_dir
    source_dir = filedialog.askdirectory(title="Seleccionar carpeta")
    
def center_widget(*widgets):
    
    # Configurar la expansión de la columna
    root.grid_columnconfigure(0, weight=1)

    # Asignar cada widget a una fila específica en la columna
    for i, widget in enumerate(widgets):
        widget.grid(row=i, column=0, pady=5)  # pady es un espacio vertical entre los widgets
    
root = Tk()


entry_dir_location = Entry(root, width=35, borderwidth=1)
entry_dir_location.grid(row=0, column=0, columnspan=2)

btn_browse_folder = Button(root, text='Browse Folder', command= select_source_directory, padx=10)
btn_browse_folder.grid(row=1, column=0)

btn_accept = Button(root, text='Accept', command= lambda: organize_files(source_dir), padx=10)
btn_accept.grid(row=1, column=1)

root.title('File Organizer')
root.geometry('300x300')
root.eval('tk::PlaceWindow . center')
root.mainloop()