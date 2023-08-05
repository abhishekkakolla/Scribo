import spacy

# Load English tokenizer, tagger, parser and NER
nlp = spacy.load("en_core_web_sm")

# Process whole documents
text = """Hello,

I am fairly certain registration proof is best obtained via your son’s registration portal as a STARS report is downloadable that shows this information.  Have your son login to my.usc.edu and see the resources available via Course Registration, and/or OASIS.  Registration and Fee Summary may also prove helpful.  I believe these same options are also available at the USC Registrar website: https://arr.usc.edu/records-transcripts/

If any other help is needed, I recommend for your son to reach out to the registrar directly or his academic advisor for further assistance.  Unfortunately, from an admission perspective, this is all out of my purview.

Best of luck,
Paul
"""


doc = nlp(text)

# Analyze syntax
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)
