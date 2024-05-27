# This is the email class file that includes all of the properties measured in the algorithm.

import spacy

# Load English tokenizer, tagger, parser and NER
nlp = spacy.load("en_core_web_sm")


class Email:
    importance = ""
    sender = ""
    subject = ""
    classified = False
    body = ""
    id = ""
    date = ""


    email_sender_length = 0
    time_sent = 0
    attachments = 0
    subject_length = 0
    body_length = 0
    num_verbs = 0
    
    
    
    def __init__(self, msg):
        self.importance = 0
        self.sender = msg.sender
        self.email_sender_length = len(msg.sender)
        self.time_sent = int(msg.date[msg.date.find(" "): msg.date.find(":")])
        self.attachments = len(msg.attachments)
        self.subject = msg.subject
        self.subject_length = len(msg.subject)
        self.body = msg.plain
        self.id = msg.id
        self.mark_read_function = msg.mark_as_read
        self.date = msg.date
        if msg.plain:
            self.body_length = len(msg.plain)

            # finding num of verbs
            doc = nlp(msg.plain)
            verbs = [token.lemma_ for token in doc if token.pos_ == "VERB"] 
            filtered_verbs = []
            for i in verbs:
                if len(i) < 12:
                    filtered_verbs.append(i)
            self.num_verbs = len(filtered_verbs) 
        else:
            self.body = ""

        
