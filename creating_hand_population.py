'''Creating a hand_population'''

# Creates the hand surface boundaries for touchsim, and sets parameters for afferent population


import pickle as pk
import numpy as np
np.set_printoptions(threshold=np.nan)
import touchsim as ts
import scipy
import somatotopy_python as sp



# Adds location tags for each area. You will need to specify these after
# after checking the boundary locations.

hand_tags_PRIMATENAME = ['D3d_t', 'D4d_t', 'D2d_t', 'D3m_f', 'D4m_f', 'D5d_t', 'D2m_f',
    'D5m_f', 'D4p_f', 'D3p_f', 'D2p_f', 'D5p_f', 'Pw3_p', 'Pw2_p', 'Pw4_p',
    'D1d_t', 'D1p_f', 'Pp1_p', 'Pw1_p', 'Pp2_p']



# Parameters for changing origin of plot hand (changes all coordinates into 
# alternative system)

hand_orig = np.array([126.985990110355, 452.062407132244])
hand_pxl_per_mm = 2.18388294387421
hand_theta = -1.24458187646155



# Set up the density of each afferent class and region.

hand_density = {('SA1','_p'):10.,('RA','_p'):25., ('PC','_p'):10.,
           ('SA1','_f'):30.,('RA','_f'):40., ('PC','_f'):10.,
           ('SA1','_t'):70.,('RA','_t'):140., ('PC','_t'):25.,}



# Create the surface object

sur_PRIMATENAME = ts.Surface(filename='PRIMATENAME_hand.tiff',orig=hand_orig,pxl_per_mm=hand_pxl_per_mm,
        theta=hand_theta,density=hand_density,tags=hand_tags_PRIMATENAME)



# Create SA1 afferent population

hand_population = ts.affpop_surface(surface=sur_PRIMATENAME,affclass='SA1',density_multiplier=0.25)

# get locations from the hand_population object

x = hand_population.location



# Save to matlab file for use with map code

scipy.io.savemat('PRIMATENAME_locations.mat', {'locations': x})




# Save the hand population

with open('PRIMATENAME_pop', 'wb') as f:
    pk.dump(hand_population, f)



# Create the regionprops file needed for matlab 
   
sp.python_create_regionprops(hand_population,'PRIMATENAME')