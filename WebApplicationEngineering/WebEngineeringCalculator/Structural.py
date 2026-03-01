print("test 321")




'''
    --> steel, concrete, wood, masonry, and aluminum
        Young's Modulus / Poissons Ratio
Structural
-moment of intertia
    https://skyciv.com/docs/tutorials/section-tutorials/calculating-the-moment-of-inertia-of-a-beam-section/
        https://skyciv.com/wp-content/uploads/2022/11/moment-of-inertia-equations-and-formula-for-easy-calculations-skyciv.png


-bending stress

-shear stress

-deflection


'''

# Units: Inches
base = 0
height = 0


    # moment of inertia of a rectangle with respect to an axis passing through its centroid
    #   &
    # moment of inertia of a rectangle with respect to a centroidal axis perpendicular to its base
def RectangularMomentOfInertia(base, height):
    XAxisInertia = (base*(height**3))/12  
    YAxisInertia = (height*(base**3))/12

    return "Solid Rectangular Moment of Inertia --> ", "I(x):", XAxisInertia, "I(y):", YAxisInertia
    
solidRectangleInertia = RectangularMomentOfInertia(5, 7)
print(solidRectangleInertia)



def HollowRectangularMomentOfInertia(base1, height1, base2, height2):
    XAxisInertia = ((base1*(height1**3))/12)-((base2*(height2**3))/12)
    
    return "Hollow Rectangular Moment of Inertia --> ", "I(x):", XAxisInertia,

HollowRectangleInertia = HollowRectangularMomentOfInertia(5, 7, 3, 5)
print(HollowRectangleInertia)




#
#   learn more about how to create a method that handles "complex" shapes like I/H Beams
#







