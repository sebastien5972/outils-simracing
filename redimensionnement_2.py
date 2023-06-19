from PIL import Image
import tkinter as tk
from tkinter import filedialog
from pathlib import Path


 
root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilenames(title='choisi les fichiers à redimensionner')
list_fichiers_png = root.tk.splitlist(file_path)
print(list_fichiers_png)
print(list_fichiers_png[0])
print(list_fichiers_png[1])

file_save_directory = filedialog.askdirectory()
print(file_save_directory)

for i in (list_fichiers_png):

    #p = Path(i)
    #extensions = "".join(p.suffixes)
    #nom_dds = str(i).removesuffix(extensions) 
    nom_dds_1 = i[88:]
    print(nom_dds_1)
    p = Path(nom_dds_1)
    extensions = "".join(p.suffixes)
    nom_dds = str(nom_dds_1).removesuffix(extensions)

    img = Image.open(i)

    img_2048 = img.resize((2048, 1152))
    img_2048.save(file_save_directory + nom_dds + ('-icon-2048x1152.png'))

    img_1024 = img.resize((1024, 576))
    img_1024.save(file_save_directory + nom_dds + ('-icon-1024x576.png'))

    img_512 = img.resize((512, 288))
    img_512.save(file_save_directory + nom_dds + ('-icon-512x288.png'))

    img_256 = img.resize((256, 144))
    img_256.save(file_save_directory + nom_dds  + ('-icon-256x144.png'))

    img_128 = img.resize((128, 72))
    img_128.save(file_save_directory + nom_dds + ('-icon-128x72.png')) 