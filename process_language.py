import nltk
nltk.download('punkt')
nltk.download('stopwords')

text = """

Dear Abhishek,

We invite you to participate in the USC Micro-Seminars that will be held as part of the USC Welcome Experience!

Micro-seminars are mini-workshops or small-group sessions that highlight a specialized topic in a short time. Structured as two 90-minute sessions, these seminars are designed to give you the chance to meet one faculty member and other first-year students and engage in an academic environment before classes begin. Attendance for most seminars is limited to just 20 students to ensure thoughtful discussion and the opportunity to meet peers with similar interests.

Micro-Seminars have two parts. You select one topic that is presented over two days. You must attend both parts. 

Part 1: Thursday, August 17, 2023 from 3:00 – 4:30 pm (PST)
Part 2: Friday, August 18, 2023 from 10:00 – 11:30 am (PST)
Part 2 is a continuation of Part 1 – same professor, topic, and peers.
Micro-Seminars will be held in person. Space is limited, so register today! For more information, visit https://ahf.usc.edu/signature-events/microseminars/

______________________________________________________________________________________________________

Frequently Asked Questions (FAQ)

Do I have to choose a seminar that’s related to my major?
?No. You can sign up for any micro-seminar! You are not required to sign up for a micro-seminar related to your major. Feel free to choose any topic that interests you.
Is Micro-Seminar open to transfers / non-first year students?
?Yes, while Micro-Seminars are typically geared towards first-years, we are opening it up to all USC students who will be on campus for the first time.
Can I register for more than one Micro-Seminar?
?No. All micro-seminars meet at the same time, so you can only choose one seminar to attend over the two days.
We hope you will take advantage of this unique opportunity as part of your Welcome Experience. Fight On! 
"""
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist

words = word_tokenize(text)

# removing stopwords
stop_words = set(stopwords.words("english"))

freqTable = dict()

freqTable = dict()
for word in words:
    word = word.lower()
    if word in stop_words:
        continue
    if word in freqTable:
        freqTable[word] += 1
    else:
        freqTable[word] = 1

print(freqTable)

sentences = sent_tokenize(text)
def get_sentence_value():
    sentence_value = dict()
    for sentence in sentences:
        for word, freq in freqTable.items():
            if word in sentence.lower():
                if sentence in sentence_value:
                    sentence_value[sentence] += freq
                else:
                    sentence_value[sentence] = freq
    print(sentence_value)
    return sentence_value

sentence_value = get_sentence_value()
print(sentence_value)

def get_sum_values():
    sum_values = 0
    for sentence in sentence_value:
        sum_values += sentence_value[sentence]

    average = int(sum_values / len(sentence_value))
    return average

average = get_sum_values()
print(average)


summary = ''
for sentence in sentences:
    if (sentence in sentence_value) and (sentence_value[sentence] > (1.2 * average)):
        summary += " " + sentence
print("Summary: " + summary)
