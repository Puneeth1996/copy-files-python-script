import os
import shutil


folder1 =  'C:\\Users\\PUNEETH\\Desktop\\copy files python script\\folder1\\'
folder2 = 'C:\\Users\\PUNEETH\\Desktop\\copy files python script\\folder2\\'
print(os.listdir(folder1),os.listdir(folder2))
for files in os.listdir(folder1):
    try:
        dir1 = folder1 + files + '\\'
        print(dir1)
        for f in os.listdir(dir1):
            print(dir1+f,end='\n\n')
            # .copy2 method helps in copying from folder1 to folder2 
            shutil.copy2(dir1+f, folder2 + f)
            # print(folder1 + files, folder2 + files)
            
            # .move method helps in cutting from folder1 to folder2 
            # shutil.move(folder1 + files, folder2 + files)
    
    except:
        pass