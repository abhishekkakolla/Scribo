import numpy as np
import os 


location = os.getenv('LOCALAPPDATA') + "\Scribo\dark.npy"
def get_current_mode():
    # create %localappdata% folder (to store dark mode data)
    

    # (First time) if there is no file here, create it and intitialize with light mode
    if not os.path.exists(location):
        # print('file doesnt exist, gonna create')
        os.makedirs(os.path.dirname(location), exist_ok=True)
        np.save(location, np.array(['light']))
        return 'light'
    else:
        # print('file exists')
        # file exists, read what mode the app is currently on
        file = open(location, "rb") # reading in binary
        array = np.load(file, allow_pickle=True)
        file.close()
        # print(array[0])
        return array[0]
    
def set_mode(str):
    file = open(location, "wb")
    new_arr = [str]
    np.save(file, new_arr)
    file.close()

get_current_mode()