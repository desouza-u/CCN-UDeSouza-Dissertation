''' Creating afferent responses with even probability'''


import pickle as pk
# import the file with the methods
import somatotopy_python as sp
import numpy as np

#load the saved hand_pop object
with open('PRIMATENAME_pop', 'rb') as f:
    hand_pop = pk.load(f)
    
# set string name of file        
name = 'PRIMATENAME'

# set random seed number
number = '1'

stimuli_num = 1000

# run the input generator file.
sp.input_create(number=number,hand_pop=hand_pop,name=name,stimuli_num=stimuli_num,visualize='True')
    