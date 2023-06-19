from PIL import Image
import tkinter as tk
from tkinter import filedialog
from pathlib import Path
 
root = tk.Tk()
root.withdraw()

#nom_dds = input('tape le nom du fichier DDS: ')


file_path = filedialog.askopenfilename()
p = Path(file_path)
extensions = "".join(p.suffixes)
nom_dds = str(p).removesuffix(extensions)
print(nom_dds )


def redimensionner ():

    file_save_directory = filedialog.askdirectory()
    print(file_save_directory)
     
    img = Image.open(file_path)

    img_1024 = img.resize((2048, 1152))
    img_1024.save(nom_dds + ('-icon-2048x1152.png'))

    img_1024 = img.resize((1024, 576))
    img_1024.save(nom_dds + ('-icon-1024x576.png'))

    img_512 = img.resize((512, 288))
    img_512.save(nom_dds + ('-icon-512x288.png'))

    img_256 = img.resize((256, 144))
    img_256.save(nom_dds  + ('-icon-256x144.png'))

    img_128 = img.resize((128, 72))
    img_128.save(nom_dds + ('-icon-128x72.png'))


redimensionner()