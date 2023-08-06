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
    "newer_than": (1, "day"),
}
messages = gmail.get_messages(query=construct_query(query_params))
# creating Email objects and adding to training data
for msg in messages:
    training_data.append(Email(msg))

for x in training_data:
    print(x.importance)
    print(x.email_sender_length)
    print(x.time_sent)
    print(x.attachments)
    print(x.subject)
    print(x.subject_length)
    print(x.num_verbs)
    print(" ")

# # writing data to file
# with open("data\\email_data.txt", "a", encoding="utf-8") as doc:
#     for msg in messages:
#         if msg.plain:
            
            
training_data_arr = numpy.array(training_data)            


file = open("data\\training_data.npy", "wb") # writing in binary
numpy.save(file, training_data_arr)
file.close()