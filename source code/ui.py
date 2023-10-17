import tkinter as tk
from tkinter import filedialog,Text,Label
import tkinter.font as tkFont
from PIL import ImageTk,Image
import numpy as np
import tensorflow as tf
from tensorflow import keras
import pygame






pygame.mixer.init()
new_model = tf.keras.models.load_model('C:/Users/ASUS/Desktop/LECTURE NOTES/sem 3/csc583/CSC583 PROJECT/saved_model/my_model')
pygame.mixer.music.load("Chill - Boom Bap Beat Prod.Senoda.mp3")
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.2)



batch_size = 32
img_height = 180
img_width = 180
class_names = ['ben_affleck', 'elton_john', 'jerry_seinfeld', 'madonna', 'mindy_kaling']
root = tk.Tk()
root.title('CELEBRITY FACIAL RECOGNITION!')
root.iconbitmap('icon.ico')
root.geometry("700x650")
filename ="null"
apps = []
def add_App():
    global filename
    filename = filedialog.askopenfilename(initialdir="/",title="Select File",
    filetypes= (("all files","*.*"),("exe","*.exe")))
    apps.append(filename)
    for app in apps:
        label = tk.Label(frame,text=app,bg="#90FFA1" ) 
        label.pack() 
    return filename  



def run_App():
    global filename
    img = keras.preprocessing.image.load_img(
    filename, target_size=(img_height, img_width))
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) # Create a batch
    predictions = new_model.predict(img_array)
    score = tf.nn.softmax(predictions[0])
    Output = (
    "This image most likely belongs to {} with a {:.2f} percent confidence."
    .format(class_names[np.argmax(score)], 100 * np.max(score)))
    labeloutput = tk.Label(frame,text=Output,bg="#90FFA1")
    labeloutput.pack()
    


canvas = tk.Canvas(root,height=900,width=1920,bg="#F8D65C")

canvas.pack()

frame =tk.Frame(root,bg="#FA7305")
frame.place(relwidth=0.4,relheight=0.83,relx=0.3,rely=0.005)



Celeb_Image =ImageTk.PhotoImage(Image.open('Untitled_Artwork.png'))

fontStyle = tkFont.Font(family="Comic Sans MS", weight = 'bold', size=20)
labeltitle = Label(frame,text="CELEBRITY FACIAL RECOGNITION" ,font= fontStyle,bg="red")
labeltitle.pack()

labelproject = Label(frame ,image=Celeb_Image)
labelproject.pack()

line = tk.Frame(frame, height=1, width=550, bg="grey80", relief='groove')
line.pack()

openFile = tk.Button(frame,text="Browse File",padx=10,pady=5,fg="white",bg="#263D42",  command=add_App  )
openFile.pack(pady=10)
RunApp = tk.Button(frame,text="Run",padx=10,pady=5,fg="white",bg="#263D42",  command=run_App  )
RunApp.pack()



root.mainloop()