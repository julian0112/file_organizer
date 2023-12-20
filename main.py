from os import listdir, path
import shutil

#DIRECTORIES
source_dir = 'D:\Julian\Documents\TestCleaner'
img_dir = 'D:\Julian\Pictures'
music_dir = 'D:\Julian\Music'
videos_dir = 'D:\Julian\Videos'
files_to_organize = listdir(source_dir)

#Different extensions for the files inside tuples
img_extensions = (".jpg", ".jpeg", ".png", ".gif", ".webp")
music_extensions = (".m4a", ".mp3", ".wav", ".flac")
video_extensions = (".mp4", ".mkv")

#Check the files in the source directory, then checks the category in where the extemsion matches and sent the file to the respective folder
for file in files_to_organize:
    match file:
        case file if file.endswith(img_extensions):
            shutil.move(path.join(source_dir, file), path.join(img_dir, file))
            print(f'El archivo {file} se ha movido a {img_dir}')
            
        case file if file.endswith(music_extensions):
            shutil.move(path.join(source_dir, file), path.join(music_dir, file))
            print(f'El archivo {file} se ha movido a {music_dir}')
            
        case file if file.endswith(video_extensions):
            shutil.move(path.join(source_dir, file), path.join(videos_dir, file))
            print(f'El archivo {file} se ha movido a {videos_dir}')
    
        
