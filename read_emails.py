from simplegmail import Gmail
from simplegmail.query import construct_query
import numpy

#initialization
gmail = Gmail()

# variables
training_data = []


# classes
class Email:
    importance = 0
    email_sender_length = 0
    time_sent = 0
    attachments = 0
    subject = ""
    subject_length = 0
    body_length = 0
    num_verbs = 0
    
    def __init__(self, msg):
        self.importance = 0
        self.email_sender_length = len(msg.sender)
        self.time_sent = int(msg.date[msg.date.find(" "): msg.date.find(":")])
        self.attachments = msg.attachments
        self.subject = msg.subject
        self.subject_length = len(msg.subject)
        if msg.plain:
            self.body_length = len(msg.plain)
        self.num_verbs = 0

# creating Email objects
query_params = {
    "newer_than": (1, "day"),
}
messages = gmail.get_messages(query=construct_query(query_params))
for msg in messages:
    training_data.append(Email(msg))

for x in training_data:
    print(x.subject)
    print(x.body_length)
    print(" ")


# # writing data to file
# with open("data\\email_data.txt", "a", encoding="utf-8") as doc:
#     for msg in messages:
#         if msg.plain:
            
            
            

