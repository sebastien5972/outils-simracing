from PIL import Image
import tkinter as tk
from tkinter import filedialog



 
root = tk.Tk()
root.withdraw()

file_path = str(filedialog.askopenfilenames())
print('le file path est: ' + file_path)
list_fichiers = []
list_fichiers.append(file_path)
print(list_fichiers )


i = 0
for name_dds in (list_fichiers):
    print(name_dds)
    print ('le premier dans la liste est: ' + name_dds[i])
    print(i)
    i += 1
    print(i)
print(list_fichiers[0], list_fichiers[1])
"""def redimensionner (name_dds[i]):

    file_save_directory = filedialog.askdirectory()
    print(file_save_directory)
    
    img = Image.open(file_path)

    img_1024 = img.resize((2048, 1152))
    img_1024.save(file_save_directory + '/' + name_dds + ('-icon-2048x1152.png'))

    img_1024 = img.resize((1024, 576))
    img_1024.save(file_save_directory + '/' + name_dds + ('-icon-1024x576.png'))

    img_512 = img.resize((512, 288))
    img_512.save(file_save_directory + '/' + name_dds + ('-icon-512x288.png'))

    img_256 = img.resize((256, 144))
    img_256.save(file_save_directory + '/' + name_dds + ('-icon-256x144.png'))

    img_128 = img.resize((128, 72))
    img_128.save(file_save_directory + '/' + name_dds + ('-icon-128x72.png'))"""


redimensionner()