"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import google.generativeai as genai
import customtkinter as ctk



filename = "data\\gemini_api.config"
contents = open(filename).read()
config = eval(contents)
key = config['key']

genai.configure(api_key=key)

# Set up the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.5-flash-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)


# prompts for SUMMARY model
prompt_parts = [
  "input: The subject, then the body contents of an email, which may include irrelevant information such as links and footer notes. Ignore anything about unsubscribing to messages, and never include long links.",
  "output: The first line should be a one sentence summary of the whole email. In bullet points on the next few lines, output the most important summarized points and omit irrelevant information (which means don't include long links). Only output this format for the given input, never on past data. Also, try to see if it is an auto-generated message, or if it is by a real person.",
  "input: Subject: Your transaction history for April 2024 is now available.\nBody: View history on Venmo.comVenmo sends this notification periodically to help you stay on top of your account activity.As required by law, we are providing you with this notification of your transaction history. Learn more.Venmo is a service of PayPal, Inc., a licensed provider of money transfer services. All money transmission is provided by PayPal, Inc. pursuant to PayPal, Inc.’s licenses.PayPal is located at 2211 North First Street, San Jose, CA 95131Please do not reply directly to this email as you will not receive a response. For assistance, please visit our Help Center.",
  "output: This email informs you that your Venmo transaction history for April 2024 is now available.\n\n- Your transaction history for April 2024 is available on Venmo.com.\n- Venmo sends this notification periodically to help you stay on top of your account activity.\n- For assistance, please visit the Venmo Help Center.",
  "input: Subject: Yakirelbaz IT Solutions is hiring for Data Entry Clerk + 13 new Office Clerk jobs in Ajax, ON\n\nBody:\nHi Abhishek,​​​​​​​The following new job opportunities matching your Talent Community profile have been posted.Technology AND Ajax, Canada JobsBilingual Business AnalystMontreal, QuebecApply NowSpecialist, Radio EngineeringToronto, OntarioApply NowSenior DevOps EngineerMontreal, QuebecApply NowSenior Advisor, Radio EngineeringToronto, OntarioApply NowSenior Architecture, Cyber SecurityMontreal, QuebecApply NowBest regards,Bell Talent Acquisition TeamReplies to this email are undeliverable.Connect with usPrivacy | Copyright © 2024, Bell Canada. All Rights Reserved.​​​​​​​​​​​​​​To ensure delivery to your inbox, please add opportunities-opportunites@jobalerts.bell.ca to your address book.​​​​​​​You can unsubscribe here and stop receiving these job alert emails.",
  "output: This email notifies you about new job opportunities that match your profile on Bell's Talent Community.\n\n- The following job opportunities are available:\n    - Bilingual Business Analyst in Montreal, Quebec\n    - Specialist, Radio Engineering in Toronto, Ontario\n    - Senior DevOps Engineer in Montreal, Quebec\n    - Senior Advisor, Radio Engineering in Toronto, Ontario\n    - Senior Architecture, Cyber Security in Montreal, Quebec\n- You can unsubscribe from these job alerts.",
  "input: Hi,Thank you for the help, I have received the email. I submitted the prerequisite form and I was just wondering: when the form gets cleared, will the \"Prerequisite and Test Score error\" automatically disappear in the portal where I have to register for classes? Thanks.",
  "output: This email is a follow-up to a previous request for help and asks when a prerequisite form is cleared, will the error message automatically disappear.\n\n- The sender has submitted the prerequisite form.\n- The sender wants to know if the \"Prerequisite and Test Score error\" will disappear once the form is cleared.",
  "input: Subject: I want to connect\nBody: Drew S Senior iOS Developer @ Bally's Interactive |…Greater Vancouver Metropolitan Area  nnections in commonAcceptView profileMore people you may knowSariha DewanHuman Biology at the University of Toronto | Research Student @ UHNView profileYashas MehtaIB Student at White Oaks Secondary SchoolView profileAli QureshiAttended University of TorontoView profileEric MaoUPenn M&T (CS + Wharton)View profileGet the new LinkedIn desktop appAlso available on mobile",
  "output: This email expresses the sender's desire to connect with the recipient.\n\n- The sender is Drew S, a Senior iOS Developer at Bally's Interactive.\n- The sender has provided a list of connections in common. \n- The sender suggests the recipient view their profile.",
  "input: Subject: Take a quick survey to earn MSI Reward points!\nbody:  Dear Customer,Thank you for reaching out to us via web ticket 1071439.In order to improve our service and better meet your expectations, we sincerely invite you to take this 1 minute survey.You’ll receive 25 reward points the first time you participated in this customer satisfaction survey.Begin SurveyYour time and feedback will be greatly appreciated.MSI Service TeamPlease do not reply to this email directly as it was issued by the system automatically.Submit and track support tickets on the go!",
  "output: This email invites you to take a one-minute survey to earn MSI Reward points.\n\n- You will receive 25 reward points the first time you participate in the survey.\n- The survey is designed to improve MSI's service and better meet customer expectations.",
  # "input: ",
  # "output: ",
]

# prompts for to-do model
prompt_parts_todo = [
  "input: The subject, then the body contents of an email, which may include irrelevant information such as links and footer notes.",
  "output: In around 1-3 bullet points, give a short to-do list on what the user should do based on what the email is saying. Essentially something you can copy and keep for later. Use language that is like a to-do: Don't use language determiners and don't use personal pronouns (like \"you\")",
  "input: Subject: Your Collision order information\nBody: Hi Abhishek,Thanks for your Collision 2024 ticket order! Here's your order reference number: FLP9FYXN We have attached the invoice for your order. If there is no attachment, don’t worry. You can always access your invoice via the ticket dashboard.To view your ticket details, and find your invoice and ticket reference, click on the ticket dashboard link below. You will use your ticket booking reference to log in to the Collision apps. Please be sure to assign all tickets in your order to someone as soon as possible.VIEW TICKET DASHBOARDAccessibility at CollisionCollision is committed to making our events accessible and welcoming for everyone. To request accessibility support for your time at Collision, please use our accessibility request form.If you have any questions, just hit reply.– Collision teamConnected Intelligence (Canada) Limited, 1055 West Hastings Street, Vancouver BC V6E 2E9, Canada.© 2024 CollisionTerms | Privacy",
  "output: Here's a to-do list based on the email:\n\n* **View ticket details and invoice:** Access your ticket dashboard at the provided link.\n* **Assign tickets:** Assign all tickets in your order to individuals as soon as possible.\n* **Request accessibility support:** If needed, use the accessibility request form provided in the email.",
  "input: Subject: RE: OISS CONTACT FORM \nBody: Hi Abhishek, Thank you for reaching out and your interest in attending Cerritos College! For F-1 international students who wish to apply to attend part-time, please visit https://www.cerritos.edu/international/Concurrent_Enrollment.htm for instructions on the application process and a list of documents to prepare. Please email all files as PDF files to intadmissions@cerritos.edu . Please don’t hesitate to reach out to us if you have any additional questions. With best regards, Jeanora Price, M.A.(Pronouns: She, Her, Hers)International Admission Specialist, Designated School Official (DSO)Office of International Student ServicesEmail: jprice@cerritos.eduPhone: 562-860-2451 ext. 2232Current Students: To schedule an appointment, please use the following link: https://cerritos.campus.eab.com/pal/yTPFevs3FT",
  "output: Here's a to-do list based on the email:\n\n* **Review part-time enrollment instructions:** Visit the provided link to learn about the application process and required documents.\n* **Email application files:** Send all files as PDFs to intadmissions@cerritos.edu.\n* **Contact for additional questions:** Reach out to Jeanora Price at jprice@cerritos.edu or 562-860-2451 ext. 2232.",
  "input: Subject: Package Notification at PKS CSC\nBody: You have received a package at the International Residential College (IRC) CSC. Please come pick it up with a photo ID at your earliest convenience.Tracking number: TBA308464650532Carrier: AmazonYou will receive one email per package we have received for you.IRC Customer Service Center3771 S. McClintock Ave Los Angeles, CA 90089University of Southern CaliforniaOffice: 213.740.1941| mailpks@usc.edu| housing.usc.eduFight On!",
  "output: Here's a to-do list based on the email:\n\n* **Pick up your package:** Visit the International Residential College (IRC) CSC with a photo ID to retrieve your package.\n* **Tracking number:** Use the provided tracking number TBA308464650532 to monitor your package's status.",
  "input: ",
  "output: ",
]



# Gemini summary
def display_ai_summary(email, ctk_label, viewbtn, todobtn, todo_frame, currently_open, email_text_frame):
  # print("Subj: " + email.subject)

  total_input = 'input: Subject: ' + email.subject + '\nBody: ' + email.body
  prompt_parts.append(total_input)
  prompt_parts.append('output: ')
  response = model.generate_content(prompt_parts, stream=True)
  all_text = ""
  for chunk in response:
    # print(all_text)
    
    all_text += chunk.text
    ctk_label.configure(text=all_text)
    ctk_label.update_idletasks()
    # frame = ctk.CTkLabel(master=body_frame, text=email.body, font=('Calibri', 16), wraplength=550)
  prompt_parts.append("output: " + response.text)
  show_viewbtn(email, viewbtn)
  show_todobtn(email, todobtn, todo_frame, currently_open)

  # only after the function has run append the components that have been added
  # currently_open.append(email_text_frame)
  # currently_open.append(viewbtn)
  # currently_open.append(todobtn)

  print("-----Showing what is open now: ")
  count = 0
  for x in currently_open:
    print(str(count) + ": " + str(x))


# Gemini to-do
def display_ai_todo(email, todo_frame, currently_open):
  # print("Subj: " + email.subject)

  todo_frame.grid()
  total_input = 'input: Subject: ' + email.subject + '\nBody: ' + email.body
  prompt_parts_todo.append(total_input)
  prompt_parts_todo.append('output: ')
  response = model.generate_content(prompt_parts_todo, stream=True)
  all_text = ""
  for chunk in response:
    # print(all_text)
    
    all_text += chunk.text
    todo_frame.delete(1.0, ctk.END)
    todo_frame.insert(1.0, all_text)
    # todo_frame.insert("0.0", all_text)
    todo_frame.update_idletasks()
    # todo_frame.configure(state='disabled')  # disable it so user can't change it
    # frame = ctk.CTkLabel(master=body_frame, text=email.body, font=('Calibri', 16), wraplength=550)
  prompt_parts_todo.append("output: " + response.text)
  # currently_open.append(todo_frame)

def helper(email, todo_frame, currently_open):
  display_ai_todo(email, todo_frame, currently_open)
  # todo_frame.after(1000, lambda : display_ai_todo(email, todo_frame, currently_open))



# display the view button -> allows user to view entire email in browser
def show_viewbtn(email, viewbtn):
  viewbtn.pack()
  viewbtn.pack(pady=12, padx=10)
  # viewbtn.place(relx=0.05, rely=0.4)
  viewbtn.configure(command= lambda : view_email_browser(email))

# display the to-do button -> generates to do
def show_todobtn(email, todobtn, todo_frame, currently_open):
  todobtn.pack()
  todobtn.pack(pady=12, padx=10)
  # viewbtn.place(relx=0.05, rely=0.4)
  todobtn.configure(command= lambda : helper(email, todo_frame, currently_open))


def view_email_browser(email):
  print("viewing in browser")
  message_id = email.id
  email_url = f"https://mail.google.com/mail/u/0/#inbox/{message_id}"
  import webbrowser
  webbrowser.open(email_url)

