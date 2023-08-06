class Email:
    importance = 0
    sender = ""
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
        self.sender = msg.sender
        self.email_sender_length = len(msg.sender)
        self.time_sent = int(msg.date[msg.date.find(" "): msg.date.find(":")])
        self.attachments = len(msg.attachments)
        self.subject = msg.subject
        self.subject_length = len(msg.subject)
        if msg.plain:
            self.body_length = len(msg.plain)