from PIL import Image
import tkinter as tk
from tkinter import filedialog



 
root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
print(file_path )



def redimensionner ():

    file_save_directory = filedialog.askdirectory()
    print(file_save_directory)
     
    img = Image.open(file_path)

    img_1024 = img.resize((1024, 576))
    img_1024.save(file_save_directory + ('/_1024x576.png'))

    img_512 = img.resize((512, 288))
    img_512.save(file_save_directory + ('/_512x288.png'))

    img_256 = img.resize((256, 144))
    img_256.save(file_save_directory + ('/_256x144.png'))

    img_128 = img.resize((128, 72))
    img_128.save(file_save_directory + ('/_128x72.png'))


redimensionner()
