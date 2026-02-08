import matplotlib.pyplot as plt
import numpy as np

print("Test 123!")

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


Year1 = [832, 765, 873, 792, 791, 663, 834, 754, 806, 799, 773, 887]
Year2 = [932, 665, 573, 222, 111, 560, 734, 654, 126, 499, 503, 817]
Months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]


fig, ax = plt.subplots()      # single axis figure
ax.plot(Months, Year1, label="Year1", marker="d")  # plot line 1
ax.plot(Months, Year2, label="Year2", marker="d")  # this is for line 2
ax.tick_params(axis='x', labelrotation=90)
ax.set_xlabel("Months")
ax.set_ylabel("in $USD")
ax.legend()
plt.show()                 # shows figure



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

species = ("Toyota Rav-4 Hybrid", "Nissan Rouge", "Hyundai Tuscon Hybrid", "Honda CRV Hybrid")
Car_Details = {
    'MPG': (39.5, 33.5, 38, 39.5),
    'Range': (594, 485, 521, 602),
    'Price': (32.6, 29.98, 34.96, 34.65),
}

highest_overall = max(max(values) for values in Car_Details.values())   #this finds the highest values in the dict value
print(highest_overall)                                                  #and sets the y-axis as that value  (auto-adjust)


x = np.arange(len(species))

width = 0.25  # the width of the bars
multiplier = 0

fig, ax = plt.subplots(layout='constrained')

for attribute, measurement in Car_Details.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    ax.bar_label(rects, padding=7)
    multiplier += 1

ax.set_ylabel('value (MPG / Range / $USD)')
ax.set_title('Car Comparison')
ax.set_xticks(x + width, species)
ax.legend(loc='upper left', ncols=7)
ax.set_ylim(0, highest_overall)

plt.show()





###  ---------------------------- QUESTON 3 ----------------------------  ###

'''

Vehicle Type        Car     Bus     Heavy       Motorbike       Bike
                                    Goods
                                    Vehicle
---------------------------------------------------------------------                                    
8 - 9 AM            37      11      5           5               15
9 - 10 AM           48      7       11          9               11
10 - 11 AM          71      5       16          2               9
11 - 12 PM          33      4       3           1               7



'''

species = (
    "8 - 9 AM",
    "9 - 10 AM",
    "10 - 11 Am",
    "11 - 12 PM",
)
weight_counts = {
    "Car": np.array([37, 48, 71, 33]),        
    "Bus": np.array([11, 7, 5, 4]),
    "Heavy Vehicle": np.array([5, 11, 16, 3]),
    "Motorcycle": np.array([5, 9, 2, 1]),
    "Bike": np.array([15, 11, 9, 7]),
}

width = 0.5

fig, ax = plt.subplots()
bottom = np.zeros(4)            # Number of data points per category

for boolean, weight_count in weight_counts.items():
    p = ax.bar(species, weight_count, width, label=boolean, bottom=bottom)
    bottom += weight_count

ax.set_title("Bridege Crossings by Vehicle Type")
#ax.legend(loc="upper right")
fig.legend(loc='outside upper right')


plt.show()





###  ---------------------------- QUESTON 4 ----------------------------  ###


'''
Country:     Yields (in lbs.) per acre:
 USA          1469
 Japan        2276
 India        728
 Siam         943
 Italy        2903
 Egypt        1688


'''

fig, ax = plt.subplots()

# Example data  5
countries = ('USA', 'Japan', 'India', 'Siam', 'Italy', 'Egypt')
y_pos = np.arange(len(countries))

performance = (1469, 2276, 728, 943, 2903, 1688)


ax.barh(y_pos, performance, align='center')
ax.set_yticks(y_pos, labels=countries)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Yields (in lbs.) per acre')
ax.set_title('Rice Production By Country')

plt.show()




###  ---------------------------- QUESTON 5 ----------------------------  ###

'''
figures for the amount of cotton exported (in 1,000 bales) :

Country: {USA, India, Egypt, Brazil, Argentina}
Export: {6367, 2999, 1688, 650, 202}


'''

labels = 'USA', 'India', 'Egypt', 'Brazil', 'Argentina'
sizes = [6367, 2999, 1688, 650, 202]

explode = (0.09, 0, 0, 0, 0)

fig, ax = plt.subplots()
ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
       textprops={'size': 'smaller'},
       shadow=True, startangle=90)
plt.show()




