from PIL import Image
import tkinter as tk
from tkinter import filedialog



 
root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
print(file_path )

def redimensionner ():

     
    img = Image.open(file_path)

    img_1024 = img.resize((1024, 576))
    img_1024.save('D:/sim racing/Rfactor 2/skins rfactor 2/skins rfactor/porsche cup 992/porsche 1/alt_P992CUP_1024x576.png')

    img_512 = img.resize((512, 288))
    img_512.save('D:/sim racing/Rfactor 2/skins rfactor 2/skins rfactor/porsche cup 992/porsche 1/alt_P992CUP_512x288.png')

    img_256 = img.resize((256, 144))
    img_256.save('D:/sim racing/Rfactor 2/skins rfactor 2/skins rfactor/porsche cup 992/porsche 1/alt_P992CUP_256x144.png')

    img_128 = img.resize((128, 72))
    img_128.save('D:/sim racing/Rfactor 2/skins rfactor 2/skins rfactor/porsche cup 992/porsche 1/alt_P992CUP_128x72.png')

#chercher_fichier()
redimensionner()
