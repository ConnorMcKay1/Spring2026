import matplotlib.pyplot as plt
import numpy as np

print("yo")

  ###  ---------------------------- QUESTON 1 ----------------------------  ###

# Year - 1: {832, 765, 873, 792, 791, 663, 834, 754, 806, 799, 773, 887}
# Year - 2: {932, 665, 573, 222, 111, 560, 734, 654, 126, 499, 503, 817}
#
# Plot the data with legend
#
# Which year do you think has more variation in the data?
#   Explain with a crude measure that you feel is appropriate.
#
#
'''
 The year that has the most variation would be Year 2.
 A crude measure that could find a specific month the largest variation or to find the slope of
 certain months that look to have a wide variation in the value/frequency.

'''


# Year1 = [832, 765, 873, 792, 791, 663, 834, 754, 806, 799, 773, 887]
# Year2 = [932, 665, 573, 222, 111, 560, 734, 654, 126, 499, 503, 817]
# Months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]


# fig, ax = plt.subplots()      # single axis figure
# ax.plot(Months, Year1, label="Year1", marker="d")  # plot line 1
# ax.plot(Months, Year2, label="Year2", marker="d")  # this is for line 2
# ax.tick_params(axis='x', labelrotation=90)
# ax.set_xlabel("Months")
# ax.set_ylabel("in $USD")
# ax.legend()
# plt.show()                 # shows figure



###  ---------------------------- QUESTON 2 ----------------------------  ###

# The average Miles Per Gallon (MPG), Range and Starting Price of 4 SUV-s are given
# below:
#
# Toyota Rav-4 Hybrid: {MPG: 39.5, Range (miles): 594, Price (Thousand dollars): 32.6}
# Nissan Rouge: {MPG: 33.5, Range (miles): 485, Price (Thousand dollars): 29.98}
# Hyundai Tuscon Hybrid: {MPG: 38, Range (miles): 521, Price (Thousand dollars): 34.96}
# Honda CRV Hybrid: {MPG: 39.5, Range (miles): 602, Price (Thousand dollars): 34.65}
#
# Show the comparison among the 4 SUV-s with a grouped Bar Diagram.


#   --->> CODE BELOW

# species = ("Toyota Rav-4 Hybrid", "Nissan Rouge", "Hyundai Tuscon Hybrid", "Honda CRV Hybrid")
# Car_Details = {
#     'MPG': (39.5, 33.5, 38, 39.5),
#     'Range': (594, 485, 521, 602),
#     'Price': (32.6, 29.98, 34.96, 34.65),
# }

# highest_overall = max(max(values) for values in Car_Details.values())   #this finds the highest values in the dict value
# print(highest_overall)                                                  #and sets the y-axis as that value  (auto-adjust)


# x = np.arange(len(species))

# width = 0.25  # the width of the bars
# multiplier = 0

# fig, ax = plt.subplots(layout='constrained')

# for attribute, measurement in Car_Details.items():
#     offset = width * multiplier
#     rects = ax.bar(x + offset, measurement, width, label=attribute)
#     ax.bar_label(rects, padding=7)
#     multiplier += 1

# ax.set_ylabel('value (MPG / Range / $USD)')
# ax.set_title('Car Comparison')
# ax.set_xticks(x + width, species)
# ax.legend(loc='upper left', ncols=7)
# ax.set_ylim(0, highest_overall)

# plt.show()





###  ---------------------------- QUESTON 3 ----------------------------  ###



