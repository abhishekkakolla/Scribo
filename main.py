# UI file


import customtkinter as ctk
from tkinter.constants import*
import numpy as np

# Loading the data
file = open("data\\training_data.npy", "rb")
emails_array = np.load(file, allow_pickle=True)



ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.geometry("800x500")
root.title("scribo")
root.resizable(False, False)

# class EmailUI:

#     def __init__(self, email_object):



def show_email():
    print("opened email")
    
    email_scroll = ctk.CTkScrollableFrame(master=frame, width=550, height=400)
    email_scroll.pack()
    email_scroll.place(relx=0.27, rely=0.1)

    count = 0
    for i in range(0, 500, 20):
        t = emails_array[count].subject
        email_scroll.label = ctk.CTkLabel(master=email_scroll, text=t)
        email_scroll.label.grid(row=i, column=0, padx=20)
        if count <= len(emails_array) - 2:
            count += 1



frame = ctk.CTkFrame(master=root)
frame.pack(fill="both", expand=True)

label = ctk.CTkLabel(master=frame, text="Demo version", font=('Verdana', 20))
label.pack(pady=12, padx=10)
label.place(relx=0.05, rely=0.1)

button = ctk.CTkButton(master=frame, text="Open", command=show_email)
button.pack(pady=12, padx=10)
button.place(relx=0.05, rely=0.2)




root.mainloop()