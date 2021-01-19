""" Rolling a random die 6,000,000 times """


# Importing required library

import random

# Initializing the frequency counters

freq_1 = 0

freq_2 = 0

freq_3 = 0 

freq_4 = 0

freq_5 = 0

freq_6 = 0


#6,000,000 die rolls

for roll in range(6000000):

    face = random.randrange(1 , 7)

    if face == 1:

        freq_1 += 1

    
    elif face == 2:

        freq_2 += 1

    elif  face == 3:

        freq_3 += 1

    elif face == 4:

        freq_4 += 1

    elif  face == 5:

        freq_5 += 1

    else:
        freq_6 += 1


print(f"Face{'Frequency':>13}")
print(f'{1:>4}{freq_1:>13}')
print(f'{2:>4}{freq_2:>13}')
print(f'{3:>4}{freq_3:>13}')
print(f'{4:>4}{freq_4:>13}')
print(f'{5:>4}{freq_5:>13}')
print(f'{6:>4}{freq_6:>13}')