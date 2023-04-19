# import Tkinter as tk
import customtkinter as ctk
from PIL import Image
import os
from threading import Thread

ctk.set_appearance_mode("system")  # default value

# Create Window
basic_window = ctk.CTk()

# Settings for Window
    # Set Window Size
basic_window.geometry("250x200")

    # Set Window Title
basic_window.title("Basic Window")

var = ctk.IntVar()
rav = ctk.IntVar()

# Creating/Settings Button
basic_button = ctk.CTkButton(master=basic_window, text="Launch Nuke", command=lambda: var.set(1))
basic_button.place(relx=0.5, rely=0.5, anchor="center")

basic_button.wait_variable(var)

basic_button.destroy()
basic_button2 = ctk.CTkButton(master=basic_window, text="Are you Sure?", command=lambda: rav.set(1))
basic_button2.place(relx=0.5, rely=0.5, anchor="center")

basic_button.wait_variable(rav)

basic_button2.destroy()

basic_window.config(bg="red")
boi = ctk.CTkLabel(master=basic_window, text="nuke launched")
boi.place(relx=0.5, rely=0.5, anchor="center")

def BANG():
    os.system("afplay " + "ohno.mp3")

t = Thread(target=BANG)

t.start()

basic_window.mainloop()
