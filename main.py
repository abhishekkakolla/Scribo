# UI file

print("importing libraries")

import time
from simplegmail import Gmail
from gaussian import get_score
from email_class import Email
from simplegmail.query import construct_query
import customtkinter as ctk
from tkinter.constants import*

from gemini import display_ai_summary, show_viewbtn



# initialization
gmail = Gmail()

print("initializing UI")


# UI
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.geometry("800x500")
root.title("scribo")
root.resizable(False, False)

currently_open = []
currently_hidden = []


# components
# create them initially so it doesn't have to recreate all the time (which is slower)
frame = ctk.CTkFrame(master=root)
email_scroll = ctk.CTkScrollableFrame(master=frame, width=550, height=400)
email_text_frame = ctk.CTkScrollableFrame(master=frame, width=550, height=400)

title_frame = ctk.CTkLabel(master=email_text_frame, text="Dummy text", font=('Calibri', 25, 'bold'), wraplength=550, pady=5)
n = ctk.CTkLabel(master=email_text_frame, text="", font=('Calibri', 16), wraplength=550, pady=10) # email body
sender_frame = ctk.CTkLabel(master=email_text_frame, text="Dummy text", font=('Calibri', 18, "italic"), wraplength=550)

viewbtn = ctk.CTkButton(master=email_text_frame, text="View")
# currently_open.append(viewbtn)

class EmailUI:
    summary = ""
    

    def get_summary():
        pass

    def __init__(self, master, email_text, email_obj, row_index):
        # frame to house preview button + mark read button
        previewframe = ctk.CTkFrame(master=master, width=550, height=40)
        master.label = previewframe

        # preview email button
        previewframe.label = ctk.CTkButton(master=previewframe, text= email_text, command= lambda: display_email(email_obj), width=500, height=30, fg_color='#5A5A5A', hover_color='#2FA572')
        previewframe.label.grid(row=row_index, column=0, padx=5, pady=0)

        # mark as read button
        read_button = ctk.CTkButton(master=previewframe, text="✔️", command= lambda : mark_read(email_obj, read_button), width=15, height=30)
        previewframe.read_button = read_button
        previewframe.read_button.grid(row=row_index, column=1, padx=5, pady=0)
        master.label.grid(row=row_index, column=0, padx=0, pady=5)
        

def mark_read(email_obj, button):
    print("marking as read: " + str (email_obj.subject))
    email_obj.mark_read_function()
    button.configure(fg_color="grey", state="disabled")




def display_email(email):
    print("currently open: ")
    print(currently_open)
    print("displaying clicked email")

    # close currently opened components
    for x in currently_open:
        print("closing " + str(x))
        x.place_forget()
        currently_open.remove(x)
        currently_hidden.append(x)


    # entire scrollable frame
    email_text_frame.pack()
    email_text_frame.place(relx=0.27, rely=0.1)

    
    
    title_frame.pack()
    title_frame.configure(text=email.subject)
    title_frame.update_idletasks()
    
    sender_frame.pack()
    sender_frame.configure(text=email.sender)
    sender_frame.update_idletasks()
    
    # Gemini AI's response which is streamed
    n.pack()
    n.update_idletasks()
    
    root.after(10, lambda : display_ai_summary(email, n, viewbtn))
    # display_ai_summary(email, n)

    # # display the view button -> allows user to view entire email in browser
    # viewbtn.pack()
    # viewbtn.pack(pady=12, padx=10)
    # viewbtn.place(relx=0.05, rely=0.4)
    # viewbtn.configure(command= lambda : view_email_browser(email))

   
    
    currently_open.append(email_text_frame)
    currently_open.append(viewbtn)
    




def show_emails(msgs):
    print("showing email list")
    
    email_scroll.pack()
    email_scroll.place(relx=0.27, rely=0.1)
    currently_open.append(email_scroll)
    
    count = 0 # index in the all messages list
    for i in range(0, 20 * len(msgs), 20):
        email_obj = Email(msgs[count])
        t = get_score(email_obj)
        email_obj.importance = t
        text = msgs[count].subject
        if len(text) > 65:
            t += text[0:65] + "..."
        else:
            t += text
        EmailUI(email_scroll, t, email_obj, i) # UI: parent, t = importance, object, i = position
        count += 1
        # if count <= len(msgs) - 2:
        #     count += 1

        
    print("printed email list")

def reopen_emails():

    # close the currently open email by resetting body to empty text
    # also remove the view button
    n.configure(text="")
    root.update_idletasks()

    print("reopening email list")
    print(currently_open)
    

    print('closing')
    for x in currently_open:
        print("closing" + str(x))
        x.place_forget()
        currently_open.remove(x)
    print(len(currently_open))
    print(currently_open)


    # reopen the email list
    for x in currently_hidden:
        x.pack()
        x.place(relx=0.27, rely=0.1)
        currently_hidden.remove(x)



# grabbing recent unread emails to display
query_params = {
    "newer_than": (1, "day"),
    "unread": True,
}
print("getting emails from gmail API")
messages = gmail.get_messages(query=construct_query(query_params))





frame.pack(fill="both", expand=True)

label = ctk.CTkLabel(master=frame, text="Demo version", font=('Verdana', 20))
label.pack(pady=12, padx=10)
label.place(relx=0.05, rely=0.1)

button = ctk.CTkButton(master=frame, text="Open", command= lambda: show_emails(messages))
button.pack(pady=12, padx=10)
button.place(relx=0.05, rely=0.2)

backbtn = ctk.CTkButton(master=frame, text="Back", command= lambda: reopen_emails())
backbtn.pack(pady=12, padx=10)
backbtn.place(relx=0.05, rely=0.3)








root.mainloop()