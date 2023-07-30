from simplegmail import Gmail
from simplegmail.query import construct_query

#initialization
gmail = Gmail()

# variables
all_emails = []

# query parameters
query_params = {
    "newer_than": (5, "day"),
}
messages = gmail.get_messages(query=construct_query(query_params))

# classes

class Email:
    def __init__(self, subject, date, plain):
        self.subject = subject
        self.date = date
        self.plain = plain

# creating Email objects
for email in messages:
    all_emails.append(Email(email.subject, email.date, email.plain))

# writing data to file
with open("data\\email_data.txt", "a", encoding="utf-8") as doc:
    for msg in all_emails:
        if msg.plain:
            doc.write(msg.subject + "\n")

