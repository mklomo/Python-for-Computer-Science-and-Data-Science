""" Dynamically graphing frequencies of die rolls """


# Initializing Phase

import random
import sys

import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import animation


# Processing Phase

def update(frame_number, rolls, faces, frequencies):
    """ Configures barplot contents for each animation frame """

    # roll die and update frequencies
    for i in range(rolls):
        frequencies[random.randrange(1 , 7) - 1] += 1


    # reconfigure the plot for updated die frequencies
    plt.cla()   #  clear old contents of current figure
    axes = sns.barplot(x= faces,y= frequencies, palette = "bright")  # New Bars
    axes.set_title(f"Die frequencies for {sum(frequencies): ,} Rolls")
    axes.set(xlabel= "Die Value", ylabel= "Frequency")
    axes.set_ylim(top=max(frequencies) * 1.2)


    # Display frequency and percentage above each patch (bar)
    for bar, frequency in zip(axes.patches, frequencies):
        text_x = bar.get_x() + bar.get_width() / 2.0
        text_y = bar.get_height()
        text = f"{frequency: ,}\n{frequency / sum(frequencies):.3%}"
        axes.text(text_x, text_y, text, ha="center", va="bottom")


# read command-line arguments for number of rolls per frame
number_of_frames = int(sys.argv[1])
rolls_per_frame = int(sys.argv[2])        

sns.set_style("whitegrid")
figure = plt.figure("Rolling a Six-Sided Die")
values = list(range(1, 7))
frequencies = [0] * 6       # six-element list of die frequencies



# Configure and start animationthat calls function update
die_animation = animation.FuncAnimation(
    figure, update, repeat= False, frames= number_of_frames, 
    interval= 33, fargs=(rolls_per_frame, values, frequencies)
)

# Display window
plt.show()
