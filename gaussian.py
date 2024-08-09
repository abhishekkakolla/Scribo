# This file gets the likelihoods using the processed data

import numpy as np
import math
from scipy.stats import norm
# import matplotlib.pyplot as plt

#ignore NaN warnings
np.seterr(divide='ignore', invalid='ignore')


mean = 0
std = 1

x = 0.5
like = norm.pdf(x, loc=mean, scale=std)

# Loading the data
file = open("data\\important_data_array.npy", "rb")
important_data_array = np.load(file, allow_pickle=True)

file2 = open("data\\unimportant_data_array.npy", "rb")
unimportant_data_array = np.load(file2, allow_pickle=True)

file3 = open("data\\training_data.npy", "rb")
training_data = np.load(file3, allow_pickle=True)


i_count = 0
# getting prior probability
for email in training_data:
    if email.importance == 1:
        i_count += 1

prior_probability = i_count / len(training_data) # of being important

def get_score(email_obj):
    # important score
    score = 0
    properties = [email_obj.email_sender_length, email_obj.time_sent, email_obj.attachments, email_obj.subject_length, email_obj.body_length, email_obj.num_verbs]
    score = math.log(prior_probability)
    # print("prior prob score: " + str(prior_probability))
    # print("score: " + str(score))

    # getting score for important properties
    for col in range(0, 6):
        # value, mean, std
        l =norm.pdf(properties[col], loc=important_data_array[0][col], scale=important_data_array[1][col])
        # print("normal dist value: " + str(l))
        if math.isnan(l): #check if the number is NaN
            continue
        # print(l)
        try:
            l = math.log(l)
        except ValueError:
            print("Value Error (out of domain): l is " + str(l))
            l = 0.00000001
            print("new l: " + str(l))
        # print("value is " + str(properties[col]) + ", avg is " + str(important_data_array[0][col]) + "std is " + str(important_data_array[1][col]) + "ans with log is " + str(l))
        score += l



    # getting score for unimportant properties

    u_score = 0
    u_score = math.log(1 - prior_probability)
    # print("u score beginning: " + str(u_score))

    for col in range(0, 6):
        l = norm.pdf(properties[col], loc=unimportant_data_array[0][col], scale=unimportant_data_array[1][col])
        # print("norm dist value: " + str(l))
        if math.isnan(l): #check if the number is NaN, aka very very small
            continue
        # print(l)
        try:
            l = math.log(l)
        except ValueError:
            print("Value Error (out of domain): l is " + str(l))
            l = 0.00000001
            print("new l: " + str(l))
        # print("value is " + str(properties[col]) + ", avg is " + str(unimportant_data_array[0][col]) + "std is " + str(unimportant_data_array[1][col]) + "ans with log is " + str(l))
        u_score += l
        # print("u score: " + str(u_score))

    # print ("----------important score: " + str(score))
    # print ("----------unimportant score: " + str(u_score))
    if score > u_score:
        
        # print("important")
        return "⭐"
    else:
        # print("unimpotant")
        return ""
