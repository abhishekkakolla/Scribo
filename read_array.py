import numpy as np

# Loading the data
file = open("data\\training_data.npy", "rb")
array = np.load(file, allow_pickle=True)


for x in array:
    print(x.subject)
    print(x.importance)
    print(x.classified)
    print(" ")