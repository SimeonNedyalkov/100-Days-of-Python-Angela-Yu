import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog
import glob, os

# Window
window=tk.Tk()
window.geometry("1100x1024")
window.title("Image Loader")


# Image
def openfilename():
    filename = filedialog.askopenfilename(title ='"pen')
    return filename

class CanvasImage():
    def __init__(self):
        x = openfilename()
        self.img = Image.open(x)
        self.image = ImageTk.PhotoImage(image=self.img)

def open_image():

    #x = openfilename()
    image = CanvasImage()
    canvas = tk.Canvas(window, width=200, height=200)
    canvas.grid(pady=100, padx=130)
    canvas.create_image(100, 100, image=image.image)


#Screen
label=tk.Label(text="This is the first GUI watermark I've made", font=('Aerial, 26')).grid(pady=0, padx=250)
button=tk.Button(text='Select image', command=open_image).grid(pady=400,padx=430)

window.mainloop()
