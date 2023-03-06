import os
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import numpy as np
import cv2
import sys

# import the Haarcascade classifier
face_cascade = cv2.CascadeClassifier( 'work\GuiSrc\haarcascade_signs.xml' )

# initialize the GUI
root = tk.Tk()
root.title("Sign Detection")
root.geometry("800x700")
root.minsize(width=500, height=500)
root.configure(background='dark grey')
root.option_add("*Font", "Helvetica 20")
root.option_add("*Button.Relief", "flat")
root.option_add("*Button.Background", "grey")
root.option_add("*Button.ActiveBackground", "white")
root.option_add("*Button.Foreground", "black")
root.option_add("*Button.ActiveForeground", "black")    
root.option_add("*Button.BorderWidth", "0")
root.resizable(False, False)

# function to open an image file and display it on the GUI
def open_image():
    path = filedialog.askopenfilename()
    image = cv2.imread(path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(image)
    image = ImageTk.PhotoImage(image)
    image_label.config(image=image)
    image_label.image = image
    detect_signs(path)

# error handling
if face_cascade.empty():
    print("Error: Unable to load the classifier")
    sys.exit(0)

# function to detect the signs in the image
def detect_signs(path):
    image = cv2.imread(path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    signs = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    for (x,y,w,h) in signs:
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(image)
    image = ImageTk.PhotoImage(image)
    image_label.config(image=image)
    image_label.image = image
    
# button to open an image file
open_button = tk.Button(root, text="Open Image", command=open_image)
open_button.pack()

# label to display the selected image
image_label = tk.Label(root)
image_label.pack()

# create console log.txt file
sys.stdout = open("work\GuiSrc\log.txt", "w")

root.mainloop()
