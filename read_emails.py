# This file reads recent emails into an array and writes the array into the training_data.npy file.
# 

from simplegmail import Gmail
from email_class import Email
from simplegmail.query import construct_query
import numpy

#initialization
gmail = Gmail()

# variables
training_data = []


# grabbing all emails that fit these parameters
query_params = {
    "newer_than": (30, "day"),
}
messages = gmail.get_messages(query=construct_query(query_params))
# creating Email objects and adding to training data
for msg in messages:
    training_data.append(Email(msg))

for x in training_data:
    print("importance: "  + str(x.importance))
    print("email-sender-len: " + str(x.email_sender_length))
    print("time-sent: " + str(x.time_sent))
    print("time sent: " + str(x.attachments))
    print("subject: " + str(x.subject))
    print("subject-len: " + str(x.subject_length))
    print("num-verbs: " + str(x.num_verbs))
    print(" ")


            
            
training_data_arr = numpy.array(training_data)            


file = open("data\\training_data.npy", "wb") # writing in binary
numpy.save(file, training_data_arr)
file.close()