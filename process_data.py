# This file stores the means and standard deviations of the email data that are to be used
# in the classification algorithm.

import numpy as np

# property lists associated with unimportant emails
u_sender_email_length_list = []
u_time_sent_list = []
u_attachments_list = []
u_subject_length_list = []
u_length_list = []
u_num_verbs_list = []
u_all_lists = [u_sender_email_length_list, u_time_sent_list, u_attachments_list, u_subject_length_list, u_length_list, u_num_verbs_list]

# property lists associated with important emails
i_sender_email_length_list = []
i_time_sent_list = []
i_attachments_list = []
i_subject_length_list = []
i_length_list = []
i_num_verbs_list = []
i_all_lists = [i_sender_email_length_list, i_time_sent_list, i_attachments_list, i_subject_length_list, i_length_list, i_num_verbs_list]


def process_list(main_list, properties_list):
    main_list[0][0] = np.mean(properties_list[0])
    main_list[1][0] = np.std(properties_list[0])

    main_list[0][1] = np.mean(properties_list[1])
    main_list[1][1] = np.std(properties_list[1])

    main_list[0][2] = np.mean(properties_list[2])
    main_list[1][2] = np.std(properties_list[2])

    main_list[0][3] = np.mean(properties_list[3])
    main_list[1][3] = np.std(properties_list[3])

    main_list[0][4] = np.mean(properties_list[4])
    main_list[1][4] = np.std(properties_list[4])

    main_list[0][5] = np.mean(properties_list[5])
    main_list[1][5] = np.std(properties_list[5])



# Loading the training data
file = open("data\\training_data.npy", "rb")
array = np.load(file, allow_pickle=True)

# putting into property lists
for item in array:
    if item.classified == True:

        if item.importance == 0:
            u_sender_email_length_list.append(item.email_sender_length)
            u_time_sent_list.append(item.time_sent)
            u_attachments_list.append(item.attachments)
            u_subject_length_list.append(item.subject_length)
            u_length_list.append(item.body_length)
            u_num_verbs_list.append(item.num_verbs)  

        if item.importance == 1:
            i_sender_email_length_list.append(item.email_sender_length)
            i_time_sent_list.append(item.time_sent)
            i_attachments_list.append(item.attachments)
            i_subject_length_list.append(item.subject_length)
            i_length_list.append(item.body_length)
            i_num_verbs_list.append(item.num_verbs)    


# #test printing
# print("unimportant: ")
# print(u_sender_email_length_list)
# print(u_time_sent_list)
# print(u_attachments_list)
# print(u_subject_length_list)
# print(u_length_list)
# print(u_num_verbs_list)


# print("important: ")
# print(i_sender_email_length_list)
# print(i_time_sent_list)
# print(i_attachments_list)
# print(i_subject_length_list)
# print(i_length_list)
# print(i_num_verbs_list)

# processing mean and std into 2 x 6 matrices
unimportant_properties = [[0 for i in range(6)] for x in range(2)] # 2 x 6 list
process_list(unimportant_properties, u_all_lists)

important_properties = [[0 for i in range(6)] for x in range(2)] # 2 x 6 list
process_list(important_properties, i_all_lists)



# # test prints
# print("unimportant")
# for row in range (0, 2):
#     for column in range (0, 6):
#         print(unimportant_properties[row][column], end=" ")
#     print(" ")

# print("important")
# for row in range (0, 2):
#     for column in range (0, 6):
#         print(important_properties[row][column], end=" ")
#     print(" ")