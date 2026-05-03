

print("   entering: STRUCTURAL.py")


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

# moment of inertia of a rectangle with respect to an axis passing through its centroid
#   &
# moment of inertia of a rectangle with respect to a centroidal axis perpendicular to its base
def RectangularMomentOfInertia(base, height):
    XAxisInertia = (base*(height**3))/12  
    YAxisInertia = (height*(base**3))/12

    return "Solid Rectangular Moment of Inertia --> ", "I(x):", XAxisInertia, "I(y):", YAxisInertia
    




def HollowRectangularMomentOfInertia(base, height, wall):
    XAxisInertia = ((base*(height**3))/12)-((base-2*(wall))*((height-2*(wall))**3))/12
    YAxisInertia = ((height*(base**3))/12)-((height-2*(wall))*((base-2*(wall))**3))/12

    return "Hollow Rectangular Moment of Inertia --> ", "I(x):", XAxisInertia,  "I(y):", YAxisInertia




#
#   learn more about how to create a method that handles "complex" shapes like I/H Beams
#   

#------------------------------/////////   BELLOW IS FROM GOOGLE COLAB      \\\\\\\\\\-----------------------#



# M = internal bending moment around the cross section
#     (Point Load at Center) M = (force * length)/4
def InternalBendingMoment(force, length):
  moment = (force * length) /4
  return moment


def RectangleBendingStress(base, height, force, length):
  moment = InternalBendingMoment(force, length)
  bendingStress = (moment*(height/2))/((base*height)**4)
  return bendingStress






'''BENDING STRESS  

https://skyciv.com/docs/tutorials/stress-tutorials/calculate-bending-stress-of-a-beam-section/

M = internal bending moment around the cross section
    (Point Load at Center) M = (force * length)/4

y = perpendicular distance from neutral axis to a point on the section
I = the moment of inertial about that section around the neutral axis

bend^max  = (M*y)/I
Pascals = (Newton Meter)*(meters) / (kilos*meters^2)

'''

# Bending stress [rectangle]
# # Bending stress [hollow rectangle]

def BendingStress(bendingMoment, height, momentOfInertia):
  perpendicularDistance = height/2
  bendingStress = (bendingMoment*perpendicularDistance)/momentOfInertia
  return bendingStress






