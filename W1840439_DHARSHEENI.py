#importing different types of libraries
from tkinter import *
import tkinter as tk
from tkinter import ttk#the latest version of tkinter with more added feautures
from tkinter import messagebox#has diff types of interactive popups
from PIL import ImageTk,Image#pillow allows images to be displayed/viewed
from tkinter.filedialog import askopenfilename#allow functions for group of files directories
import os#operating system
import shutil#allow operations like copy and remove to be carried out to a set/group of files

#creating a basic window and assigning the size,name,bg colour,and to resize/adjust the frame
dk_Win = Tk()#window
dk_Win.title("My Friends Gallery")#title
dk_Win.geometry("800x800")#window size
dk_Win.configure(background = "green")#background colour of the window
dk_Win.resizable("true", "true")#the window can be readjusted both sides and top hence true,true

# variables to refer
folder = ("img/")#assign variable locating the folder img from desktop

#defining the commands for myButton1
def show():
    column = 1#variable
    row = 2#variable
    for file in os.listdir(folder):#for loop method to present the images using list directories from folder
        default = ("img/" + file )#stating how image format should be shown
        img = Image.open(default)#refer to default variable to open image
        img= img.resize((100, 100))#resizing image before defining library
        img = ImageTk.PhotoImage(img)#defining library
        imgLabel = ttk.Label(myLabel_2, image = img )# creating imageLabel attached to myLabel_2
        imgLabel.grid(column = column, row = row )#image layout refer to variables
        imgLabel.image = img#defining img should be present in the imageLabel
        if(column==3):#setting conditions to arrange the images three in a column
            row=row+2# fourth,seventh,tenth images now will apper in following row
            column=1
        else:
            column=column+1#defining if the images are >or equal three then it will appear in the same row but next column

#defining the commands for myButton2
def Clear():
    popup = tk.messagebox.askquestion ('# WARNING: ','Are you sure to clear?',icon = 'warning')#set variable to refer to and msgbox created with title,message and icon for appear
    #popup = yes
    if popup == 'yes':#if method use if the yes button clicked on messagebox
        for child in myLabel_2.winfo_children():#calling to the children widgets in parent widget myLabel_2
            child.destroy()#deleting all child widgets

#defining the commands for myButton4
def Add():
    filename= tk.filedialog.askopenfilename(initialdir ="img/", title="Choose a file")#setting variable for if method and opening list in initial directories
    if filename:
        user_input=messagebox.askquestion("Add a friend?",  "Are you sure to add a friend?")#creating msgbox for interactive response
        if user_input == "yes":#seting condition if yes clicked
            shutil.copy(filename,"./img")#image will be copied from shutil library used to add selection of files that ends with img
            show()#will show all images on def show with the image/s added
    else:#condition if no/cancelled
        messagebox.showinfo("No", "Image not selected")#message box will appear

#defining the command for myButton3
def Delete():
    from os import remove#importing remove function from operating system
    filename= tk.filedialog.askopenfilename(initialdir ="img/", title="Choose a file")#variable filename is assigned and  a folder from initial directories will appear to choose
    if filename:#setting condition if image chosen
        user_input=messagebox.askquestion("DELETE friend?",  "Are you sure to remove friend?")#variable user input defined and popup msgbox appear for interactive response
        if user_input == "yes":#a condition within a condition and if yes button clicked
            os.remove(filename)#the seleceted image removed from filename
            Clear()#clearing the cache before rendering the images,function clear recalled
            show()#should show images after rendered,function show recalled
        else:
            messagebox.showinfo("No", "Nothing is removed")#msgbox appear if no or cancelled


    #defining the command for myButton5
def Quit():
    prompt= messagebox.askquestion("confirm","Are you sure to quit?")#creating variable and msgbox to appear for interactive response
    if prompt == "yes":#condition if yes clicked
        dk_Win.destroy()#window will be closed
    else:
        messagebox.showinfo("Information","Continue")#condition if no is clicked then msgbox apper to show info

#setting style
design = ttk.Style()#setting variabe and assigning style
design.theme_use('alt')#setting new theme style
design.configure('TLabel', background = 'yellow', foreground = 'black',
borderwidth=5,  width =10, height = 30, relief = RAISED, font=('Calibri', 18))#setting themes,font type,dimension, and font size for label,T represent for style
design.configure('TButton', background = 'lightgreen', foreground = 'purple', width = 20, borderwidth=2, focusthickness=5, focuscolor='black')
design.map('TButton', background=[('active','yellow')])#setting themes,font type,dimension, and font size for button,T represent for style

#Labelframes are created which will be displayed to main window dk_Win
myLabel = ttk.LabelFrame(dk_Win, text = "Action panel", height = 30, width = 700)# (comment1)creating,attaching the location and assigning the size and the tile of the label
myLabel.grid(row=0, column =0, padx=10, sticky = "NW")#(comment2)displaying using grid method

myLabel_2 = ttk.LabelFrame(dk_Win, text= "Friends Gallery", height = 100, width = 600)# similar procedures to (comment1)
myLabel_2.grid(row =2, column = 0, padx =10, pady = 10 , sticky = "NW")# similar procedures to (comment2)


#Buttons are created which will be shown in the LabelFrame/required location if mentioned
myButton1 = ttk.Button(myLabel, text = "Showpictures",width = 15, command = show )#(comment3)assigning size,name and location of the btn and calling specific function to work when button is clicked.
myButton1.grid (row =1 , column = 1)#button will be diplayed using grid method
myButton2 = ttk.Button(myLabel, text = "ClearGallery",width = 15,command=Clear)# similar procedures to (comment3)
myButton2.grid (row =1 , column = 2)#button will be diplayed using grid method
myButton3 = ttk.Button(myLabel, text = "Delete a Friend",width = 15, command= Delete)# similar procedures to (comment3)
myButton3.grid (row =1 , column = 3)#button will be diplayed using grid method
myButton4 = ttk.Button(myLabel, text = "Add New Friend",width = 15, command=Add)# similar procedures to (comment3)
myButton4.grid (row =1 , column = 4)#button will be diplayed using grid method
myButton5 = ttk.Button(myLabel, text = "Quit",width = 15, command= Quit)
myButton5.grid (row =1 , column = 5)#button will be diplayed using grid method


#this will keep the window active and ready to take any commands or events until the window is shut
dk_Win.mainloop()
