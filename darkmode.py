import numpy as np



def get_current_mode():
    file = open("data\\dark.npy", "rb") # writing in binary
    array = np.load(file, allow_pickle=True)
    file.close()
    return array[0]

def set_mode(str):
    file = open("data\\dark.npy", "wb")
    new_arr = [str]
    np.save(file, new_arr)
    file.close()