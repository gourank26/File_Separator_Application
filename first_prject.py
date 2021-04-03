import os, shutil
extension_dict={
    'Audio_file' : ('.mp3','.m4a','.wav','.flac','.MP3'),
    'Video_file' : ('.mp4','.mkv','.MKV','.flv','.mpeg','.AVI','.3gp'),
    'Document_file' : ('.doc','.pdf','.txt','.THM'),
    'Image_file' : ('.jpg','.png','.JPG')
}
folderpath=input('Enter folder path: ')

def file_finder(folder_path,file_extension):
    return [file for file in os.listdir(folder_path) for extension in file_extension if file.endswith(extension)]

for extension_keys,extension_values in extension_dict.items():
    newfolder=extension_keys.split('_')[0] + 'Files'
    newfolder_path=os.path.join(folderpath,newfolder)
    for item in os.listdir(folderpath):
        if newfolder in os.listdir(folderpath):
            pass
        elif item.endswith(extension_values):
            os.mkdir(newfolder_path)
            for item in file_finder(folderpath,extension_values):
                item_path=os.path.join(folderpath,item)
                item_new_path=os.path.join(newfolder_path,item)
                shutil.move(item_path,item_new_path)