"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import time
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

prompt_parts = [
  "input: The subject, then the body contents of an email, which may include irrelevant information such as links and footer notes.",
  "output: The first line should be a one sentence summary of the whole email. In bullet points on the next few lines, output the most important summarized points and omit irrelevant information (which means don't include long links). Only output this format for the given input, never on past data.",
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

def display_ai_summary(email, ctk_label):
  print("Subj: " + email.subject)

  total_input = 'input: Subject: ' + email.subject + '\nBody: ' + email.body
  prompt_parts.append(total_input)
  prompt_parts.append('output: ')
  response = model.generate_content(prompt_parts, stream=True)
  all_text = ""
  for chunk in response:
    print(chunk.text)
    time.sleep(0.1)
    
    all_text += chunk.text
    ctk_label.configure(text=all_text)
    ctk_label.update_idletasks()
    # frame = ctk.CTkLabel(master=body_frame, text=email.body, font=('Calibri', 16), wraplength=550)
  prompt_parts.append("output: " + response.text)



# print('enter subject: ')
# str = input()
# print('enter body: ')
# body = input()
# total_input = 'Subject: ' + str + '\nBody: ' + body
# prompt_parts.append(total_input)


# response = model.generate_content(prompt_parts, stream=True)
# # print(response.text)

# for chunk in response:
#   print(chunk.text)