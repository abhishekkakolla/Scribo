import nltk
nltk.download('punkt')
nltk.download('stopwords')

text = """
Hi everyone,

As you know, a different professor, Shieva Kleinschmidt, will be taking over the course starting next week. You should have received an email from her with the new syllabus. We will discuss more next week during the lectures as well as the discussion section. However, it will be good to let you know about what we will do for presentations. 

There will not be any presentaions during discussion sections. Instead, those who have not presented will complete a writing assignment instead. The grade for the writing assignment will count toward your presentation grade. Additionally, you do not need to follow the presentation schedule anymore since there will be no new readings for the next two weeks. You will need to pick one and only one of the readings from the new syllabus for the writing assignment. We will talk more about the logistics in the discussion section this week.

I know there has been a lot of changes for this course lately -- we hope to make the transition as seamless as possible given the circumstances. Thank you for the understanding! Please email me for any questions and confusions that cannot wait until Tuesday.

Best,

Levy





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

# print(freqTable)

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
    # print(sentence_value)
    return sentence_value

sentence_value = get_sentence_value()
# print(sentence_value)

def get_sum_values():
    sum_values = 0
    for sentence in sentence_value:
        sum_values += sentence_value[sentence]

    average = int(sum_values / len(sentence_value))
    return average

average = get_sum_values()
# print(average)


summary = ''
for sentence in sentences:
    if (sentence in sentence_value) and (sentence_value[sentence] > (1.2 * average)):
        summary += " " + sentence
print("Summary: " + summary)
