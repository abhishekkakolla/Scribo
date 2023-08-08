# This file is run in the terminal to classify emails during training. Not be run often.
# Reads the training data array from the training_data.npy file.

from email_class import Email
import numpy as np

# Loading the data
file = open("data\\training_data.npy", "rb")
array = np.load(file, allow_pickle=True)

print("_________________________________________________________")
print("""Training data will be iterated through. Enter 0 to indicate the email is unimportant. 
      Enter 1 to indicate it is important. Enter -1 to exit program. Only emails that have not been classified will be shown""")
print("_________________________________________________________")


ans = ""
for x in array:
    if x.classified == False:
        print("Subject: " + x.subject)
        print("Sender: " + x.sender)
        print("Is this email important?: ")

        while True: # make sure the number is an integer
            try:
                ans = int(input())
            except ValueError:
                print("Invalid. Enter again.")
                continue
            break
        if ans == -1: # end program if -1 is entered
            break

        x.classified = True # now that the email has been touched, it is now classified
        x.importance = ans
        
        print("This email's importance has been set to " + str(x.importance))


# update array in the file
file = open("data\\training_data.npy", "wb") # writing in binary
np.save(file, array)
file.close()