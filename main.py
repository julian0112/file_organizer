from os import listdir, path, mkdir
from shutil import move
from mimetypes import guess_type

#DIRECTORIES
source_dir = 'D:\Descargas'
files_to_organize = listdir(source_dir)

def detect_file_type(file_path):
    mime_type, encoding = guess_type(file_path)
    return mime_type

def create_directory(source_dir, type):
    directory_type = path.join(source_dir, type)
    if not path.exists(directory_type):
        mkdir(directory_type)
        
    return directory_type

# def organize_files(file):
    
#     secciones = file_type.split('/')

#     dir = create_directory(source_dir, )
#     move(path.join(source_dir, file), path.join(dir, file))

#Check the files in the source directory, then checks the category in where the extemsion matches and sent the file to the respective folder
# try:
for file in files_to_organize:

    file_dir = path.join(source_dir, file)
    file_type = detect_file_type(file_dir)
    
    if file_type is None:
            continue
        
    elif 'application' in file_type or 'text' in file_type:
        doc_dir = create_directory(source_dir, 'Documents')
        move(path.join(source_dir, file), path.join(doc_dir, file))
 
    elif 'image' in file_type:
        img_dir = create_directory(source_dir, 'Images')
        move(path.join(source_dir, file), path.join(img_dir, file))

    elif 'audio' in file_type: 
        music_dir = create_directory(source_dir, 'Music')
        move(path.join(source_dir, file), path.join(music_dir, file))
            
    elif 'video' in file_type:
        videos_dir = create_directory(source_dir, 'Videos')
        move(path.join(source_dir, file), path.join(videos_dir, file))
        
# except:
#     print("Error")