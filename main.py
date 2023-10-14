# UI file

from simplegmail import Gmail
from gaussian import get_score
from email_class import Email
from simplegmail.query import construct_query
import customtkinter as ctk
from tkinter.constants import*


#initialization
gmail = Gmail()


# UI
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.geometry("800x500")
root.title("scribo")
root.resizable(False, False)

currently_open = []

class EmailUI:
    summary = ""


    def get_summary():
        pass

    def __init__(self, master, email_text, email_obj, row_index, importance):
        master.label = ctk.CTkButton(master=master, text= email_text, command= lambda: display_email(email_obj), width=550, height=20)
        master.label.grid(row=row_index, column=0, padx=0)

def display_email(email):
    
    n = ctk.CTkLabel(master=frame, text=email.plain, font=('Verdana', 7))
    print(email.plain)
    n.pack()
    for x in currently_open:
        x.destroy()


def classify_email(email):
    pass

def show_emails(msgs):
    print("opened email")
    
    email_scroll = ctk.CTkScrollableFrame(master=frame, width=550, height=400)
    email_scroll.pack()
    email_scroll.place(relx=0.27, rely=0.1)
    currently_open.append(email_scroll)

    count = 0
    for i in range(0, 20 * len(msgs), 20):
        t = get_score(Email(msgs[count]))
        text = msgs[count].subject
        if len(text) > 65:
            t += text[0:65] + "..."
        else:
            t += text
        EmailUI(email_scroll, t, msgs[count], i, 1)
        if count <= len(msgs) - 2:
            count += 1




# grabbing recent unread emails to display
query_params = {
    "newer_than": (14, "day"),
    "unread": True,
}
messages = gmail.get_messages(query=construct_query(query_params))





frame = ctk.CTkFrame(master=root)
frame.pack(fill="both", expand=True)

label = ctk.CTkLabel(master=frame, text="Demo version", font=('Verdana', 20))
label.pack(pady=12, padx=10)
label.place(relx=0.05, rely=0.1)

button = ctk.CTkButton(master=frame, text="Open", command= lambda: show_emails(messages))
button.pack(pady=12, padx=10)
button.place(relx=0.05, rely=0.2)





root.mainloop()