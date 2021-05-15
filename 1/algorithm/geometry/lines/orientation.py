'''
Orientation of an ordered triplet of points in the plane can be

    counterclockwise
    clockwise
    collinear

    
The idea is to use slope.  

Slope of line segment (p1, p2): σ = (y2 - y1)/(x2 - x1)
Slope of line segment (p2, p3): τ = (y3 - y2)/(x3 - x2)

If  σ > τ, the orientation is clockwise (right turn)

Using above values of σ and τ, we can conclude that, 
the orientation depends on sign of  below expression: 

(y2 - y1)*(x3 - x2) - (y3 - y2)*(x2 - x1)

Above expression is negative when σ < τ, i.e.,  counterclockwise

'''


class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

def orientation(p1,p2,p3):
    val = (float(p2.y - p1.y)* (p3.x - p2.x)) - \
        (float(p2.x - p1.x) * (p3.y - p2.y))

    if (val > 0):
          
        # Clockwise orientation
        return 1
    elif (val < 0):
          
        # Counterclockwise orientation
        return 2
    else:
          
        # Colinear orientation
        return 0

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = Point(5, 6)
  
o = orientation(p1, p2, p3)
  
if (o == 0):
    print("Linear")
elif (o == 1):
    print("Clockwise")
else:
    print("CounterClockwise")