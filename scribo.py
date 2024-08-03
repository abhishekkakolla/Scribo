# UI file

# print("importing libraries")



from simplegmail import Gmail
import customtkinter as ctk

from tkinter.constants import*






# initialization

# print("initializing UI")


root = ctk.CTk()
def dark_mode(swap=True):
    from darkmode import get_current_mode, set_mode
    # file = open("./data/dark.npy", "r+")
    text = get_current_mode()
    if (swap == True):
        if (text == "dark"):
            text = "light"
        else:
            text = "dark"
    if (text == "dark"):
        ctk.set_appearance_mode("light")
        root.iconbitmap('scribo.ico')
        set_mode('light')
    elif (text == "light"):
        ctk.set_appearance_mode("dark")
        root.iconbitmap('scribo-white.ico')
        set_mode('dark')
    else:
        raise Exception("Error reading dark mode file")

        


# UI
dark_mode()
ctk.set_default_color_theme("green")

root.geometry("800x500")
root.title("Scribo")
root.resizable(False, False)

currently_open = []
currently_hidden = []

from email_class import Email

# components
# create them initially so it doesn't have to recreate all the time (which is slower)
frame = ctk.CTkFrame(master=root)
email_scroll = ctk.CTkScrollableFrame(master=frame, width=550, height=400)
email_text_frame = ctk.CTkScrollableFrame(master=frame, width=550, height=400)

title_frame = ctk.CTkLabel(master=email_text_frame, text="Dummy text", font=('Calibri', 25, 'bold'), wraplength=550, pady=5)
n = ctk.CTkLabel(master=email_text_frame, text="", font=('Helvetica', 17), wraplength=550, pady=10) # email body
sender_frame = ctk.CTkLabel(master=email_text_frame, text="Dummy text", font=('Calibri', 18, "italic"), wraplength=550)

viewbtn = ctk.CTkButton(master=email_text_frame, text="View", font=('Verdana', 20))
todobtn = ctk.CTkButton(master=email_text_frame, text="Generate To-Do", font=('Verdana', 20))

todo_frame = ctk.CTkTextbox(master=n, width=450, height=300, font=('Verdana', 20))



class EmailUI:
    summary = ""
    

    def get_summary():
        pass

    def __init__(self, master, email_text, email_obj, row_index):
        # frame to house preview button + mark read button
        previewframe = ctk.CTkFrame(master=master, width=550, height=40)
        master.label = previewframe

        # preview email button
        previewframe.label = ctk.CTkButton(master=previewframe, text= email_text, font=('Verdana', 13), command= lambda: display_email(email_obj), width=500, height=30, fg_color='#5A5A5A', hover_color='#2FA572')
        previewframe.label.grid(row=row_index, column=0, padx=5, pady=0)

        # mark as read button
        read_button = ctk.CTkButton(master=previewframe, text="✔️", command= lambda : mark_read(email_obj, read_button), width=15, height=30)
        previewframe.read_button = read_button
        previewframe.read_button.grid(row=row_index, column=1, padx=5, pady=0)
        master.label.grid(row=row_index, column=0, padx=0, pady=5)
        

def mark_read(email_obj, button):
    # print("marking as read: " + str (email_obj.subject))
    email_obj.mark_read_function()
    button.configure(fg_color="grey", state="disabled")



def display_email(email):
    from gemini import display_ai_summary
    from gemini import get_sender_details
    

    # print("DISPLAY_EMAIL()")

    # close currently opened components
    
    # print("-----Showing what is open: ")
    count = 0
    for x in currently_open:
        # print(str(count) + ": " + str(x))
        
        x.place_forget()
        x.update_idletasks()
        currently_open.remove(x)
        currently_hidden.append(x)

    
    

    # entire scrollable frame
    email_text_frame.pack()
    email_text_frame.place(relx=0.27, rely=0.1)

    
    
    title_frame.pack()
    title_frame.configure(text=email.subject)
    title_frame.update_idletasks()
    
    sender_frame.pack()
    simplified_text = get_sender_details(email.sender, email.date)
    sender_frame.configure(text=simplified_text)
    sender_frame.update_idletasks()
    
    # Gemini AI's response which is streamed
    n.pack()
    n.update_idletasks()
    
    root.after(1000, lambda : display_ai_summary(email, n, viewbtn, todobtn, todo_frame, currently_open, email_text_frame))

    currently_open.append(email_text_frame)

   

def show_emails():
    from gaussian import get_score
    from simplegmail.query import construct_query
    # print("SHOW_EMAILS()")
    gmail = Gmail()
    query_params = {
        "newer_than": (12, "day"),
        "unread": True,
    }
    # print("getting emails from gmail API")
    msgs = gmail.get_messages(query=construct_query(query_params))
    # print('len of msgs: ' + str(len(msgs)))

    # print(msgs)
    # print("showing email list")
    # print('len of currently open is ' + str(len(currently_open)))
    # if (len(currently_open) == 0):      
    if True:  
        button.configure(text='Reload')

        for child in email_scroll.winfo_children():
            child.destroy()

        # if email_scroll.winfo_ismapped():
            # email_scroll.destroy()
            # email_scroll.place_forget()
            # print('hi')
        # email_scroll = ctk.CTkScrollableFrame(master=frame, width=550, height=400)

        email_scroll.pack()
        email_scroll.place(relx=0.27, rely=0.1)
        currently_open.append(email_scroll)

        
        
        count = 0 # index in the all messages list
        # print("IN FOR LOOP GOING TO DISPLAY:")

        for i in range(0, 20 * len(msgs), 20):
            email_obj = Email(msgs[count])
            t = get_score(email_obj)
            email_obj.importance = t    
            text = msgs[count].subject
            # print("0: " + text)
            if len(text) > 65:
                t += text[0:65] + "..."
            else:
                t += text
            EmailUI(email_scroll, t, email_obj, i) # UI: parent, t = imprtance, object, i = position
            count += 1
            # if count <= len(msgs) - 2:
            #     count += 1

            
        # print("printed email list")



def reopen_emails():
    
    # print("REOPEN_EMAILS()")
    
    # close the currently open email by resetting body to empty text
    # also remove the buttons (by placing them off screen) and the to do frame as well
    n.configure(text="")
    root.update_idletasks()

    todo_frame.delete(1.0, ctk.END)
    todo_frame.place(relx=-100, rely=-100)
    todobtn.place(relx=-100, rely=-100)
    viewbtn.place(relx=-100, rely=-100)

    


    # print('-----Showing what is currently open and will be closed:')
    count = 0
    
    for x in currently_open:
        # print(str(count) + ": " + str(x))
        x.update_idletasks()
        x.place_forget()
        currently_open.remove(x)


    # reopen the email list
    # print('-----Showing what is currently CLOSED and will be opened: ')
    count = 0
    for x in currently_hidden:
        # print(str(count) + ": " + str(x))
        x.pack()
        x.place(relx=0.27, rely=0.1)
        currently_hidden.remove(x)



frame.pack(fill="both", expand=True)

label = ctk.CTkLabel(master=frame, text="Scribo", font=('Helvetica', 35, 'bold'))
label.pack(pady=12, padx=10)
label.place(relx=0.05, rely=0.1)

button = ctk.CTkButton(master=frame, text="Open", font=('Verdana', 20), command= lambda: show_emails())
button.pack(pady=12, padx=10)
button.place(relx=0.05, rely=0.2)

backbtn = ctk.CTkButton(master=frame, text="Back", font=('Verdana', 20), command= lambda: reopen_emails())
backbtn.pack(pady=12, padx=10)
backbtn.place(relx=0.05, rely=0.3)

darkbtn = ctk.CTkButton(master=frame, width=30, height=30, text="🌔",  hover_color='#000000', command = lambda : dark_mode(False))
darkbtn.pack(pady=5, padx=5)
darkbtn.place(relx=0.05, rely=0.4)


root.mainloop()

