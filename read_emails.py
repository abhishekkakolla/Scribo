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
    classified = False
    
    def __init__(self, msg):
        self.importance = 0
        self.email_sender_length = len(msg.sender)
        self.time_sent = int(msg.date[msg.date.find(" "): msg.date.find(":")])
        self.attachments = len(msg.attachments)
        self.subject = msg.subject
        self.subject_length = len(msg.subject)
        if msg.plain:
            self.body_length = len(msg.plain)

# grabbing all emails that fit these parameters
query_params = {
    "newer_than": (1, "day"),
}
messages = gmail.get_messages(query=construct_query(query_params))
# creating Email objects and adding to training data
for msg in messages:
    training_data.append(Email(msg))

# for x in training_data:
#     print(x.importance)
#     print(x.email_sender_length)
#     print(x.time_sent)
#     print(x.attachments)
#     print(x.subject)
#     print(x.subject_length)
#     print(x.num_verbs)
#     print(" ")

# # writing data to file
# with open("data\\email_data.txt", "a", encoding="utf-8") as doc:
#     for msg in messages:
#         if msg.plain:
            
            
training_data_arr = numpy.array(training_data)            


file = open("data\\training_data", "wb") # writing in binary
numpy.save(file, training_data_arr)
file.close()